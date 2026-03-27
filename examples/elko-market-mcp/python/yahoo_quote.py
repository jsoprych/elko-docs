"""
elko-market-mcp — yahoo_quote example
Fetches a real-time stock quote for any ticker.

Requirements: pip install requests
Server: docker run -d -p 8082:8082 jsoprych/elko-market-mcp:latest
"""

import requests
import json

BASE = "http://localhost:8082/mcp"


def get_quote(symbol: str) -> dict:
    r = requests.post(BASE, json={
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "yahoo_quote",
            "arguments": {"symbol": symbol}
        }
    })
    r.raise_for_status()
    result = r.json()
    return result["result"]["content"][0]["text"]


if __name__ == "__main__":
    for symbol in ["AAPL", "MSFT", "TSLA", "SPY"]:
        print(f"\n{'='*40}")
        print(f"  {symbol}")
        print('='*40)
        print(get_quote(symbol))
