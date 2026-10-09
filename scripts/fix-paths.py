#!/usr/bin/env python3
"""fix-paths.py v2 — depth-aware path fixer.

Compute the depth of each HTML file under ROOT, then normalize all
shared/ and locales/ paths to the correct number of ../ segments.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def depth_of(path: Path) -> int:
    rel = path.relative_to(ROOT)
    return len(rel.parts) - 1  # number of dirs above the file


def ups_for(depth: int) -> str:
    return "../" * depth


def fix_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    depth = depth_of(path)
    target = ups_for(depth)
    replacements = 0

    def replace_url(attr, old_url):
        nonlocal replacements
        # Strip all leading ../
        stripped = re.sub(r"^(?:\.\./)+", "", old_url)
        # If after stripping it starts with shared/ or locales/, normalize it
        if stripped.startswith(("shared/", "locales/")):
            new_url = target + stripped
            if new_url != old_url:
                replacements += 1
            return f'{attr}="{new_url}"', True
        return f'{attr}="{old_url}"', False

    def re_replace(match):
        attr = match.group(1)
        url = match.group(2)
        new, _ = replace_url(attr, url)
        return new

    new = re.sub(r'(href|src)="([^"]+)"', re_replace, text)

    if new != text:
        path.write_text(new, encoding="utf-8")
    return replacements


def main():
    total = 0
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT)
        if rel.parts[0] in {"scripts"}:
            continue
        n = fix_file(p)
        if n:
            print(f"[FIXED {n}] {rel}")
            total += n
    print(f"\nTotal fixes: {total}")


if __name__ == "__main__":
    main()