# Getting Started — elko-market-mcp

## 1. Run the Container

```bash
docker run -d --name elko-market \
  -p 8082:8082 \
  -v elko-market-data:/data \
  jsoprych/elko-market-mcp:latest
```

Open **http://localhost:8082** — the dashboard is ready.

---

## 2. Try a Tool

In the dashboard: select `yahoo_quote` from the sidebar, enter `AAPL`, click **Run**.

Or via curl:
```bash
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"yahoo_quote","arguments":{"symbol":"AAPL"}}}'
```

---

## 3. Connect Your AI Assistant

**Generate MCP config:**
```bash
curl -s localhost:8082/mcp.json > .mcp.json
```

**Claude Code** — run from your project directory:
```bash
curl -s localhost:8082/mcp.json > .mcp.json
claude  # picks up .mcp.json automatically
```

**Claude Desktop** — add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "elko-market": {
      "command": "docker",
      "args": ["run","--rm","-i","-v","elko-market-data:/data","jsoprych/elko-market-mcp:latest","mcp"]
    }
  }
}
```

**Cursor** — same JSON in MCP settings.

→ [Full MCP setup guide](mcp-setup.md)

---

## 4. Ask Your AI Assistant

Once connected, you can ask in plain English:

> *"What's Apple's current stock price and PE ratio?"*
> *"Show me the 10-year Treasury yield over the last 5 years."*
> *"What did Apple's revenue look like last 4 quarters?"*
> *"Which FDIC banks in Texas have the highest ROA?"*
> *"What's the current CPI trend from BLS data?"*

---

## 5. Optional API Keys

Most tools work without keys. Some have rate limits that keys lift:

| Key | Tool | Where to get |
|-----|------|-------------|
| `FRED_API_KEY` | `fred_series`, `fred_search` | [fred.stlouisfed.org/docs/api](https://fred.stlouisfed.org/docs/api/api_key.html) — free |
| `BLS_API_KEY` | `bls_series` | [data.bls.gov](https://data.bls.gov/registrationEngine/) — free |
| `SEC_USER_AGENT` | `edgar_*` | Your name + email — recommended, not a key |

```bash
docker run -d --name elko-market \
  -p 8082:8082 \
  -v elko-market-data:/data \
  -e FRED_API_KEY=your_key \
  -e SEC_USER_AGENT="Your Name your@email.com" \
  jsoprych/elko-market-mcp:latest
```

→ [Full Docker configuration](docker.md)
