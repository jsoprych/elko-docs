# MCP Setup — elko-market-mcp

Connect elko-market-mcp to any MCP-compatible AI client.

---

## Claude Code (CLI)

```bash
# Generate config from running server
curl -s localhost:8082/mcp.json > .mcp.json

# Start Claude — picks up .mcp.json automatically
claude
```

Then ask:
> *"Use the elko-market tools to get Apple's current price and last 4 quarters of earnings."*

---

## Claude Desktop

Edit `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "elko-market": {
      "command": "docker",
      "args": [
        "run", "--rm", "-i",
        "-v", "elko-market-data:/data",
        "jsoprych/elko-market-mcp:latest",
        "mcp"
      ]
    }
  }
}
```

Or connect to a running HTTP server:
```json
{
  "mcpServers": {
    "elko-market": {
      "url": "http://localhost:8082/mcp"
    }
  }
}
```

---

## Cursor

In Cursor settings → MCP → Add server:
```json
{
  "elko-market": {
    "url": "http://localhost:8082/mcp"
  }
}
```

---

## Python (requests)

```python
import requests

BASE = "http://localhost:8082/mcp"

def call_tool(name, **args):
    r = requests.post(BASE, json={
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": name, "arguments": args}
    })
    return r.json()["result"]["content"][0]["text"]

# Examples
print(call_tool("yahoo_quote", symbol="AAPL"))
print(call_tool("treasury_yields", latest=True))
print(call_tool("fred_series", series_id="FEDFUNDS", from_date="2022-01-01"))
```

---

## Python (langchain-mcp-adapters)

```python
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

client = MultiServerMCPClient({
    "elko-market": {
        "url": "http://localhost:8082/mcp",
        "transport": "streamable_http"
    }
})

tools = await client.get_tools()
agent = create_react_agent(ChatOpenAI(model="gpt-4o"), tools)
result = await agent.ainvoke({"messages": [{"role": "user", "content": "What is the current 10-year Treasury yield?"}]})
```

---

## curl (JSON-RPC 2.0)

```bash
# List all available tools
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'

# Call a tool
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"yahoo_quote","arguments":{"symbol":"TSLA"}}}'
```

---

## MCP Config File

The server self-describes its tools at `/mcp.json`:

```bash
curl -s localhost:8082/mcp.json
```

```json
{
  "mcpServers": {
    "elko-market": {
      "url": "http://localhost:8082/mcp",
      "transport": "streamable-http"
    }
  }
}
```


---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*