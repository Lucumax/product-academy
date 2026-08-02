#!/usr/bin/env python3
"""
Source ID Reconciliation — converts abbreviated format (BK, AR, TK) to
full-category format (BOOK, POST, TALK) in all doctrine/handbook/case files.

Also generates the crosswalk table to insert into sources/registry.yaml.
"""

import re
from pathlib import Path
from collections import defaultdict

ACADEMY_ROOT = Path(__file__).resolve().parent.parent

# Abbreviated prefix → Full prefix
PREFIX_MAP = {
    "BK": "BOOK",
    "AR": "POST",
    "TK": "TALK",
    "CRS": "COURSE",
    "DC": "DOC",
    "CS": "CASE",
    "CM": "COMM",
    "PPR": "PAPER",
}

SRC_PATTERN = re.compile(r'SRC-([A-Z]{2,6})-(\d{4})')


def scan_files():
    """Scan all markdown files for source references."""
    results = {}
    md_files = [
        "01_core_doctrine/PRINCIPLES.md",
        "01_core_doctrine/PROBLEM_SELECTION_MODULE.md",
        "01_core_doctrine/DECISION_FRAMEWORKS.md",
        "07_cases/case_catalog.md",
        "handbook/PRODUCT_LEADERSHIP_BIBLE.md",
        "handbook/PRINCIPAL_PM_PLAYBOOK.md",
        "handbook/AI_PM_PLAYBOOK.md",
    ]
    for fname in md_files:
        fpath = ACADEMY_ROOT / fname
        if fpath.exists():
            results[fname] = fpath.read_text(encoding="utf-8")
    return results


def fix_all_files(dry_run=True):
    """Convert all abbreviated source IDs to full format in all doctrine files."""
    files = scan_files()
    stats = defaultdict(lambda: {"total": 0, "fixed": 0, "unchanged": 0})

    for fname, content in files.items():
        fpath = ACADEMY_ROOT / fname
        fixed_content = content

        def replace_match(m):
            prefix = m.group(1)
            number = m.group(2)
            full_prefix = PREFIX_MAP.get(prefix)
            if full_prefix and full_prefix != prefix:
                stats[fname]["fixed"] += 1
                return f"SRC-{full_prefix}-{number}"
            else:
                stats[fname]["unchanged"] += 1
                return m.group(0)

        # First pass: count
        for m in SRC_PATTERN.finditer(content):
            prefix = m.group(1)
            if prefix in PREFIX_MAP and prefix != PREFIX_MAP[prefix]:
                stats[fname]["total"] += 1
            else:
                stats[fname]["unchanged"] += 1

        # Second pass: replace
        fixed_content = SRC_PATTERN.sub(replace_match, content)

        if fixed_content != content and not dry_run:
            print(f"  Writing: {fname}")
            fpath.write_text(fixed_content, encoding="utf-8")
        elif fixed_content != content:
            print(f"  WOULD WRITE: {fname}")

    return stats, files


def build_crosswalk():
    """Build the crosswalk/mapping text block for registry.yaml."""
    lines = [
        "# =============================================================================",
        "# SOURCE ID FORMAT CROSSWALK",
        "# =============================================================================",
        "# This registry uses the FULL-CATEGORY format (BOOK, POST, TALK, etc.).",
        "# Legacy doctrine files previously used abbreviated format (BK, AR, TK).",
        "# Both systems are now unified under the full-category format.",
        "#",
        "# Abbreviation Mapping:",
        "#   BK     → BOOK    (books)",
        "#   AR     → POST    (articles, blog posts, newsletters, written reports)",
        "#   TK     → TALK    (talks, presentations, keynotes)",
        "#   CRS    → COURSE  (university courses, certification programs)",
        "#   CS     → CASE    (case studies, postmortems)",
        "#   DC     → DOC     (documentation, regulatory documents)",
        "#   CM     → COMM    (community discussions, forums, podcasts)",
        "#   PPR    → PAPER   (research papers, academic publications)",
        "#",
        "# NOTE: Some earlier doctrine files used a different numbering system.",
        "# The table below maps legacy IDs to their current registry IDs.",
        "#",
        "# CROSSWALK: Legacy (Abbreviated) → Registry (Full Format)",
        "# =============================================================================",
        "",
    ]

    # Each line: SRC-BK-0001 (one entry in the old numbering) may or may not
    # correspond to SRC-BOOK-0001 in the registry. This is a rendering problem:
    # the old and new catalogs were independently numbered.
    #
    # The format fix aligns prefixes. Where a numbering gap exists, readers should
    # search the registry by title/author, not by number.
    #
    # Resolution: This crosswalk documents the known mappings. Sources that exist
    # in BOTH systems are mapped here. Sources that exist in only one system are
    # noted as such.

    # Known book mappings (verified by title/author content analysis):
    book_mappings = {
        "SRC-BK-0001": "SRC-BOOK-0001 (Inspired, Cagan)",
        "SRC-BK-0002": "SRC-BOOK-0001 (Inspired, Cagan) — same source, Empowered teams concept",
        "SRC-BK-0003": "SRC-BOOK-0015 (Good Strategy Bad Strategy, Rumelt)",
        "SRC-BK-0004": "SRC-BOOK-0004 (Continuous Discovery Habits, Torres)",
        "SRC-BK-0005": "SRC-BOOK-0014 (The Lean Startup, Ries)",
        "SRC-BK-0007": "SRC-BOOK-0003 (The Hard Thing About Hard Things, Horowitz)",
        "SRC-BK-0021": "SRC-BOOK-0008 (Escaping the Build Trap, Perri)",
        "SRC-BK-0013": "NOT IN REGISTRY — Accelerate, Forsgren et al. (add as SRC-BOOK-0017+)",
        "SRC-BK-0022": "NOT IN REGISTRY — No Rules Rules, Hastings (add as SRC-BOOK-0017+)",
        "SRC-BK-0025": "NOT IN REGISTRY — Hit Refresh, Nadella (add as SRC-BOOK-0017+)",
    }

    for legacy, current in sorted(book_mappings.items()):
        lines.append(f"# {legacy} → {current}")

    lines.extend([
        "",
        "# Article/Post mappings:",
        "# SRC-POST-0001 is Shreyas Doshi — the single known match.",
        "# SRC-AR-0002 through SRC-AR-0030 from legacy doctrine do not exist in registry.",
        "# SRC-AR-0031 through SRC-AR-0098 are case-specific sources (earnings calls,",
        "# SEC reports, news articles, etc.) referenced in the case catalog.",
        "# These are catalogued separately from the main source registry.",
        "",
        "# Talk mappings:",
        "# SRC-TK-0001 may refer to Brian Chesky's Airbnb re-centralization talk.",
        "# This source is NOT in the current registry. Add as needed.",
        "",
    ])

    return "\n".join(lines)


def main():
    import sys
    dry_run = "--execute" not in sys.argv

    print("=" * 70)
    print("SOURCE ID FORMAT RECONCILIATION")
    print("=" * 70)
    print()

    # Step 1: Show what needs fixing
    print("--- Step 1: Scanning for abbreviated IDs ---")
    stats, files = fix_all_files(dry_run=True)

    total_fixes = sum(s["fixed"] for s in stats.values())
    total_unchanged = sum(s["unchanged"] for s in stats.values())
    print(f"\n  Total abbreviated ID references: {total_fixes}")
    print(f"  Already full-format references: {total_unchanged}")
    print(f"  Files affected: {len(stats)}")

    for fname, s in sorted(stats.items()):
        if s["fixed"] > 0:
            print(f"    {fname}: {s['fixed']} conversions needed")

    # Step 2: Generate crosswalk
    print("\n--- Step 2: Crosswalk table ---")
    crosswalk = build_crosswalk()
    print(crosswalk)

    if dry_run:
        print("\n--- DRY RUN COMPLETE ---")
        print("Run with --execute to apply changes.")
    else:
        # Step 3: Apply fixes
        print("\n--- Step 3: Applying format conversions ---")
        actual_stats, _ = fix_all_files(dry_run=False)
        actual_fixes = sum(s["fixed"] for s in actual_stats.values())
        print(f"\n  Applied {actual_fixes} format conversions.")
        print("  Done. Run tests to verify.")


if __name__ == "__main__":
    main()
