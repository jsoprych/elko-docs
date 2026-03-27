# Treasury Yields Tool

Live and historical U.S. Treasury yield curve data from Treasury.gov. No API key required.

---

## `treasury_yields`

Full yield curve snapshot or historical time series — 1-month through 30-year maturities.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `latest` | bool | | `true` = most recent day only (default: false) |
| `from` | string | | Start date `YYYY-MM-DD` |
| `to` | string | | End date `YYYY-MM-DD` |

### Examples

```bash
# Today's yield curve
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"treasury_yields","arguments":{"latest":true}}}'

# Historical range
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"treasury_yields","arguments":{"from":"2024-01-01","to":"2024-12-31"}}}'
```

```python
import requests

# Get latest yield curve
r = requests.post("http://localhost:8082/mcp", json={
    "jsonrpc": "2.0", "id": 1, "method": "tools/call",
    "params": {"name": "treasury_yields", "arguments": {"latest": True}}
})
print(r.json()["result"]["content"][0]["text"])
```

### Sample Output — Latest

```
date        1mo   2mo   3mo   6mo   1y    2y    3y    5y    7y    10y   20y   30y
2024-03-27  5.37  5.40  5.41  5.35  5.10  4.72  4.55  4.35  4.33  4.30  4.55  4.40
```

### Sample Output — Historical (CSV)

```
date,1mo,2mo,3mo,6mo,1y,2y,3y,5y,7y,10y,20y,30y
2024-01-02,5.41,5.44,5.46,5.39,4.97,4.45,4.25,4.02,4.01,3.99,4.27,4.12
2024-01-03,5.41,5.45,5.46,5.37,4.93,4.41,4.21,3.98,3.97,3.96,4.25,4.11
...
```

The dashboard renders historical data as a line chart. Great for visualizing yield curve shape and inversion.

---

### Ask Your AI

> *"Is the yield curve currently inverted?"*
> *"Show me the 10-year yield trend for the past year."*
> *"Compare the 2-year and 10-year yields over the last 6 months."*
