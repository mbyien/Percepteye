#!/usr/bin/env python3.8
from typing import List, Dict
from datetime import datetime

from src.api.claude_client import ClaudeClient
from src.analysis.prompt_builder import PromptBuilder
from src.analysis.response_parser import ResponseParser
from src.data.validator import DataValidator

class SentimentAnalyzer:
    """Main sentiment analysis orchestrator."""
    
    def __init__(self, api_key: str = None):
        """
        Initialize the sentiment analyzer.
        
        Args:
            api_key: Anthropic API key (optional)
        """
        self.client = ClaudeClient(api_key)
        self.prompt_builder = PromptBuilder()
        self.parser = ResponseParser()
        self.validator = DataValidator()
    
    def analyze(self, comments: List[Dict], text_field: str = 'text') -> Dict:
        """
        Analyze sentiment of comments.
        
        Args:
            comments: List of comment dictionaries
            text_field: Field name containing comment text
            
        Returns:
            Analysis results dictionary
            
        Raises:
            ValueError: If comments are invalid
        """
        # Validate input
        is_valid, error_msg = self.validator.validate_comments(comments, text_field)
        if not is_valid:
            raise ValueError(f"Invalid comments data: {error_msg}")
        
        # Prepare prompt
        comments_text = self.prompt_builder.format_comments(comments, text_field)
        prompt = self.prompt_builder.build_sentiment_prompt(comments_text)
        
        # Get analysis from Claude
        response = self.client.send_message(prompt)
        
        # Parse response
        results = self.parser.parse_json_response(response)
        
        # Add metadata
        results["total_comments"] = len(comments)
        results["analysis_timestamp"] = datetime.now().isoformat()
        
        return results