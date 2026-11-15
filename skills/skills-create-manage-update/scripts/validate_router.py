#!/usr/bin/env python3
"""Static, read-only validation of the single-entry master skill package."""
from pathlib import Path
import re, sys
ROOT = Path(__file__).resolve().parents[1]
errors=[]
entrypoints=list(ROOT.rglob('SKILL.md'))
if entrypoints != [ROOT/'SKILL.md']:
    errors.append(f"Expected exactly one SKILL.md at root; found: {[str(p.relative_to(ROOT)) for p in entrypoints]}")
text=(ROOT/'SKILL.md').read_text(encoding='utf-8')
if not text.startswith('---\n') or '\n---\n' not in text[4:]: errors.append('Invalid/missing root frontmatter')
else:
    fm=text.split('---',2)[1]
    if not re.search(r'(?m)^name:\s*skills-create-manage-update\s*$',fm):errors.append('Incorrect name')
    if not re.search(r'(?m)^description:\s*(?:\S|[>|])',fm):errors.append('Missing description')
    try:
        import yaml
        yaml.safe_load(fm)
    except ImportError: pass
    except Exception as exc:errors.append(f'Invalid YAML: {exc}')
links=re.findall(r'\]\(([^)#]+?)(?:#[^)]*)?\)',text)
for link in links:
    if '://' in link or link.startswith('#'):continue
    if not (ROOT/link).is_file():errors.append(f'Broken master link: {link}')
guides=sorted((ROOT/'guides').glob('*/guide.md'))
for guide in guides:
    expected=f'guides/{guide.parent.name}/guide.md'
    if expected not in text:errors.append(f'Unrouted guide: {expected}')
print(f'Found {len(entrypoints)} installable SKILL.md and {len(guides)} routed specialist guides')
if errors:
    for e in errors:print('ERROR:',e)
    sys.exit(1)
print('PASS: one skill, valid master routes and archive structure')
