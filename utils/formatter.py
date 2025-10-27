#!/usr/bin/env python3.8
from typing import Dict

class ReportFormatter:
    """Formats analysis results for display."""
    
    @staticmethod
    def print_report(results: Dict):
        """
        Print a formatted analysis report.
        
        Args:
            results: Analysis results dictionary
        """
        print("\n" + "="*70)
        print("DETAILED SENTIMENT & EMOTION ANALYSIS")
        print("="*70)
        print(f"\nTotal Comments Analyzed: {results.get('total_comments', 'N/A')}")
        
        if "analysis_timestamp" in results:
            print(f"Analysis Time: {results['analysis_timestamp']}")
        
        if "emotion_breakdown" in results:
            print("\n" + "-"*70)
            print("EMOTION BREAKDOWN:")
            print("-"*70)
            emotions = results["emotion_breakdown"]
            sorted_emotions = sorted(emotions.items(), key=lambda x: x[1], reverse=True)
            for emotion, pct in sorted_emotions:
                print(f"  {emotion.replace('_', ' ').title():<25} {pct:>6}%")
        
        if "sentiment_details" in results:
            print("\n" + "-"*70)
            print("DETAILED SENTIMENT BREAKDOWN:")
            print("-"*70)
            
            for sentiment_type in ["positive", "negative", "neutral"]:
                if sentiment_type in results["sentiment_details"]:
                    details = results["sentiment_details"][sentiment_type]
                    pct = details.get("percentage", 0)
                    print(f"\n{sentiment_type.upper()} ({pct}%):")
                    
                    if "subcategories" in details:
                        for subcat, subpct in details["subcategories"].items():
                            print(f"  └─ {subcat.replace('_', ' ').title():<23} {subpct:>6}%")
        
        if "key_themes" in results:
            print("\n" + "-"*70)
            print("KEY THEMES:")
            print("-"*70)
            for theme in results["key_themes"]:
                print(f"  • {theme}")
        
        if "tone_patterns" in results:
            print("\n" + "-"*70)
            print("TONE PATTERNS:")
            print("-"*70)
            for pattern in results["tone_patterns"]:
                print(f"  • {pattern}")
        
        if "summary" in results:
            print("\n" + "-"*70)
            print("SUMMARY:")
            print("-"*70)
            print(f"\n{results['summary']}\n")
        
        print("="*70 + "\n")