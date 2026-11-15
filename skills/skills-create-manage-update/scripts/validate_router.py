#!/usr/bin/env python3
"""Read-only static checks for this router package."""
from pathlib import Path
import re, sys
ROOT = Path(__file__).resolve().parents[1]
issues = []
root_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
children = sorted(p for p in ROOT.iterdir() if p.is_dir() and (p / "SKILL.md").exists())
for md in [ROOT / "SKILL.md", *(p / "SKILL.md" for p in children)]:
    content = md.read_text(encoding="utf-8")
    if not content.startswith("---\n") or "\n---\n" not in content[4:]:
        issues.append(f"Missing YAML frontmatter: {md.relative_to(ROOT)}")
        continue
    frontmatter = content.split("---", 2)[1]
    if not re.search(r"(?m)^name:\s*\S", frontmatter):
        issues.append(f"Missing name: {md.relative_to(ROOT)}")
    if not re.search(r"(?m)^description:\s*(?:\S|[>|])", frontmatter):
        issues.append(f"Missing description: {md.relative_to(ROOT)}")
    try:
        import yaml
        parsed = yaml.safe_load(frontmatter)
        if not isinstance(parsed, dict):
            issues.append(f"Frontmatter is not a mapping: {md.relative_to(ROOT)}")
    except ImportError:
        pass
    except Exception as e:
        issues.append(f"Invalid YAML: {md.relative_to(ROOT)}: {e}")
for path in re.findall(r"\]\(([^)#]+/SKILL\.md)\)", root_text):
    if not (ROOT / path).is_file():
        issues.append(f"Broken route: {path}")
for child in children:
    if f"{child.name}/SKILL.md" not in root_text:
        issues.append(f"Unrouted child: {child.name}")
for p in ROOT.rglob("SKILL.md"):
    if p != ROOT / "SKILL.md" and p.parent not in children:
        issues.append(f"Unintended nested skill entrypoint: {p.relative_to(ROOT)}")
print(f"Checked root router and {len(children)} children")
if issues:
    print("\n".join("ERROR: " + issue for issue in issues)); sys.exit(1)
print("PASS: router targets and basic skill structure")
