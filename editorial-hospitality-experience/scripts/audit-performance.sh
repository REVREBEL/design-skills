#!/usr/bin/env bash
set -euo pipefail
TARGET="${1:-}"
if [[ -z "$TARGET" ]]; then echo "Usage: $0 <site-url>  (requires lighthouse CLI)" >&2; exit 2; fi
if [[ "$TARGET" != http://* && "$TARGET" != https://* ]]; then echo "NOT RUN: requires a running site URL" >&2; exit 2; fi
if ! command -v lighthouse >/dev/null 2>&1; then echo "NOT RUN: install lighthouse CLI and Chrome (npm i -g lighthouse)" >&2; exit 2; fi
OUT="${2:-./lighthouse-report.json}"
lighthouse "$TARGET" --chrome-flags='--headless --no-sandbox' --only-categories=performance --output=json --output-path="$OUT" --quiet
python3 - "$OUT" <<'PYCODE'
import json,sys
j=json.load(open(sys.argv[1])); audits=j.get('audits',{})
for key in ['largest-contentful-paint','cumulative-layout-shift','interaction-to-next-paint']:
 a=audits.get(key);print(key, a.get('displayValue','unavailable in this lab run') if a else 'unavailable in this lab run')
print('Lab measurements are not field Core Web Vitals. INP generally requires real user interaction/field data.')
PYCODE
