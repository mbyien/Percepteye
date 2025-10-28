#!/usr/bin/env python3.8
import sys
import argparse
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.data.loader import DataLoader
from src.analysis.sentiment_analyzer import SentimentAnalyzer
from src.utils.formatter import ReportFormatter
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

def main():
    """Main entry point for sentiment analysis."""
    parser = argparse.ArgumentParser(
        description="Analyze sentiment of Twitter comments using Claude AI"
    )
    parser.add_argument(
        "input_file",
        help="Path to input JSON file containing Twitter comments"
    )
    parser.add_argument(
        "-o", "--output",
        help="Path to output JSON file (default: data/output/results.json)",
        default="data/output/results.json"
    )
    parser.add_argument(
        "-f", "--field",
        help="JSON field containing comment text (default: 'text')",
        default="text"
    )
    parser.add_argument(
        "--no-display",
        help="Don't display formatted report",
        action="store_true"
    )
    
    args = parser.parse_args()
    
    try:
        # Load data
        logger.info(f"Loading comments from {args.input_file}")
        loader = DataLoader()
        comments = loader.load(args.input_file)
        logger.info(f"Loaded {len(comments)} comments")
        
        # Analyze sentiment
        logger.info("Starting sentiment analysis...")
        analyzer = SentimentAnalyzer()
        results = analyzer.analyze(comments, text_field=args.field)
        logger.info("Analysis complete")
        
        # Display report
        if not args.no_display:
            formatter = ReportFormatter()
            formatter.print_report(results)
        
        # Save results
        loader.save_results(results, args.output)
        logger.info(f"Results saved to {args.output}")
        
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        print("\nExpected JSON format:")
        print('[')
        print('  {"text": "This is great!", "author": "user1"},')
        print('  {"text": "Not happy about this", "author": "user2"}')
        print(']')
        sys.exit(1)
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        sys.exit(1)
        
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()