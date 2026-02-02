import os
import openai
import threading
import sys
import time

from typing import Optional
from categorizer import categorize_request
from generator import generate_story
from judger import judge_story
from refiner import refine_story

"""
Before submitting the assignment, describe here in a few sentences what you would have built next if you spent 2 more hours on this project:
- Allow children to make choices during the story that affect the narrative.
- Implement a feature to read the story aloud using text-to-speech. (Using ElevenLabs TTS or similar APIs)
"""

def call_model(prompt: str, system_prompt: Optional[str] = None, max_tokens=3000, temperature=0.1) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY") # please use your own openai api key here.

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=False,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return resp.choices[0].message["content"]  # type: ignore

example_requests = "A story about a girl named Alice and her best friend Bob, who happens to be a cat."

class LoadingAnimation:
    def __init__(self, message="Loading"):
        self.message = message
        self.running = False
        self.thread = None
    
    def _animate(self):
        dots = 0
        while self.running:
            sys.stdout.write(f"\r{self.message}{'.' * dots}{' ' * (3 - dots)}")
            sys.stdout.flush()
            dots = (dots + 1) % 4
            time.sleep(0.5)
        sys.stdout.write("\r" + " " * (len(self.message) + 5) + "\r")
        sys.stdout.flush()
    
    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._animate)
        self.thread.start()
    
    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

def display_story_with_formatting(story: str):
    print("\n" + "="*60)
    print("YOUR BEDTIME STORY")
    print("="*60 + "\n")
    print(story)

def main():
    print("\n" + "-"*50)
    user_input = input("What kind of story do you want to hear? ").strip()
    print("-"*50)

    if not user_input:
        user_input = example_requests
        print(f"Using example request: {user_input}")

    print('\nAnalyzing your request...\n')

    category = categorize_request(user_input)

    print("-"*50)
    print(f"Story Category: {category.upper()}")
    print("-"*50)
    print('\n')

    loader = LoadingAnimation("Generating")
    loader.start()
    story = generate_story(user_input, category)
    loader.stop()

    max_iterations = 3
    quality_threshold = 8.0

    for iteration in range(max_iterations):
        print(f"Quality check {iteration + 1}/{max_iterations}\n")

        loader = LoadingAnimation("Evaluating")
        loader.start()
        evaluation = judge_story(story, user_input, category)
        loader.stop()
        overall_score = evaluation.get("overall_score", 0)
        
        print(f"Score: {overall_score}/10")
        
        if overall_score >= quality_threshold:
            break
        elif iteration < max_iterations - 1:
            print(f"Improving story based on feedback...\n")
            
            improvements = evaluation.get("improvements_needed", [])
            suggestions = evaluation.get("specific_suggestions", "")
            feedback = f"Improvements needed: {'; '.join(improvements)}. {suggestions}"
            
            story = generate_story(user_input, category, previous_feedback=feedback)
        else:
            print(f"Maximum iterations reached. Presenting best version.\n")

    display_story_with_formatting(story)

    print("\n" + "-"*50)
    print("Story Evaluation:")
    print("-"*50 + "\n")
    
    scores = evaluation.get("scores", {})
    for criterion, score in scores.items():
        criterion_display = criterion.replace("_", " ").title()
        print(f"   {criterion_display}: {score}/10")

    print("\n" + "-"*60)
    print("Would you like me to modify the story?")
    print("(e.g., 'make it funnier', 'add more adventure', 'change the ending')")
    print("(Press Enter to keep the story as is)\n")
    
    user_feedback = input("Your feedback (or Enter to finish): ").strip()
    
    while user_feedback:
        loader = LoadingAnimation("Refining")
        loader.start()
        story = refine_story(story, user_input, user_feedback)
        loader.stop()
        display_story_with_formatting(story)
        
        print("Any other changes? (Press Enter to finish)\n")
        user_feedback = input("Your feedback: ").strip()
    
if __name__ == "__main__":
    main()