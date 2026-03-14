#!/usr/bin/env python3
"""
SKILL 3: Visual Audit Generator
Creates audit images in 10 minutes vs 2.5 hours manual
"""
import os
from datetime import datetime

def generate_audit_visual(company, issue, score):
    """Generate landing page audit visual"""
    print("=" * 70)
    print("SKILL 3: Visual Audit Generator")
    print("=" * 70)
    
    # Create prompt for image generation
    prompt = f"""Professional landing page audit visual for {company}.
    
    Clean critique showing:
    - "LANDING PAGE AUDIT" header
    - Score: {score}/100
    - Issue: {issue}
    - Before/After text comparison
    - Navy blue and white color scheme
    - Professional, helpful tone
    - yourcopysucks.in watermark
    - 1200x630px format
    
    Style: Minimalist, professional, constructive criticism"""
    
    # Save prompt for later image generation
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"visuals/audit_{company.replace(' ', '_').lower()}_{timestamp}.txt"
    
    os.makedirs("visuals", exist_ok=True)
    with open(filename, "w") as f:
        f.write(prompt)
    
    print(f"✓ Generated prompt for: {company}")
    print(f"✓ Score: {score}/100")
    print(f"✓ Issue: {issue}")
    print(f"✓ Saved to: {filename}")
    print("=" * 70)
    
    return filename

if __name__ == "__main__":
    generate_audit_visual("Marketing Mojo", "Long sentences, no CTA", 65)
