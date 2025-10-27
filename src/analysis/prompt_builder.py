#!/usr/bin/env python3.8
from typing import List, Dict

class PromptBuilder:
    """Builds prompts for Claude sentiment analysis."""
    
    @staticmethod
    def format_comments(comments: List[Dict], text_field: str = 'text') -> str:
        """
        Format comments for inclusion in prompt.
        
        Args:
            comments: List of comment dictionaries
            text_field: Field containing comment text
            
        Returns:
            Formatted string of numbered comments
        """
        formatted = []
        for i, comment in enumerate(comments, 1):
            text = comment.get(text_field, '')
            if text:
                formatted.append(f"{i}. {text}")
        return "\n".join(formatted)
    
    @staticmethod
    def build_sentiment_prompt(comments_text: str) -> str:
        """
        Build the sentiment analysis prompt.
        
        Args:
            comments_text: Formatted comments string
            
        Returns:
            Complete prompt for Claude
        """
        return f"""Analyze the sentiment and emotions of these Twitter comments in detail. Go beyond simple positive/negative/neutral and identify the specific emotions and reactions people are expressing.

Comments:
{comments_text}

Provide a comprehensive analysis in JSON format with:

1. **Emotion Breakdown**: Identify all emotions present with percentages (e.g., amused, angry, excited, disappointed, supportive, sarcastic, confused, enthusiastic, worried, grateful, etc.)

2. **Sentiment Details**: Within each major sentiment category (positive, negative, neutral), break down the specific reactions:
   - For positive: What specifically are people positive about? (funny, inspiring, exciting, helpful, etc.)
   - For negative: What specifically are people negative about? (angry, disappointed, concerned, frustrated, etc.)
   - For neutral: What types of neutral responses? (informational, questioning, indifferent, etc.)

3. **Key Themes**: What topics or aspects are people reacting to?

4. **Tone Patterns**: Identify communication styles (sarcastic, sincere, humorous, serious, etc.)

5. **Summary**: A narrative summary that captures the emotional landscape

Return JSON in this structure:
{{
    "emotion_breakdown": {{
        "amused": X,
        "angry": Y,
        "excited": Z,
        ...
    }},
    "sentiment_details": {{
        "positive": {{
            "percentage": X,
            "subcategories": {{
                "found_it_funny": Y,
                "inspired": Z,
                ...
            }}
        }},
        "negative": {{
            "percentage": X,
            "subcategories": {{
                "angry": Y,
                "disappointed": Z,
                ...
            }}
        }},
        "neutral": {{
            "percentage": X,
            "subcategories": {{
                "asking_questions": Y,
                "providing_info": Z,
                ...
            }}
        }}
    }},
    "key_themes": ["theme1", "theme2", ...],
    "tone_patterns": ["pattern1", "pattern2", ...],
    "summary": "Detailed narrative summary of the emotional landscape and what people are specifically reacting to"
}}"""

