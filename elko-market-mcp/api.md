# REST API Reference — elko-market-mcp

Base URL: `http://localhost:8082`

---

## Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `GET` | `/health` | No | Status, version, tool count |
| `GET` | `/v1/key-status` | No | Easy key + pro key status |
| `GET` | `/v1/key-info` | No | Key detail card |
| `GET` | `/v1/catalogue` | Yes | All registered tools with schemas |
| `POST` | `/v1/call/{tool}` | Yes | Invoke a tool |
| `GET` | `/v1/keys` | Yes | API key configuration status |
| `GET` | `/v1/logs` | Yes | Recent call log entries |
| `GET` | `/mcp.json` | No | Self-describing MCP config |
| `POST` | `/mcp` | Yes | MCP JSON-RPC 2.0 endpoint |

---

## `GET /health`

```bash
curl -s localhost:8082/health
```

```json
{"status":"ok","version":"0.3.28","tools":13}
```

---

## `GET /v1/catalogue`

Returns all tools with their JSON Schema parameter definitions.

```bash
curl -s localhost:8082/v1/catalogue
```

```json
{
  "tools": [
    {
      "name": "yahoo_quote",
      "source": "yahoo",
      "category": "equity",
      "description": "Real-time quote for any ticker",
      "schema": {
        "symbol": {"type": "string", "required": true, "description": "Ticker symbol"}
      },
      "result_format": "kv"
    },
    ...
  ]
}
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

## `POST /mcp` — JSON-RPC 2.0

Standard MCP protocol endpoint.

### Initialize

```bash
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{}}}'
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
```

```json
{
  "logs": [
    {
      "ts": 1711574400,
      "tool": "yahoo_quote",
      "args": {"symbol": "AAPL"},
      "duration_ms": 234,
      "error": null
    }
  ]
}
```


---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*