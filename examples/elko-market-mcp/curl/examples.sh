#!/usr/bin/env bash
# elko-market-mcp — curl examples
# Server: docker run -d -p 8082:8082 jsoprych/elko-market-mcp:latest

BASE="http://localhost:8082"

# ── Health check ──────────────────────────────────────────────────────────────
echo "=== Health ==="
curl -s "$BASE/health" | python3 -m json.tool

# ── List all tools ────────────────────────────────────────────────────────────
echo -e "\n=== Tools ==="
curl -s "$BASE/v1/catalogue" | python3 -c "
import json,sys
data = json.load(sys.stdin)
for t in data.get('tools', []):
    print(f\"  {t['name']:<30} {t['description']}\")
"

# ── Stock quote ───────────────────────────────────────────────────────────────
echo -e "\n=== AAPL Quote ==="
curl -s -X POST "$BASE/mcp" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"yahoo_quote","arguments":{"symbol":"AAPL"}}}' \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['result']['content'][0]['text'])"

# ── Treasury yields ───────────────────────────────────────────────────────────
echo -e "\n=== Treasury Yield Curve ==="
curl -s -X POST "$BASE/mcp" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"treasury_yields","arguments":{"latest":true}}}' \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['result']['content'][0]['text'])"

# ── FRED: Federal Funds Rate ──────────────────────────────────────────────────
echo -e "\n=== Fed Funds Rate (2022-present) ==="
curl -s -X POST "$BASE/mcp" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"fred_series","arguments":{"series_id":"FEDFUNDS","from":"2022-01-01"}}}' \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['result']['content'][0]['text'])"

# ── EDGAR: Apple company info ─────────────────────────────────────────────────
echo -e "\n=== AAPL Company Info ==="
curl -s -X POST "$BASE/mcp" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"edgar_company_info","arguments":{"symbol":"AAPL"}}}' \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['result']['content'][0]['text'])"

# ── BLS: Unemployment rate ────────────────────────────────────────────────────
echo -e "\n=== Unemployment Rate (2022-2024) ==="
curl -s -X POST "$BASE/mcp" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"bls_series","arguments":{"series_id":"LNS14000000","from":"2022","to":"2024"}}}' \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['result']['content'][0]['text'])"
