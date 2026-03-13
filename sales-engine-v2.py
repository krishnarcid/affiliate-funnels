#!/usr/bin/env python3
"""
Sales Engine - Reads from PORTFOLIO.md Master Checklist
"""
import datetime
import os
import re

def parse_portfolio():
    """Read PORTFOLIO.md and extract active projects"""
    with open(r'C:\Users\krish\.openclaw\workspace\PORTFOLIO.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract active projects from table
    projects = []
    
    # Simple parsing - look for project rows
    if "GoHighLevel" in content:
        projects.append({
            "name": "GoHighLevel",
            "url": "https://gohighlevel.sacredbod.in/gohighlevel/",
            "problem": "Agencies overpaying for 10+ tools",
            "style": "3D Blueprint"
        })
    
    if "Systeme.io" in content:
        projects.append({
            "name": "Systeme.io",
            "url": "https://systeme.sacredbod.in/systeme/",
            "problem": "Entrepreneurs paying $200+/mo for marketing stack",
            "style": "Abstract Security"
        })
    
    return projects

def get_today_project():
    """Determine today's project based on rotation"""
    day = datetime.datetime.now().timetuple().tm_yday
    rotation = ["GoHighLevel", "Systeme.io", "GoHighLevel", "Systeme.io"]
    return rotation[day % len(rotation)]

def main():
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    time = datetime.datetime.now().strftime("%H:%M")
    
    # Read portfolio
    projects = parse_portfolio()
    today_project = get_today_project()
    
    # Find project details
    project = next((p for p in projects if p["name"] == today_project), None)
    if not project:
        project = projects[0] if projects else None
    
    print("=" * 70)
    print("PORTFOLIO MASTER CHECKLIST - " + date)
    print("=" * 70)
    print()
    print("Engine Started: " + time)
    print("Active Projects: " + str(len(projects)))
    print()
    
    if project:
        print("TODAY'S PROJECT: " + project["name"].upper())
        print("-" * 70)
        print("URL: " + project["url"])
        print("Problem: " + project["problem"])
        print("Visual Style: " + project["style"])
        print()
        
        # Get content
        content = get_content(project["name"])
        
        print("LINKEDIN CONTENT:")
        print("-" * 70)
        print(content["linkedin"])
        print("-" * 70)
        print()
        print("X/TWITTER CONTENT:")
        print("-" * 70)
        print(content["twitter"])
        print("-" * 70)
        print()
    
    print()
    print("ACTION CHECKLIST:")
    print("  [ ] Copy content above")
    print("  [ ] Post to LinkedIn (10 AM IST)")
    print("  [ ] Post to X/Twitter (2 PM IST)")
    print("  [ ] Check Tally for leads: https://tally.so")
    print("  [ ] Review affiliate dashboard")
    print("  [ ] Update PORTFOLIO.md Daily Status")
    print()
    print("=" * 70)
    print("Next: Read PORTFOLIO.md for full details")
    print("Location: C:\\Users\\krish\\.openclaw\\workspace\\PORTFOLIO.md")
    print("=" * 70)
    
    # Save log
    os.makedirs("logs", exist_ok=True)
    with open("logs/today-brief.txt", "w") as f:
        f.write("Date: " + date + "\n")
        f.write("Project: " + (project["name"] if project else "None") + "\n")
        f.write("Time: " + time + "\n")
        f.write("Status: READY TO POST\n")

def get_content(project_name):
    """Get content for project"""
    if project_name == "GoHighLevel":
        return {
            "linkedin": """Running a marketing agency used to mean managing 10+ different tools:

ClickFunnels for funnels
ActiveCampaign for email
Calendly for booking
Zapier for connections
Plus 6 more...

Each with their own:
❌ Monthly bill
❌ Learning curve
❌ Integration headaches

I replaced ALL of them with ONE platform: GoHighLevel

$97/month. One login. Everything connected natively.

Try it: https://gohighlevel.sacredbod.in/gohighlevel/

#AgencyLife #Automation #SaaS""",
            
            "twitter": """Running an agency without automation is like rowing a boat with a spoon.

GoHighLevel does it all:
- CRM
- Automation
- Voicemail drops
- SMS
- Email

Stop patching 10 tools together.

👉 https://gohighlevel.sacredbod.in"""
        }
    else:  # Systeme.io
        return {
            "linkedin": """Paying $200+/mo for marketing tools?

Systeme.io replaces them ALL for FREE.

✓ Funnel builder
✓ Email marketing
✓ Course hosting
✓ Affiliate management
✓ Automation

One platform. Zero cost.

Try it: https://systeme.sacredbod.in/systeme/

#SaaS #Entrepreneur #FreeTools""",
            
            "twitter": """Email marketing should not cost $29/mo.

Systeme.io gives you:
✓ Unlimited emails
✓ Automation
✓ Sequences

All FREE.

Start here: https://systeme.sacredbod.in"""
        }

if __name__ == "__main__":
    main()
