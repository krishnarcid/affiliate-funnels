#!/usr/bin/env python3
"""
Social Media Automation for Affiliate Marketing
Posts content to Twitter/X and LinkedIn to drive traffic to affiliate funnels
"""
import json
import random
import os
from datetime import datetime, timedelta

# Content templates for GoHighLevel
CONTENT_TEMPLATES = {
    "twitter": [
        "Running an agency without automation is like rowing a boat with a spoon.\n\nGoHighLevel does it all:\n✅ CRM\n✅ Automation\n✅ Voicemail drops\n✅ SMS\n✅ Email\n\nStop patching 10 tools together.\n\n👉 https://gohighlevel.sacredbod.in",
        
        "I replaced:\n• ClickFunnels ($97/mo)\n• ActiveCampaign ($29/mo)\n• Calendly ($10/mo)\n• And 7 other tools\n\nWith ONE platform:\n\nGoHighLevel ($97/mo)\n\nSaved $200+/mo AND got better features.\n\nAgency owners, try it:\n👉 https://gohighlevel.sacredbod.in",
        
        "Leave 1000+ voicemails without dialing a single number.\n\nGoHighLevel's voicemail drops = passive follow-up on steroids.\n\nYour competitors are sleeping. You're dropping voicemails at 2am.\n\nTry it free for 14 days:\n👉 https://gohighlevel.sacredbod.in",
        
        "Indian agencies:\n\nStop charging $500/mo for manual work.\n\nAutomate 80% of it with GoHighLevel.\n\nNow you can:\n• Handle 3x more clients\n• Actually sleep\n• Charge premium rates\n\nThe playbook:\n👉 https://gohighlevel.sacredbod.in",
        
        "What I wish I knew before starting my agency:\n\nYou don't need 10 different tools.\n\nYou need ONE that does everything:\n\nGoHighLevel\n\nCRM + automation + email + SMS + funnels + courses + affiliate program\n\nAll in one.\n\nTry it:\n👉 https://gohighlevel.sacredbod.in"
    ],
    
    "linkedin": [
        """Running a marketing agency used to mean managing 10+ different tools:\n\nClickFunnels for funnels\nActiveCampaign for email\nCalendly for booking\nZapier for connections\nPlus 6 more...\n\nEach with their own:\n❌ Monthly bill\n❌ Learning curve\n❌ Integration headaches\n❌ Support tickets\n\nI replaced ALL of them with ONE platform.\n\nGoHighLevel.\n\n$97/month. One login. Everything connected natively.\n\nIn 2024, simplicity wins.\n\nIf you're running an agency and still patching together 5+ tools, you're leaving money on the table.\n\nTry GoHighLevel free for 14 days:\n👉 https://gohighlevel.sacredbod.in\n\n#AgencyLife #Automation #SaaS""",
        
        """The agency owners making $50k+/mo have a secret:\n\nThey automate 80% of client work.\n\nNot by hiring more people.\nNot by working 80-hour weeks.\n\nBy using systems that work while they sleep.\n\nGoHighLevel is that system:\n\n✅ Visual automation builder (if-this-then-that on steroids)\n✅ Voicemail drops (1000+ in minutes, no dialing)\n✅ SMS/email sequences (auto-nurture leads)\n✅ Pipeline management (see every deal)\n✅ Mobile app (manage from anywhere)\n\nI used to spend 40 hours/week on client delivery.\n\nNow? 10 hours.\n\nSame results. Better retention. Higher margins.\n\nThe difference isn't hustle.\n\nIt's leverage.\n\nIf you're serious about scaling your agency, check this out:\n👉 https://gohighlevel.sacredbod.in\n\n#AgencyGrowth #Automation #Scale""",
        
        """Most agency owners are one client away from burnout.\n\nWhy?\n\nBecause they're doing everything manually.\n\n• Manual follow-ups\n• Manual reporting\n• Manual scheduling\n• Manual everything\n\nThe solution isn't working harder.\n\nIt's building systems that don't need you.\n\nGoHighLevel automates:\n✅ Lead capture → nurture → booking\n✅ Onboarding sequences\n✅ Monthly reporting\n✅ Review requests\n✅ Referral asks\n\nYour clients get BETTER service.\nYou get your life back.\n\nI made the switch 6 months ago. Best decision ever.\n\nTry it free:\n👉 https://gohighlevel.sacredbod.in\n\n#AgencyOwner #WorkLifeBalance #Automation"""
    ]
}

def generate_posts(count=5):
    """Generate random social media posts"""
    posts = []
    
    for platform in ["twitter", "linkedin"]:
        templates = CONTENT_TEMPLATES[platform]
        selected = random.sample(templates, min(count, len(templates)))
        for post in selected:
            posts.append({
                "platform": platform,
                "content": post,
                "created_at": datetime.now().isoformat()
            })
    
    return posts

def save_posts(posts, filename="social-posts.json"):
    """Save posts to file"""
    with open(filename, 'w') as f:
        json.dump(posts, f, indent=2)
    print(f"Saved {len(posts)} posts to {filename}")

def schedule_posts():
    """Generate posting schedule"""
    schedule = []
    base_time = datetime.now() + timedelta(hours=2)
    
    for i in range(7):  # Next 7 days
        # Twitter: Morning (8-10am) and Evening (6-8pm)
        schedule.append({
            "time": base_time.replace(hour=8, minute=random.randint(0,59)) + timedelta(days=i),
            "platform": "twitter",
            "content": "[Generated]"
        })
        schedule.append({
            "time": base_time.replace(hour=18, minute=random.randint(0,59)) + timedelta(days=i),
            "platform": "twitter",
            "content": "[Generated]"
        })
        
        # LinkedIn: Mid-morning (9-11am) Tuesday/Thursday
        if i % 2 == 0:  # Every other day
            schedule.append({
                "time": base_time.replace(hour=10, minute=random.randint(0,59)) + timedelta(days=i),
                "platform": "linkedin",
                "content": "[Generated]"
            })
    
    return sorted(schedule, key=lambda x: x["time"])

if __name__ == "__main__":
    print("🚀 Social Media Automation for GoHighLevel Affiliate")
    print("=" * 50)
    
    # Generate posts
    posts = generate_posts(count=3)
    save_posts(posts)
    
    # Generate schedule
    schedule = schedule_posts()
    
    print(f"\n📅 Next 7 Days Schedule:")
    print("-" * 50)
    for post in schedule[:5]:  # Show first 5
        print(f"{post['time'].strftime('%Y-%m-%d %H:%M')} | {post['platform'].upper()}")
    print(f"... and {len(schedule)-5} more posts")
    
    print("\n✅ To post automatically, you need:")
    print("   1. Twitter/X API credentials")
    print("   2. LinkedIn API credentials")
    print("   3. Or use a scheduler like Buffer/Hootsuite")
    
    print("\n💾 Posts saved to social-posts.json")
    print("   Review and copy to your scheduler!")
