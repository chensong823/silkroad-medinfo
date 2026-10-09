// scripts/postbuild.js — copy shared/ and locales/ + SEO assets into dist/.
// Vite doesn't process files referenced via plain href/src (only imported ones),
// so we need to copy them as static assets after build.

import { promises as fs } from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const DIST = path.join(ROOT, 'dist');

const TO_COPY = [
  { src: 'shared', label: 'shared assets (CSS/JS/img/components)' },
  { src: 'locales', label: 'locales (i18n JSON)' },
  { src: '_headers', label: '_headers' },
  { src: '_redirects', label: '_redirects' },
  { src: 'shared/seo', label: 'shared/seo (sitemap.xml etc.)' },
];

async function copyDir(src, dest) {
  try {
    await fs.mkdir(dest, { recursive: true });
    const entries = await fs.readdir(src, { withFileTypes: true });
    for (const entry of entries) {
      const s = path.join(src, entry.name);
      const d = path.join(dest, entry.name);
      if (entry.isDirectory()) {
        await copyDir(s, d);
      } else if (entry.isFile()) {
        await fs.copyFile(s, d);
      }
    }
  } catch (e) {
    if (e.code === 'ENOENT') return;
    throw e;
  }
}

async function copyFile(src, dest) {
  await fs.mkdir(path.dirname(dest), { recursive: true });
  await fs.copyFile(src, dest);
}

async function main() {
  for (const { src, label } of TO_COPY) {
    const srcAbs = path.join(ROOT, src);
    const destAbs = path.join(DIST, src);
    try {
      const stat = await fs.stat(srcAbs);
      if (stat.isDirectory()) {
        await copyDir(srcAbs, destAbs);
      } else if (stat.isFile()) {
        await copyFile(srcAbs, destAbs);
      }
      console.log(`[OK] copied ${src} -> dist/${src} (${label})`);
    } catch (e) {
      console.warn(`[skip] ${src}: ${e.message}`);
    }
  }
  console.log('Postbuild complete.');
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
