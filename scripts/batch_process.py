#!/usr/bin/env python3.8
import sys
import argparse
from pathlib import Path
from typing import List

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.data.loader import DataLoader
from src.analysis.sentiment_analyzer import SentimentAnalyzer
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

def get_json_files(directory: str) -> List[Path]:
    """Get all JSON files in a directory."""
    path = Path(directory)
    return list(path.glob("*.json"))

def main():
    """Process multiple JSON files in batch."""
    parser = argparse.ArgumentParser(
        description="Batch process multiple Twitter comment files"
    )
    parser.add_argument(
        "input_dir",
        help="Directory containing JSON files"
    )
    parser.add_argument(
        "-o", "--output-dir",
        help="Output directory (default: data/output/batch/)",
        default="data/output/batch"
    )
    parser.add_argument(
        "-f", "--field",
        help="JSON field containing comment text (default: 'text')",
        default="text"
    )
    
    args = parser.parse_args()
    
    try:
        # Find all JSON files
        json_files = get_json_files(args.input_dir)
        if not json_files:
            logger.error(f"No JSON files found in {args.input_dir}")
            sys.exit(1)
        
        logger.info(f"Found {len(json_files)} files to process")
        
        # Initialize components
        loader = DataLoader()
        analyzer = SentimentAnalyzer()
        
        # Process each file
        for i, input_file in enumerate(json_files, 1):
            logger.info(f"[{i}/{len(json_files)}] Processing {input_file.name}")
            
            try:
                # Load and analyze
                comments = loader.load(str(input_file))
                results = analyzer.analyze(comments, text_field=args.field)
                
                # Save results
                output_file = Path(args.output_dir) / f"{input_file.stem}_results.json"
                loader.save_results(results, str(output_file))
                logger.info(f"  ✓ Saved to {output_file}")
                
            except Exception as e:
                logger.error(f"  ✗ Error processing {input_file.name}: {e}")
                continue
        
        logger.info("Batch processing complete")
        
    except Exception as e:
        logger.error(f"Batch processing failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()