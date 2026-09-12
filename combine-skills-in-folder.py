import os
import glob

# Master skill configuration
OUTPUT_FILE = "master-design-skills/SKILL.md"
MASTER_FRONTMATTER = """---
name: master-design-skills
description: Consolidated master playbook containing all UI visual styles, layout rules, and component architectures.
date_added: "2026-09-09"
risk: safe
---

# Master Design Skills Playbook

"""

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
    outfile.write(MASTER_FRONTMATTER)
    
    # Process every SKILL.md in subdirectories
    for filepath in sorted(glob.glob("*/SKILL.md")):
        folder_name = os.path.dirname(filepath)
        
        with open(filepath, "r", encoding="utf-8") as infile:
            content = infile.read()
            
            # Strip YAML frontmatter (between first and second '---')
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    content = parts[2].strip()
            
            # Append cleanly with horizontal rule separators
            outfile.write(f"\n\n<!-- BEGIN SKILL: {folder_name} -->\n\n")
            outfile.write(content)
            outfile.write("\n\n---\n")

print(f"Successfully combined all skills into {OUTPUT_FILE}")x
