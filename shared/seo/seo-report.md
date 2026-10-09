# SEO Report · Silk Road Medinfo v2

> **日期**：2026-09-30
> **范围**：6 个核心页面 × 3 语种 + 错误页

---

## 1. 交付清单

```
shared/seo/
├── sitemap.xml             三语种 21 个 URL + hreflang 互链
├── robots.txt               全开放，标注 sitemap
├── structured-data.json    MedicalOrganization + WebSite + BreadcrumbList × 5 + FAQPage + 2 MedicalProcedure
└── seo-report.md
```

---

## 2. 每页 SEO 配置

每页 `<head>` 包含：

| 元素 | 内容 |
|---|---|
| `<title>` | 由 `data-i18n` 注入，俄语/英语独立 title |
| `<meta name="description">` | 由 `data-i18n-attr` 注入（俄英俄语偏移补偿） |
| `<link rel="canonical">` | 锁定唯一 URL（避免 query 变体） |
| `<link rel="alternate" hreflang="...">` | 三语种互链（zh-CN / en / ru）+ `x-default` |
| `<meta property="og:title">` | 与 title 一致 |
| `<meta property="og:description">` | 与 description 一致 |
| `<meta property="og:locale">` | 按语种切换 |
| `<meta property="og:type">` | home: website / 其他: article |
| `<meta name="twitter:card">` | summary_large_image |
| `<meta name="theme-color">` | `#0B5FAE` 品牌色 |
| `<meta name="format-detection">` | `telephone=no`（避免自动拨号） |

---

## 3. JSON-LD 结构化数据

每页 `<head>` 内嵌的 JSON-LD：

| 页面 | JSON-LD 类型 |
|---|---|
| `index.html` | `MedicalOrganization` + `WebSite` + `BreadcrumbList` |
| `projects/capsule-endoscopy.html` | `MedicalOrganization` + `BreadcrumbList` + `MedicalProcedure`（capsule） |
| `projects/cardiac-mrca.html` | `MedicalOrganization` + `BreadcrumbList` + `MedicalProcedure`（cardiac） |
| `science/index.html` | `MedicalOrganization` + `BreadcrumbList` + `FAQPage` |
| `services/index.html` | `MedicalOrganization` + `BreadcrumbList` |
| `central-asia/index.html` | `MedicalOrganization` + `BreadcrumbList` |

`FAQPage` 包含 3 个高频问答（空腹 / 辐射 / 报告时间）。

---

## 4. sitemap.xml 结构

```xml
<urlset xmlns:sitemap xmlns:xhtml>
  <url>
    <loc>https://silkroad-medinfo.com/</loc>
    <lastmod>2026-09-30</lastmod>
    <priority>1.0</priority>
    <xhtml:link rel="alternate" hreflang="zh-CN" href="..." />
    <xhtml:link rel="alternate" hreflang="en" href="..." />
    <xhtml:link rel="alternate" hreflang="ru" href="..." />
    <xhtml:link rel="alternate" hreflang="x-default" href="..." />
  </url>
  ...
</urlset>
```

- 21 个 URL：6 zh-CN × 1 + 6 en/ × 1 + 6 ru/ × 1 + 3 错误页 × 1
- 每个 zh-CN 条 URL 含完整 4 xhtml:link 引用，确保搜索引擎发现全部 3 语种
- 优先级：home `1.0`，services / central-asia `0.9`，其他内容 `0.7-0.8`

---

## 5. robots.txt 配置

| 规则 | 含义 |
|---|---|
| `User-agent: *`  `Allow: /` | 默认全索引 |
| `Disallow: /api/` | API 路径不索引（未来部署后） |
| `Disallow: /404.html` / `/500.html` | 错误页不索引 |
| `User-agent: GPTBot` / `PerplexityBot` / `ClaudeBot` | 显式 Allow（AI 爬虫友好） |
| `Sitemap: https://silkroad-medinfo.com/sitemap.xml` | 站点地图位置 |
| `Host: https://silkroad-medinfo.com` | 主域（Yandex 协议） |

---

## 6. 语义化 HTML

每页严格遵循：

- `<header role="banner">` 站点头
- `<nav aria-label="...">` 顶栏 + 移动菜单 + 面包屑 + 页脚
- `<main id="main">` 主内容（含 `href="#main"` skip link）
- `<article>` 项目卡 / 文章卡
- `<aside>` 未使用（不需要侧栏）
- `<footer class="site-footer">` 页脚
- 标题层级 `h1 → h2 → h3` 严格不跳

---

## 7. hreflang 互链矩阵

| Page | zh-CN | en | ru | x-default |
|---|---|---|---|---|
| `/` | ✓ | ✓ | ✓ | ✓ |
| `/projects/capsule-endoscopy.html` | ✓ | ✓ | ✓ | - |
| `/projects/cardiac-mrca.html` | ✓ | ✓ | ✓ | - |
| `/science/` | ✓ | ✓ | ✓ | - |
| `/services/` | ✓ | ✓ | ✓ | - |
| `/central-asia/` | ✓ | ✓ | ✓ | - |

每个 zh-CN URL 都有 4 个 hreflang 链接（zh / en / ru / x-default），en / ru URL 各 2 个（仅指向自身 + zh-CN 默认）。

---

## 8. Core Web Vitals 准备

| 指标 | 目标 | 当前 |
|---|---|---|
| LCP（最大内容渲染） | < 2.5s | 待 Lighthouse 验证 |
| FID（首次输入延迟） | < 100ms | 待验证 |
| CLS（累计布局偏移） | < 0.1 | 已设置 `width`/`height` 属性防 CLS |

---

## 9. 待 Step 7（performance）补充：
- AVIF/WebP 双格式 + `srcset`
- 关键 CSS 内联（已在 4 部分上首屏 critical）
- 字体 preload + `font-display: swap`（已在 `<link rel="preload">` 上预加载）

---

> 本报告与 `shared/seo/*.{xml,txt,json}` 共同构成 v2 SEO 层。
> 部署后请在 GSC / Yandex Webmaster 提交 sitemap 注册表。