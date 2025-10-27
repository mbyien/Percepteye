#!/usr/bin/env python3.8
import json
from typing import List, Dict
from pathlib import Path

class DataLoader:
    """Handles loading Twitter comment data from JSON files."""
    
    @staticmethod
    def load(file_path: str) -> List[Dict]:
        """
        Load Twitter comments from a JSON file.
        
        Args:
            file_path: Path to the JSON file
            
        Returns:
            List of comment dictionaries
            
        Raises:
            FileNotFoundError: If file doesn't exist
            json.JSONDecodeError: If file is not valid JSON
        """
        path = Path(file_path)
        
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Handle both single dict and list of dicts
        return data if isinstance(data, list) else [data]
    
    def save_results(results: Dict, output_path: str):
        """
        Save analysis results to a JSON file.
        
        Args:
            results: Analysis results dictionary
            output_path: Path to save the output file
        """
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)