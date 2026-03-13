#!/usr/bin/env python3
"""
SDR HUNTER - Self-Sourced Lead Generation
Director: Nila | Target: 10 prospects/day | Autonomy: Full
Protocols: Your Copy Sucks + Sacredbod
"""
import datetime
import os
import json

def search_linkedin():
    """Search LinkedIn for prospects"""
    queries = [
        "SaaS founder looking for copywriter",
        "Coaching business landing page help",
        "Agency owner marketing tools",
        "Startup landing page copy critique"
    ]
    return queries

def search_twitter():
    """Search Twitter for complaints"""
    queries = [
        "hate my landing page copy",
        "need help with website copy",
        "CRM too expensive",
        "ClickFunnels slow",
        "marketing agency struggles",
        "high GHL costs"
    ]
    return queries

def search_google_maps():
    """Search Google Maps for local businesses"""
    niches = ["marketing agencies", "business coaches", "SaaS companies"]
    return niches

def audit_landing_page(url):
    """Analyze landing page for copy issues"""
    issues = [
        "Long-winded sentences",
        "No clear CTA above fold",
        "Corporate fluff language",
        "Confusing value proposition",
        "Too much text, no scannability",
        "Weak headline"
    ]
    return issues

def find_founder_email(company_url):
    """Find founder contact info"""
    sources = [
        "LinkedIn company page",
        "Company website /about",
        "Company website /team",
        "Apollo.io",
        "Hunter.io"
    ]
    return sources

def generate_audit_visual(company, issue):
    """Generate landing page audit visual"""
    prompt = f"""Professional landing page audit visual for {company}.
    
    Clean critique showing:
    - "LANDING PAGE AUDIT" header
    - Issue found: {issue}
    - Before/After text comparison
    - Navy blue and white color scheme
    - Professional, helpful tone
    - yourcopysucks.in watermark
    - 1200x630px format
    
    Style: Minimalist, professional, constructive criticism"""
    
    return prompt

def send_audit_email(company, founder_email, founder_name, visual_path):
    """Send Your Copy Sucks audit email"""
    subject = "Quick feedback on your landing page copy (not a sales pitch)"
    
    body = f"""Hi {founder_name},

I was looking at {company}'s landing page and noticed something in your copy that might be hurting conversions.

Attached: A quick visual audit pointing out the specific issue.

Not trying to sell you anything - just thought you'd find it useful since I specialize in landing page copy for SaaS companies.

Best,
Krishna
yourcopysucks.in"""
    
    return {"subject": subject, "body": body}

def sacredbod_reply(complaint_text):
    """Generate Sacredbod protocol reply"""
    
    templates = {
        "tool_costs": """I had the exact same issue - paying $297/mo for tools that barely talked to each other.

Here's what worked:

1. Audit which tools you actually use vs. pay for
2. Find one platform that replaces your top 3
3. Migrate in phases (don't rush)

We ended up cutting our stack from $297/mo to $97/mo with better integration.

DM me if you want the specific setup - happy to share.""",

        "crm_slow": """Had this exact frustration with our CRM.

3-step fix:
1. Consolidate CRM + email + pipeline into ONE platform
2. Set up automated follow-up sequences
3. Create alerts for hot leads

Now one login, one dashboard, $97/mo instead of five bills.

Works for us at Sacredbod.""",

        "automation_hard": """Setting up automation doesn't need to be complex.

Start simple:
1. Map your #1 manual process
2. Set trigger → action (e.g., form fill → email)
3. Build from there

I used to spend 10 hrs/week on manual follow-up. Now 1 hr.

The key is ONE platform that does it all, not five that kind-of integrate."""
    }
    
    return templates

def update_leads_crm(company, source, pain_point, action, status):
    """Update LEADS.md in real-time"""
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    
    new_entry = f"""
| {company} | {source} | {pain_point} | {action} | {status} | {timestamp} |
"""
    
    leads_file = r"C:\Users\krish\.openclaw\workspace\LEADS.md"
    
    try:
        with open(leads_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the table and append
        lines = content.split('\n')
        table_start = None
        for i, line in enumerate(lines):
            if 'Company Name' in line and 'Source URL' in line:
                table_start = i + 2
                break
        
        if table_start:
            lines.insert(table_start, new_entry.strip())
            new_content = '\n'.join(lines)
            
            with open(leads_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ LEADS.md updated: {company} | {status}")
            return True
    except Exception as e:
        print(f"✗ Error updating LEADS.md: {e}")
        return False

def main():
    print("=" * 80)
    print("SDR HUNTER - Self-Sourced Lead Generation")
    print("Director: Nila | Target: 10 prospects/day")
    print("Protocols: Your Copy Sucks + Sacredbod")
    print("=" * 80)
    print()
    
    print("HUNTING PROTOCOLS:")
    print("-" * 80)
    print()
    print("1. YOUR COPY SUCKS (Landing Page Audits)")
    print("   Target: SaaS/Coaching with weak copy")
    print("   Search: LinkedIn, Twitter, Google Maps")
    print("   Action: Audit → Generate visual → Send email")
    print()
    print("   Search queries:")
    for q in search_linkedin():
        print(f"     - {q}")
    print()
    
    print("   Audit criteria:")
    for issue in audit_landing_page(""):
        print(f"     - {issue}")
    print()
    
    print("   Email template:")
    print("     Subject: Quick feedback on your landing page copy")
    print("     Body: Value-first, attach audit visual")
    print()
    
    print("2. SACREDBOD (Tool Migration)")
    print("   Target: People complaining about tool costs")
    print("   Search: Social media complaints")
    print("   Action: Reply with value → Bridge to PORTFOLIO.md")
    print()
    print("   Keywords to monitor:")
    for q in search_twitter():
        print(f"     - {q}")
    print()
    
    print("   Reply strategy:")
    print("     - 3-step actionable solution")
    print("     - Bridge to Sacredbod URL")
    print("     - No hard sell")
    print()
    
    print("3. REAL-TIME CRM")
    print("   File: LEADS.md")
    print("   Columns: Company | Source | Pain Point | Action | Status | Timestamp")
    print("   Update: Immediately after contact")
    print()
    
    print("=" * 80)
    print("DAILY TARGET: 10 prospects")
    print("  - 5 Your Copy Sucks audits")
    print("  - 5 Sacredbod replies")
    print("  - All logged to LEADS.md")
    print()
    print("Next hunt: Tomorrow 09:00 AM")
    print("=" * 80)

if __name__ == "__main__":
    main()
