#!/usr/bin/env python3
"""i18n parity check for Silk Road Medinfo v2.

Validates that every locale directory has the same set of keys
across zh-CN, en, and ru. Exits 0 on full parity, 1 on mismatch.

Usage:
  python scripts/i18n-parity.py --locales ../locales
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


PLURAL_SUFFIXES = ("_zero", "_one", "_two", "_few", "_many", "_other")


def flatten(obj, prefix=""):
    """Flatten a nested dict into { 'a.b.c': value } while preserving
    plural-variant suffixes as parent keys."""
    out = {}
    if isinstance(obj, dict):
        for key, value in obj.items():
            path = f"{prefix}.{key}" if prefix else key
            if isinstance(value, dict):
                # Check if this is a plural map
                if any(k.startswith("_") for k in value.keys()) and all(
                    isinstance(v, str) for v in value.values()
                ):
                    # plural map — record the parent key
                    out[path] = value
                else:
                    out.update(flatten(value, path))
            else:
                out[path] = value
    return out


def load_locale(path):
    with path.open(encoding="utf-8") as h:
        data = json.load(h)
    return flatten(data)


def has_plural_variant(key, keyset):
    return any(k.startswith(key + ".") for k in keyset)


def main():
    parser = argparse.ArgumentParser(description="i18n parity check across locales")
    parser.add_argument("--locales", default="locales", help="locales root")
    args = parser.parse_args()

    root = Path(args.locales).resolve()
    if not root.is_dir():
        print(f"ERROR: locales dir not found: {root}", file=sys.stderr)
        return 2

    locales = sorted([d for d in root.iterdir() if d.is_dir()])
    if len(locales) < 2:
        print(f"ERROR: need at least 2 locale dirs, found {len(locales)}", file=sys.stderr)
        return 2

    locale_keys = {}
    for loc in locales:
        all_keys = set()
        for ns_file in sorted(loc.glob("*.json")):
            data = load_locale(ns_file)
            all_keys.update(data.keys())
        locale_keys[loc.name] = all_keys

    # Compute parity
    all_keys = set().union(*locale_keys.values())
    parity_report = {}
    for name, keys in locale_keys.items():
        parity_report[name] = {
            "missing": sorted(all_keys - keys),
            "extra": sorted(keys - all_keys),
        }

    # Print
    print(f"Locales found: {list(locale_keys.keys())}")
    print(f"Total unique keys across all locales: {len(all_keys)}\n")

    any_mismatch = False
    for name, rep in parity_report.items():
        missing = rep["missing"]
        extra = rep["extra"]
        status = "[OK]" if not missing and not extra else "[MISMATCH]"
        print(f"{status} {name}: {len(locale_keys[name])} keys")
        if missing:
            any_mismatch = True
            print(f"    MISSING ({len(missing)}):")
            for k in missing[:30]:
                print(f"      - {k}")
            if len(missing) > 30:
                print(f"      ... and {len(missing) - 30} more")
        if extra:
            any_mismatch = True
            print(f"    EXTRA ({len(extra)}):")
            for k in extra[:30]:
                print(f"      - {k}")
            if len(extra) > 30:
                print(f"      ... and {len(extra) - 30} more")

    print()
    if any_mismatch:
        print("RESULT: parity mismatch -- see above")
        return 1
    print("RESULT: 100% key parity across all locales")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())