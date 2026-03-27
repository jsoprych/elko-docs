# REST API Reference — elko-news-mcp

Base URL: `http://localhost:8081`

---

## Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `GET` | `/health` | No | Status, article count, sources |
| `GET` | `/v1/key-status` | No | Easy key + pro key status |
| `GET` | `/v1/headlines` | Yes | Recent articles with filters |
| `GET` | `/v1/search` | Yes | Full-text search |
| `GET` | `/v1/sources` | Yes | Article counts per source |
| `GET` | `/v1/procedures` | Yes | List saved procedures |
| `POST` | `/v1/procedures` | Yes | Create or update a procedure |
| `DELETE` | `/v1/procedures/{name}` | Yes | Delete a procedure |
| `POST` | `/v1/procedures/{name}/run` | Yes | Execute a procedure |
| `POST` | `/v1/fetch` | Yes | Trigger immediate poll of all feeds |
| `POST` | `/v1/query` | Yes | Run an ad-hoc SELECT query |
| `GET` | `/mcp.json` | No | Self-describing MCP config |
| `POST` | `/mcp` | Yes | MCP JSON-RPC 2.0 endpoint |

---

## `GET /health`

```bash
curl -s localhost:8081/health
```

```json
{"status":"ok","articles":12483,"sources":6}
```

---

## `GET /v1/headlines`

Query parameters: `?source=`, `?category=`, `?limit=`, `?hours=`

```bash
# Last 6 hours, all sources
curl -s "localhost:8081/v1/headlines?hours=6&limit=20"

# Reuters only
curl -s "localhost:8081/v1/headlines?source=reuters&limit=10"

# Technology category
curl -s "localhost:8081/v1/headlines?category=technology&hours=12"
```

---

## `GET /v1/search`

Query parameters: `?q=` (required), `?source=`, `?category=`, `?limit=`

```bash
curl -s "localhost:8081/v1/search?q=Federal+Reserve+rates&limit=10"
curl -s "localhost:8081/v1/search?q=AAPL+earnings&source=reuters"
```

---

## `POST /v1/procedures`

```bash
curl -s -X POST localhost:8081/v1/procedures \
  -H "Content-Type: application/json" \
  -d '{
    "name": "crypto_news_2h",
    "description": "Crypto news from last 2 hours",
    "sql": "SELECT title, url, source, published FROM articles WHERE published > unixepoch() - 7200 AND (title LIKE '\''%bitcoin%'\'' OR title LIKE '\''%crypto%'\'' OR title LIKE '\''%ethereum%'\'') ORDER BY published DESC"
  }'
```

---

## `POST /v1/query`

Ad-hoc SELECT queries only — no mutations.

```bash
curl -s -X POST localhost:8081/v1/query \
  -H "Content-Type: application/json" \
  -d '{"sql":"SELECT source, COUNT(*) as articles FROM articles WHERE published > unixepoch() - 3600 GROUP BY source ORDER BY articles DESC"}'
```

---

## `POST /v1/fetch`

Trigger an immediate poll of all feeds (bypasses interval timer).

```bash
curl -s -X POST localhost:8081/v1/fetch
```

---

## MCP JSON-RPC 2.0

```bash
# Headlines
curl -s -X POST http://localhost:8081/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"news_headlines","arguments":{"hours":6,"limit":10}}}'

# Search
curl -s -X POST http://localhost:8081/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"news_search","arguments":{"query":"Fed interest rates","limit":5}}}'

# Run a saved procedure
curl -s -X POST http://localhost:8081/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"fed_news_today","arguments":{}}}'
```


---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*