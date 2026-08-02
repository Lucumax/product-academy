#!/usr/bin/env python3
"""
Validate the Product Academy skill pack.

Enforces the SKILL.md template contract:
  - each skill is a folder skills/<name>/SKILL.md with references/
  - frontmatter between --- fences parses as YAML
  - required frontmatter fields: name, description, type, version, best_for,
    doctrine, license
  - type is exactly "assess" or "assist"
  - required sections: Purpose, Input, Method, Verdict Contract, Thresholds,
    Evidence & Doctrine, Common Pitfalls, Related Skills
  - doctrine references resolve to real repo paths (PRN-/CON-/CASE-/SRC- ids
    or existing file paths)

Exit 0 = pass. Non-zero = fail.
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pyyaml required: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"

REQUIRED_FRONTMATTER = ["name", "description", "type", "version", "best_for", "doctrine", "license"]
REQUIRED_SECTIONS = [
    "Purpose",
    "Input",
    "Method",
    "Verdict Contract",
    "Thresholds",
    "Evidence & Doctrine",
    "Common Pitfalls",
    "Related Skills",
]
VALID_TYPES = {"assess", "assist"}

# Stable ID patterns that must exist in the repo
ID_PATTERNS = [
    (r"PRN-\d{4}", lambda rid: (ROOT / "01_core_doctrine" / "PRINCIPLES.md").read_text(encoding="utf-8", errors="ignore").count(rid) > 0),
    (r"CON-\d{4}", lambda rid: (ROOT / "08_contradictions" / "register.yaml").read_text(encoding="utf-8", errors="ignore").count(rid) > 0),
    (r"CASE-\d{4}", lambda rid: (ROOT / "07_cases" / "case_catalog.md").read_text(encoding="utf-8", errors="ignore").count(rid) > 0),
    (r"SRC-[A-Z]{3,6}-\d{4}", lambda rid: (ROOT / "sources" / "registry.yaml").read_text(encoding="utf-8", errors="ignore").count(f"source_id: {rid}") > 0),
]

# Preload file content cache
_content = {}


def repo_content(path):
    if path not in _content:
        _content[path] = (ROOT / path).read_text(encoding="utf-8", errors="ignore")
    return _content[path]


def extract_frontmatter(text):
    """Return the YAML block between the first two --- fences."""
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    return m.group(1) if m else None


def split_refs(ref):
    """Split a doctrine ref string into individual checkable fragments.

    Handles the annotation styles the skill authors use:
      - "PRN-0004 (PMF is a condition)"            -> PRN-0004
      - "PRN-0002, PRN-0003, PRN-0007"             -> three ids
      - "09_tools/A.md, 09_tools/B.md"             -> two paths
      - "07_cases/case_catalog.md (CASE-0005)"     -> path + case id
    """
    fragments = []
    # split on commas and capture parenthetical contents as separate items
    parts = re.split(r"[,(]", ref)
    for part in parts:
        part = part.strip().rstrip(")")
        if not part:
            continue
        fragments.append(part)
        # parentheticals may contain ids like CASE-0005; split those too
        for sub in re.findall(r"(PRN-\d{4}|CON-\d{4}|CASE-\d{4}|SRC-[A-Z]{3,6}-\d{4})", part):
            if sub not in fragments:
                fragments.append(sub)
    return fragments


def resolve_path_fragment(fragment):
    """Check if a path fragment resolves to a real file."""
    candidates = [ROOT / fragment]
    for dir_name in ["01_core_doctrine", "09_tools", "05_ai_product_management", "10_simulator"]:
        candidates.append(ROOT / dir_name / fragment)
    return any(p.exists() for p in candidates)


def check_doctrine_refs(doctrine_list, errors, skill_name):
    """Validate doctrine references: IDs that exist, or file paths that exist."""
    for ref in doctrine_list:
        ref = str(ref).strip()
        for fragment in split_refs(ref):
            id_match = re.fullmatch(r"(PRN-\d{4}|CON-\d{4}|CASE-\d{4}|SRC-[A-Z]{3,6}-\d{4})", fragment)
            if id_match:
                rid = id_match.group(1)
                for pattern, check in ID_PATTERNS:
                    if re.fullmatch(pattern, rid) and check(rid):
                        break
                else:
                    errors.append(f"[{skill_name}] doctrine id not found in repo: {rid}")
                continue
            # path-like fragment
            if "/" in fragment or fragment.endswith(".md"):
                if not resolve_path_fragment(fragment):
                    errors.append(f"[{skill_name}] doctrine ref does not resolve: {fragment}")


def main():
    skills = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir() and d.name != "_template")
    errors = []
    checked = 0

    for skill_dir in skills:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"[{skill_dir.name}] missing SKILL.md")
            continue
        if not (skill_dir / "references").is_dir():
            errors.append(f"[{skill_dir.name}] missing references/ dir")

        text = skill_file.read_text(encoding="utf-8")
        fm = extract_frontmatter(text)
        if fm is None:
            errors.append(f"[{skill_dir.name}] no frontmatter (--- fences)")
            continue

        try:
            data = yaml.safe_load(fm)
        except yaml.YAMLError as e:
            errors.append(f"[{skill_dir.name}] frontmatter YAML error: {e}")
            continue

        checked += 1

        for field in REQUIRED_FRONTMATTER:
            if field not in data:
                errors.append(f"[{skill_dir.name}] missing frontmatter field: {field}")

        if "type" in data and data["type"] not in VALID_TYPES:
            errors.append(f"[{skill_dir.name}] invalid type: {data['type']} (must be assess|assist)")

        for section in REQUIRED_SECTIONS:
            if f"## {section}" not in text:
                errors.append(f"[{skill_dir.name}] missing section: {section}")

        # Verdict Contract must contain the four required sub-parts
        vc = re.search(r"## Verdict Contract(.*?)(?=\n## )", text, re.DOTALL)
        if vc:
            for sub in ["Verdict", "Confidence", "Citations", "Stated assumptions", "What would change"]:
                if sub not in vc.group(1):
                    errors.append(f"[{skill_dir.name}] Verdict Contract missing: {sub}")
        else:
            errors.append(f"[{skill_dir.name}] Verdict Contract section missing")

        # doctrine refs resolve
        for ref in data.get("doctrine", []):
            check_doctrine_refs([ref], errors, skill_dir.name)

    print("=" * 70)
    print("SKILL PACK VALIDATION")
    print("=" * 70)
    print(f"Skills checked: {checked}")
    if errors:
        print(f"FAILED: {len(errors)} issue(s)")
        for e in errors:
            print(f"  - {e}")
        print("\nRESULT: FAILURE")
        sys.exit(1)
    print("All skills conform to the template contract.")
    print("\nRESULT: SUCCESS")


if __name__ == "__main__":
    main()
