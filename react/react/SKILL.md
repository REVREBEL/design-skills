---
name: react
description: "Master router for React and Next.js development, components, hooks, performance, state management, UI patterns, React Flow, TypeScript, and modernization. Read focused internal guides for the relevant task."
---

# React: Master Skill Router

One discoverable skill with focused, internal references. Select the smallest relevant guide set rather than reading everything.

## Routing index

| User intent | Read this guide |
| --- | --- |
| React component architecture and hooks | [guides/react-patterns/GUIDE.md](guides/react-patterns/GUIDE.md) |
| Loading, errors, accessibility and UI states | [guides/react-ui-patterns/GUIDE.md](guides/react-ui-patterns/GUIDE.md) |
| State management, query caching and choosing stores | [guides/react-state-management/GUIDE.md](guides/react-state-management/GUIDE.md) |
| React and Next.js performance | [guides/react-best-practices/GUIDE.md](guides/react-best-practices/GUIDE.md) |
| Diagnosing an individual slow component | [guides/react-component-performance/GUIDE.md](guides/react-component-performance/GUIDE.md) |
| Next.js App Router and development workflow | [guides/react-nextjs-development/GUIDE.md](guides/react-nextjs-development/GUIDE.md) |
| React version upgrades, class-to-hooks migration | [guides/react-modernization/GUIDE.md](guides/react-modernization/GUIDE.md) |
| React Flow canvas, graphs, hierarchical navigation | [guides/react-flow-architect/GUIDE.md](guides/react-flow-architect/GUIDE.md) |
| Typed custom React Flow nodes | [guides/react-flow-node-ts/GUIDE.md](guides/react-flow-node-ts/GUIDE.md) |
| Showcase examples of React UI states | [guides/code-showcase-react-ui-patterns/GUIDE.md](guides/code-showcase-react-ui-patterns/GUIDE.md) |

## Workflow

1. Identify whether the task concerns React, Next.js, React Flow, or multiple layers.
2. Load the matching guide from the routing index. For ambiguous tasks, start with `react-patterns`; add one focused companion guide when useful.
3. Follow the selected guide's actual examples and safeguards; open adjacent references and rule files only as needed.
4. Treat version-specific guidance as potentially dated: check the project's installed versions and official documentation for version-sensitive APIs and behavior.
5. Validate TypeScript, tests, lint, and builds using the project's existing commands where available; do not claim to have run checks without executing them.

## Cross-guide choices

- UI components: start with `react-patterns`, then `react-ui-patterns`.
- Next.js performance: start with `react-best-practices`, then `react-nextjs-development`.
- React Flow application: start with `react-flow-architect`, then `react-flow-node-ts` for node implementation.
- Component performance: `react-component-performance` for diagnosis, `react-best-practices` for broader optimization.
- State management: `react-state-management`; avoid adding a store when local state suffices.

## Internal assets

Additional `rules/`, `references/`, `resources/`, `agents/`, and `AGENTS.md` content resides alongside each guide. These are reference material, not separately installable skills.
