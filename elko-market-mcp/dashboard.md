# elko-market-mcp — Dashboard Guide

The web dashboard is served at **http://localhost:8082** when the container is running.
No login required — open it in any browser.

---

## Panes

### Tools

![elko-market dashboard — yahoo_history chart for AAPL](https://raw.githubusercontent.com/jsoprych/elko-docs/main/assets/elko-market-mcp/01-tools-chart.png)

Auto-generated forms for all 13 tools — built from each tool's JSON Schema.

- Select a tool from the left sidebar
- Fill in the parameters (required fields are marked)
- Click **Run** — results appear in the right panel
- **Result tab** — formatted key/value output with SVG sparkline charts where applicable
- **JSON-RPC tab** — ready-to-copy `curl` and Python snippets for the exact call you just made
- **History** — last 50 results per tool, exportable as TXT / CSV / JSON

### Logs

Recent call log: tool name, arguments, result (truncated), and duration. Useful for debugging and auditing.

### Status

Health card, key info (easy key expiry, rate limits), and per-source request counts.

---

## Theme Toggle

Click the **◑ Normal** button (top-right) to cycle themes:

| Mode | Description |
|------|-------------|
| Light | Default white background |
| Dark | Dark charcoal background |
| High-contrast | Pure black-on-white, `#0000cc` accent — maximum readability |

---

## Tool Categories

| Category | Tools |
|----------|-------|
| **Equity** | `yahoo_quote`, `yahoo_history`, `yahoo_dividends` |
| **Filings** | `edgar_financials`, `edgar_company_info`, `edgar_insider_trades` |
| **Rates** | `treasury_yields` |
| **Macro** | `bls_series`, `worldbank_indicator`, `fred_series`, `fred_search` |
| **Banking** | `fdic_bank_search`, `fdic_bank_financials` |

→ [Full tool reference](tools/)

---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*
