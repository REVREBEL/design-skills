#!/usr/bin/env bash
set -euo pipefail
TARGET="${1:-}"
if [[ -z "$TARGET" ]]; then echo "Usage: $0 <site-url>  (requires @axe-core/cli)" >&2; exit 2; fi
if [[ "$TARGET" != http://* && "$TARGET" != https://* ]]; then echo "NOT RUN: requires a running site URL, not source files" >&2; exit 2; fi
if ! command -v axe >/dev/null 2>&1; then echo "NOT RUN: install @axe-core/cli and browser dependencies (npm i -g @axe-core/cli)" >&2; exit 2; fi
echo "Running axe automated accessibility checks for $TARGET; manual WCAG audit remains required"
axe "$TARGET" --exit
