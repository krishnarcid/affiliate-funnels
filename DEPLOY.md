# Deploy Instructions

## Option 1: Netlify Drop (Easiest - No signup)
1. Go to https://app.netlify.com/drop
2. Drag the entire `affiliate-funnels` folder
3. Get instant URL: `https://random-name.netlify.app`
4. Configure custom domains later

## Option 2: Netlify CLI
```bash
# Install
npm install -g netlify-cli

# Login
netlify login

# Deploy
netlify deploy --prod --dir=affiliate-funnels
```

## Option 3: GitHub + Netlify
1. Push to GitHub
2. Connect repo to Netlify
3. Auto-deploy on push

## Option 4: Manual Zip Upload
1. Zip the `affiliate-funnels` folder
2. Upload to https://app.netlify.com/drop
3. Done

## Recommended: Option 1 (Now)
Fastest. No account needed. Get live URL in 30 seconds.

After deploy:
- Get the Netlify URL
- Point GoDaddy subdomains to it via CNAME
- Or use Netlify's custom domain feature
