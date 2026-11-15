---
name: python
description: "Master router for Python development: idiomatic language patterns, architecture, scaffolding, FastAPI, async, testing, performance, packaging, Temporal, n8n Python, and python-pptx. Use when designing, writing, debugging, testing, or maintaining Python code."
---

# Python master skill

This is the **only installable skill entry point**. All specialist documents under `guides/` are internal reference material, **not independent skills**. Route based on the user’s specific task; consult only relevant guides and any associated resources.

## Routing map

| Task / trigger | Internal guide |
| --- | --- |
| Core language, idiomatic syntax, collections, typing | [`python`](guides/python/guide.md) |
| Modern production Python and tooling | [`python-pro`](guides/python-pro/guide.md) |
| Architecture and decision-making | [`python-patterns`](guides/python-patterns/guide.md) |
| Project scaffolding and new repositories | [`python-development-python-scaffold`](guides/python-development-python-scaffold/guide.md) |
| Project scaffolding alias and summary | [`python-development`](guides/python-development/guide.md) |
| FastAPI backends, validation, auth, persistence | [`python-fastapi-development`](guides/python-fastapi-development/guide.md) |
| asyncio and concurrency | [`async-python-patterns`](guides/async-python-patterns/guide.md) |
| pytest and unit/integration tests | [`python-testing-patterns`](guides/python-testing-patterns/guide.md) |
| Profiling, memory, speed optimizations | [`python-performance-optimization`](guides/python-performance-optimization/guide.md) |
| Packaging, pyproject.toml, distribution | [`python-packaging`](guides/python-packaging/guide.md) |
| Temporal Python workflows, activities, sagas | [`temporal-python-pro`](guides/temporal-python-pro/guide.md) |
| Temporal test environments, replay and mocking | [`temporal-python-testing`](guides/temporal-python-testing/guide.md) |
| Python inside n8n Code nodes | [`n8n-code-python`](guides/n8n-code-python/guide.md) |
| PowerPoint generation via python-pptx | [`python-pptx-generator`](guides/python-pptx-generator/guide.md) |

## Operating procedure

1. Identify the problem type and any environment constraints (Python version, framework, package manager, execution platform).
2. Read the most specific internal guide first. For broad Python code quality, read `guides/python/guide.md`, `guides/python-pro/guide.md`, or `guides/python-patterns/guide.md` as appropriate.
3. For cross-cutting work, combine guides selectively: FastAPI + async + testing; packaging + scaffold; Temporal + Temporal testing; performance + testing.
4. Resolve conflicts in favor of the user’s stated requirements, the actual repository and runtime, and current authoritative documentation. Older guide recommendations may need verification.
5. Reuse code examples and `resources/` files from each guide when applicable. Keep relative paths relative to that guide directory.
6. Validate output with the available project tests, linters, and type checkers when possible; distinguish performed verification from suggested commands.

## Important scope distinctions

- `python-development` is an alias-style summary; prefer `python-development-python-scaffold` for detailed scaffolding.
- `python-fastapi/TEMPLATE.md` is a standalone supporting template without its own `SKILL.md`; consult it only for FastAPI templating.
- `n8n-code-python` targets the n8n Code node runtime rather than unrestricted Python.
- `python-pptx-generator` targets generated PowerPoint decks, not all presentation workflows.
- `temporal-python-*` guidance applies to Temporal SDK workflows, not ordinary asyncio tasks.

## Package rule

When maintaining this package, preserve **exactly one** file named `SKILL.md`, at `skills/python/SKILL.md`. New specialists belong under `guides/<topic>/guide.md` (with optional resources), not nested `SKILL.md` files. The archive root must contain `skills/python/SKILL.md`.
