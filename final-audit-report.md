# Design Audit Report · Silk Road Medinfo v2

> **日期**：2026-10-08
> **审计范围**：24 个页面 + 设计原则
> **方法**：grep + 视觉 review

---

## 1. Anti-Slop 自检

### 1.1 ❌ 营销空话禁词

| 禁词（中/英/俄） | 命中 |
|---|---|
| 颠覆 / revolutionize / революционный | 0（仅在 `copy-coverage.md` 中作为"已删除"清单） |
| 引领 / leading / ведущий | 0 |
| 一站式 / one-stop / универсальный | 0 |
| 守护健康 / caring for health / заботливый | 0 |
| 跨越山海 / across mountains and seas / через границы | 0 |
| 黑科技 / cutting-edge tech / чудо-технология | 0 |
| 金标准 / gold standard / золотой стандарт | 0 |
| 零伤害 / zero harm / нулевой вред | 0 |
| 100%安全 / 100% safe / 100% безопасно | 0 |
| 根治 / complete cure / полное исцеление | 0 |
| 立竿见影 / instant effect / мгновенный эффект | 0 |
| 包治百病 / cure-all / панацея | 0 |

### 1.2 ❌ 数字型宣传

| 模式 | 命中 |
|---|---|
| 覆盖 X 城 | 0 |
| 服务 X 万 / 累计 X 万 | 0 |
| X 年沉淀 / X 年积累 | 0 |
| X 项旗舰 / X 大保障 | 0 |

### 1.3 ❌ em-dash 禁用

24 个页面扫描结果：em-dash（—）/ en-dash（–）/ horizontal bar（―）= **0 命中**。

### 1.4 ❌ Premium-consumer 失败品

| 检查项 | 状态 |
|---|---|
| 紫蓝 AI 渐变 | ✗ 不使用 |
| 玻璃态装饰 | ✗ 不使用 |
| 大块横向 4 列 stats 横幅 | ✗ 无任何 stats |
| emoji 内联 | ✗ 全站无 emoji |
| Unicode 手写图标（♥◎✚✓） | ✗ 全站统一 SVG |
| 三等分卡片 | ✗ 旗舰项目用 7fr+5fr 非对称 |
| 数据展示型 banner（"30+ cities"等） | ✗ 全站无 |

---

## 3. CTA 唯一性

| Intent | 中文 | English | Русский | 出现位置 |
|---|---|---|---|---|
| `view_service_detail` | 查看项目 | View procedure | Encyclopedia, об исследовании | 服务卡片 CTA + cross-link |
| `book_consultation` | 预约咨询 | Book a consultation | Записаться | 项目页主 CTA / final CTA |
| `contact_clinic` | 联系门诊 | Contact the clinic | Связаться | 中亚特色页 / 表单 submit |
| `read_article` | 阅读全文 | Read the article | Читать | 科普文章卡 |
| `browse_services` | 浏览全部服务 | Browse all services | Все услуги | 服务页底部 |
| `view_cross_border` | 了解跨境就医 | Cross-border program | Трансграничная | 首页 hero / 中亚特色页 |

✅ 6 个 CTA 标签，每个仅绑定 1 个 intent。

---

## 4. 视觉 / 交互 review

| 项 | 状态 | 说明 |
|---|---|---|
| 顶栏 Logo 含艾德莱斯 + 丝路线 + 医疗十字 | ✓ | 见 `components.css .site-logo-mark` SVG |
| 顶栏 4 项菜单 | ✓ | 首页 / 医疗科普 / 服务项目 / 新疆中亚特色医疗 |
| 服务项目首屏第一眼看到胶囊胃镜 + 心脏冠脉核磁 | ✓ | `services/index.html` card-grid 第一行 |
| 卡片点击图片弹 lightbox | ✓ | 全局 `[data-lightbox]` 触发 |
| 按钮 5 状态 | ✓ | default / hover / active / focus / disabled |
| 同一图标库（Phosphor / HugeIcons / 自绘 SVG） | ✓ | 自绘 SVG strokeWidth 1.5 |
| 触屏目标 ≥ 44×44px | ✓ | btn / nav-link / checkbox |
| Stagger 入场（每 section） | ✓ | `data-reveal-stagger` cap 320ms |
| 数据展示型 banner | ✗ | 无 |
| Trust strip / logo wall | ✗ | 无 |
| 折线 hero 文字 + 右侧图默认组合 | ✓ | 首页 hero 用左文本 + 右图（1024+），移动端堆叠 |

---

## 5. 动效

| 动效 | 描述 | 时长 | 缓动 |
|---|---|---|---|
| Logo 入场 | 旋转 + 缩放 | 400ms | ease-out-soft |
| Nav hover 下划线 | scaleX 0→1 | 250ms | ease-out-soft |
| Section 入场（data-reveal） | opacity + translateY 16→0 | 600ms | ease-out-soft |
| Stagger children | sibling delay 80ms × N | cap 320ms | ease-out-soft |
| Card hover | translateY -4px + shadow 加深 | 250ms | ease-out-soft |
| 按钮 hover | translateY(-1px) + shadow 加深 | 150ms | ease-out-soft |
| 按钮 active | translateY(0) + shadow 减 | 150ms | ease-out-soft |
| Lightbox 背景 | rgba(15,23,42,0→0.85) | 400ms | ease-out-soft |
| Lightbox 内容 | scale(0.95→1) | 400ms | ease-out-soft |
| Silk road route | stroke-dashoffset 2000→0 | 600ms | ease-out-soft |

`prefers-reduced-motion: reduce` 时全部压缩到 50ms 并立即显示。

---

## 6. 调色板审计

仅使用品牌色：

| 角色 | 颜色 | hex | 使用率 |
|---|---|---|---|
| 主色（磁蓝） | Magnetic blue | `#0B5FAE` | 主按钮 / 链接 / focus ring |
| 强调（生命红） | Vital red | `#E63946` | brand-label 点 / alert / error |
| 人文（人文金） | Desert gold | `#C8954A` | 人文主调 / logo 元素 |
| 暖色（驼影棕） | Camel shadow | `#8B5A3C` | 人文强调 / 表格 |
| 冷白 | Cool white | `#F4F7FB` | tech 背景 |
| 暖白 | Warm white | `#FBF7F0` | humanity 背景 |

❌ 紫蓝渐变 / 霓虹 / 玻璃态 / beige+brass / 节日色相均无。

---

## 7. 文案原则

- ✓ 字数控制：hero ≤ 14 字（中文）
- ✓ 6 个 CTA 标签，每个对应一个意图
- ✓ 卡片简介 ≤ 50 字
- ✓ 4 个 unused 字体的 fallback
- ✓ Hero h1 抓住"打开而非推销"语气
- ✓ 风险/注意区块使用 .notice 样式（含图标 + 标题 + 正文）
- ✓ 引用源（科学页）通过页 lead 提及"文献来源与最近更新日期"

---

## 8. 总结

| 类别 | 状态 |
|---|---|
| Anti-slop 文案 | ✓ PASS |
| 数字型宣传 | ✓ NONE |
| em-dash | ✓ NONE |
| Premium-picons | ✓ AVOIDED |
| CTA 唯一性 | ✓ 6 个独立 |
| 动效规范 | ✓ 全部符合 |
| 调色板一致 | ✓ 100% 品牌色 |
| 文案原则 | ✓ PASS |

**RESULT: 全部 v2 验收项 design-taste 部分达成。**

---

> 与 `craft-floor.md` 的偏离（已记录在 i18n-expert / impeccable 报告中）：
> - brand-label 用于 hero 文本顶部作为 section 上下文标识（craft-floor 推荐完全不用 kicker/eyebrow）。保留原因：brief 中明确要求 `eyebrow` 字段。
> - 未来若严格遵循 craft-floor，可全局移除 brand-label，hero 仅保留 h1 + subheadline + CTA。