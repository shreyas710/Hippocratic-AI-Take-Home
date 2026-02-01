"""
Configuration and constants for the Bedtime Story Generator.
"""

STORY_CATEGORIES = {
    "adventure": {
        "keywords": ["adventure", "quest", "journey", "explore", "discover", "treasure", "map"],
        "tone": "exciting and brave, with moments of wonder",
        "elements": ["a brave protagonist", "an exciting challenge", "a triumphant ending"]
    },
    "fantasy": {
        "keywords": ["magic", "wizard", "dragon", "fairy", "unicorn", "castle", "spell", "enchanted", "princess", "prince"],
        "tone": "magical and wondrous, full of imagination",
        "elements": ["magical abilities or items", "fantastical creatures", "an enchanted setting", "a magical resolution"]
    },
    "animal": {
        "keywords": ["dog", "cat", "rabbit", "bear", "bird", "fish", "animal", "pet", "forest animals", "zoo"],
        "tone": "warm and playful, celebrating animal friendships",
        "elements": ["animal characters with personalities", "natural settings", "friendship themes", "nature appreciation"]
    },
    "friendship": {
        "keywords": ["friend", "friendship", "together", "help", "kind", "share", "team", "buddy"],
        "tone": "warm, caring, and heartfelt",
        "elements": ["relatable characters", "a friendship challenge", "acts of kindness", "stronger bonds at the end"]
    },
}

STORY_ARC_TEMPLATE = """
A great children's story (ages 5-10) follows this structure:

1. OPENING: 
   - Introduce the main character in an interesting way
   - Set the scene with vivid, child-friendly descriptions
   - Create curiosity about what will happen

2. RISING ACTION:
   - Present a challenge, problem, or goal
   - Introduce friends or helpers
   - Build excitement with small obstacles

3. CLIMAX:
   - The most exciting part of the story
   - Character faces their biggest challenge
   - Show bravery, cleverness, or kindness

4. FALLING ACTION:
   - The problem gets solved
   - Show how the character grew or learned
   - Celebrate the victory with friends

5. ENDING:
   - Wrap up with a satisfying, happy ending
   - Include a gentle moral or lesson
   - End with a cozy, peaceful feeling perfect for bedtime
"""