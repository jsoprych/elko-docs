# Keys & Authentication

## Easy Key (bundled)

Every Docker image ships with a **91-day easy key** baked in at build time. It provides:
- Rate limiting: 60 requests/minute, 1,000 requests/day
- Automatic expiry with renewal hint (server stays up, protected routes return 401)
- No external validation — checked entirely client-side

The status bar at the bottom of each dashboard shows your key status, expiry date, and live request counters.

### Override the bundled key

```bash
docker run -e ELKO_EASY_KEY=your_custom_key ...
```

### Disable rate limiting (open mode)

```bash
docker run -e ELKO_EASY_KEY="" ...
```

---

## Pro Key (optional)

Pro keys use HMAC-SHA256 signing via `elko-keyring`. Enable by setting `ELKO_KEY_SECRET`:

```bash
docker run \
  -e ELKO_KEY_SECRET=your_32_byte_hex_secret \
  -e ELKO_REVOCATION_URL=https://your-keyserver/revoked \
  ...
```

Clients send pro keys via:
- Header: `X-API-Key: your_pro_key`
- Bearer: `Authorization: Bearer your_pro_key`

---

## Key Rotation

Keys are generated fresh at each Docker image build via CI. To rotate manually:

```bash
# Generate a new easy key (Python)
python3 -c "
import base64, json, time
exp = int(time.time()) + 91 * 86400
payload = json.dumps({'app':'emarket','exp':exp,'rpm':60,'rpd':1000}, separators=(',',':'))
b64 = base64.urlsafe_b64encode(payload.encode()).rstrip(b'=').decode()
print(f'emarket_ez_{b64}')
"
```

Pass the output as `ELKO_EASY_KEY`.

---

## Expired Key Behavior

When the easy key expires:
- Server continues running — does NOT crash
- Dashboard status bar shows `EXPIRED` in red
- Protected routes return `401` with a renewal hint message
- Public routes (`/health`, `/mcp.json`, `/v1/key-status`) remain accessible

To recover: pull a new image (which has a fresh key) or set `ELKO_EASY_KEY` to a new key.
