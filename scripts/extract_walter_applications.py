#!/usr/bin/env python3
"""
Extract Walter-specific application notes out of canonical doctrine files
into a gitignored personal file (12_personal_lab/walter_applications.md).

In canonical files, inline walter_application content is replaced with a
short pointer. The extracted file holds the full Walter-specific guidance.

Affected files:
  - 01_core_doctrine/PRINCIPLES.md  (| **walter_application** | "..." | table rows)
  - 01_core_doctrine/PROBLEM_SELECTION_MODULE.md
  - 07_cases/case_catalog.md        (### walter_application sections)
  - handbook/PRODUCT_LEADERSHIP_BIBLE.md
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "12_personal_lab" / "walter_applications.md"

FILES = [
    "01_core_doctrine/PRINCIPLES.md",
    "01_core_doctrine/PROBLEM_SELECTION_MODULE.md",
    "07_cases/case_catalog.md",
    "handbook/PRODUCT_LEADERSHIP_BIBLE.md",
]

POINTER = (
    "> Walter-specific application notes are maintained in "
    "`12_personal_lab/walter_applications.md` (not part of the public "
    "Academy content)."
)


def process_table_row(lines):
    """Replace | **walter_application** | "..." | rows with a pointer."""
    out = []
    extracted = []
    for line in lines:
        m = re.match(r"^(\|\s*\*\*walter_application\*\*\s*\|)(\s*)(.+)$", line)
        if m:
            value = m.group(3)
            extracted.append(value.strip())
            indent = " " * 0
            out.append(f"| **walter_application** | _See personal applications file._ |")
        else:
            out.append(line)
    return out, extracted


def process_case_section(lines):
    """Extract ### walter_application sections into the pointer."""
    out = []
    extracted = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "### walter_application":
            # collect until next heading (any level) or end
            j = i + 1
            body = []
            while j < len(lines) and not lines[j].startswith("#"):
                body.append(lines[j])
                j += 1
            extracted.append("\n".join(body).strip())
            out.append("### walter_application")
            out.append("")
            out.append("_See personal applications file._")
            out.append("")
            i = j
        else:
            out.append(lines[i])
            i += 1
    return out, extracted


def main():
    all_extracted = []
    for rel in FILES:
        fpath = ROOT / rel
        if not fpath.exists():
            continue
        lines = fpath.read_text(encoding="utf-8").splitlines()
        if rel.endswith("case_catalog.md"):
            new_lines, extracted = process_case_section(lines)
        else:
            new_lines, extracted = process_table_row(lines)
        if extracted:
            fpath.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
            header = f"## From {rel}\n"
            all_extracted.append(header)
            all_extracted.extend(extracted)
            print(f"  {rel}: extracted {len(extracted)} walter_application notes")

    if all_extracted:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        content = (
            "# Walter-Specific Application Notes\n\n"
            "This file is gitignored and is personal to the Academy maintainer.\n"
            "It is NOT part of the public Academy content.\n\n"
            "---\n\n" + "\n\n---\n\n".join(all_extracted) + "\n"
        )
        OUT.write_text(content, encoding="utf-8")
        print(f"Wrote {OUT.relative_to(ROOT)} with {len(all_extracted)} notes")
    else:
        print("No walter_application content found.")


if __name__ == "__main__":
    main()
