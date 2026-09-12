import os
import shutil
import glob

# Specific tight groups defined by you (duplicates removed)
MERGE_GROUPS = {
    "brutalism-suite": ["brutalism", "brutalist-skill", "brutalist-typography", "neo-brutalism"],
    "gestalt-laws": ["law-of-proximity", "law-of-common-region"],
    "minimalism-suite": ["minimalist-skill", "minimalist-ui"],
    "design-taste": ["design-taste-frontend", "taste-skill"],
    "data-design": ["data-visualization", "data-storytelling"],
    "customer-journey": ["customer-journey-mapper", "journey"],
    "layout-components": ["layout-grid", "layered-design", "card-based-design", "tile-design"],
    "typography-foundations": ["typography-scale", "typography-first"],
    "visual-hierarchy-suite": ["visual-design-foundations", "visual-hierarchy"]
}

OUTPUT_DIR = "lovable_ready_skills"
os.makedirs(OUTPUT_DIR, exist_ok=True)

processed_folders = set()

def strip_yaml(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return text.strip()

# 1. Process specified merge groups
for group_name, skills in MERGE_GROUPS.items():
    group_folder = os.path.join(OUTPUT_DIR, group_name)
    os.makedirs(group_folder, exist_ok=True)
    master_md = os.path.join(group_folder, "SKILL.md")
    
    with open(master_md, "w", encoding="utf-8") as outfile:
        # Write fresh top-level frontmatter
        outfile.write(f"---\nname: {group_name}\ndescription: Combined playbook for {group_name.replace('-', ' ')}.\nrisk: safe\n---\n\n# {group_name.replace('-', ' ').title()}\n\n")
        
        for skill in skills:
            skill_path = os.path.join(skill, "SKILL.md")
            if os.path.exists(skill_path):
                processed_folders.add(skill)
                with open(skill_path, "r", encoding="utf-8") as infile:
                    raw_content = infile.read()
                    clean_content = strip_yaml(raw_content)
                    outfile.write(f"<!-- SKILL SOURCE: {skill} -->\n\n")
                    outfile.write(clean_content)
                    outfile.write("\n\n---\n\n")

    # Package into ZIP for Lovable import
    shutil.make_archive(group_folder, 'zip', group_folder)
    print(f"Merged & Zipped: {group_name}.zip")

# 2. Package remaining standalone skills as individual ZIP files
all_folders = [f for f in os.listdir('.') if os.path.isdir(f) and os.path.exists(os.path.join(f, "SKILL.md"))]

for folder in all_folders:
    if folder not in processed_folders and folder != OUTPUT_DIR:
        dest_folder = os.path.join(OUTPUT_DIR, folder)
        os.makedirs(dest_folder, exist_ok=True)
        shutil.copy(os.path.join(folder, "SKILL.md"), os.path.join(dest_folder, "SKILL.md"))
        shutil.make_archive(dest_folder, 'zip', dest_folder)
        print(f"Standalone Zipped: {folder}.zip")

print(f"\nDone! All ready-to-upload ZIP files are in: ./{OUTPUT_DIR}/")
