# Performance

## Diagnose before changing code

1. Reproduce the slow action with representative data and record a baseline. Use a browser performance trace and network waterfall to find blocking work and a React DevTools profile to identify expensive commits. Keep the device, build, data, and interaction comparable.
2. Identify whether the cost is request latency, received bytes, JavaScript, subscription fan-out, React rendering, layout, or paint. A high render count is secondary to the cost and user-visible latency.
3. Isolate the responsible work. Test the smallest change and compare the same action. Check that loading, correctness, accessibility, and interaction responsiveness hold.

## Match the fix to the cost

| Finding | Useful first move |
| --- | --- |
| Independent requests wait for each other | Start them as soon as their inputs are available and keep true dependencies sequential |
| Heavy initial JavaScript | Inspect the bundle, move server-only work out of the client graph, and defer expensive optional features or third parties |
| Unrelated updates rerender a large tree | Move rapidly changing state down, narrow store subscriptions, and preserve stable keys |
| A measured expensive pure child repeatedly gets equivalent props | Stabilize the relevant inputs and use memoization where supported and beneficial |
| Large mounted lists or graphs dominate work | Reduce rendered content, consider virtualization, and verify navigation, accessibility, and scroll behavior |
| Urgent interaction waits on non-urgent rendering | Separate urgent input from deferred rendering or version-supported transitions |

Example: if a timer update rerenders a parent that owns a long list, place the timer state in the clock component. Re-profile the list commits before adding memoization. If sorting or filtering dominates, measure that computation separately and choose between moving the work, memoizing stable inputs, or limiting the dataset.

For SSR or route performance, measure the request waterfall, response or streaming behavior, serialized data, and client JavaScript. Scope caching to the data's lifetime and audience. Treat small loop, allocation, and DOM optimizations as targeted fixes for measured hotspots.

Official reference [React Profiler](https://react.dev/reference/react/Profiler).

Further examples [Vercel React Best Practices](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices).
