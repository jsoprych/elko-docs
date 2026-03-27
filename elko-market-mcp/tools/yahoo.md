# Yahoo Finance Tools

Three tools covering equity quotes, price history, and dividend history. No API key required.

---

## `yahoo_quote`

Live quote data for any ticker — price, volume, PE, EPS, market cap, 52-week range.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `symbol` | string | ✓ | Ticker symbol, e.g. `AAPL`, `MSFT`, `BRK-B` |

### Example

```bash
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"yahoo_quote","arguments":{"symbol":"AAPL"}}}'
```

```python
import requests
r = requests.post("http://localhost:8082/mcp", json={
    "jsonrpc": "2.0", "id": 1, "method": "tools/call",
    "params": {"name": "yahoo_quote", "arguments": {"symbol": "AAPL"}}
})
print(r.json()["result"]["content"][0]["text"])
```

### Sample Output

```
symbol          AAPL
name            Apple Inc.
price           172.43
change          +1.24 (0.72%)
volume          58,234,100
market_cap      2.71T
pe_ratio        27.8
eps             6.20
52w_high        199.62
52w_low         124.17
```

---

## `yahoo_history`

OHLCV price bars for any ticker, any time range, any interval.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `symbol` | string | ✓ | Ticker symbol |
| `period` | string | | Rolling window: `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, `ytd`, `max` |
| `interval` | string | | Bar size: `1m`, `5m`, `15m`, `30m`, `1h`, `1d`, `1wk`, `1mo` |
| `from` | string | | Start date `YYYY-MM-DD` (overrides period) |
| `to` | string | | End date `YYYY-MM-DD` (defaults to today) |

### Examples

```bash
# Last month of daily bars
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"yahoo_history","arguments":{"symbol":"AAPL","period":"1mo","interval":"1d"}}}'

# Custom date range
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"yahoo_history","arguments":{"symbol":"SPY","from":"2024-01-01","to":"2024-12-31","interval":"1wk"}}}'
```

```python
import requests
r = requests.post("http://localhost:8082/mcp", json={
    "jsonrpc": "2.0", "id": 1, "method": "tools/call",
    "params": {"name": "yahoo_history", "arguments": {
        "symbol": "AAPL", "from": "2024-01-01", "to": "2024-12-31", "interval": "1d"
    }}
})
print(r.json()["result"]["content"][0]["text"])
```

### Sample Output

```
Timestamp,Date,Open,High,Low,Close,AdjClose,Volume
1704067200,2024-01-01,185.14,185.14,182.73,185.14,184.53,42628800
1704153600,2024-01-02,184.37,185.24,182.23,185.52,184.91,53278800
...
```

Returns CSV — the dashboard renders it as a chart automatically.

---

## `yahoo_dividends`

Full dividend payment history for any ticker.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `symbol` | string | ✓ | Ticker symbol |

### Example

```bash
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"yahoo_dividends","arguments":{"symbol":"AAPL"}}}'
```

### Sample Output

```
date        amount
2024-02-09  0.2400
2023-11-10  0.2400
2023-08-11  0.2400
2023-05-12  0.2400
...
```
