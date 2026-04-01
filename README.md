# elko-docs

Documentation for the **Elko.AI** suite of tools, visual editors, and MCP servers.

---

## Studio

| App | URL | Description |
|-----|-----|-------------|
| [Transita](transita/README.md) | [elko.ai/transita](https://elko.ai/transita) | Visual diagram editor — flowcharts, state machines, business workflows |

---

## Servers

| Server | Port | Docker Hub | Description |
|--------|------|-----------|-------------|
| [elko-project-wizard](elko-project-wizard/README.md) | 8080 | [jsoprych/elko-project-wizard](https://hub.docker.com/r/jsoprych/elko-project-wizard) | AI project scaffolder — 26 directives, 8 stacks, generates AGENTS.md + CLAUDE.md + Dockerfile |
| [elko-news-mcp](elko-news-mcp/README.md) | 8081 | [jsoprych/elko-news-mcp](https://hub.docker.com/r/jsoprych/elko-news-mcp) | RSS/Atom news daemon — headlines, search, SQL procedures |
| [elko-market-mcp](elko-market-mcp/README.md) | 8082 | [jsoprych/elko-market-mcp](https://hub.docker.com/r/jsoprych/elko-market-mcp) | 13 financial data tools — Yahoo, EDGAR, Treasury, FRED, BLS, FDIC, World Bank |

---

## Quick Start — Both Servers

```bash
docker pull jsoprych/elko-news-mcp:latest
docker pull jsoprych/elko-market-mcp:latest
docker compose -f examples/docker-compose.full.yml up -d
```

Connect to Claude:
```bash
cat > .mcp.json << 'EOF'
{
  "mcpServers": {
    "elko-news":   { "url": "http://localhost:8081/mcp" },
    "elko-market": { "url": "http://localhost:8082/mcp" }
  }
}
EOF
claude
```

---

## Contents

```
transita/               ← Visual diagram editor
  getting-started.md
  node-types.md         ← Business Process palette reference

elko-market-mcp/        ← Full documentation
  getting-started.md
  tools/                ← Per-tool reference (Yahoo, EDGAR, Treasury, BLS, FDIC, FRED, World Bank)
  dashboard.md
  mcp-setup.md
  api.md
  docker.md

elko-news-mcp/          ← Full documentation
  getting-started.md
  feeds.md
  procedures.md         ← SQL procedures as MCP tools
  dashboard.md
  mcp-setup.md
  api.md
  docker.md

advanced/
  running-both.md       ← Docker Compose for both servers
  claude-integration.md ← Claude Code / Desktop / Cursor setup
  pro-keys.md           ← Key lifecycle and rotation
  procedures-cookbook.md← 15+ ready-to-use SQL procedures

examples/
  docker-compose.full.yml          ← Both servers
  elko-market-mcp/
    docker-compose.yml
    python/             ← yahoo_quote.py, treasury_yields.py, edgar_financials.py
    curl/               ← examples.sh
  elko-news-mcp/
    docker-compose.yml
    python/             ← headlines.py, save_procedure.py

assets/                 ← Screenshots for Docker Hub READMEs
  elko-market-mcp/
  elko-news-mcp/
```

---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*
