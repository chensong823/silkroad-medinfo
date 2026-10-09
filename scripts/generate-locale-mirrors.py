#!/usr/bin/env python3
"""Generate en/ and ru/ mirrors of zh-CN HTML pages.

Usage:
  python scripts/generate-locale-mirrors.py
"""

from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Map: (zh-CN source, [locale dir, lang attr])
PAGES = [
    ("index.html",                          "index.html"),
    ("projects/capsule-endoscopy.html",     "projects/capsule-endoscopy.html"),
    ("projects/cardiac-mrca.html",          "projects/cardiac-mrca.html"),
    ("science/index.html",                  "science/index.html"),
    ("services/index.html",                 "services/index.html"),
    ("central-asia/index.html",             "central-asia/index.html"),
]

LOCALES = {
    "en": {"lang": "en",  "og_locale": "en_US"},
    "ru": {"lang": "ru",  "og_locale": "ru_RU"},
}


def transform_html(html: str, lang: str, og_locale: str) -> str:
    """Transform a zh-CN page into en/ or ru/ by:
    1. Setting <html lang="...">
    2. Updating og:locale
    3. Reversing path-relative links (../ → ../../)
    4. Reversing asset paths (../shared/ → ../../shared/)
    5. Updating canonical and hreflang to point to /en/ or /ru/ mirror
    """
    # 1. <html lang="zh-CN"> → <html lang="en">
    html = re.sub(r'<html lang="[^"]+"', f'<html lang="{lang}"', html, count=1)

    # 2. og:locale meta
    html = re.sub(r'(<meta property="og:locale" content=")zh_CN"', rf'\1{og_locale}"', html)

    # 3. canonical href
    html = re.sub(
        r'<link rel="canonical" href="https://silkroad-medinfo\.com/([^"]*)"',
        rf'<link rel="canonical" href="https://silkroad-medinfo.com/{lang}/\1"',
        html
    )

    # 4. hreflang alternates (zh-CN stays pointing to /, en/ru point to /en/ and /ru/)
    def repl_hreflang(m):
        hreflang = m.group(1)
        target = m.group(2)
        if hreflang == "zh-CN":
            return m.group(0)
        if hreflang == lang:
            new = target
            if lang == "en":
                new = "/en" + target[2:] if target.startswith("/zh") else target
            elif lang == "ru":
                new = "/ru" + target[2:] if target.startswith("/zh") else target
            return f'<link rel="alternate" hreflang="{hreflang}" href="https://silkroad-medinfo.com{new}"'
        return m.group(0)
    html = re.sub(
        r'<link rel="alternate" hreflang="([^"]+)" href="(https://[^"]+)"',
        repl_hreflang,
        html
    )

    # 5. Reverse path-relative URLs: "../shared/" → "../../shared/", "../foo" → "../../foo" etc.
    # Be careful: only inside href/src attributes, and not inside the hreflang URLs (already correct)

    def shift_relative(match):
        full = match.group(0)
        attr = match.group(1)
        url = match.group(2)
        # Skip absolute and protocol-relative
        if url.startswith(("http://", "https://", "//", "mailto:", "tel:", "data:")):
            return full
        # Skip anchor-only
        if url.startswith("#"):
            return full
        # If starts with ../ it's a parent path
        if url.startswith("../"):
            url = "../" + url
        else:
            url = "../" + url
        return f'{attr}="{url}"'

    html = re.sub(r'(href|src)="([^"]+)"', shift_relative, html)

    return html


def main():
    for src_rel, _ in PAGES:
        src = ROOT / src_rel
        if not src.exists():
            print(f"SKIP {src_rel} (not found)")
            continue
        text = src.read_text(encoding="utf-8")
        for locale, meta in LOCALES.items():
            out_dir = ROOT / locale
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / src_rel
            out_path.parent.mkdir(parents=True, exist_ok=True)
            transformed = transform_html(text, meta["lang"], meta["og_locale"])
            out_path.write_text(transformed, encoding="utf-8")
            print(f"[OK] {out_path.relative_to(ROOT)}")

    # 404 / 500 mirrors
    for src_rel in ["404.html", "500.html"]:
        src = ROOT / src_rel
        if not src.exists():
            continue
        text = src.read_text(encoding="utf-8")
        for locale, meta in LOCALES.items():
            out_dir = ROOT / locale
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / src_rel
            transformed = transform_html(text, meta["lang"], meta["og_locale"])
            out_path.write_text(transformed, encoding="utf-8")
            print(f"[OK] {out_path.relative_to(ROOT)}")

    # Also copy 404/500 to en/ru
    print("\nDone.")


if __name__ == "__main__":
    main()