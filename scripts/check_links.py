#!/usr/bin/env python3
"""
Check internal markdown links across the Product Leadership Academy repository.

Scans all .md files, extracts relative links, verifies target files exist.
Reports broken links with file path and line number.

Usage:
    python scripts/check_links.py
    python scripts/check_links.py --verbose
"""

import re
import sys
from pathlib import Path


ACADEMY_ROOT = Path(__file__).resolve().parent.parent
LINK_PATTERN = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')


def check_links(verbose=False):
    md_files = sorted(ACADEMY_ROOT.rglob("*.md"))
    checked = 0
    broken = 0
    skipped_external = 0

    for md_file in md_files:
        if ".git" in md_file.parts or "__pycache__" in md_file.parts:
            continue

        try:
            lines = md_file.read_text(encoding="utf-8", errors="ignore").splitlines()
        except Exception:
            print(f"  [WARN] Could not read: {md_file.relative_to(ACADEMY_ROOT)}")
            continue

        for line_num, line in enumerate(lines, 1):
            for match in LINK_PATTERN.finditer(line):
                link_text = match.group(1)
                target = match.group(2)

                if target.startswith(("http://", "https://", "mailto:")):
                    skipped_external += 1
                    if verbose:
                        print(f"  [SKIP] External: {target}")
                    continue

                if target.startswith("#"):
                    skipped_external += 1
                    continue

                if target.startswith("/"):
                    print(f"  [WARN] Absolute path skipped: {target} in {md_file.relative_to(ACADEMY_ROOT)}:{line_num}")
                    skipped_external += 1
                    continue

                checked += 1
                anchor = None
                clean_target = target
                if "#" in clean_target:
                    clean_target, anchor = clean_target.split("#", 1)

                target_path = (md_file.parent / clean_target).resolve()

                if not target_path.exists():
                    broken += 1
                    rel_file = md_file.relative_to(ACADEMY_ROOT)
                    print(f"  [BROKEN] {rel_file}:{line_num} -> {target}")
                    if verbose and anchor:
                        print(f"           anchor: #{anchor}")
                elif verbose:
                    rel_file = md_file.relative_to(ACADEMY_ROOT)
                    print(f"  [OK]    {rel_file}:{line_num} -> {target}")

    return checked, broken, skipped_external


def main():
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    print(f"Checking internal markdown links in: {ACADEMY_ROOT}")
    print()

    checked, broken, skipped = check_links(verbose=verbose)

    print()
    print("=" * 60)
    print(f"Results:")
    print(f"  Internal links checked:  {checked}")
    print(f"  External links skipped:  {skipped}")
    print(f"  Broken links found:      {broken}")

    if broken:
        print()
        print("RESULT: FAILURE — fix the broken links above.")
        sys.exit(1)
    else:
        print()
        print("RESULT: SUCCESS — all internal links resolve.")
        sys.exit(0)


if __name__ == "__main__":
    main()
