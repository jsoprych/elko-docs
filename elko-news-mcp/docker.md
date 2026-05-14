# Docker & Configuration — elko-news-mcp

---

## Quick Run

```bash
docker run -d \
  --name elko-news \
  -p 8081:8081 \
  -v elko-news-data:/data \
  jsoprych/elko-news-mcp:latest
```

Open **http://localhost:8081** — articles start arriving within 30 seconds.

---

## Docker Compose

```yaml
services:
  elko-news:
    image: jsoprych/elko-news-mcp:latest
    ports:
      - "8081:8081"
    volumes:
      - elko-news-data:/data
    restart: unless-stopped

volumes:
  elko-news-data:
```

---

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ELKO_EASY_KEY` | bundled key | Rate-limit token (91-day demo; override with your own) |
| `ELKO_KEY_SECRET` | — | Enable pro-key HMAC validation (optional) |
| `ELKO_REVOCATION_URL` | — | Pro-key revocation list URL (requires `ELKO_KEY_SECRET`) |

The bundled easy key expires ~91 days after each release. To run without rotation:

```bash
# Disable rate limiting
docker run -e ELKO_EASY_KEY="" ...

# Override with your own key
docker run -e ELKO_EASY_KEY=your_key ...
```

---

## CLI Flags

All flags apply to both the `serve` and `mcp` commands.

| Flag | Default | Description |
|------|---------|-------------|
| `--db` | `~/.elko-news.db` | SQLite database path |
| `--port` | `8081` | HTTP port (serve mode only) |
| `--sources` | `all` | Comma-separated sources to enable, or `all` |
| `--trim-age` | `168h` | Delete articles older than this (0 = keep forever) |
| `--log-max-output` | `0` | Enable call logging — max result chars stored per entry (0 = disabled) |

### Enable call logging

```bash
docker run -d --name elko-news \
  -p 8081:8081 \
  -v elko-news-data:/data \
  jsoprych/elko-news-mcp:latest \
  serve --log-max-output 2000
```

When enabled, every MCP tool call and REST search/headline query is logged to the
`call_log` SQLite table and browsable at `GET /v1/logs`.

### Poll only specific sources

```bash
docker run -d --name elko-news \
  -p 8081:8081 \
  -v elko-news-data:/data \
  jsoprych/elko-news-mcp:latest \
  serve --sources reuters,ap,bbc,hackernews
```

### Keep articles forever

```bash
  serve --trim-age 0
```

---

## Persistent Data

All data is stored in SQLite at `/data/elko-news.db` inside the container:

| Table | Contents |
|-------|----------|
| `articles` | News articles — title, URL, source, category, lean, country, summary |
| `articles_fts` | FTS5 full-text index (auto-maintained via triggers) |
| `sources` | Source ownership metadata |
| `procedures` | Saved SQL procedures registered as MCP tools |
| `_config` | API keys saved from the dashboard |
| `feed_health` | Per-feed poll status (ok / fail / dead) |
| `call_log` | Tool call records (populated when `--log-max-output > 0`) |

```bash
# Named volume (recommended — survives container removal)
docker run -v elko-news-data:/data ...

# Host path (useful for direct SQLite access)
docker run -v /path/on/host:/data ...
```

---

## Container Lifecycle

```bash
docker stop elko-news                                           # stop (data kept)
docker start elko-news                                          # restart
docker rm elko-news                                             # remove container (volume kept)
docker rm elko-news && docker volume rm elko-news-data          # full reset
```

---

## Port Conflicts

elko-news-mcp defaults to **8081**, elko-market-mcp to **8082** — both can run simultaneously. Override:

```bash
docker run -p 9081:8081 ... jsoprych/elko-news-mcp:latest
```

---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*
