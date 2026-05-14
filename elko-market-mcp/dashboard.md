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

### Procedures

SQL procedures saved via `POST /v1/procedures` appear under a **Procedures** group in the
sidebar. They behave exactly like regular tools — auto-generated form, result panel, MCP JSON
tab, export.

### Logs

Recent call log: tool name, arguments, result (truncated), and duration. Visible only when the
server is started with `--db`. Useful for debugging and auditing.

### Status Bar

The status bar at the bottom shows easy-key expiry and rate-limit usage.

**🔑 Keys button** — opens the API key management panel. Use this to set `FRED_API_KEY`,
`BLS_API_KEY`, or `SEC_USER_AGENT` without restarting the container. The button shows a
warning badge when a required key (FRED) is not set.

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

| Source | Category | Tools |
|--------|----------|-------|
| Yahoo Finance | Equity | `yahoo_quote`, `yahoo_history`, `yahoo_dividends` |
| SEC EDGAR | Equity | `edgar_financials`, `edgar_company_info`, `edgar_insider_trades` |
| Treasury | Rates | `treasury_yields` |
| BLS | Macro | `bls_series` |
| World Bank | Macro | `worldbank_indicator` |
| FRED | Macro | `fred_series`, `fred_search` |
| FDIC | Banking | `fdic_bank_search`, `fdic_bank_financials` |
| — | SQL | Saved procedures (user-defined, appear after `POST /v1/procedures`) |

→ [Full tool reference](tools/)

---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*
