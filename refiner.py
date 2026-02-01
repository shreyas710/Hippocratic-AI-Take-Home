"""
Story Refiner
"""

"""
Refine an existing story based on user feedback.
"""
def refine_story(story: str, user_request: str, user_feedback: str) -> str:
    from main import call_model    
    system_prompt = """You are a skilled children's storyteller. You're revising a bedtime story based on feedback.
        Keep the core story intact but make the requested changes naturally and smoothly.
        Maintain age-appropriateness for children ages 5-10."""

    prompt = f"""Here's a bedtime story that needs some changes based on feedback:
    
        ORIGINAL STORY:
        ---
        {story}
        ---

        ORIGINAL REQUEST: "{user_request}"

        USER FEEDBACK: "{user_feedback}"

        Please revise the story to address the feedback while keeping it:
        - Age-appropriate for children 5-10
        - Engaging and fun
        - Perfect for bedtime
        - About the same length as before

        Revised story:"""

    return call_model(prompt, system_prompt=system_prompt, temperature=0.7)
