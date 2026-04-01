# Transita — Visual Diagram Studio

**Transita** is a visual editor for building flowcharts, state machines, and workflow diagrams.
Draw nodes, connect them, group related steps, and instantly see a plain-English pseudocode
summary of the flow — no code required.

> **Alpha preview** — Try the live demo at [elko.ai/transita](https://elko.ai/transita).
> The final product will look and work substantially different.

---

## What you can do today

- **Drag and drop** node types from the palette onto the canvas
- **Connect nodes** by hovering a node and dragging from a blue port handle to another node
- **Group nodes** by selecting two or more and pressing `G` — the group becomes a collapsible container
- **Inspect** any diagram as live JSON or a readable pseudocode summary (tabs in the right panel)
- **Undo / Redo** every action with `Ctrl+Z` / `Ctrl+Y`
- **Reset** to the default diagram at any time with the **Reset** toolbar button

---

## Diagram types

| Template | Description |
|----------|-------------|
| [Business Process](node-types.md) | Flowcharts and business workflows — tasks, decisions, documents, data stores, sub-processes |

More domain templates (LangChain agents, API pipelines, event-driven systems) are in development.

---

## Documentation

→ [Getting Started](getting-started.md) · [Node Types](node-types.md)

---

## Coming soon

Transita diagrams are designed to be machine-readable. A future **Transita MCP server** will let
AI assistants read, query, and reason about your diagrams directly — ask Claude "what happens
after the payment fails?" and get a precise answer drawn from the diagram structure.

---

*Part of the [Elko.AI](https://elko.ai) suite · [feedback@elko.ai](mailto:feedback@elko.ai)*
