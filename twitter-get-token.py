#!/usr/bin/env python3
"""
Exchange Twitter OAuth 2.0 code for access token
"""
import json
import requests
import base64

# Load credentials
with open(r'C:\Users\krish\.openclaw\workspace\config\twitter-oauth2.json', 'r') as f:
    creds = json.load(f)

client_id = creds['client_id']
client_secret = creds['client_secret']
code_verifier = creds['code_verifier']
redirect_uri = creds['callback_uri']

# Authorization code from user
auth_code = "YUI0RlNNWEtDV05WNlFoa2J5MnFxZ3lUY0pxUnRSUm9aVEMtVkZBWjgyck96OjE3NzMzOTAxMTAwODA6MToxOmFjOjE"

# Exchange code for token
token_url = "https://api.twitter.com/2/oauth2/token"

# Create Basic Auth header
auth_string = f"{client_id}:{client_secret}"
auth_bytes = auth_string.encode('ascii')
auth_b64 = base64.b64encode(auth_bytes).decode('ascii')

headers = {
    "Authorization": f"Basic {auth_b64}",
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = {
    "grant_type": "authorization_code",
    "code": auth_code,
    "redirect_uri": redirect_uri,
    "code_verifier": code_verifier
}

print("Exchanging code for token...")
response = requests.post(token_url, headers=headers, data=payload)

if response.status_code == 200:
    token_data = response.json()
    print("\n✅ SUCCESS! Got access token.")
    print(f"\nAccess Token: {token_data['access_token'][:20]}...")
    print(f"Refresh Token: {token_data.get('refresh_token', 'N/A')[:20]}...")
    print(f"Expires in: {token_data.get('expires_in', 'N/A')} seconds")
    
    # Save token
    creds['access_token'] = token_data['access_token']
    creds['refresh_token'] = token_data.get('refresh_token')
    creds['expires_in'] = token_data.get('expires_in')
    creds['token_type'] = token_data.get('token_type')
    creds['scope'] = token_data.get('scope')
    creds['status'] = 'active'
    
    with open(r'C:\Users\krish\.openclaw\workspace\config\twitter-oauth2.json', 'w') as f:
        json.dump(creds, f, indent=2)
    
    print("\n✅ Token saved to twitter-oauth2.json")
    print("\nReady to post tweets!")
else:
    print(f"\n❌ Failed: {response.status_code}")
    print(response.text)
