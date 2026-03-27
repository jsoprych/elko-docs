# SQL Procedures — elko-news-mcp

SQL procedures are named SELECT queries stored in the database. Each one is **automatically exposed as an MCP tool** — no restart, no code change.

---

## How It Works

1. Write a SELECT query in the dashboard (or via REST API)
2. Give it a name and description
3. Save — it's immediately callable as an MCP tool

Your AI assistant sees it alongside the built-in tools. Call it by name:

```bash
curl -s -X POST http://localhost:8081/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"fed_news_today","arguments":{}}}'
```

---

## Creating via Dashboard

1. Open **http://localhost:8081** → **Procedures** tab
2. Enter a name (no spaces, underscores OK): `fed_news_today`
3. Enter a description: `Fed and rates news from the last 24h`
4. Write your SELECT query
5. Click **Save Procedure**

The procedure card appears immediately with **Run** and **JSON-RPC** tabs.

---

## Creating via REST API

```bash
curl -s -X POST http://localhost:8081/v1/procedures \
  -H "Content-Type: application/json" \
  -d '{
    "name": "fed_news_today",
    "description": "Fed and rates news from the last 24h",
    "sql": "SELECT title, url, published FROM articles WHERE published > unixepoch() - 86400 AND (title LIKE '\''%Fed%'\'' OR title LIKE '\''%rate%'\'') ORDER BY published DESC LIMIT 20"
  }'
```

---

## Seeded Procedures

Three procedures are created automatically on first run:

### `fed_news_today`
Fed and interest rate news from the last 24 hours.
```sql
SELECT title, url, published
FROM articles
WHERE published > unixepoch() - 86400
  AND (title LIKE '%Fed%' OR title LIKE '%rate%')
ORDER BY published DESC
LIMIT 20
```

### `tech_headlines`
Technology headlines from the last 6 hours.
```sql
SELECT title, url, source, published
FROM articles
WHERE category = 'technology'
  AND published > unixepoch() - 21600
ORDER BY published DESC
LIMIT 25
```

### `market_movers`
Market and finance news from the last 12 hours.
```sql
SELECT title, url, source, published
FROM articles
WHERE (category = 'markets' OR category = 'business')
  AND published > unixepoch() - 43200
ORDER BY published DESC
LIMIT 30
```

---

## Cookbook — More Examples

### Breaking News (last 30 minutes)
```sql
SELECT title, source, url, datetime(published, 'unixepoch') AS time
FROM articles
WHERE published > unixepoch() - 1800
ORDER BY published DESC
```

### Source Comparison (article counts last 24h)
```sql
SELECT source, COUNT(*) AS articles
FROM articles
WHERE published > unixepoch() - 86400
GROUP BY source
ORDER BY articles DESC
```

### Keyword Frequency (what topics are trending)
```sql
SELECT
  CASE
    WHEN title LIKE '%AI%' OR title LIKE '%artificial intelligence%' THEN 'AI'
    WHEN title LIKE '%Fed%' OR title LIKE '%Federal Reserve%' THEN 'Fed'
    WHEN title LIKE '%China%' THEN 'China'
    WHEN title LIKE '%Ukraine%' THEN 'Ukraine'
    ELSE 'Other'
  END AS topic,
  COUNT(*) AS count
FROM articles
WHERE published > unixepoch() - 86400
GROUP BY topic
ORDER BY count DESC
```

### Most-Mentioned Companies (last 12h)
```sql
SELECT title, source, published
FROM articles
WHERE published > unixepoch() - 43200
  AND (title LIKE '%Apple%' OR title LIKE '%AAPL%')
ORDER BY published DESC
LIMIT 15
```

---

## Managing Procedures

```bash
# List all saved procedures
curl -s localhost:8081/v1/procedures

# Run a procedure
curl -s -X POST localhost:8081/v1/procedures/fed_news_today/run

# Delete a procedure
curl -s -X DELETE localhost:8081/v1/procedures/fed_news_today
```

---

## AI-Assisted Procedure Creation

With elko-news connected to Claude, you can ask:

> *"Create a SQL procedure called `crypto_news_2h` that returns crypto news from the last 2 hours, ordered by most recent."*

Claude will write the SQL, call the `/v1/procedures` API, and save it — callable immediately.
