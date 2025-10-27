#!/usr/bin/env python3.8
from typing import List, Dict

class DataValidator:
    """Validates input data structure."""
    
    @staticmethod
    def validate_comments(comments: List[Dict], text_field: str = 'text') -> tuple[bool, str]:
        """
        Validate that comments have the required structure.
        
        Args:
            comments: List of comment dictionaries
            text_field: Field name containing the comment text
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not comments:
            return False, "No comments provided"
        
        if not isinstance(comments, list):
            return False, "Comments must be a list"
        
        missing_field_count = 0
        for i, comment in enumerate(comments):
            if not isinstance(comment, dict):
                return False, f"Comment {i} is not a dictionary"
            
            if text_field not in comment:
                missing_field_count += 1
        
        if missing_field_count == len(comments):
            return False, f"No comments have the '{text_field}' field"
        
        return True, ""