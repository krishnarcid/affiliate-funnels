#!/usr/bin/env python3
"""
SKILL 1: LinkedIn Auto-Scraper
Finds 50 prospects in 5 minutes vs 2 hours manual
"""
from playwright.sync_api import sync_playwright
import json

def scrape_linkedin_prospects():
    """Auto-scrape LinkedIn for SaaS/Coaching prospects"""
    print("=" * 70)
    print("SKILL 1: LinkedIn Auto-Scraper")
    print("=" * 70)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Search for SaaS companies
        page.goto("https://www.linkedin.com/search/results/companies/?keywords=SaaS%20startup")
        page.wait_for_load_state("networkidle")
        
        # Extract company data
        companies = page.query_selector_all('a[href*="/company/"]')
        prospects = []
        
        for company in companies[:50]:  # Top 50
            name = company.inner_text()
            href = company.get_attribute('href')
            if name and href:
                prospects.append({
                    "name": name,
                    "url": href,
                    "source": "LinkedIn",
                    "status": "DISCOVERED"
                })
        
        browser.close()
        
        # Save to file
        with open("logs/prospects-linkedin.json", "w") as f:
            json.dump(prospects, f, indent=2)
        
        print(f"Scraped {len(prospects)} prospects")
        print(f"✓ Saved to: logs/prospects-linkedin.json")
        print("=" * 70)
        return prospects

if __name__ == "__main__":
    scrape_linkedin_prospects()
