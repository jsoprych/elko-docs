# BLS Tool

Bureau of Labor Statistics data — CPI, unemployment, payrolls, PPI, and more. Free API key increases daily request limit from 25 to 500.

**Get a free key:** [data.bls.gov/registrationEngine](https://data.bls.gov/registrationEngine/)

```bash
docker run -e BLS_API_KEY=your_key ...
```

---

## `bls_series`

Fetch any BLS time series by series ID.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `series_id` | string | ✓ | BLS series ID |
| `from` | string | | Start year (e.g. `2020`) |
| `to` | string | | End year (e.g. `2024`) |

### Common Series IDs

| ID | Description |
|----|-------------|
| `CUUR0000SA0` | CPI-U All Items (urban consumers) |
| `CUSR0000SA0` | CPI-U All Items (seasonally adjusted) |
| `LNS14000000` | Unemployment Rate (seasonally adjusted) |
| `CES0000000001` | Total Nonfarm Payrolls |
| `PCU----` | Producer Price Index (various) |
| `EIUALL` | U.S. City Average Gasoline |

### Examples

```bash
# Unemployment rate 2020–2024
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"bls_series","arguments":{"series_id":"LNS14000000","from":"2020","to":"2024"}}}'

# CPI since 2022
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"bls_series","arguments":{"series_id":"CUUR0000SA0","from":"2022"}}}'
```

```python
import requests
r = requests.post("http://localhost:8082/mcp", json={
    "jsonrpc": "2.0", "id": 1, "method": "tools/call",
    "params": {"name": "bls_series", "arguments": {
        "series_id": "LNS14000000", "from": "2022", "to": "2024"
    }}
})
print(r.json()["result"]["content"][0]["text"])
```

### Sample Output

```
year  period  value   footnotes
2024  M01     3.7
2024  M02     3.9
2024  M03     3.8
2023  M12     3.7
...
```

### Ask Your AI

> *"What's the current unemployment rate trend?"*
> *"Show me CPI month-over-month changes since 2022."*
> *"How many jobs were added last month?"*
