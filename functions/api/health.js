// functions/api/health.js — Cloudflare Pages Function
// Liveness probe for monitoring.

export const onRequestGet = async ({ env }) => {
  return new Response(JSON.stringify({
    ok: true,
    service: 'silkroad-medinfo',
    timestamp: new Date().toISOString(),
    locale: 'zh-CN,en,ru',
  }), {
    headers: {
      'Content-Type': 'application/json',
      'Cache-Control': 'no-store',
    },
  });
};
