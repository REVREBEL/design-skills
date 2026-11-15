# Skills Create, Manage & Update

A **single installable master skill** for the lifecycle of Agent Skills.

## Installation

Import the ZIP as provided. Its discoverable entry is
`skills/skills-create-manage-update/SKILL.md`. The importer should register
**only one skill**, named `skills-create-manage-update`.

All 13 specialist capabilities live under `guides/<name>/guide.md`. They are
internal resources routed by the master, not additional installable skills.

## Layout

```text
skills/
└── skills-create-manage-update/
    ├── SKILL.md                 # only installable entry point
    ├── README.md
    ├── CONSOLIDATION.md
    ├── guides/
    │   ├── skill-creator/guide.md
    │   ├── skill-writer/guide.md
    │   ├── skill-audit/guide.md
    │   ├── skill-check/guide.md
    │   ├── skill-library-restructure/guide.md
    │   └── ... 8 additional specialist guides
    └── scripts/validate_router.py
```

The internal guides retain their companion references, scripts, templates,
examples and original license files.

## Validation

Run `python3 scripts/validate_router.py` from the master skill directory. This
checks the one-entry-point contract, frontmatter and master routing targets.
It does not execute bundled skill-creation scripts or establish that a plugin
import has succeeded.

## When generating new skill packages

- For a **single master skill**, generate one `SKILL.md` and internal `guides/`.
- For **multiple independently installable skills**, use `skills/<name>/SKILL.md`
  for each one, but only when explicitly requested.
- Validate every generated archive before delivery.

## Provenance

The original archive contained 14 `SKILL.md` files. Its 13 specialist skill
entrypoints were renamed to internal `guide.md` files and moved under `guides/`.
The nested legacy `skill-writer` material remains preserved in references.
