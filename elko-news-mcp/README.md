# elko-news-mcp

A self-hosted news daemon that continuously polls RSS/Atom feeds, stores articles in SQLite, and exposes them via MCP, REST API, and a web dashboard.

![elko-news dashboard — Procedures pane](https://raw.githubusercontent.com/jsoprych/elko-docs/main/assets/elko-news-mcp/02-procedures.png)

🐳 **[Docker Hub → hub.docker.com/r/jsoprych/elko-news-mcp](https://hub.docker.com/r/jsoprych/elko-news-mcp)**

---

## Quick Start

```bash
docker pull jsoprych/elko-news-mcp:latest
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

67 sources polled out of the box across five categories:

| Category | Sources (sample) |
|----------|-----------------|
| **News & World** | Reuters, AP, BBC, Guardian, Al Jazeera, France 24, DW, NHK, SCMP, Straits Times, CBC, and more |
| **Finance & Markets** | Bloomberg, WSJ, FT, MarketWatch, The Economist |
| **Technology** | TechCrunch, The Verge, Ars Technica, Wired, MIT Tech Review, VentureBeat, Hugging Face Blog |
| **Science & AI** | arXiv (cs.AI, cs.CL, cs.CV, cs.LG, cs.RO, stat.ML), Tech Xplore, ScienceDaily, Nature |
| **Opinion & Politics** | Politico, Foreign Policy |

Each feed carries editorial metadata: owner, lean, country — queryable as filters.

→ [Full feeds guide](feeds.md) — feed format, ownership metadata, adding custom feeds

---

## Documentation

- [Getting Started](getting-started.md)
- [Feed Configuration](feeds.md)
- [SQL Procedures](procedures.md)
- [Dashboard Guide](dashboard.md)
- [MCP Setup](mcp-setup.md)
- [REST API](api.md)
- [Docker & Configuration](docker.md)


---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*