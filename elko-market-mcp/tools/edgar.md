# SEC EDGAR Tools

Three tools covering company filings, financial statements, and insider transactions. No API key required — set `SEC_USER_AGENT` as a courtesy to the SEC.

```bash
docker run -e SEC_USER_AGENT="Your Name your@email.com" ...
```

---

## `edgar_company_info`

Company metadata: CIK number, SIC code, state of incorporation, fiscal year end, filer category.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `symbol` | string | ✓ | Ticker symbol, e.g. `AAPL` |

### Example

```bash
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"edgar_company_info","arguments":{"symbol":"AAPL"}}}'
```

### Sample Output

```
cik              320193
name             Apple Inc.
sic              3571
sic_description  Electronic Computers
state            CA
fiscal_year_end  0924
category         Large accelerated filer
```

---

## `edgar_financials`

Income statement, balance sheet, or cash flow statement — annual or quarterly.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `symbol` | string | ✓ | Ticker symbol |
| `form` | string | | `10-K` (annual, default) or `10-Q` (quarterly) |
| `statement` | string | | `income`, `balance`, or `cashflow` (default: `income`) |
| `periods` | int | | Number of periods to return (default: 4) |

### Examples

```bash
# Last 4 quarters of income statements
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"edgar_financials","arguments":{"symbol":"AAPL","form":"10-Q","statement":"income","periods":4}}}'

# Annual balance sheet
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"edgar_financials","arguments":{"symbol":"MSFT","form":"10-K","statement":"balance","periods":3}}}'
```

```python
import requests
r = requests.post("http://localhost:8082/mcp", json={
    "jsonrpc": "2.0", "id": 1, "method": "tools/call",
    "params": {"name": "edgar_financials", "arguments": {
        "symbol": "AAPL", "form": "10-Q", "statement": "income", "periods": 4
    }}
})
print(r.json()["result"]["content"][0]["text"])
```

### Sample Output

```
metric              2024-Q3      2024-Q2      2024-Q1      2023-Q4
Revenue             85.78B       90.75B       119.58B      89.50B
Cost of Revenue     52.28B       55.03B       72.93B       54.25B
Gross Profit        33.50B       35.72B       46.65B       35.25B
Operating Income    24.39B       26.37B       33.89B       26.39B
Net Income          21.45B       23.20B       29.87B       23.64B
EPS (diluted)       1.40         1.52         1.96         1.54
```

---

## `edgar_insider_trades`

Form 4 insider transaction history — who bought or sold, how much, at what price.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `symbol` | string | ✓ | Ticker symbol |
| `limit` | int | | Max transactions to return (default: 20) |

### Example

```bash
curl -s -X POST http://localhost:8082/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"edgar_insider_trades","arguments":{"symbol":"AAPL","limit":10}}}'
```

### Sample Output

```
date        insider              title    type  shares    price     value
2024-03-15  Cook Timothy D       CEO      S     50,000    172.34    8.62M
2024-02-28  Maestri Luca         CFO      S     20,000    183.12    3.66M
2024-01-10  Williams Jeffrey E   COO      S     15,000    185.04    2.78M
```


---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*