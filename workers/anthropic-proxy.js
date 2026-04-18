/**
 * BIOSOFT — Anthropic CORS Proxy
 * Cloudflare Worker
 *
 * Deploy: https://workers.cloudflare.com (free tier)
 * Endpoint: https://your-worker.your-subdomain.workers.dev/
 *
 * Primeste request de la amoeba (browser),
 * adauga API key din env, trimite la Anthropic,
 * returneaza raspunsul cu header CORS.
 */

export default {
  async fetch(request, env) {

    // CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'POST, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type, x-api-key, anthropic-version',
          'Access-Control-Max-Age': '86400',
        }
      });
    }

    if (request.method !== 'POST') {
      return new Response('biosoft proxy — POST only', { status: 405 });
    }

    try {
      const body = await request.json();

      // API key: din env (recomandat) sau din header trimis de client
      const apiKey = env.ANTHROPIC_API_KEY
        || request.headers.get('x-api-key')
        || '';

      if (!apiKey) {
        return corsResponse({ error: 'no API key' }, 401);
      }

      const upstream = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': apiKey,
          'anthropic-version': '2023-06-01',
        },
        body: JSON.stringify(body),
      });

      const data = await upstream.json();
      return corsResponse(data, upstream.status);

    } catch (e) {
      return corsResponse({ error: e.message }, 500);
    }
  }
};

function corsResponse(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, x-api-key, anthropic-version',
    }
  });
}
