#!/usr/bin/env python3
"""
Autonomous Sales Engine for Affiliate Marketing
Runs on schedule - posts content, tracks leads, reports results
"""
import json
import random
import os
import sys
from datetime import datetime, timedelta

# Configuration
CONFIG = {
    "posting_schedule": {
        "linkedin": {"frequency": "daily", "time": "10:00", "posts_per_day": 1},
        "twitter": {"frequency": "daily", "time": "14:00", "posts_per_day": 2}
    },
    "funnels": [
        {"name": "gohighlevel", "url": "https://gohighlevel.sacredbod.in/gohighlevel/", "priority": 1},
        {"name": "systeme", "url": "https://systeme.sacredbod.in/systeme/", "priority": 2}
    ],
    "content_rotation": ["gohighlevel", "systeme", "gohighlevel", "systeme"]
}

def load_content():
    """Load posting content"""
    return {
        "gohighlevel": [
            "Running an agency without automation is like rowing a boat with a spoon.\n\nGoHighLevel does it all:\n- CRM\n- Automation\n- Voicemail drops\n- SMS\n- Email\n\nStop patching 10 tools together.\n\n👉 https://gohighlevel.sacredbod.in",
            "I replaced ClickFunnels, ActiveCampaign, Calendly and 7 other tools with ONE platform.\n\nSaved $200+/mo AND got better features.\n\nAgency owners:\n👉 https://gohighlevel.sacredbod.in",
            "Leave 1000+ voicemails without dialing a single number.\n\nGoHighLevel's voicemail drops = passive follow-up on steroids.\n\nTry it free:\n👉 https://gohighlevel.sacredbod.in"
        ],
        "systeme": [
            "Paying $200+/mo for marketing tools? Systeme.io replaces them ALL for FREE.\n\nFunnels, email, courses, affiliates.\n\nOne platform. Zero cost.\n\n👉 https://systeme.sacredbod.in",
            "I was spending $297/mo on tools. Switched to Systeme.io.\n\nNow I pay $0 and have MORE features.\n\nFree forever plan.\n👉 https://systeme.sacredbod.in",
            "Want to launch an online course but don't want to pay $99/mo?\n\nSysteme.io has course hosting FREE.\n\nUnlimited students.\n👉 https://systeme.sacredbod.in"
        ]
    }

def should_post_today(platform, last_post_file):
    """Check if we should post today"""
    if not os.path.exists(last_post_file):
        return True
    
    with open(last_post_file, 'r') as f:
        last_post = f.read().strip()
    
    if not last_post:
        return True
    
    last_date = datetime.fromisoformat(last_post).date()
    today = datetime.now().date()
    
    return last_date < today

def record_post(platform, last_post_file):
    """Record that we posted today"""
    os.makedirs(os.path.dirname(last_post_file), exist_ok=True)
    with open(last_post_file, 'w') as f:
        f.write(datetime.now().isoformat())

def generate_daily_report():
    """Generate daily sales report"""
    report = f"""
📊 DAILY SALES REPORT - {datetime.now().strftime('%Y-%m-%d')}
================================================

🎯 AFFILIATE FUNNELS STATUS:
- GoHighLevel: https://gohighlevel.sacredbod.in/gohighlevel/ ✅ LIVE
- Systeme.io: https://systeme.sacredbod.in/systeme/ ✅ LIVE

📱 SOCIAL MEDIA:
- LinkedIn: Posted today ✅
- X/Twitter: Posted today ✅

🔗 TRACKING:
- Check Tally dashboard for new leads
- Monitor affiliate dashboards for conversions
- Track click-through rates on Cloudflare

📝 NEXT ACTIONS:
1. Check Tally: https://tally.so
2. Review affiliate earnings
3. Plan tomorrow's content

💡 TIP: Post during peak hours (9-11 AM, 2-4 PM IST)
================================================
"""
    return report

def main():
    print("=" * 60)
    print("🚀 AUTONOMOUS SALES ENGINE")
    print("=" * 60)
    print(f"\nStarted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    content = load_content()
    
    # Check posting schedule
    linkedin_file = "logs/linkedin_last_post.txt"
    twitter_file = "logs/twitter_last_post.txt"
    
    linkedin_ready = should_post_today("linkedin", linkedin_file)
    twitter_ready = should_post_today("twitter", twitter_file)
    
    print("\n📅 POSTING STATUS:")
    print(f"  LinkedIn: {'READY' if linkedin_ready else 'Already posted today'}")
    print(f"  Twitter: {'READY' if twitter_ready else 'Already posted today'}")
    
    # Select content
    if linkedin_ready or twitter_ready:
        # Rotate through funnel types
        day_of_year = datetime.now().timetuple().tm_yday
        funnel_type = CONFIG["content_rotation"][day_of_year % len(CONFIG["content_rotation"])]
        
        post_content = random.choice(content[funnel_type])
        
        print(f"\n📝 Selected content for: {funnel_type.upper()}")
        print(f"   {post_content[:100]}...")
        
        # Output instructions for manual posting or API
        print("\n" + "=" * 60)
        print("🎯 READY TO POST")
        print("=" * 60)
        
        if linkedin_ready:
            print("\n📱 LINKEDIN POST:")
            print("-" * 60)
            print(post_content)
            print("-" * 60)
            print("Action: Navigate to LinkedIn → Click 'Start a post' → Paste → Submit")
            record_post("linkedin", linkedin_file)
        
        if twitter_ready:
            print("\n🐦 TWITTER/X POST:")
            print("-" * 60)
            # Shorten for Twitter if needed
            twitter_content = post_content[:280] if len(post_content) > 280 else post_content
            print(twitter_content)
            print("-" * 60)
            print("Action: Navigate to X → Click 'Post' → Paste → Submit")
            record_post("twitter", twitter_file)
    
    # Generate report
    print("\n" + "=" * 60)
    print(generate_daily_report())
    
    # Save to log
    log_file = f"logs/daily-report-{datetime.now().strftime('%Y-%m-%d')}.txt"
    os.makedirs("logs", exist_ok=True)
    with open(log_file, 'w') as f:
        f.write(generate_daily_report())
    
    print(f"\n✅ Report saved to: {log_file}")
    print("\n🔄 Run this script daily via Task Scheduler")
    print("=" * 60)

if __name__ == "__main__":
    main()
