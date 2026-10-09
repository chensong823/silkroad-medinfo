#!/usr/bin/env python3
"""fix-broken-paths.py — clean up malformed relative paths from mirror generation."""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def fix(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    new = text
    # Collapse ".././" -> "./"
    new = re.sub(r"\.\./\./", r"./", new)
    # Collapse "/./" -> "/"
    new = re.sub(r"/\./", r"/", new)
    # Collapse "././" -> "./"
    new = re.sub(r"(?:\./){2,}/", r"./", new)
    if new != text:
        path.write_text(new, encoding="utf-8")
        return 1
    return 0


def main():
    total = 0
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT)
        if rel.parts[0] in {"scripts"}:
            continue
        if fix(p):
            print(f"[FIXED] {rel}")
            total += 1
    print(f"\nTotal: {total}")


if __name__ == "__main__":
    main()