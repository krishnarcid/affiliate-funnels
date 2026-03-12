#!/usr/bin/env python3
"""
Deploy affiliate funnels to Netlify
"""
import json
import requests
import zipfile
import os
from pathlib import Path

NETLIFY_API = "https://api.netlify.com/api/v1"

def deploy_to_netlify(auth_token, site_name, directory):
    """Deploy a directory to Netlify"""
    
    # Create site if doesn't exist
    headers = {"Authorization": f"Bearer {auth_token}"}
    
    # Zip the directory
    zip_path = f"{site_name}.zip"
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, directory)
                zf.write(file_path, arcname)
    
    print(f"Created {zip_path}")
    
    # Create site
    site_data = {"name": site_name}
    resp = requests.post(
        f"{NETLIFY_API}/sites",
        headers=headers,
        json=site_data
    )
    
    if resp.status_code == 201:
        site = resp.json()
        site_id = site['id']
        deploy_url = site['url']
        print(f"Site created: {deploy_url}")
        
        # Deploy zip
        with open(zip_path, 'rb') as f:
            deploy_resp = requests.post(
                f"{NETLIFY_API}/sites/{site_id}/deploys",
                headers={**headers, "Content-Type": "application/zip"},
                data=f
            )
        
        if deploy_resp.status_code == 200:
            print(f"Deployed! URL: {deploy_url}")
            return deploy_url
    else:
        print(f"Error: {resp.text}")
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python deploy.py <netlify-auth-token>")
        print("Get token from: https://app.netlify.com/user/applications/personal")
        sys.exit(1)
    
    token = sys.argv[1]
    deploy_to_netlify(token, "affiliate-funnels", ".")
