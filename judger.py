"""
Story Judger
"""

import json

"""
Evaluates the story quality and provides improvement suggestions.
"""
def judge_story(story: str, user_request: str, category: str) -> dict:
    from main import call_model
        
    judge_system_prompt = """You are an expert children's literature critic and child development specialist. 
        Your role is to evaluate bedtime stories for children ages 5-10.

        You evaluate stories fairly but constructively, always providing specific, actionable feedback.
        Your goal is to help create the best possible story for young listeners."""

    judge_prompt = f"""Please evaluate this bedtime story for children ages 5-10.

        Original Request: "{user_request}"
        Story Category: {category}

        STORY TO EVALUATE:
        ---
        {story}
        ---

        Rate the story on these criteria (1-10 scale) and provide specific feedback:

        1. AGE_APPROPRIATENESS (1-10): Is the vocabulary, themes, and content suitable for ages 5-10?
        2. ENGAGEMENT (1-10): Would children find this story interesting and fun to listen to?
        3. STORY_STRUCTURE (1-10): Does it follow a good story arc with beginning, middle, climax, and satisfying end?
        4. CREATIVITY (1-10): Is the story imaginative and original?
        5. MORAL_LESSON (1-10): Does it have a gentle, positive message?
        6. BEDTIME_SUITABILITY (1-10): Does it end peacefully and promote calm, sleepy feelings?

        Respond in this exact JSON format:
        {{
            "scores": {{
                "age_appropriateness": <score>,
                "engagement": <score>,
                "story_structure": <score>,
                "creativity": <score>,
                "moral_lesson": <score>,
                "bedtime_suitability": <score>
            }},
            "overall_score": <average of all scores, rounded to 1 decimal>,
            "strengths": ["<strength 1>", "<strength 2>"],
            "improvements_needed": ["<specific improvement 1>", "<specific improvement 2>"],
            "specific_suggestions": "<detailed paragraph with specific suggestions to make this story better>"
        }}"""

    response = call_model(judge_prompt, system_prompt=judge_system_prompt, temperature=0.3)
    
    try:
        start_idx = response.find('{')
        end_idx = response.rfind('}') + 1
        if start_idx != -1 and end_idx > start_idx:
            json_str = response[start_idx:end_idx]
            return json.loads(json_str)
    except json.JSONDecodeError:
        pass
    
    return {
        "scores": {
            "age_appropriateness": 7,
            "engagement": 7,
            "story_structure": 7,
            "creativity": 7,
            "moral_lesson": 7,
            "bedtime_suitability": 7
        },
        "overall_score": 7.0,
        "strengths": ["Story was generated successfully"],
        "improvements_needed": ["Could not parse detailed feedback"],
        "specific_suggestions": "The story was created but detailed evaluation was unavailable."
    }