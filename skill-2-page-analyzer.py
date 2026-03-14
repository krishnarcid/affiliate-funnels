#!/usr/bin/env python3
"""
SKILL 2: Landing Page Analyzer
Extracts copy, identifies weaknesses, scores readability
"""
import requests
from bs4 import BeautifulSoup
import re

def analyze_landing_page(url):
    """Analyze landing page for copy issues"""
    print("=" * 70)
    print("SKILL 2: Landing Page Analyzer")
    print("=" * 70)
    
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract text
        text = soup.get_text()
        
        # Analyze issues
        issues = []
        
        # Check for long sentences
        sentences = text.split('.')
        long_sentences = [s for s in sentences if len(s) > 100]
        if long_sentences:
            issues.append(f"Long sentences: {len(long_sentences)}")
        
        # Check for CTA
        has_cta = any(word in text.lower() for word in ['sign up', 'get started', 'buy now', 'click here'])
        if not has_cta:
            issues.append("No clear CTA found")
        
        # Check word count
        words = len(text.split())
        if words > 500:
            issues.append(f"Too much text: {words} words")
        
        # Score
        score = 100 - (len(issues) * 20)
        
        result = {
            "url": url,
            "word_count": words,
            "issues": issues,
            "score": score,
            "status": "ANALYZED"
        }
        
        print(f"✓ Analyzed: {url}")
        print(f"✓ Score: {score}/100")
        print(f"✓ Issues: {len(issues)}")
        print("=" * 70)
        return result
        
    except Exception as e:
        print(f"✗ Error: {e}")
        return None

if __name__ == "__main__":
    # Test
    analyze_landing_page("https://example.com")
