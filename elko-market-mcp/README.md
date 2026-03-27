# elko-market-mcp

A self-hosted financial data server exposing **13 free market data tools** via MCP, REST API, and a web dashboard. No API keys required for core tools.

![elko-market dashboard](https://raw.githubusercontent.com/jsoprych/elko-docs/main/assets/elko-market-mcp/01-tools-chart.png)

---

## Quick Start

```bash
docker run -d --name elko-market \
  -p 8082:8082 \
  -v elko-market-data:/data \
  jsoprych/elko-market-mcp:latest
```

Open **http://localhost:8082** — the dashboard loads immediately with all 13 tools available.

---

## Tools

| Category | Tool | Description |
|----------|------|-------------|
| **Equity** | [`yahoo_quote`](tools/yahoo.md) | Live price, PE, market cap, 52-week range |
| **Equity** | [`yahoo_history`](tools/yahoo.md) | OHLCV bars — any interval, any date range |
| **Equity** | [`yahoo_dividends`](tools/yahoo.md) | Full dividend history |
| **Filings** | [`edgar_financials`](tools/edgar.md) | Income statement, balance sheet, cash flow |
| **Filings** | [`edgar_company_info`](tools/edgar.md) | CIK, SIC, state, fiscal year, filer category |
| **Filings** | [`edgar_insider_trades`](tools/edgar.md) | Form 4 insider transactions |
| **Rates** | [`treasury_yields`](tools/treasury.md) | Full yield curve — 1mo to 30yr |
| **Macro** | [`bls_series`](tools/bls.md) | CPI, unemployment, payrolls — any BLS series |
| **Banking** | [`fdic_bank_search`](tools/fdic.md) | Find banks by name or state |
| **Banking** | [`fdic_bank_financials`](tools/fdic.md) | Assets, deposits, equity, ROA, ROE |
| **Macro** | [`worldbank_indicator`](tools/worldbank.md) | GDP, inflation, debt — any country, any year |
| **Macro** | [`fred_series`](tools/fred.md) | Federal Reserve economic time series |
| **Macro** | [`fred_search`](tools/fred.md) | Search FRED by keyword |

---

## Documentation

- [Getting Started](getting-started.md)
- [Tool Reference](tools/)
- [Dashboard Guide](dashboard.md)
- [MCP Setup](mcp-setup.md)
- [REST API](api.md)
- [Docker & Configuration](docker.md)


---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*