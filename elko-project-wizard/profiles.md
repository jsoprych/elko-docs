# Profiles (Blueprints)

A **Profile** is a saved combination of directives with a name and default project name. Create one once — reuse it for every new project.

![New Profile composer](https://raw.githubusercontent.com/jsoprych/elko-docs/main/assets/elko-project-wizard/03-new-profile.png)

---

## Create a Profile

1. Click **+ New Profile** in the sidebar
2. Enter a **Profile Name** (e.g. *Go Private Greenfield*)
3. Enter a **Default Project Name** (e.g. `my-api`)
4. Optionally add a **Description**
5. Check the directives you want included
6. Click **Save Profile**

---

## Generate from a Profile

1. Select your profile from the sidebar
2. Optionally override the project name
3. Click **Generate** — download the `.zip`

---

## Example Profiles

### Go Private Greenfield
Good for: production Go services, internal tools

Directives:
- Tech Stack: **Go**
- Visibility: **Private Repo**
- Source Rules: **Greenfield**, **Idiomatic**, **Minimize Dependencies**, **Function Size**
- Workflow: **Docker & docker-compose**, **Test-First**
- Agent Setup: **Dependency Check**
- Documentation: **Mermaid Diagrams**
- User Profile: **Hero** (or your experience level)

---

### Node.js Community Project
Good for: open-source TypeScript apps

Directives:
- Tech Stack: **Node.js / TypeScript**
- Visibility: **Community / Open Source**
- Source Rules: **Greenfield**, **Idiomatic**
- Workflow: **Docker & docker-compose**
- Starter: **Hello World + SQLite**
- User Profile: **Builder**

---

### Beginner Python Starter
Good for: first projects, learning

Directives:
- Tech Stack: **Python**
- User Profile: **Zero — Complete Beginner**
- AI Provider: **Free Gemini Setup**
- Starter: **Hello World + SQLite**
- Vibe Coding: **Show Your Work**
- Agent Setup: **Dependency Check**

---

## Profile Storage

Profiles are saved to SQLite (`/app/data/wizard.db` in the container). Mount a named volume to persist them across restarts:

```bash
docker run -v wizard-data:/app/data jsoprych/elko-project-wizard:latest
```

---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*
