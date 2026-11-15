# React Flow

- Inspect the installed React Flow package and version, including import paths and controlled versus uncontrolled configuration. Preserve existing provider scope, store conventions, and persisted graph format.
- For custom nodes, define a discriminated node union keyed by node type, use the installed version's node/props generics, and keep the node/edge renderer registries stable. Narrow by type before accessing custom data. Reuse typed actions or context for editing, and preserve unique handle IDs and edge references.
- Own nodes and edges consistently. Apply library change events through the established store or controlled handlers. Subscribe to the smallest necessary slices. Keep selection and viewport state out of heavy graph computations unless they are inputs. Update node internals through the library API when dynamic handle geometry changes.
- Treat hierarchy and layout as graph operations with explicit rules. Track stable parent/child relationships, handle invalid or cyclic input where relevant, and define the behavior for edges connected to hidden nodes. Preserve selection and viewport through search, focus, collapse, and expansion. Derive visible nodes and edges without discarding the authoritative graph.
- Measure drag, pan, zoom, search, and expand or collapse before optimizing. Stabilize expensive custom nodes and handlers where profiles justify it, avoid rebuilding whole graphs for a selected ID, and avoid layout on each drag frame unless required. Use realistic graph sizes and test keyboard interaction.
- Verify persistence and rehydration, typed node registration, edge updates, dynamic handles, and layout with representative graphs. Check install-version documentation before copying older examples.

Official references [React Flow TypeScript](https://reactflow.dev/learn/advanced-use/typescript) and [React Flow performance](https://reactflow.dev/learn/advanced-use/performance).

## Example for projects using @xyflow/react

Register a typed renderer at module scope. Add the node type to the project's node union and validate external graph data before passing it into the editor.

```tsx
import type { Node, NodeProps, NodeTypes } from '@xyflow/react'

type StatusNode = Node<{ label: string; complete: boolean }, 'status'>

function StatusNodeView({ data }: NodeProps<StatusNode>) {
  return <div>{data.label} ({data.complete ? 'complete' : 'pending'})</div>
}

export const nodeTypes = { status: StatusNodeView } satisfies NodeTypes
```
