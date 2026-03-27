# Running Both Servers

elko-news (port 8081) and elko-market (port 8082) are designed to run simultaneously. Together they give your AI assistant live news AND live market data in the same session.

---

## Docker Compose (recommended)

```yaml
services:
  elko-news:
    image: jsoprych/elko-news-mcp:latest
    container_name: elko-news
    ports:
      - "8081:8081"
    volumes:
      - elko-news-data:/data
    restart: unless-stopped

  elko-market:
    image: jsoprych/elko-market-mcp:latest
    container_name: elko-market
    ports:
      - "8082:8082"
    volumes:
      - elko-market-data:/data
    restart: unless-stopped
    environment:
      - FRED_API_KEY=${FRED_API_KEY:-}
      - SEC_USER_AGENT=${SEC_USER_AGENT:-}

volumes:
  elko-news-data:
  elko-market-data:
```

```bash
# Start both
docker compose up -d

# Check both are running
curl -s localhost:8081/health
curl -s localhost:8082/health

# Stop both
docker compose down
```

---

## Separate docker run Commands

```bash
docker run -d --name elko-news   -p 8081:8081 -v elko-news-data:/data   jsoprych/elko-news-mcp:latest
docker run -d --name elko-market -p 8082:8082 -v elko-market-data:/data jsoprych/elko-market-mcp:latest
```

---

## Connect Both to Claude

```bash
# Generate configs
curl -s localhost:8081/mcp.json > .mcp.json.news
curl -s localhost:8082/mcp.json > .mcp.json.market

# Merge into one .mcp.json
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

## Cross-Server Queries

With both servers connected, Claude can combine news and market data in a single response:

> *"What's happening with Apple in the news, and how is AAPL stock performing today?"*

> *"Are there any Fed-related news stories today? And what did the 10-year Treasury yield do?"*

> *"Search for earnings news and then pull AAPL's last quarter income statement."*

> *"Give me a market briefing — top headlines, current yields, and S&P 500 status."*


---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*