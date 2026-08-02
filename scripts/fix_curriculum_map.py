#!/usr/bin/env python3
"""
Add an honest Status column to CURRICULUM_MAP.md (adversarial finding A3).

Each module gets: COMPLETE (dedicated substantive content exists),
COVERED (content exists but combined into a shared file), PARTIAL
(covered but thin), or PLANNED (no content yet).
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT / "CURRICULUM_MAP.md"

# module id -> status, based on actual files present in the repo
STATUS = {
    # Track 00
    "00.1": "COMPLETE", "00.2": "COMPLETE", "00.3": "COMPLETE",
    # Track 01 (covered by PRINCIPLES.md / PROBLEM_SELECTION_MODULE.md / DECISION_FRAMEWORKS.md)
    "01.1": "COVERED", "01.2": "COVERED", "01.3": "PARTIAL",
    "01.4": "COVERED", "01.5": "PLANNED", "01.6": "PLANNED",
    "01.7": "PLANNED", "01.8": "COVERED",
    # Track 02 (PRINCIPAL_PM.md, DIRECTOR_VP_TRANSITION.md, CPO_ROLE.md)
    "02.1": "COVERED", "02.2": "COVERED", "02.3": "COVERED",
    "02.4": "COVERED", "02.5": "PARTIAL", "02.6": "PARTIAL",
    "02.7": "PARTIAL", "02.8": "PLANNED",
    # Track 03 (BUSINESS_MODEL_MAP.md)
    "03.1": "PARTIAL", "03.2": "PLANNED", "03.3": "COVERED",
    "03.4": "COVERED", "03.5": "PLANNED", "03.6": "COVERED", "03.7": "PLANNED",
    # Track 04 (archetype_catalog.md covers all archetypes)
    "04.0": "COMPLETE", "04.1": "COVERED", "04.2": "COVERED",
    "04.3": "COVERED", "04.4": "COVERED", "04.5": "COVERED",
    "04.6": "COVERED", "04.7": "COVERED", "04.8": "COVERED",
    "04.9": "COVERED", "04.10": "COVERED", "04.11": "COVERED",
    "04.12": "COVERED", "04.13": "COVERED",
    # Track 05 (8 dedicated AI files)
    "05.1": "COVERED", "05.2": "COVERED", "05.3": "COMPLETE",
    "05.4": "COVERED", "05.5": "COVERED", "05.6": "COVERED",
    "05.7": "COVERED",
    # Track 06 (4 industry overlays)
    "06.1": "COVERED", "06.2": "PLANNED", "06.3": "PLANNED",
    "06.4": "PLANNED", "06.5": "PLANNED", "06.6": "PLANNED",
    "06.7": "PLANNED", "06.8": "PLANNED", "06.9": "PLANNED",
    # Track 07 (case_catalog.md)
    "07.1": "COVERED", "07.2": "COVERED", "07.3": "COVERED",
    "07.4": "COVERED", "07.5": "COVERED", "07.6": "COVERED",
    "07.7": "COVERED", "07.8": "COVERED",
    # Track 08 (register.yaml, 13 contradictions)
    "08.1": "COVERED", "08.2": "COVERED", "08.3": "COVERED",
    "08.4": "COVERED", "08.5": "COVERED", "08.6": "COVERED",
    "08.7": "COVERED", "08.8": "COVERED", "08.9": "COVERED",
    "08.10": "COVERED",
    # Track 09 (18 tools)
    "09.1": "COVERED", "09.2": "COVERED", "09.3": "COVERED",
    "09.4": "COVERED", "09.5": "COVERED", "09.6": "COVERED",
    "09.7": "COVERED", "09.8": "COVERED",
    # Track 10 (11 scenario files + rubric)
    "10.1": "COMPLETE", "10.2": "COMPLETE", "10.3": "COMPLETE",
    "10.4": "COMPLETE", "10.5": "COMPLETE", "10.6": "COMPLETE",
    "10.7": "COMPLETE", "10.8": "COMPLETE",
    # Track 11 (4 learning paths)
    "11.1": "COMPLETE", "11.2": "COMPLETE", "11.3": "COMPLETE",
    "11.4": "COMPLETE", "11.5": "COMPLETE",
    # Track 12 (personal lab)
    "12.1": "PLANNED", "12.2": "PLANNED", "12.3": "PLANNED",
    "12.4": "PLANNED", "12.5": "PLANNED", "12.6": "PLANNED",
    "12.7": "PLANNED",
    # Track 13 (career transitions)
    "13.0": "COMPLETE", "13.1": "COMPLETE", "13.2": "COMPLETE", "13.3": "COMPLETE",
}

LABELS = {
    "COMPLETE": "COMPLETE — dedicated, substantive content",
    "COVERED": "COVERED — combined into a shared file",
    "PARTIAL": "PARTIAL — covered but thinner than a dedicated module",
    "PLANNED": "PLANNED — not yet written",
}

LEGEND = (
    "### Module Status Legend\n\n"
    "| Status | Meaning |\n"
    "|--------|---------|\n"
    "| COMPLETE | Dedicated, substantive content exists |\n"
    "| COVERED | Content exists, combined into a shared file |\n"
    "| PARTIAL | Covered, but thinner than a dedicated module |\n"
    "| PLANNED | Not yet written |\n"
)


def add_status_col(text):
    lines = text.split("\n")
    out = []
    for line in lines:
        # table header row of a module table: | ID | Module | ...
        m = re.match(r"^\| ID \|", line)
        if m and "Status" not in line:
            out.append(line.rstrip() + " Status |")
            continue
        # separator row
        m = re.match(r"^\|----", line)
        if m:
            out.append(line.rstrip() + "---------|")
            continue
        # data row: starts with | and contains a known module id
        m = re.match(r"^\|\s*(\d{2}\.\d+)\s*\|", line)
        if m:
            mid = m.group(1)
            st = STATUS.get(mid, "PLANNED")
            out.append(line.rstrip() + f" {st} |")
            continue
        out.append(line)
    return "\n".join(out)


def main():
    text = MAP.read_text(encoding="utf-8")
    new = add_status_col(text)
    # Insert legend after the Overview intro if not already present
    if "Module Status Legend" not in new:
        new = new.replace(
            "## Level Structure",
            LEGEND + "\n## Level Structure",
            1,
        )
    if new != text:
        MAP.write_text(new, encoding="utf-8")
        print("CURRICULUM_MAP.md updated with Status column + legend.")
    else:
        print("No change.")


if __name__ == "__main__":
    main()
