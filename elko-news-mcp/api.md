# REST API Reference — elko-news-mcp

Base URL: `http://localhost:8081`

---

## Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `GET` | `/health` | No | Status, article count, feed health summary |
| `GET` | `/v1/key-status` | No | Easy key + pro key status |
| `GET` | `/v1/key-info` | No | Key detail card (expiry, days remaining) |
| `GET` | `/v1/feed-health` | No | Per-feed status — ok / fail / dead |
| `GET` | `/v1/keys` | No | API key status (env/config/unset) |
| `GET` | `/mcp.json` | No | Self-describing MCP config |
| `GET` | `/openapi.json` | No | OpenAPI 3.0 spec for ChatGPT Custom GPT |
| `POST` | `/mcp` | No | MCP JSON-RPC 2.0 endpoint |
| `PUT` | `/v1/keys` | Yes | Save an API key (persisted to volume) |
| `DELETE` | `/v1/keys/{name}` | Yes | Clear a saved API key |
| `GET` | `/v1/headlines` | Yes | Recent articles with filters |
| `GET` | `/v1/search` | Yes | Full-text search |
| `GET` | `/v1/sources` | Yes | Sources with ownership metadata |
| `PUT` | `/v1/sources/{name}` | Yes | Update source metadata |
| `POST` | `/v1/sources/{name}/enrich` | Yes | Fetch Wikidata data for a source |
| `GET` | `/v1/procedures` | Yes | List saved SQL procedures |
| `POST` | `/v1/procedures` | Yes | Create or update a procedure |
| `DELETE` | `/v1/procedures/{name}` | Yes | Delete a procedure |
| `POST` | `/v1/procedures/{name}/run` | Yes | Execute a procedure |
| `POST` | `/v1/fetch` | Yes | Trigger immediate poll of all feeds |
| `POST` | `/v1/query` | Yes | Run an ad-hoc SELECT query |
| `GET` | `/v1/export` | Yes | Bulk export (`?format=json\|csv\|md`) |
| `GET` | `/v1/logs` | Yes | Recent call log (requires `--log-max-output`) |

---

## `GET /health`

```bash
curl -s localhost:8081/health
```

```json
{
  "status": "ok",
  "version": "0.5.0",
  "articles": 12483,
  "sources": 42,
  "feeds_ok": 65,
  "feeds_fail": 2,
  "feeds_dead": 0,
  "logging": false
}
```

`status` is `"degraded"` when any feeds are in `fail` or `dead` state.

---

## `GET /v1/feed-health`

Per-feed health status. Updated automatically after every poll attempt.

```bash
curl -s localhost:8081/v1/feed-health
```

```json
{
  "feeds": [
    {
      "feed_name": "bloomberg_markets",
      "last_attempt": "2026-05-14T12:00:00Z",
      "last_success": "2026-05-14T12:00:00Z",
      "error_count": 0,
      "status": "ok"
    },
    {
      "feed_name": "some_broken_feed",
      "last_attempt": "2026-05-14T12:00:00Z",
      "last_success": "2026-05-14T10:00:00Z",
      "error_count": 3,
      "last_error": "fetch some_broken_feed: HTTP 404",
      "status": "fail"
    }
  ],
  "count": 67,
  "summary": {"ok": 65, "fail": 2, "dead": 0, "unknown": 0}
}
```

Status values: `ok` — healthy; `fail` — 1–4 consecutive errors; `dead` — 5+ consecutive errors; `unknown` — not yet polled.

---

## `GET /v1/headlines`

Query parameters: `?source=`, `?category=`, `?lean=`, `?country=`, `?limit=`, `?hours=`

```bash
# Last 6 hours, all sources
curl -s "localhost:8081/v1/headlines?hours=6&limit=20"

# Reuters only
curl -s "localhost:8081/v1/headlines?source=reuters&limit=10"

# Left-leaning tech sources
curl -s "localhost:8081/v1/headlines?category=technology&lean=center-left"

# UK articles last 24h
curl -s "localhost:8081/v1/headlines?country=GB&hours=24"
```

---

## `GET /v1/search`

Query parameters: `?q=` (required), `?source=`, `?category=`, `?lean=`, `?country=`, `?limit=`

```bash
curl -s "localhost:8081/v1/search?q=Federal+Reserve+rates&limit=10"
curl -s "localhost:8081/v1/search?q=AAPL+earnings&source=reuters"
```

---

## `GET /v1/export`

Bulk export of all articles.

```bash
curl -s "localhost:8081/v1/export?format=json" > articles.json
curl -s "localhost:8081/v1/export?format=csv"  > articles.csv
curl -s "localhost:8081/v1/export?format=md"   > articles.md
```

---

## `POST /v1/procedures`

```bash
curl -s -X POST localhost:8081/v1/procedures \
  -H "Content-Type: application/json" \
  -d '{
    "name": "crypto_news_2h",
    "description": "Crypto news from last 2 hours",
    "sql": "SELECT title, url, source, published FROM articles WHERE published > unixepoch() - 7200 AND (title LIKE '\''%bitcoin%'\'' OR title LIKE '\''%crypto%'\'') ORDER BY published DESC"
  }'
```

---

## `GET /v1/logs`

Recent call log — only available when server is started with `--log-max-output`:

```bash
curl -s "localhost:8081/v1/logs?limit=50"
curl -s "localhost:8081/v1/logs?tool=news_search"
curl -s "localhost:8081/v1/logs?error=true"
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
