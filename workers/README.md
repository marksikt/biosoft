# WORKERS — biosoft proxy layer

## anthropic-proxy.js

Cloudflare Worker care rezolva CORS pentru apeluri directe din browser.

### Deploy (5 minute, gratuit)

1. https://workers.cloudflare.com → Sign up / Log in
2. Create Worker → paste continutul din `anthropic-proxy.js`
3. Settings → Variables → Add: `ANTHROPIC_API_KEY` = `sk-ant-...`
4. Deploy → copiaza URL-ul (ex: `https://biosoft-proxy.george.workers.dev`)
5. In amoeba_game.html → panoul KEY → camp PROXY URL → paste URL

### Variante de securitate

**Fara env key** — clientul trimite key-ul sau din header. Mai simplu, dar key-ul e vizibil.
**Cu env key** — key-ul sta in Cloudflare, invizibil pentru browser. Recomandat.

### Free tier Cloudflare Workers
- 100,000 requests/zi
- 10ms CPU per request
- Suficient pentru biosoft
