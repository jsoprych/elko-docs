# REST API Reference — elko-market-mcp

Base URL: `http://localhost:8082`

---

## Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `GET` | `/health` | No | Status, version, tool count |
| `GET` | `/v1/key-status` | No | Easy key + pro key status |
| `GET` | `/v1/catalogue` | No | All registered tools with schemas |
| `GET` | `/v1/keys` | No | API key status (env/config/unset per key) |
| `GET` | `/mcp.json` | No | Self-describing MCP config |
| `GET` | `/openapi.json` | No | OpenAPI 3.0 spec for ChatGPT Custom GPT |
| `POST` | `/mcp` | No | MCP JSON-RPC 2.0 endpoint |
| `POST` | `/v1/call/{tool}` | Yes | Invoke a tool |
| `GET` | `/v1/logs` | Yes | Recent call log entries (requires `--db`) |
| `PUT` | `/v1/api-keys/{env}` | Yes | Save an API key to the server |
| `DELETE` | `/v1/api-keys/{env}` | Yes | Clear a saved API key |
| `GET` | `/v1/procedures` | Yes | List SQL procedures |
| `POST` | `/v1/procedures` | Yes | Create or update a SQL procedure |
| `GET` | `/v1/procedures/{name}` | Yes | Get a single procedure |
| `DELETE` | `/v1/procedures/{name}` | Yes | Delete a procedure |

"Auth" means the request must carry a valid easy key or pro key header.

---

## `GET /health`

```bash
curl -s localhost:8082/health
```

```json
{"status":"ok","version":"0.4.0","tools":13,"db":true}
```

---

## `GET /v1/catalogue`

Returns all tools with their JSON Schema parameter definitions.

```bash
curl -s localhost:8082/v1/catalogue
```

Filter by source or category:
```bash
curl -s "localhost:8082/v1/catalogue?source=yahoo"
curl -s "localhost:8082/v1/catalogue?category=macro"
```

---

## `POST /v1/call/{tool}`

Invoke any tool directly via REST.

```bash
curl -s -X POST http://localhost:8082/v1/call/yahoo_quote \
  -H "Content-Type: application/json" \
  -d '{"symbol":"AAPL"}'
```

```bash
curl -s -X POST http://localhost:8082/v1/call/treasury_yields \
  -H "Content-Type: application/json" \
  -d '{"latest":true}'
```

---

## `GET /v1/keys`

Returns the status of each declared API key — whether it is set from an environment
variable, saved via the dashboard, or unset.

```bash
curl -s localhost:8082/v1/keys
```

```json
{
  "keys": [
    {
      "source": "fred",
      "env": "FRED_API_KEY",
      "required": true,
      "set": false,
      "source_kind": "unset",
      "help_url": "https://fred.stlouisfed.org/docs/api/api_key.html",
      "description": "FRED — free registration required",
      "persistent": true
    }
  ],
  "missing_required": ["FRED_API_KEY"],
  "persistent": true
}
```

`source_kind` values: `"env"` (set at startup via environment variable), `"config"` (saved
from the dashboard), `"unset"`.

---

## `PUT /v1/api-keys/{env}`

Save an API key. Takes effect immediately — no restart needed. With `--db`, the key
persists to the data volume across restarts.

```bash
curl -s -X PUT http://localhost:8082/v1/api-keys/FRED_API_KEY \
  -H "Content-Type: application/json" \
  -d '{"value":"abcdef1234567890"}'
```

```json
{"env":"FRED_API_KEY","set":true,"persistent":true,"note":"FRED_API_KEY is now active. Saved to database — persists across restarts."}
```

Only keys declared in channel specs (`FRED_API_KEY`, `BLS_API_KEY`, `SEC_USER_AGENT`) are accepted.

---

## `DELETE /v1/api-keys/{env}`

Clear a key that was saved via `PUT`. Keys that were set in the process environment
at startup cannot be cleared this way (restart the container without the env var instead).

```bash
curl -s -X DELETE http://localhost:8082/v1/api-keys/FRED_API_KEY
```

```json
{"env":"FRED_API_KEY","set":false,"cleared":true}
```

---

## SQL Procedures

Named `SELECT`/`WITH` queries stored in the database. Each saved procedure auto-registers
as a live MCP tool and is callable via `POST /v1/call/{name}`.

Template substitution: `{{param}}` in the SQL is replaced with the caller's argument.

### `GET /v1/procedures`

```bash
curl -s localhost:8082/v1/procedures
```

### `POST /v1/procedures`

Create or update a procedure:

```bash
curl -s -X POST http://localhost:8082/v1/procedures \
  -H "Content-Type: application/json" \
  -d '{
    "name": "slow_tools",
    "description": "Tools with the highest average response time",
    "sql": "SELECT tool, ROUND(AVG(duration_ms)) AS avg_ms, COUNT(*) AS calls FROM call_log GROUP BY tool ORDER BY avg_ms DESC LIMIT {{limit}}",
    "parameters": [
      {"name":"limit","type":"integer","description":"Max rows","required":false,"default":10}
    ]
  }'
```

The procedure is immediately available as a tool:

```bash
curl -s -X POST http://localhost:8082/v1/call/slow_tools \
  -H "Content-Type: application/json" \
  -d '{"limit":5}'
```

### `DELETE /v1/procedures/{name}`

```bash
curl -s -X DELETE http://localhost:8082/v1/procedures/slow_tools
```

---

## `POST /mcp` — JSON-RPC 2.0

Standard MCP protocol endpoint.

### Initialize

```bash
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{}}}'
```

### List Tools

```bash
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```

### Call Tool

```bash
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "yahoo_quote",
      "arguments": {"symbol": "AAPL"}
    }
  }'
```

### Response Format

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "symbol    AAPL\nprice     172.43\n..."
      }
    ]
  }
}
```

---

## `GET /v1/logs`

Recent tool call log (requires `--db` flag).

```bash
curl -s localhost:8082/v1/logs
curl -s "localhost:8082/v1/logs?limit=50&tool=yahoo_quote&error=true"
```

---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*
