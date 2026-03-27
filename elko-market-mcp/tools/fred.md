# FRED Tools

Federal Reserve economic data — 800,000+ time series. Free API key lifts the daily request cap.

**Get a free key:** [fred.stlouisfed.org/docs/api/api_key.html](https://fred.stlouisfed.org/docs/api/api_key.html)

```bash
docker run -e FRED_API_KEY=your_key ...
```

---

## `fred_series`

Fetch any FRED time series by ID.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `series_id` | string | ✓ | FRED series ID, e.g. `CPIAUCSL`, `UNRATE`, `GDP` |
| `from` | string | | Start date `YYYY-MM-DD` |
| `to` | string | | End date `YYYY-MM-DD` |
| `limit` | int | | Max observations (default: 100) |

### Common Series IDs

| ID | Description |
|----|-------------|
| `CPIAUCSL` | Consumer Price Index (All Urban) |
| `UNRATE` | Unemployment Rate |
| `GDP` | Gross Domestic Product |
| `FEDFUNDS` | Federal Funds Rate |
| `DGS10` | 10-Year Treasury Constant Maturity Rate |
| `M2SL` | M2 Money Supply |
| `MORTGAGE30US` | 30-Year Fixed Mortgage Rate |
| `PCEPI` | PCE Price Index (Fed's preferred inflation gauge) |
| `PAYEMS` | Total Nonfarm Payrolls |
| `HOUST` | Housing Starts |

### Examples

```bash
# CPI since 2020
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"fred_series","arguments":{"series_id":"CPIAUCSL","from":"2020-01-01"}}}'

# Federal Funds Rate last 2 years
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"fred_series","arguments":{"series_id":"FEDFUNDS","from":"2022-01-01"}}}'
```

```python
import requests
r = requests.post("http://localhost:8082/mcp", json={
    "jsonrpc": "2.0", "id": 1, "method": "tools/call",
    "params": {"name": "fred_series", "arguments": {
        "series_id": "CPIAUCSL", "from": "2020-01-01"
    }}
})
print(r.json()["result"]["content"][0]["text"])
```

### Sample Output

```
date        value
2024-01-01  309.685
2024-02-01  310.326
2024-03-01  312.231
...
```

---

## `fred_search`

Search FRED's catalogue of 800,000+ series by keyword.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | ✓ | Search keywords |
| `limit` | int | | Max results (default: 10) |

### Example

```bash
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"fred_search","arguments":{"query":"housing starts monthly","limit":5}}}'
```

### Sample Output

```
id           title                                          frequency  units
HOUST        Housing Starts: Total                          Monthly    Thousands
HOUSTNSA     Housing Starts: Total (Not Seasonally Adj.)   Monthly    Thousands
PERMIT       New Private Housing Units Authorized           Monthly    Thousands
...
```

Use the `id` from search results with `fred_series` to fetch the actual data.


---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*