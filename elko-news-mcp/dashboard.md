# elko-news-mcp — Dashboard Guide

The web dashboard is served at **http://localhost:8081** when the container is running.
No login required — open it in any browser.

---

## Panes

### Headlines

Live article feed. Search bar and filter controls (source, category, lean, country, time window). Click any headline to open the original article. **Fetch All** button triggers an immediate server-side poll of every feed. Export dropdown downloads results as JSON, CSV, or Markdown.

### Procedures

![elko-news dashboard — Procedures pane](https://raw.githubusercontent.com/jsoprych/elko-docs/main/assets/elko-news-mcp/02-procedures.png)

Saved SQL procedures — each one is automatically exposed as an MCP tool your AI assistant can call by name.

- **Name** — the MCP tool name (e.g. `fed_news_today`)
- **Description** — shown to the AI as the tool description
- **SQL** — a `SELECT` query against the articles table
- **JSON-RPC tab** — ready-to-copy `curl` and Python snippets for each procedure

**Create a procedure:**
1. Click **New Procedure**
2. Enter a name, description, and SELECT query
3. Click **Save** — it immediately appears as an MCP tool

Three starter procedures are seeded on first run: `fed_news_today`, `tech_headlines`, `market_movers`.

### Sources

Publication ownership table — name, owner, type, HQ country, stock ticker (if public), editorial lean, and article count. Click **Enrich** on any source to fetch live metadata from Wikidata.

### MCP Playground

Interactive tool tester. Pick a tool, fill in parameters, click **Call**, and see the raw MCP result alongside the ready-to-copy `curl` snippet.

### Status

Health card (articles, sources, version), easy-key expiry and rate-limit usage, lean distribution chart, and per-source article counts.

---

## API Keys

Click the 🔑 **Keys** button in the status bar to open the key management panel.
No keys are required for elko-news-mcp — this panel is available for future
feed sources that require authentication headers.

---

## Theme Toggle

Click the theme button (top of sidebar) to cycle:

| Mode | Description |
|------|-------------|
| Light | Default white background |
| Dark | Dark charcoal background |
| High-contrast | Pure black-on-white, `#0000cc` accent |

---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*
