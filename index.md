# Elko.AI — Documentation

**Elko** is a suite of self-hosted tools and MCP (Model Context Protocol) servers — run locally or in Docker, connect to Claude or any MCP-compatible client, and get live data back in plain English.

---

## Tools

### [elko-project-wizard](elko-project-wizard/README.md) — AI Project Scaffolder
Port `8080` · 🐳 [Docker Hub](https://hub.docker.com/r/jsoprych/elko-project-wizard) · `docker pull jsoprych/elko-project-wizard:latest`

Stop briefing your AI agent from a blank page. Pick directives, compose a profile, hit Generate — get a `.zip` with `AGENTS.md`, `CLAUDE.md`, `Dockerfile`, and more in under 60 seconds.

26 built-in directives · 11 categories · 8 tech stacks · Quick Start Wizard included

→ [Getting Started](elko-project-wizard/getting-started.md) · [Directives](elko-project-wizard/directives.md) · [Profiles](elko-project-wizard/profiles.md) · [Dashboard](elko-project-wizard/dashboard.md) · [API](elko-project-wizard/api.md) · [Docker](elko-project-wizard/docker.md)

---

## MCP Servers

### [elko-market-mcp](elko-market-mcp/README.md) — Financial Market Data
Port `8082` · 🐳 [Docker Hub](https://hub.docker.com/r/jsoprych/elko-market-mcp) · `docker pull jsoprych/elko-market-mcp:latest`

13 tools covering equities, bonds, macro, banking, and economic data:
Yahoo Finance · SEC EDGAR · U.S. Treasury · BLS · FDIC · World Bank · FRED

→ [Getting Started](elko-market-mcp/getting-started.md) · [Tools](elko-market-mcp/tools/) · [Dashboard](elko-market-mcp/dashboard.md) · [API](elko-market-mcp/api.md) · [Docker](elko-market-mcp/docker.md)

---

### [elko-news-mcp](elko-news-mcp/README.md) — News & RSS Feeds
Port `8081` · 🐳 [Docker Hub](https://hub.docker.com/r/jsoprych/elko-news-mcp) · `docker pull jsoprych/elko-news-mcp:latest`

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
