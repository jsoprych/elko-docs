# Getting Started — elko-news-mcp

## 1. Run the Container

```bash
docker run -d --name elko-news \
  -p 8081:8081 \
  -v elko-news-data:/data \
  jsoprych/elko-news-mcp:latest
```

Open **http://localhost:8081** — articles begin arriving within 30 seconds.

---

## 2. Try the Headlines Tool

```bash
curl -s -X POST http://localhost:8081/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"news_headlines","arguments":{"hours":6,"limit":10}}}'
```

---

## 3. Search for a Topic

```bash
curl -s -X POST http://localhost:8081/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"news_search","arguments":{"query":"Federal Reserve interest rates","limit":5}}}'
```

---

## 4. Connect Your AI Assistant

```bash
curl -s localhost:8081/mcp.json > .mcp.json
claude  # Claude Code picks it up automatically
```

Then ask:
> *"What are the top tech stories from the last 2 hours?"*
> *"Search for news about the Fed and summarize the key themes."*
> *"What's happening in markets today?"*

→ [Full MCP setup guide](mcp-setup.md)

---

## 5. Save a SQL Procedure

Open the dashboard → Procedures tab → write a SELECT query → Save.

It becomes an MCP tool instantly. Your AI assistant can call it by name.

Example:
```sql
SELECT title, url, published
FROM articles
WHERE published > unixepoch() - 3600
  AND (title LIKE '%earnings%' OR title LIKE '%revenue%')
ORDER BY published DESC
LIMIT 20
```

Save as `earnings_news_1h` — now callable via MCP as `tools/call { "name": "earnings_news_1h" }`.

→ [Procedures guide](procedures.md)


---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*