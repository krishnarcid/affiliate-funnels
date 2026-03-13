#!/usr/bin/env python3
"""
Sales Engine - Daily Automation Checklist
"""
import datetime
import os

def main():
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    day = datetime.datetime.now().timetuple().tm_yday
    
    # Rotate content
    funnels = ["GoHighLevel", "Systeme.io", "GoHighLevel", "Systeme.io"]
    funnel = funnels[day % len(funnels)]
    
    print("="*60)
    print("AUTONOMOUS SALES ENGINE - " + date)
    print("="*60)
    print()
    print("TODAY'S FUNNEL: " + funnel)
    print()
    
    if funnel == "GoHighLevel":
        print("LINKEDIN POST:")
        print("-"*60)
        print("Running an agency used to mean managing 10+ different tools:")
        print()
        print("ClickFunnels for funnels")
        print("ActiveCampaign for email")
        print("Calendly for booking")
        print("Zapier for connections")
        print("Plus 6 more...")
        print()
        print("I replaced ALL of them with ONE platform: GoHighLevel")
        print()
        print("Link: https://gohighlevel.sacredbod.in/gohighlevel/")
        print("-"*60)
        print()
        print("TWITTER/X POST:")
        print("-"*60)
        print("Running an agency without automation is like rowing a boat")
        print("with a spoon. GoHighLevel does it all.")
        print()
        print("Link: https://gohighlevel.sacredbod.in")
        
    else:
        print("LINKEDIN POST:")
        print("-"*60)
        print("Paying $200+/mo for marketing tools?")
        print("Systeme.io replaces them ALL for FREE.")
        print()
        print("Funnels, email, courses, affiliates.")
        print("One platform. Zero cost.")
        print()
        print("Link: https://systeme.sacredbod.in/systeme/")
        print("-"*60)
        print()
        print("TWITTER/X POST:")
        print("-"*60)
        print("Email marketing should not cost $29/mo.")
        print("Systeme.io gives unlimited emails FREE.")
        print()
        print("Link: https://systeme.sacredbod.in")
    
    print("-"*60)
    print()
    print("ACTIONS:")
    print("  [ ] Copy content above")
    print("  [ ] Post to LinkedIn (10 AM IST)")
    print("  [ ] Post to X/Twitter (2 PM IST)")
    print("  [ ] Check Tally dashboard for leads")
    print("  [ ] Check affiliate dashboards for clicks")
    print()
    print("TALLY DASHBOARD: https://tally.so")
    print("AFFILIATE LINKS:")
    print("  - GoHighLevel: https://gohighlevel.sacredbod.in")
    print("  - Systeme.io: https://systeme.sacredbod.in")
    print()
    print("NEXT RUN: Tomorrow same time")
    print("="*60)
    
    # Save to file
    os.makedirs("logs", exist_ok=True)
    with open("logs/today-checklist.txt", "w") as f:
        f.write("Sales Engine - " + date + "\n")
        f.write("Funnel: " + funnel + "\n")
        f.write("Status: READY TO POST\n")
    
    print("\nChecklist saved to: logs/today-checklist.txt")

if __name__ == "__main__":
    main()
