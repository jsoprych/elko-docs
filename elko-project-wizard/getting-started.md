# Getting Started — elko-project-wizard

## 1. Pull and Run

```bash
docker pull jsoprych/elko-project-wizard:latest

docker run -d \
  --name elko-project-wizard \
  -p 8080:8080 \
  -v wizard-data:/app/data \
  jsoprych/elko-project-wizard:latest
```

Open **http://localhost:8080** — the dashboard loads immediately.

---

## 2. Use the Quick Start Wizard

If this is your first time, click **🚀 Quick Start Wizard** in the sidebar.

![Quick Start Wizard](https://raw.githubusercontent.com/jsoprych/elko-docs/main/assets/elko-project-wizard/04-quick-start-wizard.png)

1. **Choose your tech stack** — Go, Node.js/TypeScript, Python, Rust, LAMP, C, C++
2. **Pick your coding experience** — Zero (beginner), Builder (intermediate), Hero (expert)
3. **Name your project** — e.g. `my-api`
4. **Review what's included** — see the directives that will be bundled
5. Click **Generate** — your `.zip` downloads automatically

---

## 3. Use Your Scaffold

```bash
unzip my-api.zip
cd my-api
git init
# Open Claude Code or OpenCode — AGENTS.md already briefs the agent
claude
```

Your AI agent reads `AGENTS.md` (via `CLAUDE.md → @AGENTS.md`) and knows your stack, rules, and preferences before writing a single line.

---

## 4. Save a Profile for Next Time

Click **+ New Profile** in the sidebar, select your directives, name it (e.g. *Go Private Greenfield*), and save. Next project — one click to generate.

→ [Profiles guide](profiles.md)

---

## Stop / Remove

```bash
docker stop elko-project-wizard
docker start elko-project-wizard
docker rm elko-project-wizard                                        # remove container (data kept)
docker rm elko-project-wizard && docker volume rm wizard-data        # full removal
```

---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*
