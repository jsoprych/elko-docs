# SQL Procedures Cookbook

Ready-to-use SQL procedures for elko-news-mcp. Save any of these via the dashboard or REST API and they become MCP tools instantly.

---

## News Monitoring

### Breaking News (last 30 minutes)
```sql
SELECT title, source, url, datetime(published, 'unixepoch', 'localtime') AS time
FROM articles
WHERE published > unixepoch() - 1800
ORDER BY published DESC
```

### Top Stories Last Hour by Source
```sql
SELECT source, COUNT(*) AS count, MAX(title) AS latest
FROM articles
WHERE published > unixepoch() - 3600
GROUP BY source
ORDER BY count DESC
```

### Overnight News (8pm–8am)
```sql
SELECT title, source, url
FROM articles
WHERE published BETWEEN
  strftime('%s', date('now') || ' 20:00:00') - 86400
  AND strftime('%s', date('now') || ' 08:00:00')
ORDER BY published DESC
LIMIT 50
```

---

## Finance & Markets

### Fed & Interest Rates (24h)
```sql
SELECT title, source, url, datetime(published, 'unixepoch', 'localtime') AS time
FROM articles
WHERE published > unixepoch() - 86400
  AND (
    title LIKE '%Federal Reserve%' OR title LIKE '%Fed%'
    OR title LIKE '%interest rate%' OR title LIKE '%FOMC%'
    OR title LIKE '%Powell%'
  )
ORDER BY published DESC
LIMIT 20
```

### Earnings Season Tracker
```sql
SELECT title, source, url, published
FROM articles
WHERE published > unixepoch() - 43200
  AND (
    title LIKE '%earnings%' OR title LIKE '%revenue%'
    OR title LIKE '%quarterly%' OR title LIKE '%EPS%'
    OR title LIKE '%beats%' OR title LIKE '%misses%'
  )
ORDER BY published DESC
LIMIT 25
```

### Inflation & CPI News
```sql
SELECT title, source, url, datetime(published, 'unixepoch', 'localtime') AS time
FROM articles
WHERE published > unixepoch() - 86400
  AND (
    title LIKE '%inflation%' OR title LIKE '%CPI%'
    OR title LIKE '%consumer price%' OR title LIKE '%PCE%'
  )
ORDER BY published DESC
```

### IPO & Deal Flow
```sql
SELECT title, source, url
FROM articles
WHERE published > unixepoch() - 86400
  AND (
    title LIKE '%IPO%' OR title LIKE '%acquisition%'
    OR title LIKE '%merger%' OR title LIKE '%buyout%'
    OR title LIKE '%raises%' OR title LIKE '%funding%'
  )
ORDER BY published DESC
LIMIT 20
```

---

## Technology

### AI & Machine Learning (6h)
```sql
SELECT title, source, url, datetime(published, 'unixepoch', 'localtime') AS time
FROM articles
WHERE published > unixepoch() - 21600
  AND (
    title LIKE '%AI%' OR title LIKE '%artificial intelligence%'
    OR title LIKE '%machine learning%' OR title LIKE '%ChatGPT%'
    OR title LIKE '%OpenAI%' OR title LIKE '%Anthropic%'
    OR title LIKE '%LLM%' OR title LIKE '%GPT%'
  )
ORDER BY published DESC
LIMIT 20
```

### Cybersecurity Incidents
```sql
SELECT title, source, url
FROM articles
WHERE published > unixepoch() - 86400
  AND (
    title LIKE '%hack%' OR title LIKE '%breach%'
    OR title LIKE '%ransomware%' OR title LIKE '%vulnerability%'
    OR title LIKE '%cybersecurity%' OR title LIKE '%malware%'
  )
ORDER BY published DESC
```

---

## Geopolitics

### Conflict & Geopolitical Risk
```sql
SELECT title, source, url, published
FROM articles
WHERE published > unixepoch() - 43200
  AND (
    title LIKE '%war%' OR title LIKE '%sanctions%'
    OR title LIKE '%military%' OR title LIKE '%conflict%'
    OR title LIKE '%NATO%' OR title LIKE '%tariff%'
  )
ORDER BY published DESC
LIMIT 25
```

---

## Analytics

### Source Activity (last 24h)
```sql
SELECT
  source,
  COUNT(*) AS articles,
  datetime(MAX(published), 'unixepoch', 'localtime') AS last_article,
  datetime(MIN(published), 'unixepoch', 'localtime') AS first_article
FROM articles
WHERE published > unixepoch() - 86400
GROUP BY source
ORDER BY articles DESC
```

### Hourly Article Volume (today)
```sql
SELECT
  strftime('%H:00', published, 'unixepoch', 'localtime') AS hour,
  COUNT(*) AS articles
FROM articles
WHERE published > strftime('%s', date('now'))
GROUP BY hour
ORDER BY hour
```

### Keyword Trending Score
```sql
SELECT keyword, COUNT(*) AS mentions
FROM (
  SELECT 'AI'         AS keyword FROM articles WHERE title LIKE '%AI%'         AND published > unixepoch() - 3600
  UNION ALL
  SELECT 'Fed'        AS keyword FROM articles WHERE title LIKE '%Fed%'        AND published > unixepoch() - 3600
  UNION ALL
  SELECT 'recession'  AS keyword FROM articles WHERE title LIKE '%recession%'  AND published > unixepoch() - 3600
  UNION ALL
  SELECT 'inflation'  AS keyword FROM articles WHERE title LIKE '%inflation%'  AND published > unixepoch() - 3600
  UNION ALL
  SELECT 'China'      AS keyword FROM articles WHERE title LIKE '%China%'      AND published > unixepoch() - 3600
  UNION ALL
  SELECT 'tariff'     AS keyword FROM articles WHERE title LIKE '%tariff%'     AND published > unixepoch() - 3600
)
GROUP BY keyword
ORDER BY mentions DESC
```
