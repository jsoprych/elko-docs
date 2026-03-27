# REST API — elko-project-wizard

Base URL: `http://localhost:8080`

All endpoints return JSON. Errors use `{"error": "message"}` with appropriate HTTP status.

---

## Directives

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/directives` | List all directives (`?category=tech-stack` to filter) |
| `GET` | `/api/directives/{id}` | Get a single directive |
| `POST` | `/api/directives` | Create a custom directive |
| `DELETE` | `/api/directives/{id}` | Delete a custom directive (built-ins protected) |

**Directive object:**
```json
{
  "id": "stack-go",
  "name": "Go",
  "category": "tech-stack",
  "description": "Go project conventions and tooling.",
  "tags": ["go", "backend"],
  "content": "## Tech Stack: Go\n...",
  "builtin": true,
  "created_at": 1711500000
}
```

---

## Profiles

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/profiles` | List all saved profiles |
| `GET` | `/api/profiles/{id}` | Get a single profile |
| `POST` | `/api/profiles` | Create a new profile |
| `PUT` | `/api/profiles/{id}` | Update a profile |
| `DELETE` | `/api/profiles/{id}` | Delete a profile |

**Profile object:**
```json
{
  "id": 1,
  "name": "Go Private Greenfield",
  "project_name": "my-api",
  "description": "Go service, private, full tooling",
  "directive_ids": ["stack-go", "visibility-private", "workflow-docker"],
  "created_at": 1711500000
}
```

---

## Generate

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/generate` | Generate and download a project ZIP |

**Request:**
```json
{ "profile_id": 1, "project_name": "my-api" }
```

**Response:** ZIP file download (`Content-Disposition: attachment; filename="my-api.zip"`)

---

## AI Assist

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/prompt` | Generate a custom directive via AI |

Returns `{"mode": "api", "result": {...}}` if `ANTHROPIC_API_KEY` is set, or `{"mode": "sandwich", "prompt": "..."}` for manual paste into any AI chat.

---

## Generation History

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/generations` | Last 50 generated projects (DESC order) |

---

## Examples

```bash
# List all tech-stack directives
curl http://localhost:8080/api/directives?category=tech-stack

# Generate from profile 1
curl -X POST http://localhost:8080/api/generate \
  -H "Content-Type: application/json" \
  -d '{"profile_id": 1, "project_name": "my-api"}' \
  -o my-api.zip
```

---

*Built by [Elko.AI](https://elko.ai) & [DARKFABRIK.AI](https://darkfabrik.ai) · [dev@elko.ai](mailto:dev@elko.ai)*
