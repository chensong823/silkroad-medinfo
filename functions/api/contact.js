// functions/api/contact.js — Cloudflare Pages Function
// Receives contact-form submissions, validates, then forwards to one
// or more channels: Telegram, WeCom, Resend email.
//
// Deploy with Cloudflare Pages. Secrets are set via:
//   wrangler pages secret put TELEGRAM_BOT_TOKEN --project-name silkroad-medinfo
//   wrangler pages secret put TELEGRAM_CHAT_ID   --project-name silkroad-medinfo
//   wrangler pages secret put WECOM_WEBHOOK      --project-name silkroad-medinfo
//   wrangler pages secret put RESEND_API_KEY     --project-name silkroad-medinfo
//   wrangler pages secret put TURNSTILE_SECRET   --project-name silkroad-medinfo  (optional)

export const onRequestPost = async ({ request, env }) => {
  const cors = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Content-Type': 'application/json',
  };

  let data;
  try {
    data = await request.json();
  } catch (e) {
    return new Response(JSON.stringify({ ok: false, error: 'Invalid JSON' }), {
      status: 400, headers: cors,
    });
  }

  // Honeypot
  if (data.website) {
    return new Response(JSON.stringify({ ok: true }), { status: 200, headers: cors });
  }

  // Validate
  const missing = [];
  if (!data.name || data.name.length < 2) missing.push('name');
  if (!data.phone || !/^\+?[\d\s\-()]{8,}$/.test(data.phone)) missing.push('phone');
  if (!data.topic) missing.push('topic');
  if (!data.consent) missing.push('consent');
  if (missing.length) {
    return new Response(JSON.stringify({ ok: false, error: 'Missing fields', missing }), {
      status: 400, headers: cors,
    });
  }

  // Optional Turnstile (Cloudflare captcha)
  if (env.TURNSTILE_SECRET && data.turnstile) {
    const verifyRes = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ secret: env.TURNSTILE_SECRET, response: data.turnstile }),
    }).then((r) => r.json()).catch(() => null);
    if (!verifyRes || !verifyRes.success) {
      return new Response(JSON.stringify({ ok: false, error: 'Turnstile failed' }), {
        status: 403, headers: cors,
      });
    }
  }

  // Telegram forwarding
  if (env.TELEGRAM_BOT_TOKEN && env.TELEGRAM_CHAT_ID) {
    try {
      await fetch(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          chat_id: env.TELEGRAM_CHAT_ID,
          text: [
            '📩 *新咨询*',
            `姓名: ${data.name}`,
            `电话: ${data.phone}`,
            `邮箱: ${data.email || '—'}`,
            `类型: ${data.topic}`,
            '',
            (data.message || '(无留言)').slice(0, 1500),
          ].join('\n'),
          parse_mode: 'Markdown',
        }),
      });
    } catch (e) {
      console.error('Telegram forward failed:', e.message);
    }
  }

  // WeCom bot webhook
  if (env.WECOM_WEBHOOK) {
    try {
      await fetch(env.WECOM_WEBHOOK, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          msgtype: 'markdown',
          markdown: {
            content: `**新咨询**\n> 姓名：${data.name}\n> 电话：${data.phone}\n> 邮箱：${data.email || '—'}\n> 类型：${data.topic}\n\n${data.message || ''}`.slice(0, 4000),
          },
        }),
      });
    } catch (e) {
      console.error('WeCom forward failed:', e.message);
    }
  }

  // Resend email
  if (env.RESEND_API_KEY && env.ADMIN_EMAIL) {
    try {
      await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${env.RESEND_API_KEY}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          from: 'Silk Road Medinfo <noreply@silkroad-medinfo.com>',
          to: [env.ADMIN_EMAIL],
          reply_to: data.email || undefined,
          subject: `[新咨询] ${data.topic} — ${data.name}`,
          text: `姓名: ${data.name}\n电话: ${data.phone}\n邮箱: ${data.email || '—'}\n类型: ${data.topic}\n留言:\n${data.message || '(无)'}`,
        }),
      });
    } catch (e) {
      console.error('Resend email failed:', e.message);
    }
  }

  return new Response(JSON.stringify({ ok: true }), { status: 200, headers: cors });
};

export const onRequestOptions = async () => {
  return new Response(null, {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Max-Age': '86400',
    },
  });
};

export const onRequestGet = () => new Response('Method Not Allowed', {
  status: 405,
  headers: { 'Allow': 'POST, OPTIONS' },
});
