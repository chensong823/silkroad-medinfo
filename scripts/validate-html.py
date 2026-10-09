#!/usr/bin/env python3
"""validate-html.py — Silk Road Medinfo v2 HTML sanity checks.

Runs:
  1. HTML parser check (every page must parse without error)
  2. Link integrity scan (no orphan links to non-existent files)
  3. i18n key parity (every data-i18n key in HTML must exist in all locales)
  4. em-dash ban (em-dash — must not appear in copy)
  5. Required meta tags present
  6. Each language version must have proper lang attr

Usage:
  python scripts/validate-html.py
"""

from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES_REL = [
    "index.html",
    "projects/capsule-endoscopy.html",
    "projects/cardiac-mrca.html",
    "science/index.html",
    "services/index.html",
    "central-asia/index.html",
    "404.html",
    "500.html",
]

EM_DASH = "—"
ANY_EM = re.compile(r"[—–―]")  # em/en/horizontal-bar


def collect_pages(root: Path):
    pages = []
    for rel in PAGES_REL:
        for lang_dir in ["", "en", "ru"]:
            base = root / lang_dir if lang_dir else root
            path = base / rel
            if path.exists():
                pages.append(path)
    return pages


def check_html_parses(path: Path):
    """Lightweight HTML structural check via tag-balance + required attrs."""
    text = path.read_text(encoding="utf-8")
    errors = []

    # Required root tags
    if "<html" not in text:
        errors.append("missing <html>")
    if "<head" not in text:
        errors.append("missing <head>")
    if "<body" not in text:
        errors.append("missing <body>")
    if "</html>" not in text:
        errors.append("missing </html>")

    # Required head meta
    for required in ['charset="UTF-8"', 'viewport', 'theme-color']:
        if required not in text:
            errors.append(f"missing head meta: {required}")

    # Tag balance check (simple)
    open_tags = re.findall(r"<([a-zA-Z][\w-]*)\b[^>]*?(?<!/)>", text)
    close_tags = re.findall(r"</([a-zA-Z][\w-]*)>", text)
    self_closing = {"meta", "link", "img", "br", "hr", "input", "source"}
    open_count = {}
    for t in open_tags:
        if t.lower() not in self_closing:
            open_count[t.lower()] = open_count.get(t.lower(), 0) + 1
    close_count = {}
    for t in close_tags:
        close_count[t.lower()] = close_count.get(t.lower(), 0) + 1
    for tag, oc in open_count.items():
        cc = close_count.get(tag, 0)
        if oc != cc:
            errors.append(f"unbalanced <{tag}>: open={oc} close={cc}")

    return errors


def check_em_dash(path: Path):
    text = path.read_text(encoding="utf-8")
    found = list(ANY_EM.finditer(text))
    return [(m.start(), text[max(0, m.start()-20):m.end()+20]) for m in found]


def check_meta_lang(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.search(r'<html\s+lang="([^"]+)"', text)
    if not m:
        return "missing <html lang>"
    lang = m.group(1)
    expected_map = {"": "zh-CN", "en": "en", "ru": "ru"}
    rel_dir = path.relative_to(ROOT).parts[0] if path.relative_to(ROOT).parts[0] in ["en", "ru"] else ""
    expected = expected_map.get(rel_dir, "zh-CN")
    if lang != expected:
        return f"lang mismatch: expected {expected}, got {lang}"
    return None


def check_required_assets(path: Path):
    """Verify each href and src resolves to an existing file (for relative URLs)."""
    text = path.read_text(encoding="utf-8")
    errors = []
    urls = re.findall(r'(?:href|src)="([^"#]+)"', text)
    for url in urls:
        if url.startswith(("http://", "https://", "//", "mailto:", "tel:", "data:")):
            continue
        if url.startswith("#"):
            continue
        if url.startswith("/") and not url.startswith("//"):
            # Absolute path; skip — they reference domain root, not file system
            continue
        target = path.parent / url
        try:
            target_resolved = target.resolve()
        except (OSError, RuntimeError):
            errors.append(f"unresolvable path: {url}")
            continue
        try:
            target_resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"path escapes project root: {url}")
            continue
        if not target_resolved.exists():
            errors.append(f"missing asset: {url}")
    return errors


def check_i18n_keys(path: Path):
    """Every data-i18n= in HTML must have a corresponding key in the appropriate locale JSON."""
    text = path.read_text(encoding="utf-8")
    keys_used = set(re.findall(r'data-i18n="([^"]+)"', text))
    if not keys_used:
        return []

    rel_dir = path.relative_to(ROOT).parts[0] if path.relative_to(ROOT).parts[0] in ["en", "ru"] else ""
    locale_map = {"": "zh-CN", "en": "en", "ru": "ru"}
    locale = locale_map.get(rel_dir, "zh-CN")
    locale_dir = ROOT / "locales" / locale
    if not locale_dir.is_dir():
        return [f"locale dir missing: {locale}"]

    flat = set()
    for ns_file in locale_dir.glob("*.json"):
        try:
            data = json.loads(ns_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return [f"unparsable JSON: {ns_file.name}"]
        ns_name = ns_file.stem
        def walk(obj, prefix=""):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    walk(v, f"{prefix}.{k}" if prefix else k)
            elif isinstance(obj, list):
                flat.add(prefix)
            else:
                flat.add(prefix)
        walk(data)
        # Now add namespace prefix to all flat entries
        # We need to remember what was added in this iteration
        ns_keys = set()
        def walk2(obj, prefix=""):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    walk2(v, f"{prefix}.{k}" if prefix else k)
            elif isinstance(obj, list):
                ns_keys.add(prefix)
            else:
                ns_keys.add(prefix)
        walk2(data)
        for k in ns_keys:
            flat.add(f"{ns_name}.{k}")

    missing = []
    for k in keys_used:
        if "[" in k:
            root_key = re.sub(r"\[[^\]]+\]", "", k)
            if root_key not in flat and not any(k2.startswith(root_key + ".") for k2 in flat):
                missing.append(k)
            continue
        if k not in flat and not any(k2.startswith(k + ".") for k2 in flat):
            missing.append(k)
    return missing


def main():
    print("=" * 64)
    print("validate-html.py · Silk Road Medinfo v2")
    print("=" * 64)

    pages = collect_pages(ROOT)
    print(f"Found {len(pages)} pages\n")

    all_passed = True
    summary = {"HTML parse": [], "em-dash": [], "lang attr": [], "asset integrity": [], "i18n keys": []}

    for path in sorted(pages):
        rel = path.relative_to(ROOT)
        parse_errors = check_html_parses(path)
        em_hits = check_em_dash(path)
        lang_err = check_meta_lang(path)
        asset_errs = check_required_assets(path)
        i18n_missing = check_i18n_keys(path)

        ok = not (parse_errors or em_hits or lang_err or asset_errs or i18n_missing)
        status = "[OK]" if ok else "[FAIL]"
        if not ok:
            all_passed = False

        print(f"{status} {rel}")
        for e in parse_errors:
            print(f"    PARSE: {e}")
        for i, ctx in em_hits:
            print(f"    EM-DASH at offset {i}: {ctx!r}")
        if lang_err:
            print(f"    LANG: {lang_err}")
        for e in asset_errs:
            print(f"    ASSET: {e}")
        for k in i18n_missing:
            print(f"    I18N: missing key '{k}'")

        summary["HTML parse"].extend(parse_errors)
        summary["em-dash"].extend(em_hits)
        summary["lang attr"].extend(lang_err or [])
        summary["asset integrity"].extend(asset_errs)
        summary["i18n keys"].extend(i18n_missing)

    print("\n" + "=" * 64)
    print("SUMMARY")
    print("=" * 64)
    for cat, items in summary.items():
        n = len(items)
        marker = "OK" if n == 0 else "FAIL"
        print(f"  [{marker}] {cat}: {n} issues")

    print()
    if all_passed:
        print("RESULT: ALL CHECKS PASSED")
        return 0
    print("RESULT: ISSUES FOUND - see above")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())