# Claude Integration Guide

## Claude Code (CLI) — Quickest Path

```bash
# 1. Start containers
docker run -d --name elko-news   -p 8081:8081 -v elko-news-data:/data   jsoprych/elko-news-mcp:latest
docker run -d --name elko-market -p 8082:8082 -v elko-market-data:/data jsoprych/elko-market-mcp:latest

# 2. Generate MCP config
cat > .mcp.json << 'EOF'
{
  "mcpServers": {
    "elko-news":   { "url": "http://localhost:8081/mcp" },
    "elko-market": { "url": "http://localhost:8082/mcp" }
  }
}
EOF

# 3. Start Claude
claude
```

Claude automatically discovers all tools from both servers. No configuration needed.

---

## Claude Desktop

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "elko-news": {
      "url": "http://localhost:8081/mcp"
    },
    "elko-market": {
      "url": "http://localhost:8082/mcp"
    }
  }
}
```

Restart Claude Desktop after editing. The tools appear in the toolbar.

---

## Cursor

Settings → Features → MCP → Add Server:

```json
{
  "elko-news":   { "url": "http://localhost:8081/mcp" },
  "elko-market": { "url": "http://localhost:8082/mcp" }
}
```

---

## What to Ask

### Market Research
> *"Get Apple's current quote, last 4 quarters of income statements, and any insider selling in the last month."*

### Macro Analysis
> *"Pull CPI from FRED, unemployment from BLS, and the current yield curve. Give me a macro summary."*

### News + Data Combined
> *"What's in the news about the Fed today? Then show me the federal funds rate history from FRED since 2022."*

### Earnings Season
> *"Search for earnings news from the last 24 hours. Then pull revenue and EPS for any companies mentioned."*

### Fixed Income
> *"Show me the Treasury yield curve and explain whether it's inverted."*

### Banking Analysis
> *"Find the top 10 banks in California by assets and compare their ROA and ROE."*

---

## Pro Tips

**Combine news search with financial data:**
```
User: "Is there news about AAPL? If so, what's the stock doing?"
```
Claude will call `news_search` then `yahoo_quote` in sequence.

**Create procedures from conversation:**
```
User: "Save a procedure called 'ai_news_4h' that returns AI news from the last 4 hours"
```
Claude will write the SQL and call `POST /v1/procedures` to save it.

**Schedule a morning briefing with a saved procedure:**
Create a procedure `morning_brief` that pulls headlines, market data via SQL, then ask Claude to run it each morning.
