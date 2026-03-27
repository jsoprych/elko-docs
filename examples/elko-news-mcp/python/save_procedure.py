"""
elko-news-mcp — save and run SQL procedures
Demonstrates creating custom MCP tools via the procedures API.

Requirements: pip install requests
Server: docker run -d -p 8081:8081 jsoprych/elko-news-mcp:latest
"""

import requests

BASE_REST = "http://localhost:8081"
BASE_MCP  = "http://localhost:8081/mcp"

PROCEDURES = [
    {
        "name": "ai_news_4h",
        "description": "AI and machine learning news from the last 4 hours",
        "sql": """
            SELECT title, source, url, datetime(published, 'unixepoch', 'localtime') AS time
            FROM articles
            WHERE published > unixepoch() - 14400
              AND (
                title LIKE '%AI%' OR title LIKE '%artificial intelligence%'
                OR title LIKE '%machine learning%' OR title LIKE '%ChatGPT%'
                OR title LIKE '%OpenAI%' OR title LIKE '%Anthropic%'
              )
            ORDER BY published DESC
            LIMIT 20
        """.strip()
    },
    {
        "name": "market_open_brief",
        "description": "Market and business news from the last 2 hours",
        "sql": """
            SELECT title, source, url, datetime(published, 'unixepoch', 'localtime') AS time
            FROM articles
            WHERE published > unixepoch() - 7200
              AND (category = 'markets' OR category = 'business')
            ORDER BY published DESC
            LIMIT 25
        """.strip()
    },
    {
        "name": "breaking_30min",
        "description": "All articles from the last 30 minutes across all sources",
        "sql": """
            SELECT title, source, url, datetime(published, 'unixepoch', 'localtime') AS time
            FROM articles
            WHERE published > unixepoch() - 1800
            ORDER BY published DESC
        """.strip()
    },
]


def save_procedure(proc: dict):
    r = requests.post(f"{BASE_REST}/v1/procedures",
                      json=proc,
                      headers={"Content-Type": "application/json"})
    r.raise_for_status()
    print(f"  ✓ Saved: {proc['name']}")


def run_procedure(name: str) -> str:
    r = requests.post(BASE_MCP, json={
        "jsonrpc": "2.0", "id": 1,
        "method": "tools/call",
        "params": {"name": name, "arguments": {}}
    })
    r.raise_for_status()
    return r.json()["result"]["content"][0]["text"]


def list_procedures():
    r = requests.get(f"{BASE_REST}/v1/procedures")
    r.raise_for_status()
    return r.json().get("procedures", [])


if __name__ == "__main__":
    print("=== Saving Procedures ===")
    for proc in PROCEDURES:
        save_procedure(proc)

    print("\n=== Saved Procedures (now MCP tools) ===")
    for p in list_procedures():
        print(f"  {p['name']:<25} {p['description']}")

    print("\n=== Running: ai_news_4h ===")
    print(run_procedure("ai_news_4h"))
