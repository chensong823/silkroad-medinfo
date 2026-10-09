# shared/img/svg — Brand SVG Placeholders

> **24 个占位 SVG**，与 `imagegen-prompt-sheet.md` 一一对应。

## 文件清单

| Section | A: Central Asian | B: East Asian | C: Scene |
|---|---|---|---|
| 01-hero | `01-hero-A-central-asian.svg` | `01-hero-B-east-asian.svg` | `01-hero-C-scene.svg` |
| 02-science | `02-science-A-central-asian.svg` | `02-science-B-east-asian.svg` | `02-science-C-scene.svg` |
| 03-flagship | `03-flagship-A-central-asian.svg` | `03-flagship-B-east-asian.svg` | `03-flagship-C-scene.svg` |
| 04-capsule | `04-capsule-A-central-asian.svg` | `04-capsule-B-east-asian.svg` | `04-capsule-C-scene.svg` |
| 05-cardiac | `05-cardiac-A-central-asian.svg` | `05-cardiac-B-east-asian.svg` | `05-cardiac-C-scene.svg` |
| 06-central-asia | `06-central-asia-A-central-asian.svg` | `06-central-asia-B-east-asian.svg` | `06-central-asia-C-scene.svg` |
| 07-cta | `07-cta-A-central-asian.svg` | `07-cta-B-east-asian.svg` | `07-cta-C-scene.svg` |
| 08-footer | `08-footer-A-central-asian.svg` | `08-footer-B-east-asian.svg` | `08-footer-C-scene.svg` |

## 设计原则

- **画布**：1920×1080（16:9 横版），preserveAspectRatio="xMidYMid slice"
- **配色**：仅使用 v2 品牌色板（磁蓝 / 生命红 / 沙漠金 / 驼影棕 / 冷白 / 暖白 / 深墨）
- **避免**：beige+brass premium slop、紫蓝 AI 渐变、霓虹边缘
- **人物**：仅用几何化剪影，无面部细节（避免肖像权问题）
- **几何**：八角星 / 丝路曲线 / 医疗十字 三种母题，作为品牌符号重复

## 何时替换

实际部署前，按 `imagegen-prompt-sheet.md` 中的 24 个 prompt 跑图（推荐 Midjourney v6.1 / DALL·E 3 / Stable Diffusion XL），输出到：

```
shared/img/web/01-hero-A-central-asian.{png,webp,avif}
...
shared/img/web/08-footer-C-scene.{png,webp,avif}
```

然后在 HTML 中将 SVG 引用替换为真实图片（带 srcset / AVIF / WebP / 尺寸）。

## HTML 中的使用

```html
<!-- 占位（开发期） -->
<img src="/shared/img/svg/01-hero-A-central-asian.svg"
     alt="丝路医讯首页主图"
     width="1920" height="1080" />

<!-- 部署期 -->
<picture>
  <source srcset="/shared/img/web/01-hero-A-central-asian.avif" type="image/avif" />
  <source srcset="/shared/img/web/01-hero-A-central-asian.webp" type="image/webp" />
  <img src="/shared/img/web/01-hero-A-central-asian.png"
       alt="丝路医讯首页主图"
       width="1920" height="1080"
       loading="lazy" decoding="async" />
</picture>
```

## 重新生成

```bash
python scripts/generate-svg-placeholders.py --out shared/img/svg
```

可修改 `SECTIONS` / `VARIANTS` / 颜色变量 / 几何元素，24 个 SVG 一次性重新出图。