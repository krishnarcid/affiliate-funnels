#!/usr/bin/env python3
"""
Twitter OAuth 2.0 Authorization URL Generator
User needs to click this URL and authorize the app
"""
import json
import base64
import urllib.parse

# Load credentials
with open(r'C:\Users\krish\.openclaw\workspace\config\twitter-oauth2.json', 'r') as f:
    creds = json.load(f)

client_id = creds['client_id']
redirect_uri = creds['callback_uri']
scope = "tweet.read tweet.write users.read offline.access"

# Generate PKCE values (for security)
import secrets
code_verifier = secrets.token_urlsafe(32)
code_challenge = base64.urlsafe_b64encode(
    base64.urlsafe_b64decode(code_verifier + '==')
).decode('utf-8').rstrip('=')

# Save code verifier for later
creds['code_verifier'] = code_verifier
with open(r'C:\Users\krish\.openclaw\workspace\config\twitter-oauth2.json', 'w') as f:
    json.dump(creds, f, indent=2)

# Build authorization URL
params = {
    'response_type': 'code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'scope': scope,
    'state': secrets.token_urlsafe(16),
    'code_challenge': code_challenge,
    'code_challenge_method': 'S256'
}

auth_url = f"https://twitter.com/i/oauth2/authorize?{urllib.parse.urlencode(params)}"

print("=" * 60)
print("TWITTER OAUTH 2.0 AUTHORIZATION REQUIRED")
print("=" * 60)
print("\nStep 1: Click this URL to authorize:\n")
print(auth_url)
print("\nStep 2: After authorizing, Twitter will redirect to:")
print(redirect_uri)
print("\nStep 3: Copy the 'code' parameter from the URL")
print("         (looks like: ?code=ABC123...)")
print("\nStep 4: Send me that code!")
print("=" * 60)

# Save the expected state
creds['expected_state'] = params['state']
with open(r'C:\Users\krish\.openclaw\workspace\config\twitter-oauth2.json', 'w') as f:
    json.dump(creds, f, indent=2)
