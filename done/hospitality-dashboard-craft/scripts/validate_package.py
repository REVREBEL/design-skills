#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
root=Path(__file__).resolve().parents[1]
errors=[]
main=(root/'SKILL.md').read_text()
if not main.startswith('---\nname:'): errors.append('Missing skill YAML header')
for file in root.rglob('*'):
    if file.is_file() and file.suffix in {'.md','.json','.css','.tsx','.py'}:
        text=file.read_text()
        if '\x0c' in text: errors.append(f'Form feed: {file}')
        if file.suffix=='.json':
            try: json.loads(text)
            except Exception as e: errors.append(f'JSON {file}: {e}')
for folder in ['references','workflows','patterns','examples','evals','scripts']:
    if not list((root/folder).iterdir()):errors.append(f'Empty {folder}')
for path in re.findall(r'`((?:references|workflows|patterns|assets)/[^`\s]+\.(?:md|css|tsx))`',main):
    if not (root/path).is_file():errors.append('Missing '+path)
if errors:
    print('\n'.join(errors));sys.exit(1)
print('PASS: package structure, referenced documents, JSON and text controls')
