"""
Story categorizer
"""

from config import STORY_CATEGORIES

"""
Categorize the user's story request into one of the predefined story categories.
"""
def categorize_request(user_request: str) -> str:
    from main import call_model
    
    categorizer_prompt = f"""Analyze this bedtime story request and categorize it into one of these categories:
        - adventure: stories with journeys, quests, or explorations
        - fantasy: stories with magic, supernatural elements, or mythical creatures
        - animal: stories with animals as main characters
        - friendship: stories about friendship and relationships

        Story request: "{user_request}"

        Respond with only the category name (one word, lowercase). If multiple could apply, pick the most dominant one."""

    category = call_model(categorizer_prompt, temperature=0.1).strip().lower()
    
    if category not in STORY_CATEGORIES:
        category = "adventure"
    
    return category
