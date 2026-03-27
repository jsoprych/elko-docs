"""
elko-market-mcp — treasury_yields example
Fetches the current U.S. Treasury yield curve and checks for inversion.

Requirements: pip install requests
Server: docker run -d -p 8082:8082 jsoprych/elko-market-mcp:latest
"""

import requests

BASE = "http://localhost:8082/mcp"


def get_yields(latest=True, from_date=None, to_date=None) -> str:
    args = {}
    if latest:
        args["latest"] = True
    if from_date:
        args["from"] = from_date
    if to_date:
        args["to"] = to_date

    r = requests.post(BASE, json={
        "jsonrpc": "2.0", "id": 1,
        "method": "tools/call",
        "params": {"name": "treasury_yields", "arguments": args}
    })
    r.raise_for_status()
    return r.json()["result"]["content"][0]["text"]


if __name__ == "__main__":
    print("=== Current Yield Curve ===")
    latest = get_yields(latest=True)
    print(latest)

    # Parse and check inversion (2yr vs 10yr)
    lines = [l for l in latest.strip().split("\n") if l and not l.startswith("date")]
    if lines:
        cols = lines[-1].split()
        # columns: date 1mo 2mo 3mo 6mo 1y 2y 3y 5y 7y 10y 20y 30y
        if len(cols) >= 11:
            try:
                y2 = float(cols[6])   # 2yr
                y10 = float(cols[10]) # 10yr
                spread = y10 - y2
                print(f"\n2yr: {y2:.2f}%  |  10yr: {y10:.2f}%  |  Spread: {spread:+.2f}%")
                if spread < 0:
                    print("⚠️  Yield curve is INVERTED (10yr < 2yr)")
                else:
                    print("✓  Yield curve is normal")
            except (ValueError, IndexError):
                pass

    print("\n=== Historical 10yr Yield (last 90 days) ===")
    from datetime import date, timedelta
    to_date = date.today().isoformat()
    from_date = (date.today() - timedelta(days=90)).isoformat()
    print(get_yields(latest=False, from_date=from_date, to_date=to_date))
