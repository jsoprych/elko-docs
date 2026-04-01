# Getting Started — Transita

> **Live demo:** [elko.ai/transita](https://elko.ai/transita) — no sign-up required.

---

## 1. Open the editor

Go to [elko.ai/transita](https://elko.ai/transita). A welcome dialog explains what you are
looking at. Click **Enter demo →** to dismiss it and start editing.

The default canvas shows a small *Order Processing* diagram — a complete start-to-finish
example you can explore before building your own.

---

## 2. Add a node

Drag any item from the **palette** (left panel) onto the canvas. Release the mouse to drop
the node at that position.

Each item in the palette is a node type with a fixed shape and colour — see
[Node Types](node-types.md) for the full list.

You can also **double-click** an empty area of the canvas to create a default Task node at
that position.

---

## 3. Connect two nodes

1. Hover over a node — four blue **port handles** appear (top, right, bottom, left).
2. Click and drag from any handle toward another node.
3. Release on the target node to create a connection.

A curved arrow appears between the two nodes. The arrow direction follows the drag direction.

---

## 4. Edit a node

Click a node to select it. The **Properties** panel (right side) shows editable fields:

- **Label** — the node's display name
- **Type-specific fields** — e.g. *Responsible* and *Est. Duration* for a Task node;
  *Condition* for a Decision node

Changes apply immediately and are visible on the canvas.

---

## 5. Group related nodes

Select two or more nodes (click the first, then `Shift`-click others, or drag a
selection box around them). Press **`G`** to wrap them in a group.

The group appears as a dashed-border container. Child nodes stay visible inside it as
line sketches. You can:

- **Move the group** by dragging its border — children move with it
- **Move a child** by dragging it within the group — it cannot escape the group border
- **Ungroup** by selecting the group and pressing `U`

---

## 6. Read the pseudocode

Click the **Pseudo** tab in the top-right panel area. Transita walks the diagram from the
Start node and generates a plain-English program summary:

```
PROGRAM  Order Processing
────────────────────────────────────────────────

BEGIN
  // ── Start ──
  Validate Order()
  IF (Order Valid?)  // TRUE
    Process Payment()
    STOP  // End — Success
  ELSE  // FALSE
    STOP  // End — Rejected
  END IF

END
────────────────────────────────────────────────
```

If any nodes are not connected to the main flow they appear at the bottom under
**Orphaned Nodes** with a category (`[disconnected]`, `[unreachable]`, `[dead end]`).

Use the **Copy** button above the panel to copy the pseudocode to the clipboard.

---

## 7. Inspect the raw diagram

Click the **Inspect** tab to see:

- **JSON view** (left) — the live diagram model as structured data
- **Event stack** (right) — every action taken since the diagram was opened, newest first;
  the `▶` marker shows the current undo position

---

## 8. Undo and redo

| Action | Shortcut |
|--------|----------|
| Undo | `Ctrl+Z` / `Cmd+Z` |
| Redo | `Ctrl+Y` / `Cmd+Shift+Z` |
| Reset to default | **Reset** button in toolbar |

---

## 9. Zoom and pan

| Action | How |
|--------|-----|
| Zoom in / out | Scroll wheel, or **+** / **−** toolbar buttons |
| Pan | Middle-mouse drag, or hold `Space` and drag |
| Fit diagram to screen | **Fit** toolbar button |

---

## Keyboard shortcuts

| Key | Action |
|-----|--------|
| `G` | Group selected nodes |
| `U` | Ungroup selected group |
| `Delete` / `Backspace` | Delete selected node(s) or connection |
| `Ctrl+Z` | Undo |
| `Ctrl+Y` | Redo |
| `Escape` | Cancel current action / deselect |

---

*→ [Node Types reference](node-types.md)*
