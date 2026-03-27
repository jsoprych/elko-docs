# elko-news-mcp

A self-hosted news daemon that continuously polls RSS/Atom feeds, stores articles in SQLite, and exposes them via MCP, REST API, and a web dashboard.

![elko-news dashboard — Procedures pane](https://raw.githubusercontent.com/jsoprych/elko-docs/main/assets/elko-news-mcp/02-procedures.png)

---

## Quick Start

```bash
docker run -d --name elko-news \
  -p 8081:8081 \
  -v elko-news-data:/data \
  jsoprych/elko-news-mcp:latest
```

Open **http://localhost:8081** — articles start appearing within 30 seconds.

---

## MCP Tools

| Tool | Description |
|------|-------------|
| `news_headlines` | Latest articles — filter by source, category, time window |
| `news_search` | Full-text search across title and summary (FTS5) |
| `news_sources` | Article counts per source |
| *saved procedures* | Any SQL procedure you save becomes an MCP tool automatically |

---

## Feeds

Sources polled out of the box:

| Source | Category | Interval |
|--------|----------|----------|
| Reuters Top News | general | 15m |
| Reuters Business | business | 15m |
| Associated Press | general | 15m |
| Hacker News | technology | 30m |
| Wall Street Journal Markets | markets | 15m |
| MarketWatch Headlines | markets | 15m |

→ [Full feeds guide](feeds.md) — adding custom feeds, intervals, headers

---

## Documentation

- [Getting Started](getting-started.md)
- [Feed Configuration](feeds.md)
- [SQL Procedures](procedures.md)
- [Dashboard Guide](dashboard.md)
- [MCP Setup](mcp-setup.md)
- [REST API](api.md)
- [Docker & Configuration](docker.md)
