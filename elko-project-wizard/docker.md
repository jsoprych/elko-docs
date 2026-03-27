# Docker & Configuration — elko-project-wizard

## Run

```bash
docker run -d \
  --name elko-project-wizard \
  -p 8080:8080 \
  -v wizard-data:/app/data \
  jsoprych/elko-project-wizard:latest
```

## Docker Compose

```yaml
services:
  elko-project-wizard:
    image: jsoprych/elko-project-wizard:latest
    ports:
      - "8080:8080"
    volumes:
      - wizard-data:/app/data
    restart: unless-stopped

volumes:
  wizard-data:
```

---

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ANTHROPIC_API_KEY` | — | Enables AI Assist direct mode (Claude API). Without it, AI Assist returns a prompt sandwich for manual paste. |
| `ELKO_EASY_KEY` | bundled | Rate-limit token (91-day demo). Override with your own or set `""` to disable. |

```bash
# With AI Assist (Claude API)
docker run -d -p 8080:8080 -v wizard-data:/app/data \
  -e ANTHROPIC_API_KEY=sk-ant-... \
  jsoprych/elko-project-wizard:latest
```

---

## Ports

| Port | Description |
|------|-------------|
| `8080` | REST API + web dashboard |

> If port 8080 is in use, map to any free port: `-p 9090:8080`

---

## Data Persistence

All profiles, custom directives, and generation history are stored in SQLite at `/app/data/wizard.db` inside the container.

```bash
# Named volume (recommended)
docker run -v wizard-data:/app/data ...

# Host path
docker run -v /path/on/host:/app/data ...
```

---

## Stop / Remove

```bash
docker stop elko-project-wizard          # stop
docker start elko-project-wizard         # restart
docker rm elko-project-wizard            # remove container (data volume kept)
docker rm elko-project-wizard && docker volume rm wizard-data   # full removal
```

---

## Platforms

`linux/amd64` · `linux/arm64`

---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*
