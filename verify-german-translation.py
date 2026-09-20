#!/usr/bin/env python3
"""
Verify German translation completeness
Check for any remaining English text patterns
"""

import re
from pathlib import Path

def check_english_patterns(filepath):
    """Check for common English patterns that shouldn't be in German pages"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Patterns that indicate English text (excluding technical terms and brand names)
    english_patterns = [
        (r'\bdownload\b(?!\.html)', 'download (should be herunterladen)'),
        (r'\bwatermark\b', 'watermark (should be Wasserzeichen)'),
        (r'\bfree\b(?! TikTok)', 'free (should be kostenlos)'),
        (r'\bfast\b', 'fast (should be schnell)'),
        (r'\bthumbnail\b', 'thumbnail (should be Miniaturansicht)'),
        (r'\bstory\b(?!\.html)', 'story (should be Story/Geschichte)'),
        (r'\bquality\b', 'quality (should be Qualität)'),
        (r'\bdevice\b', 'device (should be Gerät)'),
        (r'\bsafe\b', 'safe (should be sicher)'),
        (r'\bprivate\b', 'private (should be privat)'),
        (r'(?i)\busing\b', 'using (should be verwenden)'),
        (r'(?i)\bwithout\b', 'without (should be ohne)'),
        (r'(?i)\bthe best\b', 'the best (should be der beste)'),
        (r'(?i)\ball devices\b', 'all devices (should be alle Geräte)'),
        (r'(?i)\bour TikTok video downloader\b', 'our TikTok video downloader (check translation)'),
    ]
    
    issues_found = []
    
    # Skip script tags and style tags
    content_without_scripts = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
    content_without_styles = re.sub(r'<style[^>]*>.*?</style>', '', content_without_scripts, flags=re.DOTALL)
    
    # Also skip URLs and technical attributes
    content_check = re.sub(r'(href|src|content|id|class|data-[^=]*)="[^"]*"', '', content_without_styles)
    
    for pattern, description in english_patterns:
        matches = re.findall(pattern, content_check, re.IGNORECASE)
        if matches:
            # Get context for each match
            for match in set(matches):
                context_pattern = f'.{{0,50}}{re.escape(match)}.{{0,50}}'
                contexts = re.findall(context_pattern, content_check, re.IGNORECASE)
                if contexts:
                    issues_found.append({
                        'pattern': description,
                        'match': match,
                        'context': contexts[0][:100]
                    })
    
    return issues_found

def generate_report():
    """Generate verification report for German pages"""
    
    files = [
        "frontend/de/index.html",
        "frontend/de/mp3.html",
        "frontend/de/miniatur.html",
        "frontend/de/story.html"
    ]
    
    print("=" * 70)
    print("GERMAN TRANSLATION VERIFICATION REPORT")
    print("=" * 70)
    print()
    
    all_clean = True
    
    for filepath in files:
        print(f"\n📄 Checking: {filepath}")
        print("-" * 70)
        
        if not Path(filepath).exists():
            print(f"❌ File not found: {filepath}")
            continue
        
        issues = check_english_patterns(filepath)
        
        if issues:
            all_clean = False
            print(f"⚠️  Found {len(issues)} potential issue(s):\n")
            for i, issue in enumerate(issues, 1):
                print(f"{i}. {issue['pattern']}")
                print(f"   Match: '{issue['match']}'")
                print(f"   Context: ...{issue['context']}...")
                print()
        else:
            print("✅ No English patterns detected - looks good!")
    
    print("\n" + "=" * 70)
    if all_clean:
        print("🎉 ALL GERMAN PAGES VERIFIED - TRANSLATION COMPLETE!")
    else:
        print("⚠️  Some potential issues found - please review above")
    print("=" * 70)

if __name__ == "__main__":
    generate_report()
