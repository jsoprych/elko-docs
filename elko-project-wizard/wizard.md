# Quick Start Wizard

The Quick Start Wizard is the fastest path from zero to a working AI-briefed project scaffold.

The wizard is a **5-tab dialog** — work left to right. Each tab is locked until its prerequisites are complete. Clicking a locked tab shows a warning instead of navigating. Tabs show **✓** when done and can be clicked directly to jump back. A yellow **legal-pad checklist** in the sidebar mirrors your progress live.

---

## Tab 1 — 📋 Your Project

Enter the basics that go into your `AGENTS.md` header:

| Field | Required | Notes |
|-------|----------|-------|
| **Project Name** | ✓ | Lowercase + hyphens — becomes the ZIP folder name |
| **Your Name** | ✓ | Written into the AGENTS.md author line |
| **Email** | optional | Also written into AGENTS.md |
| **What Are You Building?** | optional | Functional description only — no tech stack or coding rules |

The "What Are You Building?" field accepts plain English describing features, users, and business rules. Keep it functional — stack, coding standards, and agent rules are handled by the later tabs.

Click **Next →** once a project name and author name are entered.

---

## Tab 2 — 🎓 Experience

Tells the AI agent how to calibrate its explanations and communication style:

| Level | Description |
|-------|-------------|
| **Zero** | Brand new to coding — plain English, step-by-step, no jargon. Go, Python, and Node.js get a ⭐ beginner-friendly badge. |
| **Builder** | Know the basics — skip fundamentals, explain reasoning, show diffs |
| **Hero** | Experienced developer — terse, diff-first, respect your decisions |

Your selection also influences how the Tech Stack tab is presented (compact grid for Hero, highlighted beginner stacks for Zero).

Click a level card to select it, then click **Next →**.

---

## Tab 3 — 🛠️ Tech Stack

Pick the language and framework for your project:

| Stack | Best For |
|-------|---------|
| **Go** | APIs, CLIs, backend services |
| **Node.js / TypeScript** | Web apps, REST APIs, tooling |
| **Python** | Scripts, data, ML, web |
| **Rust** | Systems, performance-critical tools |
| **LAMP (Apache + MySQL + PHP)** | Classic web apps, CMS |
| **LAMP (Apache + SQLite + PHP)** | Lightweight PHP apps, no DB server |
| **C** | Embedded, OS-level, systems |
| **C++** | Games, performance, graphics |

Click a stack card to select it, then click **Next →**.

---

## Tab 4 — ⚡ Generate

Review the bundle — exactly what will be inside your ZIP:

| File / Directive | Purpose |
|-----------------|---------|
| **AGENTS.md + CLAUDE.md** | AI agent context, stack-specific, includes author + project brief |
| **Coding Experience directive** | Calibrates agent communication style |
| **Dependency Check directive** | Agents verify tools before building |
| **Hello World + SQLite directive** | Minimal starter with database |
| **setup-1st.sh / setup-1st.bat** | Preflight scripts — run once before coding |
| **GETTING_STARTED.md** | Install links + one-command run instructions (personalised greeting when name is set) |
| **.gitignore** | Stack-appropriate ignores |

Click **⬇ Generate & Download ZIP**. The `.zip` downloads automatically and the wizard advances to the **Bundle Preview** tab.

---

## Tab 5 — 📦 Bundle Preview

Unlocks after a successful generation. Shows a **✓ BUNDLE READY** badge and a file tree of everything inside the ZIP.

- Click any file row to open a modal inspector
- `.md` files (AGENTS.md, GETTING_STARTED.md, etc.) render as **formatted Markdown** by default — toggle to Raw to see the source
- Modal footer has a **⬇ Download ZIP** button to re-download without regenerating
- The **⬇ Download ZIP Again** nav button also re-downloads at any time

---

## After Download

```bash
unzip my-project.zip
cd my-project
git init
claude        # or: opencode, cursor, zed, etc.
```

Your AI agent reads `AGENTS.md` automatically (via `CLAUDE.md → @AGENTS.md`) and is fully briefed on your stack, rules, and experience level before writing a single line.

---

## Navigation

- Click any **unlocked** tab header to jump directly to it
- Clicking a **locked** tab shows a warning — complete the earlier steps first
- **← Back** moves one step left (visible on all steps including Bundle Preview)
- **Next →** / **Generate** is disabled until the current step's requirements are satisfied
- The sidebar legal pad shows live ✓ / ! / → status for each step

---

## No LLM Required

The default community build runs entirely without an AI API key. All generation is template-based — directives are static JSON, the generator fills Go templates. No outbound calls, no tokens spent.

AI Assist (custom directive generation) works in **sandwich mode** without a key — returns a prompt you paste into any AI chat. Set `ANTHROPIC_API_KEY` or `DEEPSEEK_API_KEY` for fully automated generation (home-lab build).

---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*
