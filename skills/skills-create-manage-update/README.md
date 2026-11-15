# Skills Create, Manage & Update

A **master router Agent Skill** for creating, improving, evaluating, restructuring, and managing other Agent Skills.

## Installation

Keep the entire `skills-create-manage-update/` folder together in the skills directory recognized by your agent/client. Register or reference its top-level `SKILL.md`. Do not flatten the children: the router uses relative paths to their own `SKILL.md` files. Installation paths and auto-discovery behavior depend on the host application.

## Architecture

```text
skills-create-manage-update/
├── SKILL.md                       # only master router
├── README.md
├── CONSOLIDATION.md              # input provenance
├── skill-inventory/SKILL.md
├── skill-audit/SKILL.md
├── skill-review/SKILL.md
├── skill-check/SKILL.md
├── skill-make-template/SKILL.md
├── skill-writer/SKILL.md
├── skill-creator/SKILL.md
├── skill-improver/SKILL.md
├── skill-optimizer/SKILL.md
├── skill-manage/SKILL.md
├── skill-library-restructure/SKILL.md
├── skills-writing/SKILL.md       # reference library
└── template-skill-enhanced/SKILL.md # worked example
```

Children retain their original supporting folders and assets, including references, scripts, samples, and source licenses.

## Usage examples

- "Create a master routing skill from these ZIP files" → `skill-library-restructure`, with inventory and check.
- "Write a new Webflow skill from these notes" → `skill-writer`, then `skill-check`.
- "Audit all the skills for risky scripts" → `skill-audit`.
- "Fix the triggers in this existing SKILL.md" → `skill-improver`; optionally consult `skill-optimizer` first.
- "Install and synchronize my skill collection" → `skill-manage`.

## Verification

Run `python3 scripts/validate_router.py` in this directory to verify YAML frontmatter (when PyYAML is available), routing targets, and basic skill structure. It performs **static checks only** and does not run any bundled executable scripts.

## Provenance

The nested `skill-writer/skill-writer/SKILL.md` included in the source ZIP was retained as a reference at `skill-writer/references/legacy-claude-skill-writer.md` to avoid an accidental duplicate runnable nested child. Other child skills remain in their original directories. Original `CONSOLIDATION.md` is retained.
