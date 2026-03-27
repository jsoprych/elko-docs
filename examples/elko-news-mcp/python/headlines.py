"""
elko-news-mcp — headlines example
Fetches and displays recent news headlines grouped by source.

Requirements: pip install requests
Server: docker run -d -p 8081:8081 jsoprych/elko-news-mcp:latest
"""

import requests
from datetime import datetime

BASE = "http://localhost:8081/mcp"


def get_headlines(hours=6, limit=20, source=None, category=None) -> str:
    args = {"hours": hours, "limit": limit}
    if source:
        args["source"] = source
    if category:
        args["category"] = category

    r = requests.post(BASE, json={
        "jsonrpc": "2.0", "id": 1,
        "method": "tools/call",
        "params": {"name": "news_headlines", "arguments": args}
    })
    r.raise_for_status()
    return r.json()["result"]["content"][0]["text"]


def search_news(query: str, limit=10) -> str:
    r = requests.post(BASE, json={
        "jsonrpc": "2.0", "id": 1,
        "method": "tools/call",
        "params": {"name": "news_search", "arguments": {"query": query, "limit": limit}}
    })
    r.raise_for_status()
    return r.json()["result"]["content"][0]["text"]


def get_sources() -> str:
    r = requests.post(BASE, json={
        "jsonrpc": "2.0", "id": 1,
        "method": "tools/call",
        "params": {"name": "news_sources", "arguments": {}}
    })
    r.raise_for_status()
    return r.json()["result"]["content"][0]["text"]


if __name__ == "__main__":
    print("=== Sources ===")
    print(get_sources())

    print("\n=== Top Headlines (last 6h) ===")
    print(get_headlines(hours=6, limit=15))

    print("\n=== Tech News (last 12h) ===")
    print(get_headlines(hours=12, limit=10, category="technology"))

    print("\n=== Search: Federal Reserve ===")
    print(search_news("Federal Reserve interest rates", limit=5))
