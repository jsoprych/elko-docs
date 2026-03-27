# FDIC Tools

FDIC bank data — search institutions and pull financial health metrics. No API key required.

---

## `fdic_bank_search`

Find FDIC-insured banks by name, state, or city.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | | Bank name (partial match) |
| `state` | string | | Two-letter state code, e.g. `TX`, `NY` |
| `limit` | int | | Max results (default: 10) |

### Examples

```bash
# Search by name
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"fdic_bank_search","arguments":{"name":"Wells Fargo"}}}'

# All banks in Texas
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"fdic_bank_search","arguments":{"state":"TX","limit":20}}}'
```

### Sample Output

```
cert    name                     city         state  asset_size
3511    Wells Fargo Bank, NA     Sioux Falls  SD     1.93T
478480  Wells Fargo Bank South   Phoenix      AZ     4.2B
...
```

Use the `cert` number with `fdic_bank_financials` to get financial details.

---

## `fdic_bank_financials`

Financial health metrics for any FDIC-insured institution.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `cert` | int | ✓ | FDIC certificate number (from `fdic_bank_search`) |
| `periods` | int | | Number of reporting periods (default: 4) |

### Example

```bash
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"fdic_bank_financials","arguments":{"cert":3511,"periods":4}}}'
```

```python
import requests
r = requests.post("http://localhost:8082/mcp", json={
    "jsonrpc": "2.0", "id": 1, "method": "tools/call",
    "params": {"name": "fdic_bank_financials", "arguments": {"cert": 3511, "periods": 4}}
})
print(r.json()["result"]["content"][0]["text"])
```

### Sample Output

```
metric            2024-Q3     2024-Q2     2024-Q1     2023-Q4
total_assets      1.93T       1.93T       1.93T       1.93T
total_deposits    1.34T       1.34T       1.36T       1.36T
total_equity      196.4B      195.1B      191.8B      191.1B
net_income        5.6B        4.9B        4.6B        3.4B
roa               1.17%       1.02%       0.96%       0.71%
roe               11.5%       10.2%       9.8%        7.2%
tier1_capital     11.9%       11.8%       11.6%       11.4%
```

### Ask Your AI

> *"Which community banks in North Carolina have the highest ROE?"*
> *"Compare JPMorgan and Wells Fargo's capital ratios."*
> *"Show me SVB's financials for the 4 quarters before it failed."*
