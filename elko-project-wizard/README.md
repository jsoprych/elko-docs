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

**No LLM required.** The default build is 100% template-based — no API keys, no outbound calls.

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
| 1 | **Quick Start Wizard** — 5-tab guided flow: project name, experience level, tech stack, generate, preview |
| 2 | **Browse & Compose** — browse 26+ built-in directives, compose reusable profiles (Blueprints) |
| 3 | **Generate & Go** — download a `.zip` scaffold, inspect every file before unzipping, then `git init` and code |

---

## Quick Start Wizard — 5 Steps

The wizard walks you through setup in order and prevents skipping ahead:

| Tab | What You Do |
|-----|-------------|
| 📋 **Your Project** | Project name, your name, optional email + project description |
| 🎓 **Experience** | Zero / Builder / Hero — calibrates how the AI agent talks to you |
| 🛠️ **Tech Stack** | Go, Node.js/TS, Python, Rust, LAMP, C, C++ |
| ⚡ **Generate** | Review bundle contents, download ZIP |
| 📦 **Bundle Preview** | Browse every file in the ZIP — click to inspect, Markdown files render beautifully |

---

## What's in the ZIP

| File | Always? | Purpose |
|------|---------|---------|
| `AGENTS.md` | ✓ | Full AI agent briefing — directives + author + project description |
| `CLAUDE.md` | ✓ | `@AGENTS.md` shim — Claude Code reads this first |
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
| Built-in directives | **26+** |
| Categories | **11** |
| Tech stacks | **8** |
| Zero to coding | **60 seconds** |
| LLM required | **No** |

---

## AI Assist (Optional)

Without an API key, AI Assist returns a **prompt sandwich** — paste it into Claude, ChatGPT, Grok, or DeepSeek and import the result as a custom directive.

For fully automated custom directive generation, run the home-lab build with API keys:

```bash
# Requires .env.homelab — copy env.homelab.example and fill in your keys
make homelab
```

Supported: `ANTHROPIC_API_KEY` (Claude), `DEEPSEEK_API_KEY`.

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
