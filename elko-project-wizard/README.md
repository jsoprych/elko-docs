# elko-project-wizard

Stop briefing your AI agent from a blank page.

![elko-project-wizard — home](https://raw.githubusercontent.com/jsoprych/elko-docs/main/assets/elko-project-wizard/01-home.png)

🐳 **[Docker Hub → hub.docker.com/r/jsoprych/elko-project-wizard](https://hub.docker.com/r/jsoprych/elko-project-wizard)**

```bash
docker pull jsoprych/elko-project-wizard:latest
```

---

## What It Does

Pick your directives. Compose a profile. Hit **Generate**.

Get a `.zip` with `AGENTS.md`, `CLAUDE.md`, `Dockerfile`, and more — ready to `cd` into and start coding in under 60 seconds. Your AI agent is already briefed before it writes a single line.

---

## Quick Start

```bash
docker run -d \
  --name elko-project-wizard \
  -p 8080:8080 \
  -v wizard-data:/app/data \
  jsoprych/elko-project-wizard:latest
```

Open **http://localhost:8080** — the wizard loads immediately.

---

## How It Works

| Step | Action |
|------|--------|
| 1 | **Browse Directives** — pick from 26 built-in policies across coding standards, tech stack, visibility, and workflow |
| 2 | **Compose a Profile** — combine directives into a reusable blueprint saved for every future project |
| 3 | **Generate & Go** — download a `.zip` scaffold, unzip, `git init`, open Claude Code or OpenCode — your agent is already briefed |

---

## What's in the ZIP

| File | Always? | Purpose |
|------|---------|---------|
| `AGENTS.md` | ✓ | Full AI agent briefing — your directives concatenated |
| `CLAUDE.md` | ✓ | `@AGENTS.md` — Claude Code reads this first |
| `.gitignore` | ✓ | Stack-appropriate boilerplate |
| `README.md` | ✓ | Stub template |
| `Dockerfile` + `docker-compose.yml` | Docker directive | Production-ready multi-stage build |
| `setup-1st.sh` / `setup-1st.bat` | Starter directive | Preflight dependency check |
| `GETTING_STARTED.md` | Starter directive | Stack-specific install & run guide |
| `FREE_AI_SETUP.md` | AI Provider directive | Free Gemini API key walkthrough |

---

## Stats

| | |
|--|--|
| Built-in directives | **26** |
| Categories | **11** |
| Tech stacks | **8** |
| Zero to coding | **60 seconds** |

---

## Documentation

- [Getting Started](getting-started.md)
- [Quick Start Wizard](wizard.md)
- [Directives Reference](directives.md)
- [Profiles (Blueprints)](profiles.md)
- [Dashboard Guide](dashboard.md)
- [REST API](api.md)
- [Docker & Configuration](docker.md)

---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*
