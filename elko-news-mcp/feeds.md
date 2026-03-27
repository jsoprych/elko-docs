# Feed Configuration — elko-news-mcp

Feeds are JSON files embedded in the binary at compile time. To add a feed, drop a JSON file in `feeds/<source>/` and rebuild — no code changes needed.

---

## Built-in Feeds

| Name | Source | Category | Interval |
|------|--------|----------|----------|
| `reuters_top_news` | reuters | general | 15m |
| `reuters_business` | reuters | business | 15m |
| `ap_headlines` | ap | general | 15m |
| `hackernews_frontpage` | hackernews | technology | 30m |
| `wsj_markets` | wsj | markets | 15m |
| `marketwatch_headlines` | marketwatch | markets | 15m |

---

## Feed Spec Format

Each feed is a JSON file at `feeds/<source>/<name>.json`:

```json
{
  "name":          "reuters_top_news",
  "source":        "reuters",
  "category":      "general",
  "url":           "https://feeds.reuters.com/reuters/topNews",
  "format":        "rss",
  "poll_interval": "15m",
  "max_items":     50
}
```

### Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `name` | string | required | Unique identifier |
| `source` | string | required | Source group name |
| `category` | string | `""` | Category label for filtering |
| `url` | string | required | RSS or Atom feed URL |
| `format` | string | `auto` | `rss`, `atom`, or `auto` (auto-detect) |
| `poll_interval` | duration | `15m` | Go duration: `5m`, `30m`, `1h`, etc. |
| `max_items` | int | `50` | Max articles per poll |
| `headers` | object | `{}` | HTTP headers (e.g. `User-Agent`, auth) |

---

## Adding a Feed (Docker)

Mount a local feeds directory to override or extend built-in feeds:

```bash
# Create your feed file
mkdir -p feeds/ars_technica
cat > feeds/ars_technica/feed.json << 'EOF'
{
  "name": "ars_technica_main",
  "source": "ars_technica",
  "category": "technology",
  "url": "https://feeds.arstechnica.com/arstechnica/index",
  "format": "rss",
  "poll_interval": "30m",
  "max_items": 30
}
EOF
```

---

## Filtering Sources at Runtime

```bash
# Only poll specific sources
docker run -d --name elko-news \
  -p 8081:8081 \
  -v elko-news-data:/data \
  jsoprych/elko-news-mcp:latest \
  serve --sources reuters,ap,hackernews
```

The `--sources` flag accepts `all` (default) or a comma-separated list of source names.

---

## Feed Ideas

| Category | Feed |
|----------|------|
| Finance | `https://feeds.bloomberg.com/markets/news.rss` |
| Tech | `https://feeds.arstechnica.com/arstechnica/index` |
| Tech | `https://www.wired.com/feed/rss` |
| Science | `https://www.newscientist.com/feed/home/` |
| Crypto | `https://cointelegraph.com/rss` |
| Sports | `https://www.espn.com/espn/rss/news` |
| General | `https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml` |


---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*