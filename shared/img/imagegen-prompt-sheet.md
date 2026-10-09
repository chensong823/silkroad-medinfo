# Silk Road Medinfo · v2 Image Generation Prompt Sheet

> **Date**: 2026-09-30
> **Sections**: 8 horizontal sections × 3 variants (Central Asian / East Asian / no-people) = **24 images**
> **Format target**: 1920×1080 (16:9), single section per frame, never combined
> **Palette lock**: `#0B5FAE` magnetic blue · `#E63946` vital red · `#C8954A` desert gold · `#8B5A3C` camel-shadow brown · `#F4F7FB` cool white · `#FBF7F0` warm white

---

## §1 通用 Negative Prompts（所有 24 个模板前置）

```
text, watermark, logo, signature, brand name on clothing or equipment, caption,
cartoon, anime, illustration, painting, sketch, low quality, blurry, jpeg artifacts,
oversaturated, overexposed, deformed, extra limbs, extra fingers, mutated hands,
duplicate, tiling, frame, border, collage, split screen,
nudity, gore, blood, horror, weapons, military, nsfw,
religious symbols, country flags, political symbols
```

Plus v2-specific bans: **no beige+brass premium slop**, **no purple AI glow**, **no neon edges**, **no gradient text as shortcut**, **no fake dashboards**, **no stock-photo cliches**.

---

## §2 Section 1 · 首页 Hero

> Story: 医疗精度（科技）+ 一带一路温度（人文）。Open gently, not sell hard.

### Section 1-A · 中亚面孔 Hero

**Subject**: A 35-year-old Central Asian female doctor in a clean white coat stands at left-third of frame, soft natural window light, calm professional expression, behind her a softly blurred clinic corridor leading to a window with warm Xinjiang golden-hour sky (no direct sun visible), a single capsule endoscope device on a side table to her right (in focus, clinical cool-white tone), depth haze in corridor.
**Style**: cinematic medical lifestyle photography, editorial, soft analog film grain ≤ 6%, 8K, Hasselblad X2D 38mm.
**Composition**: bottom-left text-safe area reserved 35% lower-third, doctor at left-third intersection, device at right-third, top 20% negative space, foreground slight atmospheric haze.
**Color Palette**: dominant `#FBF7F0` warm cream background, doctor coat `#FBF7F0`, doctor scarf `#C8954A` desert gold, corridor walls `#E8D5A8`, device surface cool white with `#0B5FAE` accent ring, sky `#C8954A` to `#FBF7F0` warm gradient.
**Lighting**: soft window light camera-left 4500K warm, gentle ceiling fill 20%, no flash, natural catchlights in eyes, warm rim from window.
**Detail Modifiers**: matte cotton coat with visible weave, natural skin texture with pores, shallow depth of field f/2.0 on device, subtle film grain ISO 200, accurate anatomy.
**Negative Prompts**: (通用 §1) + no stethoscope clutter, no chart papers, no computer screens, no text overlays on walls, no sunglasses, no watches visible, no Chinese characters.

### Section 1-B · 东亚面孔 Hero

**Subject**: A 40-year-old East Asian male doctor in a clean white coat stands at left-third of frame, soft natural window light, calm professional expression, behind him a softly blurred clinic reception with warm Xinjiang afternoon light filtering through arched windows (referencing Silk Road architecture subtly via the arch shape), a single cardiac MRI scanner silhouette visible far back through a glass partition (cool clinical blue tone).
**Style**: cinematic medical lifestyle photography, editorial, soft analog film grain, 8K, Sony A7CR 35mm.
**Composition**: bottom-left text-safe area reserved, doctor at left-third, MRI silhouette at right-third depth, top 20% negative space, foreground atmospheric depth.
**Color Palette**: dominant `#F4F7FB` cool white background, doctor coat `#FBF7F0`, deep navy lapel pin `#0B5FAE`, corridor `#E8EDF2`, MRI gantry inner ring `#0B5FAE` to `#1E5B8A`, arched window frame `#C8954A` warm wood accent.
**Lighting**: soft window light camera-left 4800K, ceiling fill 20%, warm rim from arched window, no flash, natural catchlights.
**Detail Modifiers**: matte cotton coat weave, natural skin texture, shallow depth of field f/2.5, subtle grain ISO 200.
**Negative Prompts**: (通用 §1) + no stethoscope, no clipboards, no glasses, no Chinese characters, no traditional medicine props.

### Section 1-C · 无人纯场景 Hero

**Subject**: An empty clinic consultation room at dawn, two white-coat hooks hanging on the wall (one with a stethoscope draped, one empty), a single warm wood desk at right with an open notebook and a small potted succulent, soft window light streaming through a tall arched window referencing Silk Road vernacular architecture, a single capsule endoscope device resting on a side shelf in soft focus, no human present.
**Style**: cinematic still-life medical photography, editorial calm, soft film grain, 8K, Fujifilm GFX 100S 63mm.
**Composition**: centered subject, desk and notebook at lower-third, arched window at upper-third, hooks at left-third, ample negative space, foreground atmospheric haze.
**Color Palette**: walls `#FBF7F0` warm cream, desk wood `#8B5A3C`, succulent `#A89070` muted green-gray, notebook paper `#F4F7FB`, stethoscope `#0B5FAE` accent, arch window light `#C8954A` to `#FBF7F0`.
**Lighting**: dawn light from upper-right 3800K warm, ambient fill 15%, soft window shadow on wall, no flash.
**Detail Modifiers**: wood grain on desk, paper texture, soft bokeh on far elements, depth of field f/4, grain ISO 400.
**Negative Prompts**: (通用 §1) + no people, no hands, no faces, no screens, no charts on walls.

---

## §3 Section 2 · 医疗科普入口区

> Story: Understand it first. Then decide. Calm library feel, not lab.

### Section 2-A · 中亚面孔 科普

**Subject**: A 35-year-old Central Asian female physician-scientist in a white coat sits at a long warm wood library table reading a medical journal, soft window light, three open textbooks and one tablet arranged asymmetrically on the table, a single warm-toned ceramic mug, background is a softly blurred medical library with warm wood shelves, no obvious brand text.
**Style**: editorial documentary photography, warm natural light, candid authentic, 8K, Leica Q3 50mm.
**Composition**: right-third caption + left-two-thirds visual (inverted classic, intentional), physician at left-third intersection, top 25% and bottom 15% negative space.
**Color Palette**: dominant `#FBF7F0` warm white, table wood `#8B5A3C`, books varied `#C8954A` to `#A89070`, physician scarf `#C8954A` accent, tablet bezel `#0B5FAE` muted.
**Lighting**: window light camera-left 4400K warm, ceiling fill 25%, no flash, natural eye-light reflections.
**Detail Modifiers**: visible book pages, paper texture, natural skin, depth of field f/2.0, grain ISO 400.
**Negative Prompts**: (通用 §1) + no reading glasses pushed down, no writing hand close-up, no cluttered desk.

### Section 2-B · 东亚面孔 科普

**Subject**: A 45-year-old East Asian male physician in a white coat stands in front of a softly lit floor-to-ceiling medical library shelf, gesturing gently toward an open book on a stand, soft natural light, two-three closed textbooks on a lower shelf, background blurred warm wood shelving, no visible logos.
**Style**: editorial documentary photography, warm natural light, candid authentic, 8K, Sony A7CR 50mm.
**Composition**: left-third caption + right-two-thirds visual (classic), physician at left-third, top 25% and bottom 15% negative space.
**Color Palette**: white coat `#FBF7F0`, book covers varied `#0B5FAE` `#C8954A` `#A89070`, shelf wood `#8B5A3C`, accent scarf `#0B5FAE`.
**Lighting**: window light camera-right 4500K warm, ceiling fill 25%.
**Detail Modifiers**: book spine details, natural skin, depth of field f/2.5, grain ISO 200.
**Negative Prompts**: (通用 §1) + no pointing finger close-up, no cluttered shelves.

### Section 2-C · 无人纯场景 科普

**Subject**: An overhead editorial shot of a clean warm wood library table with an open medical textbook in center, a second closed book at right, a tablet at left showing a soft blue-toned medical scan (no text overlay), a ceramic mug, a pair of reading glasses resting at lower-left corner, soft natural light from upper-left casting long gentle shadows, no human hands visible.
**Style**: still-life editorial photography, soft analog film, contemplative, 8K, Fujifilm GFX 100S 80mm.
**Composition**: top-down editorial, books at center, tablet at upper-left, mug at lower-right, glasses at lower-left, strict asymmetric balance.
**Color Palette**: table `#8B5A3C`, pages `#FBF7F0`, book covers `#C8954A` `#0B5FAE`, tablet screen `#0B5FAE` soft glow.
**Lighting**: window light upper-left 4400K warm, no flash, soft shadows.
**Detail Modifiers**: paper fiber texture, depth of field f/4, grain ISO 400.
**Negative Prompts**: (通用 §1) + no hands, no human presence, no food, no drink liquid visible.

---

## §4 Section 3 · 服务项目 · 美年旗舰模块标题

> Story: Two flagship procedures, one calm headline. Editorial poster energy.

### Section 3-A · 中亚面孔 旗舰模块

**Subject**: A clean editorial two-card product poster composition on warm cream paper background: left card shows a soft-focus capsule endoscope device (Anhan-style AI magnetic capsule, no brand text), right card shows a stylized 3.0T MRI gantry ring (no scanner body), between them at center a small Central Asian female physician silhouette in white coat reading a tablet, all three elements separated by a thin Silk Road route line (0.5px, `#C8954A`) connecting them across the frame as a single arc.
**Style**: modern editorial product poster, soft duotone-treated photography with paper texture, premium matte feel, 8K.
**Composition**: three-element poster layout, left card 35% width, center figure 30% width, right card 35% width, single horizon line at lower-third, top 20% negative space for headline.
**Color Palette**: paper background `#FBF7F0`, capsule device `#E8EDF2` with `#0B5FAE` accent ring, MRI gantry ring `#0B5FAE` to `#1E5B8A`, physician silhouette `#C8954A` warm wash, route line `#C8954A` 0.5px.
**Lighting**: even ambient, no harsh direction, soft tonal depth.
**Detail Modifiers**: paper fiber texture 3%, subtle ink-bleed on device edges, soft duotone grade.
**Negative Prompts**: (通用 §1) + no text on devices, no model numbers, no screen content.

### Section 3-B · 东亚面孔 旗舰模块

**Subject**: Same as 3-A but center figure is an East Asian male physician silhouette in white coat holding a clipboard, no brand text anywhere, route line `#0B5FAE` thin 0.5px.
**Style, Composition, Palette, Lighting**: same as 3-A with `#0B5FAE` route line accent.
**Negative Prompts**: same as 3-A.

### Section 3-C · 无人纯场景 旗舰模块

**Subject**: Same as 3-A but no center figure, instead a single Silk Road route line drawing arches gracefully between left capsule device and right MRI gantry ring, with a small abstract camel silhouette at bottom-right as a quiet Silk Road motif, all on warm cream paper.
**Style, Composition, Palette, Lighting**: same as 3-A.
**Detail Modifiers**: hand-drawn line quality on route, paper fiber 3%, soft duotone.
**Negative Prompts**: (通用 §1) + no people, no hands.

---

## §5 Section 4 · 服务项目 · 胶囊胃镜卡片封面

> Story: A capsule, no tube, no sedation. Clinical precision meets quiet calm.

### Section 4-A · 中亚面孔 胶囊胃镜

**Subject**: Macro editorial product shot of a single magnetic-guided capsule endoscope device (capsule form factor, matte medical polymer, no brand engraving) resting on a small clean white medical tray, behind it softly out of focus a Central Asian female physician's white-coated shoulder and gentle hand gesture, soft natural light, single shallow ceramic bowl of dried camel-thorn at upper-right adding warm cultural texture, no text.
**Style**: editorial medical lifestyle, soft analog grain ≤ 6%, premium tactile feel, 8K, Hasselblad X2D 80mm macro.
**Composition**: capsule at right-third intersection, tray at lower-third, blurred physician shoulder at left-third, top 25% negative space.
**Color Palette**: capsule matte `#E8EDF2` with subtle `#0B5FAE` indicator LED, tray `#F4F7FB`, physician coat `#FBF7F0`, dried branches `#8B5A3C` warm brown.
**Lighting**: window light upper-left 4500K, ambient 20%, soft shadow under tray.
**Detail Modifiers**: capsule polymer texture, tray matte ceramic, branch texture sharp, depth of field f/2.8 on capsule, grain ISO 200.
**Negative Prompts**: (通用 §1) + no visible face, no stethoscope, no brand engraving on capsule.

### Section 4-B · 东亚面孔 胶囊胃镜

**Subject**: Same as 4-A with an East Asian male physician's hand gently offering the capsule on a clean medical tray, no face visible, soft window light.
**Style, Composition, Palette, Lighting**: same as 4-A.
**Negative Prompts**: same as 4-A.

### Section 4-C · 无人纯场景 胶囊胃镜

**Subject**: Pure editorial product shot: single capsule endoscope device resting at center on a clean warm cream paper surface, beside it a small thin camel-silk textile fragment (suggesting Silk Road cultural touch), a single warm-toned ceramic bowl of dried camel-thorn at upper-right, soft window light from upper-left casting long gentle shadow, no human presence.
**Style**: editorial still-life, soft analog grain, premium matte, 8K, Fujifilm GFX 100S 80mm macro.
**Composition**: capsule at exact center, textile at lower-left, branches at upper-right, strict asymmetric balance.
**Color Palette**: paper `#FBF7F0`, capsule `#E8EDF2` with `#0B5FAE` LED, textile `#C8954A` to `#8B5A3C`, branches `#8B5A3C`.
**Lighting**: window light upper-left 4400K, no flash.
**Detail Modifiers**: paper fiber 4%, capsule polymer texture, soft shadow, depth of field f/4, grain ISO 400.
**Negative Prompts**: (通用 §1) + no people, no hands.

---

## §6 Section 5 · 服务项目 · 心脏冠脉核磁卡片封面

> Story: A 14-second breath hold, no radiation, no contrast. Quiet medical precision.

### Section 5-A · 中亚面孔 心脏冠脉核磁

**Subject**: Editorial wide shot of a 3.0T MRI gantry (United Imaging uMR880-style, no brand engraving) viewed from a three-quarter angle, a Central Asian female technologist in white coat stands at the side console at left-third (small in frame, soft focus), soft clinical cool-white lighting, behind the gantry a softly blurred cardiac monitor screen showing a stylized ECG waveform in soft blue, no text overlays.
**Style**: cinematic clinical product photography, soft analog grain, premium medical, 8K, Hasselblad X2D 50mm.
**Composition**: gantry at right-two-thirds intersection, technologist at left-third, top 20% negative space for headline.
**Color Palette**: gantry cool white `#E8EDF2` with `#0B5FAE` inner ring, technologist coat `#F4F7FB`, ECG waveform `#3FC1E9` cyan glow, background `#0A2540` deep navy fading to `#061A2E`.
**Lighting**: two-point clinical lighting, key 60° upper-left 5200K, fill 30% upper-right 4800K with cool gel, soft ground reflection.
**Detail Modifiers**: matte powder-coated gantry finish, glossy inner ring, depth of field f/4, grain ISO 100.
**Negative Prompts**: (通用 §1) + no brand text on gantry, no model numbers, no patient on table.

### Section 5-B · 东亚面孔 心脏冠脉核磁

**Subject**: Same as 5-A with an East Asian male technologist at the console.
**Style, Composition, Palette, Lighting**: same as 5-A.
**Negative Prompts**: same as 5-A.

### Section 5-C · 无人纯场景 心脏冠脉核磁

**Subject**: Editorial wide shot of an empty 3.0T MRI gantry (no technologist), three-quarter angle, cool clinical lighting, ECG waveform monitor softly glowing in background, gantry bore entrance subtly lit with cool `#0B5FAE` accent ring, no human presence, no text overlays.
**Style, Composition, Palette, Lighting**: same as 5-A.
**Detail Modifiers**: matte gantry finish, soft glow from bore, depth of field f/5.6.
**Negative Prompts**: (通用 §1) + no people, no patients, no chairs, no clutter.

---

## §7 Section 6 · 新疆中亚特色医疗区

> Story: From Almaty, Tashkent, Bishkek to Urumqi. A medical doorway, opened gently.

### Section 6-A · 中亚面孔 跨境

**Subject**: Editorial warm-life shot of two figures meeting at a clinic doorway, one Central Asian female patient in a soft traditional patterned shawl (Uyghur geometric pattern, no religious symbols), one East Asian male doctor in white coat extending a welcoming hand toward the patient, soft Xinjiang golden-hour window light, behind them softly visible a Silk Road route map line drawing on a clean wall (no country labels), warm cream tones throughout, no text.
**Style**: cinematic lifestyle editorial, soft analog film grain ≤ 8%, premium documentary feel, 8K, Sony A7CR 35mm.
**Composition**: doctor at left-third, patient at right-third, doorway center, top 25% and bottom 15% negative space.
**Color Palette**: dominant `#FBF7F0`, doctor coat `#FBF7F0`, patient shawl `#C8954A` `#8B5A3C` `#2F6B4F` geometric, wall map line `#C8954A`, doorway arch `#8B5A3C` warm wood.
**Lighting**: golden-hour window light camera-right 4200K warm, ambient fill 25%, natural catchlights.
**Detail Modifiers**: fabric weave visible on shawl, natural skin texture, depth of field f/2.5, grain ISO 400.
**Negative Prompts**: (通用 §1) + no country flags, no religious symbols, no embraces, no kissing, no children.

### Section 6-B · 东亚面孔 跨境

**Subject**: Same as 6-A but the patient is an East Asian Han Chinese elderly person in a soft Tangzhuang navy jacket, the doctor is Central Asian female, same composition and palette.
**Style, Composition, Palette, Lighting**: same as 6-A.
**Negative Prompts**: same as 6-A.

### Section 6-C · 无人纯场景 跨境

**Subject**: A warm editorial still-life of a clean clinic doorway with an arched frame (referencing Silk Road vernacular architecture), a small wooden side table beside it holding a brass tray with three small ceramic cups of herbal tea (Uyghur or Kazakh traditional), a small patterned textile draped over the table corner, soft Xinjiang golden-hour window light from upper-right, no human presence.
**Style**: still-life editorial, soft analog film grain, warm contemplative mood, 8K, Fujifilm GFX 100S 50mm.
**Composition**: arch at center, table at lower-right, cups at center on tray, textile at lower-left.
**Color Palette**: arch `#8B5A3C` warm wood, cups `#FBF7F0` `#C8954A` `#0B5FAE` muted, tea liquid `#A89070` warm amber, textile `#C8954A` `#8B5A3C` `#2F6B4F` geometric.
**Lighting**: golden-hour light upper-right 4200K, soft ambient 20%, gentle shadows.
**Detail Modifiers**: ceramic glaze texture, wood grain, textile weave, depth of field f/2.8, grain ISO 400.
**Negative Prompts**: (通用 §1) + no people, no hands.

---

## §8 Section 7 · CTA Banner

> Story: Book a consultation. Care coordinator replies within one business day. Calm closing.

### Section 7-A · 中亚面孔 CTA

**Subject**: A single warm editorial composition: a Central Asian female care coordinator in a soft beige cardigan sits at a clean warm wood desk, gentle smile, soft afternoon window light from upper-right, behind her a softly blurred clean clinic wall with a single small Silk Road textile wall hanging (geometric pattern, no text), a small potted succulent on desk corner, a ceramic mug of tea, an open notebook with a pen resting diagonally, no screens visible.
**Style**: cinematic lifestyle editorial, warm natural light, soft film grain ≤ 6%, premium documentary, 8K, Leica Q3 35mm.
**Composition**: coordinator at right-third, notebook at lower-left, textile wall hanging at upper-left, top 20% and bottom 25% text-safe area.
**Color Palette**: cardigan `#C8954A`, desk wood `#8B5A3C`, wall `#FBF7F0`, textile `#C8954A` `#8B5A3C` geometric, succulent `#A89070`, mug `#FBF7F0` with `#C8954A` glaze.
**Lighting**: afternoon window light upper-right 4400K warm, ambient 25%, no flash.
**Detail Modifiers**: cardigan weave, wood grain, paper texture, depth of field f/2.0 on coordinator, grain ISO 200.
**Negative Prompts**: (通用 §1) + no screens, no computers, no phones visible, no name badges.

### Section 7-B · 东亚面孔 CTA

**Subject**: Same as 7-A with an East Asian male care coordinator in soft warm gray cardigan at the desk.
**Style, Composition, Palette, Lighting**: same as 7-A.
**Negative Prompts**: same as 7-A.

### Section 7-C · 无人纯场景 CTA

**Subject**: An editorial overhead-three-quarter shot of a clean warm wood desk surface with an open notebook showing handwritten lines (no actual text, suggested marks), a small ceramic mug of amber tea, a single pen lying diagonally, a small potted succulent, a thin Silk Road textile draped at upper-left corner, soft afternoon window light from upper-right, no human presence.
**Style**: still-life editorial, soft film grain, contemplative, 8K, Fujifilm GFX 100S 50mm.
**Composition**: notebook center, mug upper-right, pen diagonal, succulent lower-right, textile upper-left.
**Color Palette**: wood `#8B5A3C`, paper `#FBF7F0`, mug `#FBF7F0` `#C8954A`, tea `#A89070`, succulent `#A89070`, textile `#C8954A` `#8B5A3C`.
**Lighting**: afternoon light upper-right 4400K, soft shadow.
**Detail Modifiers**: wood grain, paper fiber, ceramic glaze, depth of field f/4, grain ISO 400.
**Negative Prompts**: (通用 §1) + no people, no hands, no screens.

---

## §9 Section 8 · Footer 装饰

> Story: Quiet Silk Road brand mark. Discreet, dignified, never decorative noise.

### Section 8-A · 中亚面孔 Footer

**Subject**: A wide horizontal brand motif composition: on the left third, a single silhouette of a Central Asian woman in profile (small, dignified, no facial detail) standing at a Silk Road window arch, on the right two-thirds an abstract hand-drawn Silk Road route line drawing extending horizontally across the frame with subtle node dots representing waypoints (Almaty, Tashkent, Bishkek, Urumqi — no labels), warm cream paper background, subtle medical cross mark in `#0B5FAE` at top-right as quiet brand anchor, no text overlays.
**Style**: editorial brand mark illustration in photographic style, soft duotone, premium paper feel, 8K.
**Composition**: figure silhouette at left 25%, route line spanning 75% of width, cross mark at upper-right.
**Color Palette**: paper `#FBF7F0`, silhouette `#8B5A3C` warm brown, route line `#C8954A` 0.5px, node dots `#E63946` small, cross mark `#0B5FAE`.
**Lighting**: even ambient, soft tonal grade.
**Detail Modifiers**: paper fiber 4%, hand-drawn line quality, soft duotone.
**Negative Prompts**: (通用 §1) + no faces with sharp detail, no labels, no country names, no flags.

### Section 8-B · 东亚面孔 Footer

**Subject**: Same as 8-A with an East Asian figure silhouette in profile at left-third, same route line and cross mark.
**Style, Composition, Palette, Lighting**: same as 8-A.
**Negative Prompts**: same as 8-A.

### Section 8-C · 无人纯场景 Footer

**Subject**: Same composition but no figure silhouette — pure Silk Road route line drawing extending across the frame with node dots, subtle medical cross mark at upper-right, warm cream paper.
**Style, Composition, Palette, Lighting**: same as 8-A.
**Negative Prompts**: (通用 §1) + no people, no hands, no labels.

---

## §10 文件命名规范（实际生成时）

```
output_html/v2/shared/img/
├── 01-hero-A-central-asian.{png,webp,avif}
├── 01-hero-B-east-asian.{png,webp,avif}
├── 01-hero-C-scene.{png,webp,avif}
├── 02-science-A-central-asian.{png,webp,avif}
├── 02-science-B-east-asian.{png,webp,avif}
├── 02-science-C-scene.{png,webp,avif}
├── 03-flagship-A-central-asian.{png,webp,avif}
├── 03-flagship-B-east-asian.{png,webp,avif}
├── 03-flagship-C-scene.{png,webp,avif}
├── 04-capsule-A-central-asian.{png,webp,avif}
├── 04-capsule-B-east-asian.{png,webp,avif}
├── 04-capsule-C-scene.{png,webp,avif}
├── 05-cardiac-A-central-asian.{png,webp,avif}
├── 05-cardiac-B-east-asian.{png,webp,avif}
├── 05-cardiac-C-scene.{png,webp,avif}
├── 06-central-asia-A-central-asian.{png,webp,avif}
├── 06-central-asia-B-east-asian.{png,webp,avif}
├── 06-central-asia-C-scene.{png,webp,avif}
├── 07-cta-A-central-asian.{png,webp,avif}
├── 07-cta-B-east-asian.{png,webp,avif}
├── 07-cta-C-scene.{png,webp,avif}
├── 08-footer-A-central-asian.{png,webp,avif}
├── 08-footer-B-east-asian.{png,webp,avif}
└── 08-footer-C-scene.{png,webp,avif}
```

每个文件：PNG 原图 + WebP (q=82) + AVIF 双优化版本。

---

## §11 推荐生成工具

| 工具 | 适用场景 | 参数 |
|---|---|---|
| **Midjourney v6.1** | 默认主力 | `--ar 16:9 --style raw --stylize 200 --seed 20260930 --v 6.1` |
| **DALL·E 3** | 文字渲染好（Banner / 文字元素） | `size: 1792x1024`, `quality: hd`, `style: natural` |
| **Stable Diffusion XL** | 高保真医疗设备 | JuggernautXL checkpoint, CFG 7, steps 35 |
| **Adobe Firefly** | 商业版权安全 | Firefly Image 3, Photo mode |

每个 section 跑 4 张候选 + 1 张终选，保留 Seed + 原图以备举证（肖像权 / 版权）。

---

## §12 一致性技巧

1. **Seed 区间**：`--seed 20260930` 至 `20260950`，跨变体保持视觉血缘。
2. **Style Reference**：第一张标杆图确定后，所有后续变体用 `--sref <URL>` 引用。
3. **hex 锁色**：所有颜色用 hex，不用"磁蓝"等描述词。
4. **同一光照语言**：科技主调 5200K–5600K 冷白，医学摄影；人文主调 4200K–4500K 暖光，生活场景。
5. **统一颗粒**：医学摄影 ISO 100–200，人文摄影 ISO 400–800。

---

## §13 SVG 占位符（已生成）

`shared/img/svg/*.svg` 提供 24 个轻量级品牌 SVG 占位符，可在真实图片生成前先用于：

- 设计 review / stakeholder walkthrough
- 占位开发（避免布局抖动）
- A11y 验证（确保图片缺失时布局仍稳定）

占位符使用品牌色板 + 抽象几何表达，不含人物面孔细节。

---

> 本 prompt sheet 与 `shared/img/svg/*.svg` 占位符共同构成 v2 图片层。真实生成时按 §11 工具推荐执行，保留 Seed 与原图，输出 PNG + WebP + AVIF 三格式。