import os
import shutil
import glob

GROUPS = {
    "visual-styles": [
        "brutalism", "brutalist-skill", "neo-brutalism", "frutiger-aero", 
        "glassmorphism", "neumorphism", "skeuomorphism", "flat-design", 
        "retro-design", "retro-futurism"
    ],
    "layout-architecture": [
        "card-based-design", "tile-design", "layout-grid", "component-architecture", 
        "floating-ui", "responsive-design", "layered-design"
    ],
    "typography-data": [
        "brutalist-typography", "typography-first", "typography-scale", 
        "readable-measure", "data-storytelling", "data-visualization"
    ],
    "design-foundations": [
        "visual-design-foundations", "visual-hierarchy", "design-system-patterns", 
        "theming-architecture", "spacing-system", "color-blocking", 
        "high-end-visual-design", "illustration-style", "editorial-design"
    ],
    "ux-laws-strategy": [
        "law-of-common-region", "law-of-proximity", "von-restorff-effect", 
        "customer-journey-mapper", "journey", "design-thinking", "strategize", 
        "design-taste-frontend", "taste-skill", "minimalist-skill", "minimalist-ui", 
        "redesign-skill"
    ]
}

OUTPUT_DIR = "lovable_bundles"
os.makedirs(OUTPUT_DIR, exist_ok=True)

for group_name, skills in GROUPS.items():
    bundle_folder = os.path.join(OUTPUT_DIR, group_name)
    os.makedirs(bundle_folder, exist_ok=True)
    master_file_path = os.path.join(bundle_folder, "SKILL.md")
    
    with open(master_file_path, "w", encoding="utf-8") as outfile:
        # Write clean YAML header for the category bundle
        outfile.write(f"---\nname: {group_name}\ndescription: Consolidated playbook for {group_name.replace('-', ' ')}.\nrisk: safe\n---\n\n# {group_name.replace('-', ' ').title()} Playbook\n\n")
        
        for skill in skills:
            skill_file = os.path.join(skill, "SKILL.md")
            if os.path.exists(skill_file):
                with open(skill_file, "r", encoding="utf-8") as infile:
                    content = infile.read()
                    
                    # Strip individual YAML frontmatter
                    if content.startswith("---"):
                        parts = content.split("---", 2)
                        if len(parts) >= 3:
                            content = parts[2].strip()
                            
                    outfile.write(f"\n\n<!-- SKILL: {skill} -->\n\n")
                    outfile.write(content)
                    outfile.write("\n\n---\n")

    # Zip each category bundle folder
    shutil.make_archive(bundle_folder, 'zip', bundle_folder)
    print(f"Created: {group_name}.zip")
