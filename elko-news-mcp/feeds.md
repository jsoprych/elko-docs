# Feed Configuration — elko-news-mcp

67 RSS/Atom feeds are embedded in the binary at compile time, across five
categories with full editorial metadata per source.

---

## Built-in Feed Coverage

| Category | Count | Sample sources |
|----------|-------|---------------|
| **News & World** | 28 | Reuters (via Google News), AP, BBC, Guardian, Al Jazeera, DW, France 24, CBC, NHK, SCMP, Xinhua, Moscow Times, Haaretz, Sky News, and more |
| **Finance & Markets** | 8 | Bloomberg, WSJ, FT, MarketWatch (CNBC), The Economist |
| **Technology** | 14 | TechCrunch, The Verge, Ars Technica, Wired, MIT Tech Review, VentureBeat, Hugging Face Blog, Tech Xplore ML/AI |
| **Science & AI** | 14 | arXiv cs.AI, cs.CL, cs.CV, cs.LG, cs.RO, stat.ML · ScienceDaily, Nature, Science AAAS, Phys.org Tech |
| **Opinion & Politics** | 3 | Politico, Foreign Policy |

---

## Feed Spec Format

Each feed is a JSON file at `feeds/<source>/<name>.json`:

```json
{
  "name":          "techcrunch_ai",
  "source":        "techcrunch",
  "category":      "technology",
  "url":           "https://techcrunch.com/category/artificial-intelligence/feed/",
  "format":        "rss",
  "poll_interval": "15m",
  "max_items":     50,
  "lean":          "center-left",
  "country":       "US",
  "display_name":  "TechCrunch",
  "owner":         "AOL / Verizon Media",
  "owner_type":    "private",
  "owner_country": "US",
  "wikidata_id":   "Q1336987"
}
```

### Core fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `name` | string | required | Unique identifier (used as MCP filter value) |
| `source` | string | required | Source group — multiple feeds share a source |
| `category` | string | `""` | Category label for filtering |
| `url` | string | required | RSS or Atom feed URL |
| `format` | string | `auto` | `rss`, `atom`, `rdf`, or `auto` (auto-detect) |
| `poll_interval` | duration | `15m` | Go duration: `5m`, `30m`, `1h`, etc. |
| `max_items` | int | `50` | Max articles stored per poll |
| `headers` | object | `{}` | HTTP request headers (e.g. `User-Agent`, auth) |

### Ownership metadata (optional — powers Sources pane + lean filter)

| Field | Description |
|-------|-------------|
| `lean` | Editorial bias: `far-left` `left` `center-left` `center` `center-right` `right` `far-right` |
| `country` | ISO 3166-1 alpha-2 publication country |
| `display_name` | Human-readable name shown in the dashboard |
| `owner` | Parent company or individual |
| `owner_type` | `public` `private` `state` `nonprofit` `cooperative` |
| `owner_country` | ISO 3166-1 alpha-2 owner country |
| `owner_ticker` | Stock ticker (if publicly traded) |
| `wikidata_id` | Wikidata Q-identifier — enables one-click enrichment |

---

## Filtering Sources at Runtime

```bash
# Only poll specific sources
docker run -d --name elko-news \
  -p 8081:8081 \
  -v elko-news-data:/data \
  jsoprych/elko-news-mcp:latest \
  serve --sources reuters,ap,hackernews,bbc
```

The `--sources` flag accepts `all` (default) or a comma-separated list of source names.

---

## Adding a Custom Feed

Since feeds are compiled in, custom feeds require rebuilding from source. For a simpler
approach — add a feed at runtime by POSTing a new source and using `POST /v1/fetch`:

```bash
# 1. The feed poller picks up new sources on restart.
# 2. For now, use POST /v1/query to query articles from any source once they arrive.
```

For production custom feeds, fork the repo, add your JSON file to `feeds/<source>/`,
and rebuild with `go build`.

---

## Feed Health

Every feed's polling status is tracked automatically:

```bash
curl -s localhost:8081/v1/feed-health | jq '.summary'
# {"ok": 65, "fail": 2, "dead": 0, "unknown": 0}
```

A feed becomes `fail` after one error, `dead` after five consecutive errors.
The `/health` endpoint reports `status: "degraded"` when any feeds are in `fail` or `dead` state.

---

## Feed Ideas

| Category | URL |
|----------|-----|
| Crypto | `https://cointelegraph.com/rss` |
| Science | `https://www.newscientist.com/feed/home/` |
| Sports | `https://www.espn.com/espn/rss/news` |
| General | `https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml` |
| Finance | `https://feeds.bloomberg.com/markets/news.rss` |

---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*
