#!/usr/bin/env python3
"""
Twitter Automation for Affiliate Marketing
Posts content from social-content-updated.json
"""
import json
import random
import os
import sys

# Load Twitter credentials
def load_credentials():
    with open(os.path.expanduser('~/.openclaw/workspace/config/twitter.json'), 'r') as f:
        return json.load(f)

# Load posts
def load_posts():
    with open(os.path.expanduser('~/.openclaw/workspace/affiliate-funnels/social-content-updated.json'), 'r') as f:
        return json.load(f)

def post_to_twitter(text, creds):
    """Post to Twitter using API v2"""
    import requests
    from requests_oauthlib import OAuth1
    
    # OAuth1 authentication
    auth = OAuth1(
        creds['consumer_key'],
        creds['consumer_secret'],
        creds['access_token'],
        creds['access_token_secret']
    )
    
    # API v2 endpoint
    url = "https://api.twitter.com/2/tweets"
    
    payload = {"text": text}
    
    try:
        response = requests.post(url, auth=auth, json=payload)
        if response.status_code == 201:
            tweet_id = response.json()['data']['id']
            print("Posted! Tweet ID: " + str(tweet_id))
            return True
        else:
            print("Failed: " + str(response.status_code) + " - " + response.text)
            return False
    except Exception as e:
        print("Error: " + str(e))
        return False

def main():
    print("Twitter Automation for Affiliate Marketing")
    print("=" * 50)
    
    # Load credentials
    try:
        creds = load_credentials()
        print("Loaded credentials for: " + str(creds.get('username', 'unknown')))
    except Exception as e:
        print("Failed to load credentials: " + str(e))
        sys.exit(1)
    
    # Load posts
    try:
        posts = load_posts()
        print("Loaded " + str(len(posts.get('gohighlevel_twitter', []))) + " GoHighLevel posts")
        print("Loaded " + str(len(posts.get('systeme_twitter', []))) + " Systeme.io posts")
    except Exception as e:
        print("Failed to load posts: " + str(e))
        sys.exit(1)
    
    # Select random post
    all_posts = posts.get('gohighlevel_twitter', []) + posts.get('systeme_twitter', [])
    if not all_posts:
        print("No posts available")
        sys.exit(1)
    
    selected = random.choice(all_posts)
    print("\nSelected post (" + str(len(selected)) + " chars):")
    print(selected[:100] + "...")
    
    # Post
    print("\nPosting to Twitter...")
    if post_to_twitter(selected, creds):
        print("\nSUCCESS! Tweet posted.")
    else:
        print("\nFAILED. Check errors above.")
        sys.exit(1)

if __name__ == "__main__":
    # Check if requests_oauthlib is installed
    try:
        import requests_oauthlib
    except ImportError:
        print("Installing required package: requests_oauthlib...")
        os.system("pip install requests requests-oauthlib")
        print("Please run again.")
        sys.exit(0)
    
    main()
