# Elko.AI — Documentation

**Elko** is a suite of self-hosted MCP (Model Context Protocol) servers that connect your AI assistant to real-world data — no API keys required for core features, no cloud dependency, no usage caps.

Run them locally or in Docker. Connect Claude, Cursor, or any MCP-compatible client. Ask questions in plain English and get live data back.

---

## Servers

### [elko-market-mcp](elko-market-mcp/README.md) — Financial Market Data
Port `8082` · Docker: `jsoprych/elko-market-mcp:latest`

13 tools covering equities, bonds, macro, banking, and economic data:
Yahoo Finance · SEC EDGAR · U.S. Treasury · BLS · FDIC · World Bank · FRED

→ [Getting Started](elko-market-mcp/getting-started.md) · [Tools](elko-market-mcp/tools/) · [Dashboard](elko-market-mcp/dashboard.md) · [API](elko-market-mcp/api.md) · [Docker](elko-market-mcp/docker.md)

---

### [elko-news-mcp](elko-news-mcp/README.md) — News & RSS Feeds
Port `8081` · Docker: `jsoprych/elko-news-mcp:latest`

Polls RSS/Atom feeds continuously. Full-text search. SQL procedures auto-registered as MCP tools. Sources include Reuters, AP, Bloomberg, BBC, Hacker News, and more.

→ [Getting Started](elko-news-mcp/getting-started.md) · [Feeds](elko-news-mcp/feeds.md) · [Procedures](elko-news-mcp/procedures.md) · [Dashboard](elko-news-mcp/dashboard.md) · [API](elko-news-mcp/api.md)

---

## Run Both Together

```bash
docker run -d --name elko-news   -p 8081:8081 -v elko-news-data:/data   jsoprych/elko-news-mcp:latest
docker run -d --name elko-market -p 8082:8082 -v elko-market-data:/data jsoprych/elko-market-mcp:latest
```

Or with [Docker Compose](advanced/running-both.md).

---

## Connect to Claude

```bash
curl -s localhost:8081/mcp.json > elko-news.mcp.json
curl -s localhost:8082/mcp.json > elko-market.mcp.json
```

→ [Full MCP setup guide](advanced/claude-integration.md)

---

## Advanced

- [Running both servers](advanced/running-both.md)
- [Claude Desktop / Cursor integration](advanced/claude-integration.md)
- [Pro keys & key rotation](advanced/pro-keys.md)
- [SQL Procedures cookbook](advanced/procedures-cookbook.md)

---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*
