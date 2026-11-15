# Editorial Hospitality Experience Architect

This release consolidates the latest master skill/evaluation suite with detailed, preserved reference, workflow, and pattern content from earlier editions. It adds editorial creative-direction guidance, provenance rules and honest verification tooling.

## How to use
Install the `editorial-hospitality-experience` directory in an Agent Skills-compatible environment, preserving paths. Invoke the skill through a hospitality web/app design, audit, or implementation request.

## Knowledge precedence
`SKILL.md` > current reference introductions > expanded historical research context. Original materials may contain prescriptive design ratios and unverified quantitative claims; these are not universal standards. See `references/00-source-provenance.md`.

## Validation
Run `python3 scripts/validate-design-tokens.py assets/design-token-schema.json` if compatible with validator CLI, or consult `--help` output. Run accessibility/performance scripts against a running URL only after installing external CLIs. Check `scripts/README.md`.
