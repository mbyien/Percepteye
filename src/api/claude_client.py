#!/usr/bin/env python3.8
import anthropic
from typing import Dict
from config.settings import settings

class ClaudeClient:
    """Wrapper for Claude API interactions."""
    
    def __init__(self, api_key: str = None):
        """
        Initialize Claude client.
        
        Args:
            api_key: Anthropic API key (defaults to settings)
        """
        self.api_key = api_key or settings.ANTHROPIC_API_KEY
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not set")
        
        self.client = anthropic.Anthropic(api_key=self.api_key)
    
    def send_message(self, prompt: str, model: str = None, max_tokens: int = None) -> str:
        """
        Send a message to Claude and get response.
        
        Args:
            prompt: The prompt to send
            model: Model to use (defaults to settings)
            max_tokens: Max tokens in response (defaults to settings)
            
        Returns:
            Response text from Claude
        """
        model = model or settings.DEFAULT_MODEL
        max_tokens = max_tokens or settings.MAX_TOKENS
        
        message = self.client.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return message.content[0].text