---
name: components
description: Master router for designing, building, auditing, documenting, and distributing accessible reusable UI components, component libraries, design-system primitives, and React/Tailwind UI implementations. Select the appropriate internal guide and examples for the task.
---

# Components | Master Skill Router

Use this **single skill entry point** for all component-design and component-engineering work. The linked guides are internal reference documents, **not independently installable skills**. Read only the guides needed for the user's task, then consult their referenced source files.

## Routing table

| User request / intent | Internal guide | Scope |
| --- | --- | --- |
| Architecture, compound components, component APIs, composition, testing patterns | [Component architecture](guides/component-architecture.md) | Architectural patterns and examples |
| Build accessible, composable primitives or publish a reusable component library | [Building components](guides/building-components/guide.md) | Reference hub for accessibility, polymorphism, tokens, distribution, and docs |
| Generate a new component in an existing StyleSeed/Tailwind v4 project | [UI component](guides/ui-component/guide.md) | Project-specific conventions; apply **only** if its prerequisites hold |
| Work with core library, semantic tokens, layout and common component APIs | [Core components](guides/core-components/guide.md) | Design-system patterns (platform-specific examples) |
| Produce core-component showcases / examples | [Code showcase core components](guides/code-showcase-core-components/guide.md) | Showcase-specific component conventions |
| Examine existing UI component implementations | [UI examples](examples/ui/) | Source examples; adapt to project's dependencies |

## Execution workflow

1. Determine whether the work is architecture, construction, audit, documentation, showcase, or distribution; choose relevant guides from the table.
2. Inspect the actual project's framework, versions, tokens, components, imports, accessibility conventions, and test setup before applying any guide's examples.
3. Prefer existing project components and design tokens over inventing parallel primitives. Treat StyleSeed, React Native-like token APIs, and shadcn/Radix-style examples as distinct conventions, not universal defaults.
4. For new or modified components, define the accessible interaction model, controlled/uncontrolled API, typing, state, keyboard/focus behavior, styling, variants, and integration boundaries.
5. Implement and validate with the project's formatter, type checker, tests, story/preview system, and accessibility checks when available. Do not claim tests ran unless they did.
6. For npm/registry publishing or external distribution, consult the distribution references under `guides/building-components/references/`.

## Further references

The [Building Components guide](guides/building-components/guide.md) links to its topic-level `.mdx` references, including accessibility, composition, design tokens, state, types, documentation, registry, and npm distribution.
The `examples/ui/` folder contains **source examples**, not a ready-to-install standalone library; check local dependencies and aliases before reuse.
