"""
elko-market-mcp — edgar_financials example
Pulls SEC EDGAR income statements for a company and prints key metrics.

Requirements: pip install requests
Server: docker run -d -p 8082:8082 jsoprych/elko-market-mcp:latest
"""

import requests

BASE = "http://localhost:8082/mcp"


def call_tool(name: str, **args) -> str:
    r = requests.post(BASE, json={
        "jsonrpc": "2.0", "id": 1,
        "method": "tools/call",
        "params": {"name": name, "arguments": args}
    })
    r.raise_for_status()
    return r.json()["result"]["content"][0]["text"]


def company_deep_dive(symbol: str):
    print(f"\n{'='*50}")
    print(f"  {symbol} — SEC EDGAR Deep Dive")
    print('='*50)

    print("\n--- Company Info ---")
    print(call_tool("edgar_company_info", symbol=symbol))

    print("\n--- Income Statement (last 4 quarters) ---")
    print(call_tool("edgar_financials", symbol=symbol, form="10-Q", statement="income", periods=4))

    print("\n--- Balance Sheet (last 4 quarters) ---")
    print(call_tool("edgar_financials", symbol=symbol, form="10-Q", statement="balance", periods=4))

    print("\n--- Recent Insider Trades ---")
    print(call_tool("edgar_insider_trades", symbol=symbol, limit=10))


if __name__ == "__main__":
    company_deep_dive("AAPL")
    # company_deep_dive("MSFT")
    # company_deep_dive("NVDA")
