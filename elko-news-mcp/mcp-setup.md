# MCP Setup — elko-news-mcp

## Claude Code (CLI)

```bash
curl -s localhost:8081/mcp.json > .mcp.json
claude
```

Ask:
> *"What are the top stories from the last hour?"*
> *"Search for news about Federal Reserve rate decisions."*
> *"Run the fed_news_today procedure and summarize the key themes."*

---

## Claude Desktop

```json
{
  "mcpServers": {
    "elko-news": {
      "command": "docker",
      "args": [
        "run", "--rm", "-i",
        "-v", "elko-news-data:/data",
        "jsoprych/elko-news-mcp:latest",
        "mcp", "--db", "/data/elko-news.db"
      ]
    }
  }
}
```

Or HTTP transport to a running container:
```json
{
  "mcpServers": {
    "elko-news": {
      "url": "http://localhost:8081/mcp"
    }
  }
}
```

---

## Cursor

```json
{
  "elko-news": {
    "url": "http://localhost:8081/mcp"
  }
}
```

---

## Python

```python
import requests

BASE = "http://localhost:8081/mcp"

def call_tool(name, **args):
    r = requests.post(BASE, json={
        "jsonrpc": "2.0", "id": 1,
        "method": "tools/call",
        "params": {"name": name, "arguments": args}
    })
    return r.json()["result"]["content"][0]["text"]

# Latest headlines
print(call_tool("news_headlines", hours=6, limit=10))

# Search
print(call_tool("news_search", query="Federal Reserve", limit=5))

# Run a saved procedure
print(call_tool("fed_news_today"))
```

---

## Run Both Servers Together

```bash
curl -s localhost:8081/mcp.json > elko-news.mcp.json
curl -s localhost:8082/mcp.json > elko-market.mcp.json
```

Or merge into a single `.mcp.json`:
```json
{
  "mcpServers": {
    "elko-news":   { "url": "http://localhost:8081/mcp" },
    "elko-market": { "url": "http://localhost:8082/mcp" }
  }
}
```

Then ask Claude:
> *"What's in the news about Apple, and what does their stock look like right now?"*

→ [Running both servers](../advanced/running-both.md)


---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*