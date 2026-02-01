"""
Story Generator
"""

from typing import Optional
from config import STORY_CATEGORIES, STORY_ARC_TEMPLATE

"""
Generate a story using category-specific prompting and story arc structure.
"""
def generate_story(user_request: str, category: str, previous_feedback: Optional[str] = None) -> str:
    from main import call_model
    
    cat_info = STORY_CATEGORIES[category]
    
    system_prompt = f"""You are a bedtime storyteller for children ages 5-10.

        Create stories that are:
        - Simple vocabulary, 400-600 words
        - Warm, positive, with gentle humor
        - End peacefully for bedtime
        - Have a moral or lesson subtly woven in

        Tone: {cat_info['tone']}
        Include: {', '.join(cat_info['elements'])}

        {STORY_ARC_TEMPLATE}"""

    improvement_note = ""
    if previous_feedback:
        improvement_note = f"""

        IMPORTANT: A previous version of this story was reviewed and needs improvement. Please address this feedback:
        {previous_feedback}

        Create an improved version that addresses all the feedback while maintaining the story's charm."""

    user_prompt = f"""Please create a wonderful bedtime story based on this request:

        "{user_request}"

        Story Category: {category}
        {improvement_note}

        Remember to:
        1. Follow the story arc structure
        2. Use engaging, age-appropriate language
        3. Include descriptions
        4. End with a warm, satisfying conclusion
        5. Keep it perfect for bedtime reading (400-600 words)

        Begin the story now:"""

    return call_model(user_prompt, system_prompt=system_prompt, temperature=0.8)