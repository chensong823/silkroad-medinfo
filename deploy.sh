#!/usr/bin/env bash
# deploy.sh - Cross-unix deployment for Silk Road Medinfo v2
# Same flags as deploy.ps1 — auto-runs whichever deploy target you choose.

set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

CLOUDFLARE=0
VERCEL=0
NETLIFY=0
SKIP_BUILD=0
SKIP_VALIDATE=0
INIT_REMOTE=""

for arg in "$@"; do
  case "$arg" in
    --cloudflare) CLOUDFLARE=1 ;;
    --vercel) VERCEL=1 ;;
    --netlify) NETLIFY=1 ;;
    --skip-build) SKIP_BUILD=1 ;;
    --skip-validate) SKIP_VALIDATE=1 ;;
    --init-remote=*) INIT_REMOTE="${arg#*=}" ;;
    *) ;;
  esac
done

step() { echo ""; echo "===> $*"; }
ok()   { echo "[OK] $*"; }
warn() { echo "[!] $*"; }
die()  { echo "[X] $*" >&2; exit 1; }

# Pre-flight
command -v node >/dev/null 2>&1 || die "Node.js not installed"
command -v npm  >/dev/null 2>&1 || die "npm not installed"
ok "Node: $(node --version)"
ok "npm: $(npm --version)"

# Git init
if [[ -n "$INIT_REMOTE" ]]; then
  step "Initializing git + remote"
  [[ -d .git ]] || git init -b main
  git add .
  git commit -m "feat(v2): initial silk road medinfo v2 deploy" || true
  git remote remove origin 2>/dev/null || true
  git remote add origin "$INIT_REMOTE"
  git push -u origin main
  ok "Pushed to $INIT_REMOTE"
fi

# Validate
if [[ $SKIP_VALIDATE -eq 0 ]]; then
  if command -v python >/dev/null 2>&1; then
    step "Validating HTML + i18n"
    python scripts/validate-html.py
    python scripts/i18n-parity.py --locales locales
  else
    warn "Python not found, skipping validation"
  fi
fi

# Build
if [[ $SKIP_BUILD -eq 0 ]]; then
  step "Installing dependencies"
  [[ -d node_modules/vite ]] || npm install --legacy-peer-deps

  step "Building production bundle"
  npm run build
  [[ -f dist/index.html ]] || die "dist/index.html not found"

  if [[ -d functions ]]; then
    cp -r functions dist/functions
    ok "Functions copied to dist/"
  fi
  ok "Built to dist/"
fi

# Verify
step "Verifying dist/"
DIST_SIZE=$(du -sh dist | cut -f1)
ok "dist size: $DIST_SIZE"

# Deploy
if [[ $CLOUDFLARE -eq 1 ]]; then
  step "Deploying to Cloudflare Pages"
  command -v wrangler >/dev/null 2>&1 || npm install wrangler --save-dev
  npx wrangler pages deploy dist --project-name silkroad-medinfo --branch main
  ok "Done. Visit: https://silkroad-medinfo.pages.dev"
elif [[ $VERCEL -eq 1 ]]; then
  step "Deploying to Vercel"
  command -v vercel >/dev/null 2>&1 || die "Install Vercel CLI: npm i -g vercel"
  vercel --prod
elif [[ $NETLIFY -eq 1 ]]; then
  step "Deploying to Netlify"
  command -v netlify >/dev/null 2>&1 || die "Install Netlify CLI: npm i -g netlify-cli"
  netlify deploy --prod --dir=dist
else
  step "Local-only mode"
  echo "  Run: npm run preview"
  echo "  Choose target: --cloudflare | --vercel | --netlify"
fi

step "All done"
