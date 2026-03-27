# Docker & Configuration — elko-market-mcp

## Quick Run

```bash
docker run -d --name elko-market \
  -p 8082:8082 \
  -v elko-market-data:/data \
  jsoprych/elko-market-mcp:latest
```

## With API Keys

```bash
docker run -d --name elko-market \
  -p 8082:8082 \
  -v elko-market-data:/data \
  -e FRED_API_KEY=your_fred_key \
  -e BLS_API_KEY=your_bls_key \
  -e SEC_USER_AGENT="Your Name your@email.com" \
  jsoprych/elko-market-mcp:latest
```

---

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ELKO_EASY_KEY` | bundled | 91-day rate-limit token baked at build time |
| `ELKO_KEY_SECRET` | — | Enable HMAC pro-key validation |
| `ELKO_REVOCATION_URL` | — | Pro-key revocation list URL |
| `FRED_API_KEY` | — | Free FRED key — lifts daily cap |
| `BLS_API_KEY` | — | Free BLS key — lifts cap from 25→500/day |
| `SEC_USER_AGENT` | — | `"Name email"` — recommended for EDGAR |

---

## Docker Compose

```yaml
services:
  elko-market:
    image: jsoprych/elko-market-mcp:latest
    container_name: elko-market
    ports:
      - "8082:8082"
    volumes:
      - elko-market-data:/data
    restart: unless-stopped
    environment:
      - FRED_API_KEY=${FRED_API_KEY:-}
      - BLS_API_KEY=${BLS_API_KEY:-}
      - SEC_USER_AGENT=${SEC_USER_AGENT:-}

volumes:
  elko-market-data:
```

---

## Port Configuration

Default port is `8082`. Override with `-p`:

```bash
# Run on port 9082 (host) → 8082 (container)
docker run -p 9082:8082 ... jsoprych/elko-market-mcp:latest
```

---

## Data Persistence

SQLite database at `/data/elko.db` inside the container.

```bash
# Named volume (recommended — survives container removal)
docker run -v elko-market-data:/data ...

# Host directory
docker run -v /path/on/host:/data ...
```

---

## Container Management

```bash
docker stop elko-market          # stop
docker start elko-market         # start
docker restart elko-market       # restart
docker logs elko-market          # view logs
docker logs -f elko-market       # follow logs

# Remove container (data volume preserved)
docker rm elko-market

# Full removal including data
docker rm elko-market && docker volume rm elko-market-data
```

---

## GHCR Alternative

Images are also published to GitHub Container Registry:

```bash
docker run -d --name elko-market \
  -p 8082:8082 \
  -v elko-market-data:/data \
  ghcr.io/jsoprych/elko-market-mcp:latest
```


---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*