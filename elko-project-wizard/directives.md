# Directives Reference

Directives are named policy blocks that tell your AI agent how to work. Each one is a focused instruction set — combine them into a [Profile](profiles.md) to fully brief your agent.

![Directives browser](https://raw.githubusercontent.com/jsoprych/elko-docs/main/assets/elko-project-wizard/02-directives.png)

**26 built-in directives across 11 categories.**

---

## Agent Setup

| Directive | Description |
|-----------|-------------|
| **Dependency Check** | Instructs AI agents to verify all required tech-stack tools and dependencies are present before starting work |

---

## AI Provider

| Directive | Description |
|-----------|-------------|
| **AI Provider: Free Gemini Setup (No Credit Card)** | Guides the AI agent to help a total beginner get a free Google Gemini API key and connect it to OpenCode |

---

## Documentation

| Directive | Description |
|-----------|-------------|
| **Mermaid Diagrams** | Instructs the AI agent to use Mermaid diagrams in all markdown docs — architecture, flows, DB schemas, sequences |

---

## Source Rules

| Directive | Description |
|-----------|-------------|
| **Function & File Size Limits** | Max 80 lines per function, 300 lines per file — keep functions and files small and focused |
| **Greenfield: Always Latest Stable** | New projects use the latest stable versions of all tools and dependencies |
| **Idiomatic & Standard Patterns** | Write standard, idiomatic code — no clever tricks |
| **Minimize Dependencies** | Prefer stdlib over 3rd party packages — every dependency must be justified |

---

## Starter

| Directive | Description |
|-----------|-------------|
| **Hello World + SQLite** | Beginner starter: build a minimal web server with a SQLite-backed visit counter — the simplest possible full-stack Hello World |

---

## Tech Stack

| Directive | Description |
|-----------|-------------|
| **Go** | Go modules, `cmd/` + `internal/` layout, stdlib-first, table-driven tests |
| **Node.js / TypeScript** | TypeScript strict mode, npm/pnpm, Jest/Vitest, ESLint, Prettier |
| **Python** | Python 3.12+, `uv`/pip, pytest, ruff/black, virtual environments |
| **Rust** | Stable toolchain via rustup, cargo, clippy, deny warnings, tokio async, thiserror |
| **LAMP (Classic)** | Linux, Apache, MySQL/MariaDB, PHP 8.2+ |
| **LAMP (SQLite)** | Linux, Apache, SQLite, PHP 8.2+ — no MySQL server required |
| **C** | C17, CMake/Make, GCC/Clang, valgrind, CMocka |
| **C++** | C++23, CMake, GoogleTest, AddressSanitizer, clang-tidy, RAII, smart pointers |

---

## User Profile (Coding Experience)

| Directive | Description |
|-----------|-------------|
| **Zero — Complete Beginner** | Use plain English, explain everything step by step, celebrate wins, no jargon |
| **Builder — Intermediate** | Skip basics, explain reasoning, treat as a peer-in-progress |
| **Hero — Experienced Developer** | Lead with solution, be terse, show diffs not full files, respect decisions |

---

## Vibe Coding

| Directive | Description |
|-----------|-------------|
| **Vibe Coding: Prompt Coaching** | Agent teaches better prompts by offering coaching tips after each response |
| **Vibe Coding: Show Your Work** | Agent explains every change in plain English — "what I just did" + "what this means" |

---

## Visibility

| Directive | Description |
|-----------|-------------|
| **Private Repo (Full IP)** | All source, docs, and IP stay internal — no public references |
| **Community / Open Source** | Public repo with community-first mindset — permissive license, contribution guide |
| **Dual Edition (Private + Community)** | Private source of truth + pruned public edition via `publish-community.sh` |

---

## Workflow

| Directive | Description |
|-----------|-------------|
| **Docker & docker-compose** | Multi-stage Dockerfile, Alpine runtime, docker-compose for local dev, health checks |
| **Test-First Discipline** | Write tests alongside code — tests run before every commit via pre-commit hook |

---

## Custom Directives

You can create your own directives from the **+ New Directive** button, or use the **AI Assist** feature:

- **Community mode** — describe what you want; get a prompt to paste into Claude / ChatGPT / DeepSeek; import the result
- **Private mode** (with `ANTHROPIC_API_KEY`) — AI generates the directive JSON directly

---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*
