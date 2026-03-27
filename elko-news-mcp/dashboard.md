# elko-news-mcp — Dashboard Guide

The web dashboard is served at **http://localhost:8081** when the container is running.
No login required — open it in any browser.

---

## Panes

### Headlines

Live article feed. Filter by source, category, or time window. Click any headline to open the original article.

### Search

Full-text search across article titles and summaries (SQLite FTS5). Results update as you type.

### Procedures

![elko-news dashboard — Procedures pane](https://raw.githubusercontent.com/jsoprych/elko-docs/main/assets/elko-news-mcp/02-procedures.png)

Saved SQL procedures — each one is automatically exposed as an MCP tool your AI assistant can call by name.

- **Name** — the MCP tool name (e.g. `fed_news_today`)
- **Description** — shown to the AI as the tool description
- **SQL** — a `SELECT` query; use `{{param}}` placeholders for runtime substitution
- **JSON-RPC tab** — ready-to-copy `curl` and Python snippets for each procedure

**Create a procedure:**
1. Click **New Procedure**
2. Enter a name, description, and SELECT query
3. Click **Save** — it immediately appears as an MCP tool

### Sources

Article counts per feed source. Shows which sources are active and how many articles each has contributed.

### Status

Health card, key info (easy key expiry, rate limits), and feed poll status.

---

## Theme Toggle

Click the **◑ Normal** button (top-right) to cycle themes:

| Mode | Description |
|------|-------------|
| Light | Default white background |
| Dark | Dark charcoal background |
| High-contrast | Pure black-on-white, `#0000cc` accent — maximum readability |

---

## Export

From the Headlines pane, use the **Export** dropdown to download articles as:
- `JSON` — full structured data
- `CSV` — spreadsheet-friendly
- `Markdown` — paste into notes or docs

---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*
