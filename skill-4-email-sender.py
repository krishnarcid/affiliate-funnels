#!/usr/bin/env python3
"""
SKILL 4: Email Sequence Manager
Automates Gmail sending with tracking
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

def send_audit_email(to_email, company, founder_name, visual_path):
    """Send Your Copy Sucks audit email"""
    print("=" * 70)
    print("SKILL 4: Email Sequence Manager")
    print("=" * 70)
    
    # Load credentials
    with open("../config/email-config.json") as f:
        config = json.load(f)
    
    subject = "Quick feedback on your landing page copy (not a sales pitch)"
    
    body = f"""Hi {founder_name},

I was looking at {company}'s landing page and noticed something in your copy that might be hurting conversions.

Attached: A quick visual audit pointing out the specific issue.

Not trying to sell you anything - just thought you'd find it useful since I specialize in landing page copy for SaaS companies.

Best,
Krishna
yourcopysucks.in"""
    
    msg = MIMEMultipart()
    msg['From'] = config['sender_email']
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(config['smtp_server'], config['smtp_port'])
        server.starttls()
        server.login(config['sender_email'], config['sender_password'])
        server.send_message(msg)
        server.quit()
        
        print(f"✓ Email sent to: {to_email}")
        print(f"✓ Company: {company}")
        print("=" * 70)
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    print("Email skill ready. Use send_audit_email() function.")
