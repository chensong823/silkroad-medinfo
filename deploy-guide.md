# Deploy Guide · Silk Road Medinfo v2

> **三种部署方式**：Vercel（推荐）/ Netlify / GitHub Pages
> **最低命令**：`npm install && npm run build`

---

## 1. Vercel（推荐，零配置）

```bash
# 安装 CLI（仅首次）
npm i -g vercel

# 登录
vercel login

# 部署到生产
cd output_html/v2
vercel --prod
```

Vercel 自动识别 `vercel.json`，应用所有缓存 / CSP / 重写规则。

**自定义域名**：Vercel Dashboard → Project Settings → Domains → 添加 `silkroad-medinfo.com`，按提示配置 DNS（CNAME 或 ALIAS）。

**区域**：`hkg1` / `sin1`（香港 / 新加坡）—— 对中亚与中国新疆用户延迟最低。

---

## 2. Netlify

```bash
# 安装 CLI（仅首次）
npm i -g netlify-cli

# 登录
netlify login

# 首次：关联项目
cd output_html/v2
netlify init    # 自动创建 netlify site

# 部署
netlify deploy --prod --dir=dist
```

Netlify 自动应用 `netlify.toml` + `_headers` + `_redirects`。

**自定义域名**：Netlify Dashboard → Domain settings → 添加 `silkroad-medinfo.com`，按提示配置 DNS（CNAME）。

---

## 3. GitHub Pages

```bash
# 1. 创建 GitHub 仓库
# 2. 推送 output_html/v2 内容到 main 分支
git init
git add .
git commit -m "feat(v2): initial silk road medinfo v2 site"
git remote add origin git@github.com:<org>/<repo>.git
git push -u origin main

# 3. GitHub 仓库 Settings → Pages
#    Source: GitHub Actions
#    自动触发 .github/workflows/deploy.yml
```

`deploy.yml` 在每次 push 到 main 时自动：
1. 安装依赖
2. 运行 `npm run build`
3. 拷贝 `dist/` 内容 + `CNAME` + `.nojekyll`
4. 部署到 `https://<user>.github.io/<repo>/`

**自定义域名**：`CNAME` 文件已就位（`silkroad-medinfo.com`）。在 GitHub 仓库 Settings → Pages → Custom domain 配置。

---

## 4. 部署前必查清单

| 项 | 命令 |
|---|---|
| i18n key 100% 对齐 | `python scripts/i18n-parity.py --locales locales` |
| HTML 语法 + 资产完整 | `python scripts/validate-html.py` |
| 构建无报错 | `npm run build` |
| 关键路径烟测（本地） | `npm run preview` → 浏览首页 / 项目 / lightbox / 语言切换 |

## 5. 部署后必做

| 项 | 工具 |
|---|---|
| 提交 sitemap | Google Search Console + Yandex Webmaster |
| 验证 hreflang | GSC → International Targeting |
| 监控 404 | `_redirects` 已加 / 404.html 友好页 |
| Lighthouse CI | chrome-launcher + lighthouse npm 包 |
| 真实图片生成后 | 替换 `shared/img/svg/*` 为 `shared/img/web/*.{png,webp,avif}` |

## 6. 环境变量

v2 暂不需要 env。如未来加追踪：

```
# .env.example
PUBLIC_SITE_URL=https://silkroad-medinfo.com
PUBLIC_GA_MEASUREMENT_ID=G-XXXXXXXX
```

## 7. 故障排查

| 现象 | 解决 |
|---|---|
| 404 / 找不到资源 | 检查 `dist/` 是否包含 `shared/`，或 `_redirects` 规则 |
| 字体加载失败 | Google Fonts CDN 受限地区可在 `<link rel="preload">` 上自托管 woff2 |
| CSP 报错 | `script-src 'self' 'unsafe-inline'` 已允许 inline；如需更严，去掉 `unsafe-inline` 并改造所有 inline script |
| 镜像页空白 | 检查 `../shared/css/tokens.css` 路径层级（`fix-paths.py` 已自动修复） |
| 语言切换不持久 | localStorage 受限 → 检查是否在 HTTPS 部署 |

---

## 8. 升级路线

- **真实图片**：将 `shared/img/svg/*.svg` 替换为 `shared/img/web/*.{png,webp,avif}`，加 `srcset` + `<picture>`
- **联系表单后端**：替换 `data-endpoint` 指向真实 API（如 `/api/contact`）
- **CMS 集成**：把 `locales/{zh-CN,en,ru}/services.json` 接入 Headless CMS（如 Sanity / Strapi）
- **PWA**：添加 manifest.json + Service Worker 离线缓存
- **Analytics**：Plausible / Umami（隐私友好，符合 GDPR）

---

> 部署完成后，所有维护工作都可通过 `git push` 自动触发 CI/CD 完成。
> 一键部署命令：`npm i && npm run build && vercel --prod`。