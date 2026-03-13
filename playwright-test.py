#!/usr/bin/env python3
"""
Playwright Test - SDR Hunter Automation
Director: Nila | 24/7 Browser Automation
"""
from playwright.sync_api import sync_playwright
import time

def test_linkedin_hunt():
    """Test LinkedIn prospect hunting with Playwright"""
    print("=" * 70)
    print("PLAYWRIGHT TEST - LinkedIn SDR Hunter")
    print("=" * 70)
    print()
    
    with sync_playwright() as p:
        # Launch browser
        print("Launching Chromium...")
        browser = p.chromium.launch(headless=False)  # Visible for testing
        context = browser.new_context()
        page = context.new_page()
        
        # Navigate to LinkedIn
        print("Navigating to LinkedIn...")
        page.goto("https://www.linkedin.com")
        
        # Wait for load
        page.wait_for_load_state("networkidle")
        print("Page loaded")
        print(f"  URL: {page.url}")
        print(f"  Title: {page.title()}")
        
        # Check if logged in
        try:
            # Look for search box (means logged in)
            search_box = page.wait_for_selector('input[placeholder="Search"]', timeout=5000)
            if search_box:
                print("Already logged in")
        except:
            print("Not logged in - will need authentication")
        
        # Search for SaaS companies
        print("\nSearching for 'SaaS startup'...")
        page.goto("https://www.linkedin.com/search/results/companies/?keywords=SaaS%20startup")
        page.wait_for_load_state("networkidle")
        
        # Extract company names
        companies = page.query_selector_all('a[href*="/company/"]')
        print(f"Found {len(companies)} company links")
        
        # Get first 5 company names
        print("\nFirst 5 companies:")
        for i, company in enumerate(companies[:5], 1):
            name = company.inner_text()
            href = company.get_attribute('href')
            print(f"  {i}. {name[:50]}... ({href[:40]}...)")
        
        # Screenshot
        print("\nTaking screenshot...")
        page.screenshot(path="logs/playwright-test.png")
        print("✓ Screenshot saved: logs/playwright-test.png")
        
        # Close
        browser.close()
        print("\n✓ Browser closed")
        print("=" * 70)
        print("PLAYWRIGHT TEST: SUCCESS")
        print("Ready for 24/7 SDR automation")
        print("=" * 70)

if __name__ == "__main__":
    test_linkedin_hunt()
