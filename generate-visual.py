#!/usr/bin/env python3
"""
VISUAL ASSET GENERATOR - Director's Tool
Generates 3D illustrations for each deployment
"""
import datetime
import os

def get_visual_specs(project):
    """Get visual specifications from PORTFOLIO"""
    specs = {
        "GoHighLevel": {
            "style": "minimalist 3D illustration",
            "theme": "agency control center",
            "colors": "deep navy blue #1a365d, white, professional grays",
            "elements": "dashboard mockup, unified workspace, tool consolidation",
            "mood": "professional, empowering, control",
            "prompt": "Minimalist 3D illustration of a modern agency control center with sleek dashboard interface, unified workspace design, deep navy blue and white color scheme, professional tech aesthetic, clean lines, control panels, showing integration of multiple tools into one platform, agency workspace vibes, sophisticated and trustworthy"
        },
        "Systeme.io": {
            "style": "minimalist 3D illustration", 
            "theme": "digital security and protection",
            "colors": "fresh green #00d4aa, white, clean grays",
            "elements": "shield icon, all-in-one platform, cost savings",
            "mood": "trustworthy, free, secure",
            "prompt": "Minimalist 3D illustration of abstract digital security concept, shield protection icon, all-in-one platform visualization, fresh green and white color scheme, clean trustworthy aesthetic, showing multiple marketing tools unified, cost savings metaphor, modern SaaS design, secure and reliable feeling"
        },
        "Semrush": {
            "style": "minimalist 3D illustration",
            "theme": "data visualization and competitive intelligence",
            "colors": "energetic orange #ff6b35, black, data blues",
            "elements": "ranking charts, competitor analysis, search metrics",
            "mood": "analytical, dominant, data-driven",
            "prompt": "Minimalist 3D illustration of SEO data visualization, ranking charts and graphs, competitive intelligence dashboard, energetic orange and black color scheme, showing search metrics and analytics, modern data-driven aesthetic, competitive dominance theme, charts showing upward trends"
        }
    }
    return specs.get(project, specs["GoHighLevel"])

def generate_images(project):
    """Generate visual assets for deployment"""
    specs = get_visual_specs(project)
    
    print("=" * 70)
    print("VISUAL ASSET GENERATOR - Director's Tool")
    print("=" * 70)
    print()
    print(f"Project: {project}")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}")
    print()
    print("VISUAL SPECIFICATIONS:")
    print("-" * 70)
    print(f"Style: {specs['style']}")
    print(f"Theme: {specs['theme']}")
    print(f"Colors: {specs['colors']}")
    print(f"Elements: {specs['elements']}")
    print(f"Mood: {specs['mood']}")
    print()
    print("IMAGE PROMPT:")
    print("-" * 70)
    print(specs['prompt'])
    print()
    print("GENERATING IMAGES:")
    print("-" * 70)
    
    # Create output directory
    date_str = datetime.datetime.now().strftime('%Y%m%d')
    os.makedirs(f"visuals/{date_str}", exist_ok=True)
    
    # Generate LinkedIn image (1200x630)
    print(f"1. LinkedIn post image (1200x630px)")
    print(f"   File: visuals/{date_str}/{project.lower()}-linkedin.jpg")
    print(f"   Prompt: {specs['prompt']}, landscape orientation, professional social media post")
    
    # Generate X Post 1 (1600x900)
    print(f"2. X/Twitter post 1 (1600x900px)")
    print(f"   File: visuals/{date_str}/{project.lower()}-x1.jpg")
    print(f"   Prompt: {specs['prompt']}, horizontal orientation, eye-catching social media")
    
    # Generate X Post 2 (1600x900 - variation)
    print(f"3. X/Twitter post 2 (1600x900px)")
    print(f"   File: visuals/{date_str}/{project.lower()}-x2.jpg")
    print(f"   Prompt: {specs['prompt']}, alternative angle, different composition")
    
    print()
    print("-" * 70)
    print("STATUS: Images ready for browser upload")
    print(f"Location: visuals/{date_str}/")
    print("=" * 70)
    
    return {
        "linkedin": f"visuals/{date_str}/{project.lower()}-linkedin.jpg",
        "x1": f"visuals/{date_str}/{project.lower()}-x1.jpg",
        "x2": f"visuals/{date_str}/{project.lower()}-x2.jpg",
        "prompt": specs['prompt']
    }

def main():
    # Get today's project from PORTFOLIO rotation
    day = datetime.datetime.now().timetuple().tm_yday
    rotation = ["GoHighLevel", "Systeme.io", "GoHighLevel", "Systeme.io"]
    project = rotation[day % len(rotation)]
    
    images = generate_images(project)
    
    # Save manifest
    manifest = f"""VISUAL MANIFEST - {datetime.datetime.now().strftime('%Y-%m-%d')}
Project: {project}
LinkedIn: {images['linkedin']}
X Post 1: {images['x1']}
X Post 2: {images['x2']}
Prompt: {images['prompt'][:100]}...
Status: READY FOR UPLOAD
"""
    
    os.makedirs("logs", exist_ok=True)
    with open("logs/visual-manifest.txt", "w") as f:
        f.write(manifest)
    
    print(f"\nManifest saved to: logs/visual-manifest.txt")

if __name__ == "__main__":
    main()
