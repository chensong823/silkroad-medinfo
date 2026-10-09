# Silk Road Medinfo v2

> 由美年健康新疆公司运营的医疗信息门户，为中亚五国与中国新疆地区患者提供可读、可信、可预约的医疗内容。

## 站点结构

```
output_html/v2/
├── index.html                          # 中文首页（默认入口）
├── projects/                           # 项目详情
│   ├── capsule-endoscopy.html         # 胶囊胃镜（D005）
│   └── cardiac-mrca.html              # 心脏冠脉核磁（D002）
├── science/index.html                  # 医疗科普
├── services/index.html                 # 服务项目
├── central-asia/index.html             # 新疆中亚特色医疗
├── en/  ru/                            # 英文 / 俄文镜像
├── 404.html / 500.html                 # 友好错误页
├── shared/
│   ├── css/                            # 5 个 CSS 模块
│   ├── js/                             # 6 个 JS 模块
│   ├── img/svg/                        # 24 个 SVG 占位图
│   ├── components/                     # 可复用模板（联系表单）
│   └── seo/                            # sitemap / robots / JSON-LD
├── locales/{zh-CN,en,ru}/              # i18n key 体系（24 个 JSON）
├── copy-final/                          # 文案原始输出
├── scripts/                            # 校验与生成脚本
├── package.json / vite.config.js
├── vercel.json / netlify.toml
├── _headers / _redirects
├── .github/workflows/deploy.yml
└── CNAME / .nojekyll / .nvmrc
```

## 快速开始

```bash
# 1. 安装依赖（仅 Vite）
npm install

# 2. 本地开发（端口 5180）
npm run dev

# 3. 构建生产版本（输出 dist/）
npm run build

# 4. 预览构建产物（端口 4180）
npm run preview

# 5. i18n key 对齐检查
python scripts/i18n-parity.py --locales locales

# 6. HTML 语法 / 资产完整性 / 链接完整性 校验
python scripts/validate-html.py
```

## 部署

### 一键部署到 Vercel

```bash
npm install -g vercel
vercel --prod
```

### 一键部署到 Netlify

```bash
npm install -g netlify-cli
netlify deploy --prod --dir=dist
```

### GitHub Pages 自动部署

`main` 分支 push 后，`.github/workflows/deploy.yml` 自动构建 + 发布。

## 浏览器兼容

Chrome / Edge / Safari / Firefox 最近 2 版 + iOS 14+ / Android 10+。

## 多语言

- zh-CN（中文，默认）
- en（英文）
- ru（俄语 — 中亚通用，最高优先级）

界面右上角切换，URL 与 hreflang 同步。

## 品牌色板

| 用途 | 颜色 | hex |
|---|---|---|
| 主色 | Magnetic blue | `#0B5FAE` |
| 强调 | Vital red | `#E63946` |
| 人文 | Desert gold | `#C8954A` |
| 暖色 | Camel shadow | `#8B5A3C` |
| 冷白 | Cool white | `#F4F7FB` |
| 暖白 | Warm white | `#FBF7F0` |

## CTA 体系

| Intent | 中文 | English | Русский |
|---|---|---|---|
| view_service_detail | 查看项目 | View procedure | Подробнее об исследовании |
| book_consultation | 预约咨询 | Book a consultation | Записаться на консультацию |
| contact_clinic | 联系门诊 | Contact the clinic | Связаться с клиникой |
| read_article | 阅读全文 | Read the article | Читать материал |
| browse_services | 浏览全部服务 | Browse all services | Все услуги |
| view_cross_border | 了解跨境就医 | Cross-border program | Трансграничная программа |

每个 CTA 仅绑定一个意图。

## 验收

| 项 | 状态 |
|---|---|
| 24 个 HTML 页面 × 3 语种 + 友好错误页 | ✓ |
| 154 i18n key × 3 语种 100% 对齐 | ✓ |
| 5 个 CSS 模块 + 6 个 JS 模块 + 24 张 SVG 占位 | ✓ |
| sitemap.xml / robots.txt / JSON-LD 全套 | ✓ |
| CSP / cache / security headers | ✓ |
| WCAG 2.2 AA 代码层达标 | ✓ |
| Lighthouse 性能预估 ≥ 90 | ✓ |
| Vite + Vercel/Netlify/GH Pages 一键部署 | ✓ |

详细审计：`test-report.html`、`final-audit-report.md`、`a11y-audit-report.md`、`performance-audit.md`。