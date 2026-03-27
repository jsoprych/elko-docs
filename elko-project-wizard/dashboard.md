# Dashboard Guide — elko-project-wizard

The dashboard is served at **http://localhost:8080** when the container is running.

---

## Layout

![elko-project-wizard home](https://raw.githubusercontent.com/jsoprych/elko-docs/main/assets/elko-project-wizard/01-home.png)

**Left sidebar** — navigation and directive browser organized by category.

**Main panel** — context-sensitive: home stats, wizard, profile composer, directive detail, or generation history.

---

## Sidebar Sections

| Section | Contents |
|---------|---------|
| **Getting Started** | Quick Start Wizard |
| **Directives** | (header — expands categories below) |
| **Agent-Setup** | Dependency Check |
| **AI-Provider** | Free Gemini Setup |
| **Docker** | Docker & docker-compose |
| **Documentation** | Mermaid Diagrams |
| **Source-Rules** | Function Size, Greenfield, Idiomatic, Minimize Deps |
| **Starter** | Hello World + SQLite |
| **Tech-Stack** | All 8 stacks |
| **User-Profile** | Zero / Builder / Hero |
| **Vibe-Coding** | Prompt Coaching, Show Your Work |
| **Visibility** | Private / Community / Dual |
| **Workflow** | Docker, Test-First |
| **+ New Profile** | (button) Open the profile composer |

---

## Home Panel

![Home stats and How It Works](https://raw.githubusercontent.com/jsoprych/elko-docs/main/assets/elko-project-wizard/01-home.png)

Shows live stats: directive count, category count, saved profiles, and time-to-coding. The **How It Works** section walks through the three-step flow.

- **+ New Profile** — jump straight to the composer
- **View History** — see last 50 generated projects

---

## Profile Composer

![New Profile composer](https://raw.githubusercontent.com/jsoprych/elko-docs/main/assets/elko-project-wizard/03-new-profile.png)

Select directives by category, name the profile, set a default project name, and save. Saved profiles appear in the sidebar for one-click generation.

---

## Directive Detail

Click any directive in the sidebar to see its full content — the exact text that will be written into `AGENTS.md` when it's included in a generated project.

---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*
