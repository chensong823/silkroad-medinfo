// vite.config.js — Silk Road Medinfo v2 (Multi-Page App)
//
// v2 is a static HTML site with 3 locale mirrors (zh-CN, en, ru).
// Vite MPA mode preserves each HTML file as a separate entrypoint
// and copies assets verbatim via the publicDir convention.

import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  root: '.',
  publicDir: false, // we manage assets directly
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    target: 'es2020',
    minify: 'esbuild',
    cssMinify: 'esbuild',
    sourcemap: false,
    cssCodeSplit: true,
    assetsInlineLimit: 2048,
    rollupOptions: {
      input: {
        // Default zh-CN pages
        'index': resolve(__dirname, 'index.html'),
        'science': resolve(__dirname, 'science/index.html'),
        'services': resolve(__dirname, 'services/index.html'),
        'central-asia': resolve(__dirname, 'central-asia/index.html'),
        'projects/capsule-endoscopy': resolve(__dirname, 'projects/capsule-endoscopy.html'),
        'projects/cardiac-mrca': resolve(__dirname, 'projects/cardiac-mrca.html'),
        '404': resolve(__dirname, '404.html'),
        '500': resolve(__dirname, '500.html'),
        // English mirrors
        'en/index': resolve(__dirname, 'en/index.html'),
        'en/science': resolve(__dirname, 'en/science/index.html'),
        'en/services': resolve(__dirname, 'en/services/index.html'),
        'en/central-asia': resolve(__dirname, 'en/central-asia/index.html'),
        'en/projects/capsule-endoscopy': resolve(__dirname, 'en/projects/capsule-endoscopy.html'),
        'en/projects/cardiac-mrca': resolve(__dirname, 'en/projects/cardiac-mrca.html'),
        // Russian mirrors
        'ru/index': resolve(__dirname, 'ru/index.html'),
        'ru/science': resolve(__dirname, 'ru/science/index.html'),
        'ru/services': resolve(__dirname, 'ru/services/index.html'),
        'ru/central-asia': resolve(__dirname, 'ru/central-asia/index.html'),
        'ru/projects/capsule-endoscopy': resolve(__dirname, 'ru/projects/capsule-endoscopy.html'),
        'ru/projects/cardiac-mrca': resolve(__dirname, 'ru/projects/cardiac-mrca.html'),
      }
    }
  },
  server: {
    port: 5180,
    open: '/'
  },
  preview: {
    port: 4180,
    host: '0.0.0.0'
  }
});