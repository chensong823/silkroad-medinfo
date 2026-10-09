#!/usr/bin/env python3
"""Generate 24 brand SVG placeholders for Silk Road Medinfo v2.

8 sections x 3 variants (central-asian / east-asian / scene) = 24 SVGs.
Each is 1920x1080 horizontal, uses the v2 brand palette, and avoids
beige+brass premium slop.

Usage:
  python scripts/generate-svg-placeholders.py --out ../shared/img/svg
"""

from __future__ import annotations
import argparse
from pathlib import Path

# v2 brand palette
PALETTE = {
    "blue":    "#0B5FAE",  # magnetic blue (primary tech)
    "red":     "#E63946",  # vital red
    "gold":    "#C8954A",  # desert gold
    "brown":   "#8B5A3C",  # camel shadow
    "cool":    "#F4F7FB",  # cool white
    "warm":    "#FBF7F0",  # warm white
    "ink":     "#0F172A",  # deep ink
    "slate":   "#334155",  # slate text
    "mist":    "#E8EDF2",  # mist
    "dawn":    "#D4B585",  # dawn warm
    "navy":    "#0A2540",  # deep navy
    "cyan":    "#3FC1E9",  # cyan accent
}

# Section metadata: (slug, label_en, label_zh, composition)
SECTIONS = [
    ("01-hero",            "Hero",                 "首页主图",       "centered_low"),
    ("02-science",         "Patient Library",      "医疗科普入口",    "inverted"),
    ("03-flagship",        "Flagship Module",      "美年旗舰模块",    "triptych"),
    ("04-capsule",         "Capsule Endoscopy",    "胶囊胃镜卡片",    "macro"),
    ("05-cardiac",         "Cardiac MR",           "心脏冠脉核磁卡",  "wide"),
    ("06-central-asia",    "Xinjiang & CA",        "新疆中亚特色",    "two_figures"),
    ("07-cta",             "CTA Banner",           "行动号召",        "warm_life"),
    ("08-footer",          "Footer Decoration",    "页脚装饰",        "brand_mark"),
]

VARIANTS = [
    ("A", "central-asian"),
    ("B", "east-asian"),
    ("C", "scene"),
]

W, H = 1920, 1080


def svg_open() -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'preserveAspectRatio="xMidYMid slice" role="img">\n'
    )


def svg_defs(extra: str = "") -> str:
    return f"""  <defs>
    <linearGradient id="bg-warm" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{PALETTE['warm']}"/>
      <stop offset="100%" stop-color="{PALETTE['dawn']}"/>
    </linearGradient>
    <linearGradient id="bg-cool" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{PALETTE['cool']}"/>
      <stop offset="100%" stop-color="{PALETTE['mist']}"/>
    </linearGradient>
    <linearGradient id="bg-navy" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{PALETTE['navy']}"/>
      <stop offset="100%" stop-color="#061A2E"/>
    </linearGradient>
    <radialGradient id="vignette" cx="50%" cy="50%" r="70%">
      <stop offset="60%" stop-color="rgba(0,0,0,0)"/>
      <stop offset="100%" stop-color="rgba(15,23,42,0.18)"/>
    </radialGradient>
    {extra}
  </defs>
"""


def svg_close() -> str:
    return "</svg>\n"


def text_label(section_label: str, variant_label: str) -> str:
    """Small placeholder annotation in bottom-left corner."""
    return f"""  <g opacity="0.55" font-family="Inter, system-ui, sans-serif" font-size="22" fill="{PALETTE['slate']}">
    <text x="48" y="1010" font-weight="600">Silk Road Medinfo · placeholder</text>
    <text x="48" y="1040" font-size="18" fill="{PALETTE['slate']}" opacity="0.75">{section_label} · variant {variant_label}</text>
  </g>
"""


def silk_road_route() -> str:
    """Decorative Silk Road route line arc, 0.5px stroke, used in footer / flagship."""
    return f"""  <g opacity="0.6" fill="none" stroke="{PALETTE['gold']}" stroke-width="1.5" stroke-linecap="round">
    <path d="M 120 760 Q 480 600 960 720 T 1800 660" stroke-dasharray="0"/>
    <circle cx="120" cy="760" r="6" fill="{PALETTE['red']}"/>
    <circle cx="640" cy="678" r="5" fill="{PALETTE['gold']}"/>
    <circle cx="1180" cy="694" r="5" fill="{PALETTE['gold']}"/>
    <circle cx="1800" cy="660" r="6" fill="{PALETTE['red']}"/>
  </g>
"""


def silk_road_geometric_pattern(x: float, y: float, scale: float = 1.0) -> str:
    """Eight-point Uyghur geometric pattern (no religious symbol, generic)."""
    s = scale
    return f"""  <g transform="translate({x},{y}) scale({s})" fill="{PALETTE['brown']}" opacity="0.85">
    <polygon points="0,-40 12,-12 40,0 12,12 0,40 -12,12 -40,0 -12,-12"/>
    <polygon points="0,-22 7,-7 22,0 7,7 0,22 -7,7 -22,0 -7,-7" fill="{PALETTE['gold']}"/>
    <circle cx="0" cy="0" r="6" fill="{PALETTE['red']}"/>
  </g>
"""


def figure_silhouette(x: float, y: float, height: float, skin: str, coat: str, accent: str) -> str:
    """Simple human silhouette: head + shoulders + body. No facial detail."""
    h = height
    head_r = h * 0.085
    head_cy = y
    body_top = y + head_r + 6
    body_bot = y + h
    shoulder_w = h * 0.32
    return f"""  <g>
    <circle cx="{x}" cy="{head_cy}" r="{head_r}" fill="{skin}"/>
    <path d="M {x - shoulder_w/2} {body_top}
             Q {x - shoulder_w/2 - 10} {body_top + h*0.18} {x - shoulder_w*0.7} {body_top + h*0.35}
             L {x - shoulder_w*0.7} {body_bot}
             L {x + shoulder_w*0.7} {body_bot}
             L {x + shoulder_w*0.7} {body_top + h*0.35}
             Q {x + shoulder_w/2 + 10} {body_top + h*0.18} {x + shoulder_w/2} {body_top}
             Z"
          fill="{coat}"/>
    <path d="M {x - shoulder_w*0.18} {body_top + h*0.05}
             L {x + shoulder_w*0.18} {body_top + h*0.05}
             L {x + shoulder_w*0.10} {body_top + h*0.20}
             L {x - shoulder_w*0.10} {body_top + h*0.20} Z"
          fill="{accent}"/>
  </g>
"""


def capsule_device(x: float, y: float, w: float = 220, h: float = 80) -> str:
    """Magnetic capsule endoscope product shape: rounded cylinder."""
    rx = h / 2
    return f"""  <g>
    <rect x="{x - w/2}" y="{y - h/2}" width="{w}" height="{h}" rx="{rx}" ry="{rx}"
          fill="{PALETTE['mist']}" stroke="{PALETTE['slate']}" stroke-width="0.5"/>
    <rect x="{x - w/2 + 8}" y="{y - h/2 + 8}" width="{w*0.45}" height="{h - 16}" rx="{(h-16)/2}"
          fill="{PALETTE['blue']}" opacity="0.85"/>
    <circle cx="{x + w/2 - 20}" cy="{y}" r="6" fill="{PALETTE['red']}"/>
  </g>
"""


def mri_gantry(cx: float, cy: float, scale: float = 1.0) -> str:
    """Stylized MRI gantry ring (bore view)."""
    s = scale
    R_outer = 220 * s
    R_inner = 130 * s
    return f"""  <g>
    <circle cx="{cx}" cy="{cy}" r="{R_outer}" fill="{PALETTE['mist']}" stroke="{PALETTE['slate']}" stroke-width="1"/>
    <circle cx="{cx}" cy="{cy}" r="{R_inner}" fill="{PALETTE['cool']}" stroke="{PALETTE['blue']}" stroke-width="6"/>
    <circle cx="{cx}" cy="{cy}" r="{R_inner - 12}" fill="{PALETTE['navy']}"/>
    <circle cx="{cx}" cy="{cy}" r="{R_inner - 60}" fill="none" stroke="{PALETTE['cyan']}" stroke-width="2" opacity="0.6"/>
  </g>
"""


# Per-section generators ---------------------------------------------------

def gen_01_hero(variant: str) -> str:
    bg = "bg-warm"
    if variant == "B":
        bg = "bg-cool"
    if variant == "C":
        bg = "bg-warm"
    parts = [svg_open(), svg_defs(), f'  <rect width="{W}" height="{H}" fill="url(#{bg})"/>']
    parts.append(f'  <rect width="{W}" height="{H}" fill="url(#vignette)"/>')

    if variant == "A":  # central-asian
        parts.append(figure_silhouette(560, 560, 360, "#C8954A", PALETTE['warm'], PALETTE['gold']))
        parts.append(capsule_device(1500, 600, 240, 90))
        parts.append(silk_road_route())
    elif variant == "B":  # east-asian
        parts.append(figure_silhouette(560, 560, 360, "#D4B585", PALETTE['warm'], PALETTE['blue']))
        parts.append(mri_gantry(1480, 600, 0.85))
    else:  # scene
        # Empty consultation room: wood desk + arch window
        parts.append(f"""  <g>
    <rect x="240" y="640" width="540" height="280" fill="{PALETTE['brown']}" rx="8"/>
    <rect x="1080" y="120" width="600" height="780" fill="{PALETTE['warm']}" stroke="{PALETTE['gold']}" stroke-width="2" rx="280" ry="280"/>
    <line x1="1380" y1="120" x2="1380" y2="900" stroke="{PALETTE['gold']}" stroke-width="1.5"/>
    <line x1="1080" y1="510" x2="1680" y2="510" stroke="{PALETTE['gold']}" stroke-width="1.5"/>
    <rect x="320" y="640" width="120" height="180" fill="{PALETTE['cool']}" rx="4"/>
    <rect x="460" y="660" width="80" height="60" fill="{PALETTE['blue']}" rx="6"/>
  </g>""")

    parts.append(text_label("Hero", variant))
    parts.append(svg_close())
    return "".join(parts)


def gen_02_science(variant: str) -> str:
    bg = "bg-warm" if variant != "B" else "bg-cool"
    parts = [svg_open(), svg_defs(), f'  <rect width="{W}" height="{H}" fill="url(#{bg})"/>']
    parts.append(f'  <rect width="{W}" height="{H}" fill="url(#vignette)"/>')

    # Books on a table
    base_y = 820
    parts.append(f'  <rect x="0" y="{base_y}" width="{W}" height="{H - base_y}" fill="{PALETTE["brown"]}" opacity="0.85"/>')
    # Open book
    parts.append(f"""  <g>
    <path d="M 760 {base_y - 40} L 1160 {base_y - 40} L 1180 {base_y + 200} L 740 {base_y + 200} Z" fill="{PALETTE['cool']}" stroke="{PALETTE['slate']}" stroke-width="1"/>
    <line x1="960" y1="{base_y - 40}" x2="960" y2="{base_y + 200}" stroke="{PALETTE['slate']}" stroke-width="0.5" opacity="0.4"/>
    <line x1="800" y1="{base_y - 10}" x2="920" y2="{base_y - 10}" stroke="{PALETTE['slate']}" stroke-width="0.5" opacity="0.3"/>
    <line x1="800" y1="{base_y + 10}" x2="920" y2="{base_y + 10}" stroke="{PALETTE['slate']}" stroke-width="0.5" opacity="0.3"/>
    <line x1="800" y1="{base_y + 30}" x2="920" y2="{base_y + 30}" stroke="{PALETTE['slate']}" stroke-width="0.5" opacity="0.3"/>
    <line x1="1000" y1="{base_y - 10}" x2="1120" y2="{base_y - 10}" stroke="{PALETTE['slate']}" stroke-width="0.5" opacity="0.3"/>
    <line x1="1000" y1="{base_y + 10}" x2="1120" y2="{base_y + 10}" stroke="{PALETTE['slate']}" stroke-width="0.5" opacity="0.3"/>
  </g>""")

    # Closed book + tablet
    parts.append(f"""  <g>
    <rect x="380" y="{base_y - 120}" width="220" height="320" fill="{PALETTE['gold']}" stroke="{PALETTE['brown']}" stroke-width="1.5"/>
    <rect x="400" y="{base_y - 100}" width="180" height="280" fill="{PALETTE['brown']}" opacity="0.4"/>
    <rect x="1320" y="{base_y - 60}" width="280" height="180" fill="{PALETTE['navy']}" rx="8"/>
    <rect x="1336" y="{base_y - 48}" width="248" height="156" fill="{PALETTE['blue']}" opacity="0.65" rx="4"/>
  </g>""")

    # Mug
    parts.append(f"""  <g>
    <ellipse cx="1700" cy="{base_y - 30}" rx="60" ry="14" fill="{PALETTE['warm']}" stroke="{PALETTE['slate']}" stroke-width="1"/>
    <path d="M 1640 {base_y - 30} L 1660 {base_y + 120} L 1740 {base_y + 120} L 1760 {base_y - 30} Z" fill="{PALETTE['warm']}" stroke="{PALETTE['slate']}" stroke-width="1"/>
    <ellipse cx="1700" cy="{base_y - 30}" rx="46" ry="8" fill="{PALETTE['dawn']}"/>
  </g>""")

    if variant == "A":  # central-asian
        parts.append(figure_silhouette(1700, 380, 320, "#C8954A", PALETTE['warm'], PALETTE['gold']))
    elif variant == "B":  # east-asian
        parts.append(figure_silhouette(1700, 380, 320, "#D4B585", PALETTE['warm'], PALETTE['blue']))

    parts.append(text_label("Patient Library", variant))
    parts.append(svg_close())
    return "".join(parts)


def gen_03_flagship(variant: str) -> str:
    parts = [svg_open(), svg_defs(), f'  <rect width="{W}" height="{H}" fill="{PALETTE["warm"]}"/>']
    parts.append(f'  <rect width="{W}" height="{H}" fill="url(#vignette)"/>')

    # Three panels: capsule | figure | MRI gantry
    parts.append(capsule_device(420, 540, 280, 110))
    parts.append(mri_gantry(1500, 540, 0.95))
    if variant == "A":
        parts.append(figure_silhouette(960, 380, 320, "#C8954A", PALETTE['warm'], PALETTE['gold']))
    elif variant == "B":
        parts.append(figure_silhouette(960, 380, 320, "#D4B585", PALETTE['warm'], PALETTE['blue']))
    # Silk road route between
    parts.append(silk_road_route())

    parts.append(text_label("Flagship Module", variant))
    parts.append(svg_close())
    return "".join(parts)


def gen_04_capsule(variant: str) -> str:
    bg = "bg-warm"
    parts = [svg_open(), svg_defs(), f'  <rect width="{W}" height="{H}" fill="url(#{bg})"/>']
    parts.append(f'  <rect width="{W}" height="{H}" fill="url(#vignette)"/>')

    # Macro: capsule on a clean tray
    parts.append(f"""  <g>
    <ellipse cx="960" cy="640" rx="340" ry="60" fill="{PALETTE['mist']}" opacity="0.6"/>
    <rect x="620" y="620" width="680" height="50" fill="{PALETTE['cool']}" rx="4" stroke="{PALETTE['slate']}" stroke-width="0.5" opacity="0.7"/>
  </g>""")
    parts.append(capsule_device(960, 600, 380, 130))

    # Camel-thorn branches in upper-right (small visual accent)
    parts.append(f"""  <g opacity="0.7" stroke="{PALETTE['brown']}" stroke-width="2" fill="none" stroke-linecap="round">
    <path d="M 1480 280 Q 1560 200 1620 320"/>
    <path d="M 1500 240 Q 1560 180 1640 240"/>
    <path d="M 1520 200 Q 1580 140 1680 180"/>
    <circle cx="1620" cy="320" r="3" fill="{PALETTE['brown']}"/>
    <circle cx="1640" cy="240" r="3" fill="{PALETTE['brown']}"/>
    <circle cx="1680" cy="180" r="3" fill="{PALETTE['brown']}"/>
  </g>""")

    if variant == "A":
        parts.append(figure_silhouette(360, 540, 360, "#C8954A", PALETTE['warm'], PALETTE['gold']))
    elif variant == "B":
        parts.append(figure_silhouette(360, 540, 360, "#D4B585", PALETTE['warm'], PALETTE['blue']))

    parts.append(text_label("Capsule Endoscopy", variant))
    parts.append(svg_close())
    return "".join(parts)


def gen_05_cardiac(variant: str) -> str:
    parts = [svg_open(), svg_defs(), f'  <rect width="{W}" height="{H}" fill="url(#bg-cool)"/>']
    parts.append(f'  <rect width="{W}" height="{H}" fill="url(#bg-navy)" opacity="0.85"/>')
    parts.append(f'  <rect width="{W}" height="{H}" fill="url(#vignette)"/>')

    # MRI gantry right-two-thirds
    parts.append(mri_gantry(1300, 540, 1.4))

    # ECG waveform in background (left third)
    parts.append(f"""  <g opacity="0.4" fill="none" stroke="{PALETTE['cyan']}" stroke-width="2">
    <path d="M 0 540 L 100 540 L 110 540 L 120 480 L 140 600 L 160 480 L 180 540 L 540 540"/>
  </g>""")

    if variant == "A":
        parts.append(figure_silhouette(280, 540, 360, "#C8954A", PALETTE['mist'], PALETTE['gold']))
    elif variant == "B":
        parts.append(figure_silhouette(280, 540, 360, "#D4B585", PALETTE['mist'], PALETTE['blue']))

    parts.append(text_label("Cardiac MR", variant))
    parts.append(svg_close())
    return "".join(parts)


def gen_06_central_asia(variant: str) -> str:
    parts = [svg_open(), svg_defs(), f'  <rect width="{W}" height="{H}" fill="url(#bg-warm)"/>']
    parts.append(f'  <rect width="{W}" height="{H}" fill="url(#vignette)"/>')

    # Doorway arch center
    parts.append(f"""  <g>
    <path d="M 760 940 L 760 540 Q 760 320 960 320 Q 1160 320 1160 540 L 1160 940 Z"
          fill="{PALETTE['warm']}" stroke="{PALETTE['brown']}" stroke-width="3"/>
    <rect x="760" y="540" width="400" height="400" fill="{PALETTE['dawn']}" opacity="0.5"/>
  </g>""")

    # Wall map line drawing
    parts.append(f"""  <g opacity="0.4" fill="none" stroke="{PALETTE['gold']}" stroke-width="1">
    <path d="M 200 240 Q 400 180 600 260 T 1100 220 T 1700 280"/>
    <circle cx="200" cy="240" r="3" fill="{PALETTE['red']}"/>
    <circle cx="600" cy="260" r="3" fill="{PALETTE['red']}"/>
    <circle cx="1100" cy="220" r="3" fill="{PALETTE['red']}"/>
    <circle cx="1700" cy="280" r="3" fill="{PALETTE['red']}"/>
  </g>""")

    if variant == "A":
        parts.append(figure_silhouette(620, 480, 360, "#C8954A", PALETTE['warm'], PALETTE['brown']))
        parts.append(figure_silhouette(1300, 480, 360, "#D4B585", PALETTE['warm'], PALETTE['gold']))
    elif variant == "B":
        parts.append(figure_silhouette(620, 480, 360, "#D4B585", PALETTE['warm'], PALETTE['brown']))
        parts.append(figure_silhouette(1300, 480, 360, "#C8954A", PALETTE['warm'], PALETTE['gold']))
    else:
        # scene variant: table with tea cups
        parts.append(f"""  <g>
    <rect x="220" y="800" width="380" height="180" fill="{PALETTE['brown']}" rx="4"/>
    <rect x="300" y="760" width="60" height="50" fill="{PALETTE['warm']}" stroke="{PALETTE['slate']}" stroke-width="0.5"/>
    <ellipse cx="330" cy="760" rx="28" ry="6" fill="{PALETTE['dawn']}"/>
    <rect x="380" y="760" width="60" height="50" fill="{PALETTE['warm']}" stroke="{PALETTE['slate']}" stroke-width="0.5"/>
    <ellipse cx="410" cy="760" rx="28" ry="6" fill="{PALETTE['dawn']}"/>
    <rect x="460" y="760" width="60" height="50" fill="{PALETTE['warm']}" stroke="{PALETTE['slate']}" stroke-width="0.5"/>
    <ellipse cx="490" cy="760" rx="28" ry="6" fill="{PALETTE['dawn']}"/>
  </g>""")
        # Camel silhouette at bottom-right
        parts.append(f"""  <g fill="{PALETTE['brown']}" opacity="0.85">
    <ellipse cx="1500" cy="900" rx="120" ry="40"/>
    <rect x="1430" y="860" width="20" height="50"/>
    <rect x="1480" y="860" width="20" height="50"/>
    <rect x="1530" y="860" width="20" height="50"/>
    <rect x="1580" y="860" width="20" height="50"/>
    <ellipse cx="1380" cy="870" rx="50" ry="30"/>
    <rect x="1370" y="900" width="8" height="40"/>
    <rect x="1410" y="900" width="8" height="40"/>
  </g>""")

    parts.append(text_label("Xinjiang & Central Asia", variant))
    parts.append(svg_close())
    return "".join(parts)


def gen_07_cta(variant: str) -> str:
    parts = [svg_open(), svg_defs(), f'  <rect width="{W}" height="{H}" fill="url(#bg-warm)"/>']
    parts.append(f'  <rect width="{W}" height="{H}" fill="url(#vignette)"/>')

    # Desk surface lower half
    parts.append(f'  <rect x="0" y="780" width="{W}" height="{H-780}" fill="{PALETTE["brown"]}" opacity="0.85"/>')

    # Notebook center
    parts.append(f"""  <g>
    <rect x="780" y="700" width="500" height="220" fill="{PALETTE['cool']}" stroke="{PALETTE['slate']}" stroke-width="1" rx="4" transform="rotate(-4 1030 810)"/>
    <line x1="820" y1="730" x2="1240" y2="730" stroke="{PALETTE['slate']}" stroke-width="0.5" opacity="0.4"/>
    <line x1="820" y1="760" x2="1240" y2="760" stroke="{PALETTE['slate']}" stroke-width="0.5" opacity="0.4"/>
    <line x1="820" y1="790" x2="1180" y2="790" stroke="{PALETTE['slate']}" stroke-width="0.5" opacity="0.4"/>
    <line x1="820" y1="820" x2="1220" y2="820" stroke="{PALETTE['slate']}" stroke-width="0.5" opacity="0.4"/>
  </g>""")

    # Mug right
    parts.append(f"""  <g>
    <path d="M 1480 720 L 1500 880 L 1600 880 L 1620 720 Z" fill="{PALETTE['warm']}" stroke="{PALETTE['slate']}" stroke-width="1"/>
    <ellipse cx="1550" cy="720" rx="60" ry="12" fill="{PALETTE['dawn']}"/>
  </g>""")

    # Succulent left
    parts.append(f"""  <g>
    <ellipse cx="380" cy="860" rx="80" ry="20" fill="{PALETTE['brown']}"/>
    <path d="M 380 860 Q 340 800 360 760 Q 380 740 400 760 Q 420 800 380 860 Z" fill="{PALETTE['dawn']}"/>
    <path d="M 380 860 Q 350 820 370 780" fill="none" stroke="{PALETTE['brown']}" stroke-width="1"/>
  </g>""")

    # Wall textile hanging
    parts.append(f"""  <g opacity="0.7">
    <rect x="160" y="180" width="180" height="240" fill="{PALETTE['gold']}" stroke="{PALETTE['brown']}" stroke-width="2"/>
    {silk_road_geometric_pattern(250, 300, 0.5)}
  </g>""")

    if variant == "A":
        parts.append(figure_silhouette(1300, 380, 360, "#C8954A", PALETTE['gold'], PALETTE['brown']))
    elif variant == "B":
        parts.append(figure_silhouette(1300, 380, 360, "#D4B585", PALETTE['slate'], PALETTE['brown']))

    parts.append(text_label("CTA Banner", variant))
    parts.append(svg_close())
    return "".join(parts)


def gen_08_footer(variant: str) -> str:
    parts = [svg_open(), svg_defs(), f'  <rect width="{W}" height="{H}" fill="{PALETTE["warm"]}"/>']

    # Long Silk Road route across
    parts.append(f"""  <g opacity="0.7" fill="none" stroke="{PALETTE['gold']}" stroke-width="2" stroke-linecap="round">
    <path d="M 60 540 Q 360 460 660 540 T 1260 500 T 1860 560"/>
    <circle cx="60" cy="540" r="6" fill="{PALETTE['red']}"/>
    <circle cx="660" cy="540" r="5" fill="{PALETTE['gold']}"/>
    <circle cx="1260" cy="500" r="5" fill="{PALETTE['gold']}"/>
    <circle cx="1860" cy="560" r="6" fill="{PALETTE['red']}"/>
  </g>""")

    # Medical cross brand mark upper-right
    parts.append(f"""  <g transform="translate(1820, 120)">
    <rect x="-30" y="-10" width="60" height="20" fill="{PALETTE['blue']}"/>
    <rect x="-10" y="-30" width="20" height="60" fill="{PALETTE['blue']}"/>
    <circle r="38" fill="none" stroke="{PALETTE['blue']}" stroke-width="1" opacity="0.4"/>
  </g>""")

    # Figure or pattern on left
    if variant == "A":
        parts.append(figure_silhouette(220, 380, 320, "#8B5A3C", PALETTE['brown'], PALETTE['gold']))
    elif variant == "B":
        parts.append(figure_silhouette(220, 380, 320, "#8B5A3C", PALETTE['brown'], PALETTE['blue']))
    else:
        parts.append(silk_road_geometric_pattern(220, 540, 1.0))

    parts.append(text_label("Footer Decoration", variant))
    parts.append(svg_close())
    return "".join(parts)


GENERATORS = {
    "01-hero":         gen_01_hero,
    "02-science":      gen_02_science,
    "03-flagship":     gen_03_flagship,
    "04-capsule":      gen_04_capsule,
    "05-cardiac":      gen_05_cardiac,
    "06-central-asia": gen_06_central_asia,
    "07-cta":          gen_07_cta,
    "08-footer":       gen_08_footer,
}


def main():
    parser = argparse.ArgumentParser(description="Generate 24 SVG placeholders")
    parser.add_argument("--out", default="../shared/img/svg", help="output dir")
    args = parser.parse_args()

    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    count = 0
    for slug, _label_en, _label_zh, _comp in SECTIONS:
        for letter, vlabel in VARIANTS:
            gen = GENERATORS[slug]
            svg = gen(letter)
            fpath = out_dir / f"{slug}-{letter}-{vlabel}.svg"
            fpath.write_text(svg, encoding="utf-8")
            count += 1
            print(f"[OK] {fpath.name}")
    print(f"\nGenerated {count} SVG placeholders in {out_dir}")


if __name__ == "__main__":
    main()