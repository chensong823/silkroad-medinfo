# deploy.ps1 - Silk Road Medinfo v2 automated deployment
# Usage:
#   .\deploy.ps1                 # build + validate + preview locally
#   .\deploy.ps1 -Cloudflare     # build + deploy to Cloudflare Pages
#   .\deploy.ps1 -Vercel         # build + deploy to Vercel
#   .\deploy.ps1 -Netlify        # build + deploy to Netlify
#   .\deploy.ps1 -SkipBuild      # skip build (use existing dist/)
#   .\deploy.ps1 -InitRemote <url>  # init git + add remote + initial commit

param(
    [switch]$Cloudflare,
    [switch]$Vercel,
    [switch]$Netlify,
    [switch]$SkipBuild,
    [switch]$SkipValidate,
    [string]$InitRemote = "",
    [switch]$Help
)

$ErrorActionPreference = 'Stop'
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

function Write-Step($msg) { Write-Host "`n===> $msg" -ForegroundColor Cyan }
function Write-OK($msg) { Write-Host "[OK] $msg" -ForegroundColor Green }
function Write-Warn($msg) Write-Host "[!] $msg" -ForegroundColor Yellow
function Write-Err($msg) { Write-Host "[X] $msg" -ForegroundColor Red; exit 1 }

if ($Help) {
    Get-Help $MyInvocation.MyCommand.Path -Detailed
    exit 0
}

# ------------------------------------------------------------------
# 1. Pre-flight checks
# ------------------------------------------------------------------
Write-Step "Pre-flight checks"

if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
    Write-Err "Node.js not installed. Download from https://nodejs.org/"
}
Write-OK "Node: $(node --version)"

if (-not (Get-Command npm -ErrorAction SilentlyContinue)) {
    Write-Err "npm not installed."
}
Write-OK "npm: $(npm --version)"

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Warn "Python not found, skipping validation"
    $SkipValidate = $true
}

# ------------------------------------------------------------------
# 2. Initial git + remote (optional)
# ------------------------------------------------------------------
if ($InitRemote) {
    Write-Step "Initializing Git + remote"
    if (-not (Test-Path .git)) {
        git init
        git branch -M main
    }
    git add .
    git commit -m "feat(v2): initial silk road medinfo v2 deploy"
    git remote remove origin 2>$null
    git remote add origin $InitRemote
    git push -u origin main
    Write-OK "Git initialized and pushed to $InitRemote"
}

# ------------------------------------------------------------------
# 3. Validate (unless skipped)
# ------------------------------------------------------------------
if (-not $SkipValidate) {
    Write-Step "Validating HTML + i18n"
    python scripts/validate-html.py
    if ($LASTEXITCODE -ne 0) { Write-Err "HTML validation failed" }
    python scripts/i18n-parity.py --locales locales
    if ($LASTEXITCODE -ne 0) { Write-Err "i18n parity check failed" }
    Write-OK "All validations passed"
}

# ------------------------------------------------------------------
# 4. Build
# ------------------------------------------------------------------
if (-not $SkipBuild) {
    Write-Step "Installing dependencies (if needed)"
    if (-not (Test-Path node_modules/vite)) {
        npm install --legacy-peer-deps
        if ($LASTEXITCODE -ne 0) { Write-Err "npm install failed" }
    } else {
        Write-OK "node_modules already exists"
    }

    Write-Step "Building production bundle"
    npm run build
    if ($LASTEXITCODE -ne 0) { Write-Err "Build failed" }
    if (-not (Test-Path dist/index.html)) { Write-Err "dist/index.html not found" }
    Write-OK "Built to dist/"

    # Copy Cloudflare Functions to dist (Pages Functions need to be in dist/functions/)
    if (Test-Path functions) {
        Write-Step "Copying Cloudflare Functions to dist/"
        Copy-Item -Recurse -Force functions dist/functions
        Write-OK "Functions copied"
    }
}

# ------------------------------------------------------------------
# 5. Verify dist integrity
# ------------------------------------------------------------------
Write-Step "Verifying dist/"
$distSize = (Get-ChildItem -Recurse dist/ | Measure-Object -Property Length -Sum).Sum
Write-OK "dist size: $([math]::Round($distSize / 1MB, 2)) MB"
Write-Host "  Files in dist/: $((Get-ChildItem -Recurse dist/ | Measure-Object).Count)"

# ------------------------------------------------------------------
# 6. Deploy to selected platform
# ------------------------------------------------------------------
if ($Cloudflare) {
    Write-Step "Deploying to Cloudflare Pages"
    if (-not (Get-Command wrangler -ErrorAction SilentlyContinue)) {
        Write-Warn "wrangler not installed. Installing..."
        npm install wrangler --save-dev
    }
    wrangler pages deploy dist --project-name silkroad-medinfo --branch main --commit-dirty=true
    if ($LASTEXITCODE -ne 0) { Write-Err "Cloudflare deploy failed" }
    Write-OK "Cloudflare deploy complete"
    Write-Host "  Visit: https://silkroad-medinfo.pages.dev"
    Write-Host "  After DNS: https://silkroad-medinfo.com"
}
elseif ($Vercel) {
    Write-Step "Deploying to Vercel"
    if (-not (Get-Command vercel -ErrorAction SilentlyContinue)) {
        Write-Warn "vercel CLI not installed. Run: npm i -g vercel"
        exit 1
    }
    vercel --prod
    Write-OK "Vercel deploy complete"
}
elseif ($Netlify) {
    Write-Step "Deploying to Netlify"
    if (-not (Get-Command netlify -ErrorAction SilentlyContinue)) {
        Write-Warn "netlify CLI not installed. Run: npm i -g netlify-cli"
        exit 1
    }
    netlify deploy --prod --dir=dist
    Write-OK "Netlify deploy complete"
}
else {
    Write-Step "Done — local-only mode"
    Write-Host "  Run: npm run preview  (or: python -m http.server --directory dist 8080)"
    Write-Host "  Choose a deploy target with: -Cloudflare | -Vercel | -Netlify"
    Write-Host ""
    Write-Host "  Quickest path:"
    Write-Host "    1. Push to GitHub:        git push origin main"
    Write-Host "    2. Cloudflare Dashboard:  Workers/Pages > Create > Pages > Connect Git"
    Write-Host "    3. Custom domain:         Pages project > Custom domains > silkroad-medinfo.com"
}

Write-Step "All done"
