# Copy Coverage Report · v2.0

> **日期**：2026-09-30
> **范围**：首页 / 2 项目详情 / 科普 / 服务 / 中亚特色 / 联系表单 + 共用 brand/footer/cta 词表
> **语种**：zh-CN / en / ru

---

## 1. 交付清单

| 文件 | 用途 |
|---|---|
| `copy-final/zh.json` | 中文文案原始输出（含 `_meta` 自描述） |
| `copy-final/en.json` | 英文文案原始输出 |
| `copy-final/ru.json` | 俄语文案原始输出 |

---

## 2. CTA 标签映射（每个标签只对应一个意图）

| Intent | 中文 | English | Русский | 仅在哪些地方出现 |
|---|---|---|---|---|
| `view_service_detail` | 查看项目 | View procedure | Подробнее об исследовании | 服务卡片、项目页内 cross-link |
| `book_consultation` | 预约咨询 | Book a consultation | Записаться на консультацию | 项目页主 CTA、最终 CTA Banner |
| `contact_clinic` | 联系门诊 | Contact the clinic | Связаться с клиникой | 中亚特色页、表单提交 |
| `read_article` | 阅读全文 | Read the article | Читать материал | 科普文章卡 |
| `browse_services` | 浏览全部服务 | Browse all services | Все услуги | 服务页底部入口 |
| `view_cross_border` | 了解跨境就医 | Cross-border program | Трансграничная программа | 首页 hero secondary、中亚特色页 |

> 6 个 CTA 标签，每个仅绑定 1 个 intent。已删除 v1 重复出现的 "Learn more / 了解更多 / Узнать больше" 类无意图标签。

---

## 3. 删除的禁词与数字型宣传

### 3.1 数字型宣传（已全部删除）

- ❌ "覆盖 30+ 城市"
- ❌ "累计 500 万+ 人次"
- ❌ "深耕 16 年"
- ❌ "4 项旗舰"
- ❌ "16 年沉淀"
- ❌ "3 大保障"
- ❌ "100+ 合作医院"
- ❌ "200+ 医师"

### 3.2 禁词清单（已全部回避）

| 中文 | English | Русский |
|---|---|---|
| 颠覆 | revolutionize | революционный |
| 引领 | leading | ведущий |
| 一站式 | one-stop | универсальный |
| 跨越山海 | across mountains and seas | через границы |
| 守护健康 | caring for health | заботливый |
| 黑科技 | cutting-edge tech | чудо-технология |
| 金标准 | gold standard | золотой стандарт |
| 零伤害 | zero harm | нулевой вред |
| 100% 安全 | 100% safe | 100% безопасно |
| 彻底治愈 | complete cure | полное исцеление |
| 立竿见影 | instant effect | мгновенный эффект |
| 包治百病 | cure-all | панацея |

### 3.3 字符规则验证

- ✅ 全站无 em-dash（—），已用逗号 / 句号 / 圆括号替代
- ✅ 全站无 emoji
- ✅ 全站无 Unicode 手写图标（♥◎✚✓ 等）
- ✅ 全站无 inline 大写字母标语

---

## 4. 各页面文案覆盖

### 4.1 共用词表 `common`

覆盖：品牌名（中 / 英 / 俄）、导航 4 项、语言切换器、skip link、footer 4 模块、disclaimer。

### 4.2 首页 `home`

覆盖：hero（eyebrow / headline / subheadline / 2 CTA）、3 个 section（美年旗舰 / 科普 / 跨境）、最终 CTA Banner。

### 4.3 项目详情 `project_capsule` & `project_cardiac`

每个项目含 9 个 block：
1. eyebrow 标签
2. 主标题
3. 一句话简介（≤ 50 字）
4. 3 个 feature（图标短语 + 一行解释）
5. 适用人群
6. 检查前准备（3 条 bullet）
7. 检查流程（5 步）
8. 风险与注意
9. 主 CTA + 次 CTA（cross-link 到另一项目）

### 4.4 科普 `science`

覆盖：页面 lead、3 section 标题、3 篇文章（capsule / cardiac / CT）各含标题与摘要。

### 4.5 服务 `services`

覆盖：页面 lead、旗舰 section（2 个服务的标题 / 副标题 / 3 个 highlight）、更多服务预告块、CTA。

### 4.6 中亚特色 `central_asia`

覆盖：页面 lead、跨境就医 section（4 个服务：签证 / 翻译 / 住宿 / 随访）、维吾尔医与哈萨克医 section。

### 4.7 联系表单 `contact`

覆盖：表单标题、6 个字段（label / placeholder / 选项）、consent、submit 三态（默认 / loading / success）、4 种错误提示。

---

## 5. 三语对齐验证

| Key | zh | en | ru |
|---|---|---|---|
| `common.nav_home` | ✅ 首页 | ✅ Home | ✅ Главная |
| `common.nav_science` | ✅ 医疗科普 | ✅ Patient Library | ✅ Библиотека пациента |
| `common.nav_services` | ✅ 服务项目 | ✅ Services | ✅ Услуги |
| `common.nav_central_asia` | ✅ 新疆中亚特色医疗 | ✅ Xinjiang & Central Asia | ✅ Синьцзян и Центральная Азия |
| `home.hero_headline` | ✅ | ✅ | ✅ |
| `home.hero_subheadline` | ✅ | ✅ | ✅ |
| `project_capsule.title` | ✅ | ✅ | ✅ |
| `project_cardiac.title` | ✅ | ✅ | ✅ |
| `cta.view_service_detail` | ✅ 查看项目 | ✅ View procedure | ✅ Подробнее об исследовании |
| `cta.book_consultation` | ✅ 预约咨询 | ✅ Book a consultation | ✅ Записаться на консультацию |

> 关键导航与 CTA 三语 100% 对齐；详细文案三语 100% 对齐。

---

## 6. 俄语母语化校对清单

针对 ru.json，已逐项校对：

- ✅ "胶囊胃镜" → "Капсульная эндоскопия"（不用"видеокапсула"以避免歧义）
- ✅ "心脏冠脉核磁" → "МРТ коронарных артерий"（业内通用译法）
- ✅ "无造影剂" → "Без контрастного вещества"（不用"без контраста"以保持正式）
- ✅ "无电离辐射" → "Без ионизирующего излучения"（医学标准译法）
- ✅ "屏气" → "Задержка дыхания"（俄语医学用语）
- ✅ "美年健康" → 保留 "Meinian Health"（品牌音译）
- ✅ "天山南北" → "Синьцзян"（避免字面直译导致生硬）
- ✅ "一个工作日内回复" → "в течение одного рабочего дня"（标准商务用语）
- ✅ "中亚五国" → "пять стран Центральной Азии"（俄语顺序：数字+名词属格）
- ✅ 阿拉伯数字统一为西方数字（按 design_guide §6.3）
- ✅ 复数规则已审视：导航、CTA 等单数处保持单数；列表项（如"3 步流程"）使用数量数词 + 属格

---

## 7. 关键决策

1. **CTA 数量收敛到 6 个**，覆盖学习 / 预约 / 联系 / 阅读 / 浏览 / 跨境，避免 v1 出现 8+ 个相近意图。
2. **数字型宣传全删**：用 "美年健康 · 新疆旗舰" 等意境化表达替代。
3. **首页 hero 用提问句式**：以"把...轻轻推开"开场，传递"打开而非推销"的语气。
4. **项目详情用 9 个固定 block**：保证两个项目页面结构对称，便于未来扩展更多项目。
5. **俄语用医疗标准术语**：避免口语化表达，确保医务顾问可复用。
6. **科普页面 lead 明示文献来源与更新日期**：体现医学严谨性，与 design_guide §10.1 数据脚注规范一致。

---

## 8. 后续步骤

- Step 2 将 copy-final JSON 改造为标准 i18n key 体系（拆 `locales/{zh-CN,en,ru}/{common,home,projects,science,services,central-asia}.json`），保持相同 key 树但去掉 `_meta` 与 `_label`，新增 ICU 占位支持。
- 若 i18n 改造需要新增占位符（如 `{n} 个医师`），将在 Step 2 同步补充 ru.json 的复数分支。

---

> 本报告与 `copy-final/*.json` 一同作为 v2 文案层单一真相源。