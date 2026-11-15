---
name: react-master
description: Design, implement, review, debug, and modernize React applications, components, and hooks. Use for React and TSX composition, effects, state management, forms, accessibility, async UI, testing, profiling and performance, SSR and hydration, Next.js App Router and Server Components, Vite setup and production builds, React upgrades, and typed React Flow diagrams.
---

# React Master

## Workflow

1. Identify the installed React, renderer, framework, and relevant library versions. Inspect the affected component tree, route, state ownership, project conventions, and existing checks. Keep generic React guidance separate from APIs that require a specific framework or version.
2. Reproduce the behavior through the normal app entry point. Identify the user interaction or render that triggers it and distinguish state identity, synchronization, data fetching, hydration, and rendering cost.
3. Keep rendering pure and place state at its nearest shared owner. Derive values during render and keep interaction-driven work in event handlers. Use effects for external synchronization with matching cleanup. Follow the installed React version's rules for hooks.
4. Build the smallest change that preserves component contracts and the project's design system. Cover interaction, focus, pending, empty, error, and recovery states where the feature needs them. Reuse the project's framework data APIs, cache, and tooling.
5. Verify the affected user path with existing checks. Include realistic keyboard interaction and async failure cases when relevant. For server-rendered changes, test a fresh load and client navigation. For performance, compare the same interaction before and after. Report the checks actually run.

## References

| Task | Reference |
| --- | --- |
| Components, hooks, identity, typed props, accessibility, and testing | [Components and hooks](references/components-and-hooks.md) |
| State ownership, Redux Toolkit, Zustand, Jotai, TanStack Query, forms, and async UI | [State and async UI](references/state-and-async-ui.md) |
| Profiler, render isolation, waterfalls, bundles, and long lists | [Performance](references/performance.md) |
| React + Vite setup, project structure, aliases, HMR, env, testing, assets, and builds | [Vite](references/vite.md) |
| Next.js routing, Server Components, hydration, caching, and mutations | [Next.js and server rendering](references/nextjs-and-server-rendering.md) |
| Class-to-hooks migrations, version upgrades, codemods, and React 19 adoption | [Modernization](references/modernization.md) |
| Typed React Flow nodes, graph state, layout, navigation, and profiling | [React Flow](references/react-flow.md) |

Use the repository's pinned dependencies. Verify version-sensitive APIs against official documentation before adopting them. For general TypeScript type design, use TypeScript Master when available.
