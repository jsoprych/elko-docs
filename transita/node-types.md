# Node Types — Business Process Template

The **Business Process** template is the default diagram type in Transita.
It covers the common building blocks of flowcharts and business workflows.

---

## Events

### Start
**Shape:** Rounded pill · **Colour:** Green

The single entry point of the diagram. Every process has exactly one Start node.
Nothing connects *into* a Start; it only has an outgoing connection.

### End
**Shape:** Rounded pill · **Colour:** Red

A terminal point. A diagram can have multiple End nodes (e.g. *Success*, *Rejected*,
*Timeout*). Nothing connects *out of* an End.

---

## Activities

### Task
**Shape:** Rectangle · **Colour:** Blue

A single process step or activity performed by a person or system.

| Property | Description |
|----------|-------------|
| Responsible | Person or role who performs the task |
| Est. Duration | Rough time estimate, e.g. `2h`, `1d` |

### Sub-Process
**Shape:** Rectangle with `+` · **Colour:** Indigo

A compound activity that expands into its own diagram. Use this when a step is too
complex to show inline — reference a separate process by name.

| Property | Description |
|----------|-------------|
| Process Reference | Name or ID of the sub-process, e.g. `Payment-v2` |

---

## Gateways

### Decision
**Shape:** Diamond · **Colour:** Amber

A conditional branch point. A Decision node has two outgoing connections:
one for **Yes** (the condition is true) and one for **No**.

| Property | Description | Required |
|----------|-------------|---------|
| Condition | The question being tested, e.g. `amount > 1000` | Yes |

---

## Data

### Document
**Shape:** Page with wavy bottom · **Colour:** Green

A document produced or consumed during the process (e.g. an invoice, a report).
Connections to/from a Document are optional.

| Property | Description |
|----------|-------------|
| Document Name | What the document is, e.g. `Invoice PDF` |
| Format | File or data format, e.g. `PDF`, `JSON` |

### Database
**Shape:** Cylinder · **Colour:** Purple

A persistent data store that the process reads from or writes to.

| Property | Description |
|----------|-------------|
| Table / Collection | e.g. `orders`, `customers` |
| Operation | `READ`, `WRITE`, or `UPDATE` |

### I/O
**Shape:** Parallelogram · **Colour:** Teal

An external input or output operation — anything that crosses the process boundary,
such as a form submission, an API call, or an email.

| Property | Description |
|----------|-------------|
| Channel | How the data moves, e.g. `REST API`, `Form`, `Email` |

---

## Connection rules

| Rule | Detail |
|------|--------|
| Nothing connects *into* Start | Start is always the entry point |
| Nothing connects *out of* End | End is always a terminal |
| Decision has exactly two outputs | Yes and No |
| All other nodes | Any number of inputs and outputs |

---

## Validation

Transita checks diagrams for common mistakes:

| Check | What it catches |
|-------|----------------|
| Single Start | Diagram must have exactly one Start node |
| At least one End | Diagram must have at least one End node |
| All nodes reachable | Every node must be reachable from Start |
| Orphaned nodes | Nodes not connected to the main flow are flagged in the pseudocode view |

---

*→ [Getting Started](getting-started.md)*
