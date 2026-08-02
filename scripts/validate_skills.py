#!/usr/bin/env python3
"""
Validate the Product Academy skill pack.

Enforces the shared skill contract (skills/_shared/SKILL_CONTRACT.md):
  - each skill is a folder skills/<name>/SKILL.md with references/
  - frontmatter between --- fences parses as YAML
  - required frontmatter fields: name, description, type, version, best_for,
    doctrine, license
  - type is exactly "assess" or "assist"
  - required sections (Purpose, Use when, Do not use when, Inputs, Missing-data
    behavior, Context classification, Fast mode, Full mode, Method, Evidence
    classification, Output schema, Verdict Contract, Failure modes, Reversal
    conditions, Worked example, Composition hooks, Related Skills)
  - Verdict Contract has all sub-parts: Verdict, Confidence, Assumptions,
    What would change, Next action
  - fast/full mode presence and output-schema presence are enforced by the
    required-section list
  - doctrine references resolve to real repo paths or stable IDs
  - unique skill identifiers (folder name == frontmatter name, globally unique)
  - valid internal links (relative links in SKILL.md resolve to real files)
  - references/doctrine-map.md exists for active skills
  - workflow files reference only existing skills
  - deprecated skills declare replaced_by that resolves to an active skill
  - portfolio index consistency: INDEX.md table and PORTFOLIO_MAP.md reference
    only existing skills; plugin manifest skills exist
  - skill-count drift: plugin manifest and INDEX table must match the active
    skill set

Exit 0 = pass. Non-zero = fail.
"""

import json
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
NON_SKILL_DIRS = {"_template", "_shared", "__pycache__", "quality", "evals", "workflows"}

REQUIRED_FRONTMATTER = ["name", "description", "type", "version", "best_for", "doctrine", "license"]
REQUIRED_SECTIONS = [
    "Purpose",
    "Use when",
    "Do not use when",
    "Inputs",
    "Missing-data behavior",
    "Context classification",
    "Fast mode",
    "Full mode",
    "Method",
    "Evidence classification",
    "Output schema",
    "Verdict Contract",
    "Failure modes",
    "Reversal conditions",
    "Worked example",
    "Composition hooks",
    "Related Skills",
]
VERDICT_CONTRACT_SUBPARTS = [
    "Verdict",
    "Confidence",
    "Assumptions",
    "What would change",
    "Next action",
]
VALID_TYPES = {"assess", "assist"}

# Stable ID patterns that must exist in the repo
ID_PATTERNS = [
    (r"PRN-\d{4}", lambda rid: (ROOT / "01_core_doctrine" / "PRINCIPLES.md").read_text(encoding="utf-8", errors="ignore").count(rid) > 0),
    (r"CON-\d{4}", lambda rid: (ROOT / "08_contradictions" / "register.yaml").read_text(encoding="utf-8", errors="ignore").count(rid) > 0),
    (r"CASE-\d{4}", lambda rid: (ROOT / "07_cases" / "case_catalog.md").read_text(encoding="utf-8", errors="ignore").count(rid) > 0),
    (r"SRC-[A-Z]{3,6}-\d{4}", lambda rid: (ROOT / "sources" / "registry.yaml").read_text(encoding="utf-8", errors="ignore").count(f"source_id: {rid}") > 0),
]

_content = {}


def repo_content(path):
    if path not in _content:
        _content[path] = (ROOT / path).read_text(encoding="utf-8", errors="ignore")
    return _content[path]


def extract_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    return m.group(1) if m else None


def split_refs(ref):
    fragments = []
    parts = re.split(r"[,(]", ref)
    for part in parts:
        part = part.strip().rstrip(")")
        if not part:
            continue
        fragments.append(part)
        for sub in re.findall(r"(PRN-\d{4}|CON-\d{4}|CASE-\d{4}|SRC-[A-Z]{3,6}-\d{4})", part):
            if sub not in fragments:
                fragments.append(sub)
    return fragments


def resolve_path_fragment(fragment):
    candidates = [ROOT / fragment]
    for dir_name in ["01_core_doctrine", "09_tools", "05_ai_product_management", "10_simulator"]:
        candidates.append(ROOT / dir_name / fragment)
    return any(p.exists() for p in candidates)


def check_doctrine_refs(doctrine_list, errors, skill_name):
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
            if ("/" in fragment and " " not in fragment) or fragment.endswith(".md"):
                if not resolve_path_fragment(fragment):
                    errors.append(f"[{skill_name}] doctrine ref does not resolve: {fragment}")


def collect_skills():
    return sorted(
        d.name for d in SKILLS_DIR.iterdir()
        if d.is_dir() and d.name not in NON_SKILL_DIRS
    )


def check_internal_links(skill_name, text, errors):
    """Relative markdown links inside a SKILL.md must resolve within the repo."""
    skill_dir = SKILLS_DIR / skill_name
    for m in re.finditer(r"\]\(([^)]+)\)", text):
        target = m.group(1)
        if target.startswith("http") or target.startswith("#") or target.startswith("mailto:"):
            continue
        # anchor-stripped target
        t = target.split("#")[0]
        if not t:
            continue
        resolved = (skill_dir / t).resolve()
        if not resolved.exists():
            resolved = (ROOT / "skills" / t).resolve()
        if not resolved.exists():
            errors.append(f"[{skill_name}] internal link does not resolve: {target}")


def main():
    skills = collect_skills()
    errors = []
    checked = 0
    active = []
    deprecated = []

    for skill_name in skills:
        skill_dir = SKILLS_DIR / skill_name
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"[{skill_name}] missing SKILL.md")
            continue

        text = skill_file.read_text(encoding="utf-8")
        fm = extract_frontmatter(text)
        if fm is None:
            errors.append(f"[{skill_name}] no frontmatter (--- fences)")
            continue
        try:
            data = yaml.safe_load(fm)
        except yaml.YAMLError as e:
            errors.append(f"[{skill_name}] frontmatter YAML error: {e}")
            continue

        checked += 1
        is_deprecated = bool(data.get("deprecated"))

        for field in REQUIRED_FRONTMATTER:
            if field not in data:
                errors.append(f"[{skill_name}] missing frontmatter field: {field}")

        if "name" in data and data["name"] != skill_name:
            errors.append(f"[{skill_name}] frontmatter name '{data['name']}' != folder name '{skill_name}'")

        if "type" in data and data["type"] not in VALID_TYPES:
            errors.append(f"[{skill_name}] invalid type: {data['type']} (must be assess|assist)")

        if is_deprecated:
            # Deprecated routing contract
            if not data.get("replaced_by"):
                errors.append(f"[{skill_name}] deprecated skill must declare replaced_by")
            else:
                if not (SKILLS_DIR / data["replaced_by"] / "SKILL.md").exists():
                    errors.append(f"[{skill_name}] replaced_by '{data['replaced_by']}' does not resolve to a skill")
            if "## Deprecated routing" not in text and "## Purpose" not in text:
                errors.append(f"[{skill_name}] deprecated skill missing routing content")
            deprecated.append(skill_name)
            continue

        active.append(skill_name)

        if not (skill_dir / "references").is_dir():
            errors.append(f"[{skill_name}] missing references/ dir")
        if not (skill_dir / "references" / "doctrine-map.md").exists():
            errors.append(f"[{skill_name}] missing references/doctrine-map.md")

        for section in REQUIRED_SECTIONS:
            if f"## {section}" not in text:
                errors.append(f"[{skill_name}] missing section: {section}")

        vc = re.search(r"## Verdict Contract(.*?)(?=\n## )", text, re.DOTALL)
        if vc:
            for sub in VERDICT_CONTRACT_SUBPARTS:
                if sub not in vc.group(1):
                    errors.append(f"[{skill_name}] Verdict Contract missing: {sub}")
        else:
            errors.append(f"[{skill_name}] Verdict Contract section missing")

        # Fast mode must differ from Full mode
        fm = re.search(r"## Fast mode(.*?)(?=\n## )", text, re.DOTALL)
        ff = re.search(r"## Full mode(.*?)(?=\n## )", text, re.DOTALL)
        if fm and ff and fm.group(1).strip() == ff.group(1).strip():
            errors.append(f"[{skill_name}] Fast mode and Full mode are identical")

        # Output schema must be a parseable JSON fence matching the envelope,
        # and every verdict token must appear in the Verdict Contract
        osm = re.search(r"## Output schema(.*?)(?=\n## )", text, re.DOTALL)
        if osm and "```json" in osm.group(1):
            fence = re.search(r"```json\n(.*?)```", osm.group(1), re.DOTALL)
            if not fence:
                errors.append(f"[{skill_name}] Output schema JSON fence malformed")
            else:
                try:
                    schema = json.loads(fence.group(1))
                except json.JSONDecodeError as e:
                    errors.append(f"[{skill_name}] Output schema is not valid JSON: {e}")
                else:
                    if schema.get("skill") != skill_name:
                        errors.append(f"[{skill_name}] Output schema 'skill' != '{skill_name}'")
                    for key in ("verdict", "next_action"):
                        if key not in schema:
                            errors.append(f"[{skill_name}] Output schema missing '{key}'")
                    na = schema.get("next_action")
                    if isinstance(na, dict):
                        for k in ("what", "who", "by_when"):
                            if k not in na:
                                errors.append(f"[{skill_name}] next_action missing '{k}'")
                    if vc:
                        for token in str(schema.get("verdict", "")).split("|"):
                            token = token.strip()
                            if token and token not in vc.group(1):
                                errors.append(f"[{skill_name}] verdict '{token}' not in Verdict Contract")

        check_internal_links(skill_name, text, errors)
        for ref in data.get("doctrine", []):
            check_doctrine_refs([ref], errors, skill_name)

    # --- cross-pack checks -------------------------------------------------
    dup_names = {s for s in active if active.count(s) > 1}
    if dup_names:
        errors.append(f"duplicate skill identifiers: {sorted(dup_names)}")

    # workflow references
    workflows_dir = SKILLS_DIR / "workflows"
    if workflows_dir.is_dir():
        wf_steps = {}
        for wf in sorted(workflows_dir.glob("*.md")):
            wtext = wf.read_text(encoding="utf-8")
            for m in re.finditer(r"`([a-z][a-z0-9-]+)`", wtext):
                token = m.group(1)
                if token in {"skills", "fast", "full"}:
                    continue
                if token.startswith("09_tools"):
                    continue
                if not (SKILLS_DIR / token / "SKILL.md").exists():
                    errors.append(f"[workflows/{wf.name}] references unknown skill: {token}")
            wf_steps[wf.stem] = {
                m.group(1) for m in re.finditer(r"^\|\s*(\d+(?:\.\d+)?)\s*\|", wtext, re.MULTILINE)
            }
        # workflow step-number references in skill composition hooks
        for skill_name in active:
            text = (SKILLS_DIR / skill_name / "SKILL.md").read_text(encoding="utf-8")
            for m in re.finditer(r"([a-z][a-z0-9-]+) \(step (\d+(?:\.\d+)?)\)", text):
                wf_name, step = m.group(1), m.group(2)
                if wf_name in wf_steps and step not in wf_steps[wf_name]:
                    errors.append(f"[{skill_name}] references {wf_name} step {step}, not defined in workflow")

    # portfolio map references
    pmap = SKILLS_DIR / "PORTFOLIO_MAP.md"
    if pmap.exists():
        pmtext = pmap.read_text(encoding="utf-8")
        for m in re.finditer(r"\]\(([a-z][a-z0-9-]*/SKILL\.md)\)", pmtext):
            token = m.group(1).split("/")[0]
            if not (SKILLS_DIR / token / "SKILL.md").exists():
                errors.append(f"[PORTFOLIO_MAP.md] references unknown skill: {token}")

    # INDEX table rows reference existing skills
    index_md = SKILLS_DIR / "INDEX.md"
    if index_md.exists():
        itext = index_md.read_text(encoding="utf-8")
        for m in re.finditer(r"\]\(([a-z][a-z0-9-]*)/SKILL\.md\)", itext):
            token = m.group(1)
            if token in NON_SKILL_DIRS:
                continue
            if not (SKILLS_DIR / token / "SKILL.md").exists():
                errors.append(f"[INDEX.md] references unknown skill: {token}")

    # plugin manifest consistency
    manifest = ROOT / ".claude-plugin" / "plugin.json"
    if manifest.exists():
        try:
            plugin = json.loads(manifest.read_text(encoding="utf-8"))
            plugin_skills = [p.split("/")[-1] for p in plugin.get("skills", []) if p.startswith("skills/")]
            for ps in plugin_skills:
                if ps not in active and ps not in deprecated:
                    errors.append(f"[plugin.json] references unknown skill: {ps}")
            missing_from_manifest = set(active) - set(plugin_skills)
            if missing_from_manifest:
                errors.append(f"[plugin.json] active skills missing from manifest: {sorted(missing_from_manifest)}")
        except json.JSONDecodeError as e:
            errors.append(f"[plugin.json] invalid JSON: {e}")

    # deprecated routing in INDEX
    if index_md.exists():
        itext = index_md.read_text(encoding="utf-8")
        for d in deprecated:
            if d not in itext:
                errors.append(f"[INDEX.md] deprecated skill {d} missing from index (routing note)")

    print("=" * 70)
    print("SKILL PACK VALIDATION")
    print("=" * 70)
    print(f"Active skills checked: {len(active)}")
    print(f"Deprecated skills: {len(deprecated)}")
    if errors:
        print(f"FAILED: {len(errors)} issue(s)")
        for e in errors:
            print(f"  - {e}")
        print("\nRESULT: FAILURE")
        sys.exit(1)
    print("All skills conform to the shared contract.")
    print("\nRESULT: SUCCESS")


if __name__ == "__main__":
    main()
