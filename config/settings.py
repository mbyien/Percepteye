#!/usr/bin/env python3.8
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "claude-sonnet-4-20250514")
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "3000"))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    # Default field names
    DEFAULT_TEXT_FIELD = "text"
    DEFAULT_AUTHOR_FIELD = "author"

settings = Settings()
