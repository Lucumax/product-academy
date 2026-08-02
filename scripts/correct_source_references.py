#!/usr/bin/env python3
"""
Correct Source References — repairs the blind prefix swap from
reconcile_source_ids.py.

The legacy doctrine files used an independent numbering scheme (SRC-BK-0001,
SRC-AR-0001, SRC-TK-0001). The registry uses SRC-BOOK-0001, SRC-POST-0001,
SRC-TALK-0001 with DIFFERENT numbers for most sources. The blind swap kept
legacy numbers, silently mislabeling many citations (e.g. legacy SRC-BK-0003
= Good Strategy Bad Strategy became SRC-BOOK-0003, which is actually The
Hard Thing About Hard Things in the registry).

This script re-maps every legacy-derived citation in the doctrine/handbook/
case files to the correct registry ID, using the authoritative crosswalk
documented in sources/registry.yaml.

Run with --execute to apply. Dry run by default.
"""

import re
import sys
from pathlib import Path

ACADEMY_ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Authoritative legacy -> registry crosswalk (from registry.yaml header).
# Current on-disk IDs are legacy numbers under a full-format prefix.
# ---------------------------------------------------------------------------
LEGACY_BOOK = {
    "0001": "SRC-BOOK-0001",  # Inspired (numbers coincide)
    "0002": "SRC-BOOK-0001",  # Inspired, same source, different aspect
    "0003": "SRC-BOOK-0015",  # Good Strategy Bad Strategy
    "0004": "SRC-BOOK-0004",  # Continuous Discovery (numbers coincide)
    "0005": "SRC-BOOK-0014",  # The Lean Startup
    "0006": "SRC-BOOK-0021",  # Zero to One
    "0007": "SRC-BOOK-0003",  # Hard Thing About Hard Things
    "0008": "SRC-BOOK-0022",  # Blitzscaling
    "0009": "SRC-BOOK-0023",  # PLG pricing research
    "0010": "SRC-BOOK-0024",  # Predictable Revenue
    "0011": "SRC-BOOK-0025",  # Platform Revolution
    "0012": "SRC-BOOK-0026",  # Getting Real
    "0013": "SRC-BOOK-0027",  # Accelerate (DORA)
    "0014": "SRC-BOOK-0028",  # Site Reliability Engineering
    "0015": "SRC-BOOK-0029",  # Trustworthy Online Experiments
    "0016": "SRC-BOOK-0030",  # Building Evolutionary Architectures
    "0017": "SRC-BOOK-0031",  # Architecture governance
    "0018": "SRC-BOOK-0032",  # Customer Success Economy
    "0019": "SRC-BOOK-0033",  # 37signals/Getting Real extended
    "0020": "SRC-BOOK-0034",  # Subscription Business Model
    "0021": "SRC-BOOK-0008",  # Escaping the Build Trap
    "0022": "SRC-BOOK-0035",  # No Rules Rules
    "0023": "SRC-BOOK-0036",  # Steve Jobs (Isaacson)
    "0024": "SRC-BOOK-0037",  # Becoming Steve Jobs
    "0025": "SRC-BOOK-0038",  # Hit Refresh
    "0026": "SRC-BOOK-0039",  # The Real Coke
    "0027": "SRC-BOOK-0040",  # Dogfight
}

LEGACY_TALK = {
    "0001": "SRC-TALK-0005",  # Brian Chesky, Airbnb re-centralization
}

# Legacy AR numbers that already coincide with a correct registry POST record.
LEGACY_POST_MATCH = {
    "0001": "SRC-POST-0001",  # Shreyas Doshi
}

# Legacy AR numbers that are case-specific sources. These were always
# catalogued outside the main registry (documented inline in the case
# catalog). Keep the SRC-POST-XXXX id (0031..0098) as-is so the
# cross-reference test can resolve them against the case-catalog section.
CASE_SPECIFIC_POST_RANGE = (31, 98)

TARGET_FILES = [
    "01_core_doctrine/PRINCIPLES.md",
    "01_core_doctrine/PROBLEM_SELECTION_MODULE.md",
    "07_cases/case_catalog.md",
    "handbook/PRODUCT_LEADERSHIP_BIBLE.md",
]


def correct_content(content):
    """Rewrite legacy-derived citations to correct registry IDs."""
    def fix_book(m):
        num = m.group(1)
        if num in LEGACY_BOOK:
            return LEGACY_BOOK[num]
        return m.group(0)

    def fix_talk(m):
        num = m.group(1)
        if num in LEGACY_TALK:
            return LEGACY_TALK[num]
        return m.group(0)

    content = re.sub(r"SRC-BOOK-(\d{4})", fix_book, content)
    content = re.sub(r"SRC-TALK-(\d{4})", fix_talk, content)
    return content


def scan():
    for fname in TARGET_FILES:
        fpath = ACADEMY_ROOT / fname
        if not fpath.exists():
            print(f"  MISSING: {fname}")
            continue
        content = fpath.read_text(encoding="utf-8")
        fixed = correct_content(content)
        if fixed != content:
            print(f"  CHANGED: {fname}")
        else:
            print(f"  OK:      {fname}")


def apply():
    for fname in TARGET_FILES:
        fpath = ACADEMY_ROOT / fname
        if not fpath.exists():
            continue
        content = fpath.read_text(encoding="utf-8")
        fixed = correct_content(content)
        if fixed != content:
            print(f"  WRITING: {fname}")
            fpath.write_text(fixed, encoding="utf-8")
        else:
            print(f"  OK:      {fname}")


def main():
    dry_run = "--execute" not in sys.argv
    print("=" * 70)
    print("SOURCE REFERENCE CORRECTION (legacy numbering -> registry)")
    print("=" * 70)
    if dry_run:
        print("\n--- DRY RUN ---")
        scan()
        print("\nRun with --execute to apply changes.")
    else:
        print("\n--- APPLYING ---")
        apply()


if __name__ == "__main__":
    main()
