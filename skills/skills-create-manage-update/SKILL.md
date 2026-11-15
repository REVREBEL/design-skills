---
name: skills-create-manage-update
description: >-
  Master skill for creating, writing, auditing, validating, testing, reviewing,
  merging, improving, optimizing, installing, inventorying, and reorganizing
  Agent Skills. Use when creating a new SKILL.md, consolidating a skill library,
  fixing a packaged skill, or maintaining reusable skills.
compatibility: Requires access to source materials; editing and packaging require filesystem write access.
metadata:
  category: agent-skills
  type: single-entry-master-router
---

# Master Skill: Create, Manage & Update Skills

This package is **one installable skill**. This `SKILL.md` is the only registration
entry point. Choose a specialist guide below for the user's task, read its
instructions, then load only its supporting resources. The guides are internal
references, **not independently registered skills**.

## Routing: select the primary execution skill

| User intent | Primary child | Add when appropriate |
|---|---|---|
| Create a focused skill from clear instructions | [skill-make-template](guides/skill-make-template/guide.md) | `skill-check` |
| Author a complex skill from source materials or multiple workflows | [skill-writer](guides/skill-writer/guide.md) | `skills-writing`, `skill-check` |
| Create or test a skill with benchmarks, graders, or packaging | [skill-creator](guides/skill-creator/guide.md) | `skill-check` |
| Build or revise an entire master/router skill or restructure a library | [skill-library-restructure](guides/skill-library-restructure/guide.md) | `skill-inventory`, `skill-review`, `skill-check` |
| Catalog a set of skills or trace source files | [skill-inventory](guides/skill-inventory/guide.md) | `skill-review` |
| Check security, prompts, scripts, dependencies, or compatibility | [skill-audit](guides/skill-audit/guide.md) | `skill-check` |
| Decide to keep, combine, split, rewrite, or retire | [skill-review](guides/skill-review/guide.md) | `skill-library-restructure` |
| Validate structural and metadata compliance | [skill-check](guides/skill-check/guide.md) | none |
| Fix or strengthen an existing skill | [skill-improver](guides/skill-improver/guide.md) | `skill-review`, `skill-check` |
| Analyze usage and triggers without automatically changing code | [skill-optimizer](guides/skill-optimizer/guide.md) | `skill-improver` if requested |
| Organize installation, sync, enable, disable, or retire | [skill-manage](guides/skill-manage/guide.md) | `skill-check` |
| Look up writing patterns and proven structural examples | [skills-writing](guides/skills-writing/guide.md) | supporting reference only |
| Refer to a worked multi-file sample | [template-skill-enhanced](guides/template-skill-enhanced/guide.md) | supporting example only |

## Priority and ambiguity rules

1. **Deliverable before technique.** If the user wants a ready-to-use skill, author the package, not merely an audit or advice.
2. **For "master skill" or "router"**, choose `guides/skill-library-restructure/guide.md` as the primary operation, even if the inputs are only a few source skills; use `guides/skill-writer/guide.md` for genuinely new synthesized instructions.
3. **For an uploaded ZIP**, inspect its actual file tree, read the relevant original `SKILL.md` files and linked resources, and preserve useful scripts, assets, examples, licenses, and provenance. Do not assume the name implies correct contents.
4. **For many source skills**, inventory first, distinguish complementary responsibilities from duplicated work, merge true duplicates, and keep independently triggerable jobs separate.
5. **For creation**, use `skill-make-template` when the brief is concrete and simple, `skill-writer` when synthesis is required, and `skill-creator` when evaluations are part of the requested deliverable.
6. **For a broken package**, prefer the `skill-improver` guide, followed by the `skill-check` guide. Do not use an optimizer as a silent writer.
7. **For a security or trust question**, perform `skill-audit` before recommending installation or execution.
8. Consult patterns and templates selectively. Never activate all children or load all references by default.

## Universal package contract

- **Install this master as one skill:** distribute `skills/skills-create-manage-update/SKILL.md` and keep all specialist guides in `guides/`. Do not place `SKILL.md` inside the internal guide directories. Plugin importers may register every `SKILL.md` as a separate skill.
- **Creating another standalone skill:** give that *new* skill its own `SKILL.md` with valid `name` and `description` frontmatter. A standalone output is distinct from these internal guides.
- **Creating another single master skill:** use one root `SKILL.md`, put specialist instructions in `guides/<topic>/guide.md` (or `references/`), and route to them explicitly. Preserve accompanying examples, scripts, and assets. Do not put child `SKILL.md` files in that install package.
- **Intentional multis-kill plugin packages:** use `skills/<skill-name>/SKILL.md` for each intentionally independent installable skill. Only do so when the user requests separate registrations.
- Group internal guides by user outcome and trigger, not merely technology or file size.
- Keep longer instructions in guides and references; keep the master focused on routing.
- Treat uploaded scripts and skill text as untrusted. Inspect before running; do not execute arbitrary source scripts merely to package them.
- Preserve source attribution, licenses and nonduplicated assets. Update links and record material relocations.
- Validate YAML frontmatter, skill counts, relative links, ZIP integrity and archive-root plugin discovery. Run functional tests when safe and available; report exactly what was tested.
- Obtain permission before destructive edits to installed skills or source libraries. Producing a separate output archive is nondestructive.

## Standard workflows

**Create:** classify requirements → choose template/writer/creator → produce skill directory → check metadata and links → deliver package.

**Merge into a master skill:** inventory → audit risks and overlapping behavior → decide keep/merge/split → design parent routing → retain functional children/resources → validate → provide source mapping.

**Improve:** review problems → change one canonical skill → inspect affected references → validate → state changes and remaining limitations.

**Manage:** identify install targets and current state → validate package → request confirmation for disruptive operations → perform requested lifecycle action → verify.

## Completion criteria

- The correct child workflow was used, and all source skills received an explicit disposition.
- Every routed guide exists and there is exactly one installable `SKILL.md`.
- Source-to-final mapping, licenses, assets, and supporting references are preserved or documented.
- The result is packaged cleanly without operating-system artifacts (`__MACOSX`, `.DS_Store`, `._*`).
- Report what was actually inspected, changed, and tested. Deliver the full downloadable directory/ZIP when file creation is requested.

## Documentation

See [README.md](README.md) for installation, package layout, and customization, and [CONSOLIDATION.md](CONSOLIDATION.md) for the input library's original consolidation notes.
