# Validation tools

`validate-design-tokens.py` validates local token schema according to its implemented rules. `audit-accessibility.sh <URL>` runs axe CLI when installed and a running URL is available. `audit-performance.sh <URL>` runs a Lighthouse lab audit. Missing requirements return code 2 (NOT RUN), not a false success. Automated scans do not replace manual WCAG review, keyboard testing, real booking tests, or field Web Vitals monitoring.
