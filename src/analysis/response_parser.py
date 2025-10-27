#!/usr/bin/env python3.8
import json
from typing import Dict

class ResponseParser:
    """Parses Claude's response into structured data."""
    
    @staticmethod
    def parse_json_response(response_text: str) -> Dict:
        """
        Extract and parse JSON from Claude's response.
        
        Args:
            response_text: Raw response text from Claude
            
        Returns:
            Parsed dictionary or raw response if parsing fails
        """
        try:
            # Try to find JSON in the response
            start = response_text.find('{')
            end = response_text.rfind('}') + 1
            
            if start != -1 and end > start:
                json_str = response_text[start:end]
                return json.loads(json_str)
            else:
                return {"raw_analysis": response_text}
                
        except json.JSONDecodeError:
            return {"raw_analysis": response_text}