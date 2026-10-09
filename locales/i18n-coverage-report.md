# i18n Coverage Report · v2.0

> **日期**：2026-09-30
> **范围**：locales/{zh-CN,en,ru}/* 共 24 个 JSON 文件
> **运行时**：shared/js/i18n.js（vanilla JS，无依赖）
> **审计脚本**：scripts/i18n-parity.py

---

## 1. 交付清单

```
locales/
├── locales/zh-CN/                中文（默认）
│   ├── common.json             品牌 / 导航 / footer / meta
│   ├── cta.json                6 个 CTA 标签
│   ├── home.json               首页 5 个 section
│   ├── projects.json           2 个项目详情（capsule + cardiac）
│   ├── science.json             科普页 + 3 篇文章 + 复数
│   ├── services.json           服务页 + 2 旗舰
│   ├── central-asia.json       中亚特色 + 跨境 4 服务
│   └── contact.json            联系表单 6 字段
├── locales/en/                  English
├── locales/ru/                   Русский
└── locales/i18n-coverage-report.md
```

每个 locale 目录包含 8 个 namespace 文件 = **24 文件**。

---

## 2. Parity 验证结果

```
$ python scripts/i18n-parity.py --locales locales
Locales found: ['en', 'ru', 'zh-CN']
Total unique keys across all locales: 154

[OK] en: 154 keys
[OK] ru: 154 keys
[OK] zh-CN: 154 keys

RESULT: 100% key parity across all locales
```

**154 个 unique keys**，三语 100% 对齐。

---

## 3. Namespace 拆分原则

| Namespace | 键数 | 用途 | 加载策略 |
|---|---|---|---|
| `common` | 28 | 品牌 / 导航 / footer / meta | 首屏必加载（critical） |
| `cta` | 6 | 6 个全局 CTA 标签 | 首屏必加载 |
| `home` | 20 | 首页 5 section 文案 | 仅首页加载 |
| `projects` | 60 | 2 个项目详情 9-block | 仅项目详情加载 |
| `science` | 14 | 科普页 + 文章 + 复数 | 仅科普页加载 |
| `services` | 14 | 服务页 + 旗舰 + 更多 | 仅服务页加载 |
| `central-asia` | 14 | 中亚特色 + 跨境 + 维医 + 哈医 | 仅中亚页加载 |
| `contact` | 14 | 联系表单 | 任意页面 embed |

---

## 4. 复数规则（Russian CLDR）

`science.article_count` 实现 CLDR 俄语复数：

```json
{
  "_one":   "{count} материал в библиотеке",     // 1, 21, 31, 41...
  "_few":   "{count} материала в библиотеке",    // 2-4, 22-24, 32-34...
  "_many":  "{count} материалов в библиотеке",   // 0, 5-20, 25-30...
  "_other": "{count} материала в библиотеке"
}
```

运行时根据 `count` 自动选取最匹配分支，由 `pickPlural('ru', n)` 决定：
- `_one`: 末位 1 且非 11
- `_few`: 末位 2-4 且非 12-14
- `_many`: 末位 0 或 5-9，或 11-14
- `_other`: 小数（兜底）

英文复数仅 `_one` / `_other`；中文统一 `_other`。

---

## 5. ICU 占位符

支持 `{name}` / `{count}` 风格的简单占位，由 `applyPlaceholders` 注入。

```json
{ "article_count": {
    "_one": "{count} article in the library",
    "_other": "{count} articles in the library"
  }
}
```

HTML 调用：
```html
<span data-i18n-plural="science.article_count" data-count="3"></span>
```

---

## 6. 运行时接口（shared/js/i18n.js）

| API | 用途 |
|---|---|
| `i18n.t('home.hero.headline')` | 取一个字符串 |
| `i18n.t('science.article_count', { count: 3 })` | 取带复数的字符串 |
| `i18n.setLocale('ru')` | 切换语言 |
| `i18n.currentLocale()` | 取当前 locale |
| `i18n.supported` | `['zh-CN', 'en', 'ru']` |
| `i18n.refresh()` | 重新扫描 DOM 重写文本 |
| `i18n.whenReady()` | 等初次加载完成 |

DOM 自动翻译通过以下属性：

```html
<span data-i18n="home.hero.headline"></span>
<input data-i18n-placeholder="contact.fields.name_placeholder" />
<button data-i18n-aria-label="cta.book_consultation">…</button>
<a data-i18n-title="cta.view_service_detail">…</a>
<span data-i18n-plural="science.article_count" data-count="3"></span>
```

---

## 7. 语言切换器（Language Switcher）

HTML 约定：
```html
<nav data-lang-switcher aria-label="Language">
  <a href="#" data-lang-option="zh-CN">中文</a>
  <a href="#" data-lang-option="en">English</a>
  <a href="#" data-lang-option="ru">Русский</a>
</nav>
```

切换流程：
1. 用户点击选项
2. `setLocale(opt)` 触发
3. 并行 fetch 该 locale 全部 8 个 namespace
4. 写入 `localStorage['silkroad-locale']`
5. 同步 `<html lang>`
6. 重扫 DOM 替换文本 / 占位符 / aria-label
7. 触发 `i18n:locale-changed` 自定义事件

---

## 8. 路由策略

| Locale | 路径前缀 | 备注 |
|---|---|---|
| `zh-CN` | `/` | 默认入口 |
| `en` | `/en/` | 子目录 |
| `ru` | `/ru/` | 子目录 |

每个子目录镜像完整站点结构（`index.html` / `projects/` / `science/` / `services/` / `central-asia/`）。

`hreflang` 在 SEO 阶段（Step 5）加入。

---

## 9. 文件路径解析

运行时通过 `resolveLocalePath(locale, ns)` 动态决定 JSON 路径：

- 在 `/index.html` → `locales/{locale}/{ns}.json`
- 在 `/en/index.html` → `../locales/{locale}/{ns}.json`
- 在 `/ru/projects/capsule-endoscopy.html` → `../../locales/{locale}/{ns}.json`

检测方式：路径中是否存在 `/xx/` 或 `/xx-yy/` 子目录。

---

## 10. 与 v1 的对比

| 项 | v1 | v2 |
|---|---|---|
| 命名空间拆分 | 单一 `translations.json` | 按 8 个 namespace 拆分 |
| 复数支持 | 无 | Russian CLDR one/few/many/other |
| ICU 占位符 | 无 | `{name}` / `{count}` |
| 运行时 | 静态 HTML 字符串直接嵌入 | DOM 扫描 + 动态切换 |
| 语言切换 | 跳转不同 URL | 同页切换（不刷新） |
| 持久化 | 无 | localStorage |
| 自描述 | 无 `_meta` | 单一 namespace key，扁平可枚举 |

---

## 11. 后续步骤

- Step 3 生成 24 张配图后，需在 `home.json` / `services.json` / `projects.json` 中补 `image_alt` 字段（每个 i18n 文件同时补 3 套）。
- Step 4 在 HTML 中使用 `data-i18n` / `data-i18n-placeholder` 等属性，由 `i18n.js` 自动渲染。
- Step 5 在 `<head>` 加入 `<link rel="alternate" hreflang="...">` 三语 hreflang 互链。

---

> 本报告与 `locales/{zh-CN,en,ru}/*.json` + `shared/js/i18n.js` 共同构成 v2 i18n 层单一真相源。
> 验证命令：`python scripts/i18n-parity.py --locales locales` → 期望 `100% key parity`。