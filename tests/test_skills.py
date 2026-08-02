"""Tests for the agent skill pack: structure, links, routing, and consistency."""

import json
import re
from pathlib import Path

import pytest
import yaml

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
VERDICT_CONTRACT_SUBPARTS = ["Verdict", "Confidence", "Assumptions", "What would change", "Next action"]


def skill_dirs(skills_root):
    return sorted(
        d for d in skills_root.iterdir()
        if d.is_dir() and d.name not in NON_SKILL_DIRS
    )


def read_frontmatter(skill_file):
    text = skill_file.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    assert m, f"{skill_file} has no frontmatter"
    return yaml.safe_load(m.group(1))


def skill_text(skill_file):
    return skill_file.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def skills_root(academy_root):
    return academy_root / "skills"


class TestSkillStructure:
    """Every production skill conforms to the shared contract."""

    def test_every_skill_has_skl_and_references(self, skills_root):
        for d in skill_dirs(skills_root):
            assert (d / "SKILL.md").exists(), f"{d.name} missing SKILL.md"
            assert (d / "references" / "doctrine-map.md").exists(), (
                f"{d.name} missing references/doctrine-map.md"
            )

    def test_required_frontmatter(self, skills_root):
        for d in skill_dirs(skills_root):
            fm = read_frontmatter(d / "SKILL.md")
            for field in REQUIRED_FRONTMATTER:
                assert field in fm, f"{d.name} missing frontmatter {field}"

    def test_folder_name_matches_frontmatter_name(self, skills_root):
        for d in skill_dirs(skills_root):
            fm = read_frontmatter(d / "SKILL.md")
            assert fm["name"] == d.name, f"{d.name}: name mismatch"

    def test_valid_type(self, skills_root):
        for d in skill_dirs(skills_root):
            fm = read_frontmatter(d / "SKILL.md")
            assert fm["type"] in {"assess", "assist"}, f"{d.name}: invalid type"

    def test_required_sections(self, skills_root):
        for d in skill_dirs(skills_root):
            fm = read_frontmatter(d / "SKILL.md")
            if fm.get("deprecated"):
                continue
            text = skill_text(d / "SKILL.md")
            for section in REQUIRED_SECTIONS:
                assert f"## {section}" in text, f"{d.name}: missing section {section}"

    def test_output_contract_presence(self, skills_root):
        for d in skill_dirs(skills_root):
            fm = read_frontmatter(d / "SKILL.md")
            if fm.get("deprecated"):
                continue
            text = skill_text(d / "SKILL.md")
            vc = re.search(r"## Verdict Contract(.*?)(?=\n## )", text, re.DOTALL)
            assert vc, f"{d.name}: no Verdict Contract"
            for sub in VERDICT_CONTRACT_SUBPARTS:
                assert sub in vc.group(1), f"{d.name}: Verdict Contract missing {sub}"

    def test_fast_and_full_mode_presence(self, skills_root):
        for d in skill_dirs(skills_root):
            fm = read_frontmatter(d / "SKILL.md")
            if fm.get("deprecated"):
                continue
            text = skill_text(d / "SKILL.md")
            assert "## Fast mode" in text, f"{d.name}: missing Fast mode"
            assert "## Full mode" in text, f"{d.name}: missing Full mode"

    def test_fast_and_full_mode_differ(self, skills_root):
        for d in skill_dirs(skills_root):
            fm = read_frontmatter(d / "SKILL.md")
            if fm.get("deprecated"):
                continue
            text = skill_text(d / "SKILL.md")
            mf = re.search(r"## Fast mode(.*?)(?=\n## )", text, re.DOTALL)
            ml = re.search(r"## Full mode(.*?)(?=\n## )", text, re.DOTALL)
            assert mf and ml
            assert mf.group(1).strip() != ml.group(1).strip(), (
                f"{d.name}: Fast mode and Full mode are identical"
            )

    def test_output_schema_presence(self, skills_root):
        for d in skill_dirs(skills_root):
            fm = read_frontmatter(d / "SKILL.md")
            if fm.get("deprecated"):
                continue
            text = skill_text(d / "SKILL.md")
            assert "## Output schema" in text, f"{d.name}: missing Output schema"
            vc = re.search(r"## Output schema(.*?)(?=\n## )", text, re.DOTALL)
            assert vc and "```json" in vc.group(1), f"{d.name}: Output schema not a JSON block"

    def test_output_schema_is_valid_json_envelope(self, skills_root):
        for d in skill_dirs(skills_root):
            fm = read_frontmatter(d / "SKILL.md")
            if fm.get("deprecated"):
                continue
            text = skill_text(d / "SKILL.md")
            osm = re.search(r"## Output schema(.*?)(?=\n## )", text, re.DOTALL)
            assert osm, f"{d.name}: no Output schema"
            fence = re.search(r"```json\n(.*?)```", osm.group(1), re.DOTALL)
            assert fence, f"{d.name}: Output schema has no JSON fence"
            import json
            schema = json.loads(fence.group(1))
            assert schema.get("skill") == d.name, f"{d.name}: schema 'skill' mismatch"
            assert "verdict" in schema, f"{d.name}: schema missing verdict"
            na = schema["next_action"]
            for k in ("what", "who", "by_when"):
                assert k in na, f"{d.name}: next_action missing {k}"

    def test_schema_verdicts_appear_in_verdict_contract(self, skills_root):
        for d in skill_dirs(skills_root):
            fm = read_frontmatter(d / "SKILL.md")
            if fm.get("deprecated"):
                continue
            text = skill_text(d / "SKILL.md")
            osm = re.search(r"## Output schema(.*?)(?=\n## )", text, re.DOTALL)
            fence = re.search(r"```json\n(.*?)```", osm.group(1), re.DOTALL)
            schema = json.loads(fence.group(1))
            vc = re.search(r"## Verdict Contract(.*?)(?=\n## )", text, re.DOTALL)
            assert vc, f"{d.name}: no Verdict Contract"
            for token in str(schema["verdict"]).split("|"):
                token = token.strip()
                if token:
                    assert token in vc.group(1), (
                        f"{d.name}: verdict '{token}' not in Verdict Contract"
                    )

    def test_unique_skill_identifiers(self, skills_root):
        names = [read_frontmatter(d / "SKILL.md")["name"] for d in skill_dirs(skills_root)]
        assert len(names) == len(set(names)), f"duplicate identifiers: {names}"


class TestSkillLinks:
    """Internal links and workflow references resolve."""

    def test_internal_links_resolve(self, skills_root):
        for d in skill_dirs(skills_root):
            text = skill_text(d / "SKILL.md")
            for m in re.finditer(r"\]\(([^)]+)\)", text):
                target = m.group(1)
                if target.startswith(("http", "#", "mailto:")):
                    continue
                t = target.split("#")[0]
                if not t:
                    continue
                resolved = (d / t).resolve()
                if not resolved.exists():
                    resolved = (skills_root / t).resolve()
                assert resolved.exists(), (
                    f"{d.name}: internal link does not resolve: {target}"
                )

    def test_workflow_references_existing_skills(self, skills_root):
        wf_dir = skills_root / "workflows"
        assert wf_dir.is_dir(), "workflows/ directory missing"
        for wf in wf_dir.glob("*.md"):
            text = wf.read_text(encoding="utf-8")
            for m in re.finditer(r"`([a-z][a-z0-9-]+)`", text):
                token = m.group(1)
                if token in {"skills", "fast", "full"} or token.startswith("09_tools"):
                    continue
                assert (skills_root / token / "SKILL.md").exists(), (
                    f"{wf.name}: references unknown skill {token}"
                )

    def test_workflows_exist(self, skills_root):
        wf_dir = skills_root / "workflows"
        wf_files = list(wf_dir.glob("*.md"))
        assert len(wf_files) >= 3, f"expected at least 3 workflows, found {len(wf_files)}"

    def test_workflow_step_numbers_resolve(self, skills_root):
        wf_dir = skills_root / "workflows"
        steps = {}
        for wf in wf_dir.glob("*.md"):
            wtext = wf.read_text(encoding="utf-8")
            steps[wf.stem] = {
                m.group(1) for m in re.finditer(r"^\|\s*(\d+(?:\.\d+)?)\s*\|", wtext, re.MULTILINE)
            }
        for d in skill_dirs(skills_root):
            fm = read_frontmatter(d / "SKILL.md")
            if fm.get("deprecated"):
                continue
            text = skill_text(d / "SKILL.md")
            for m in re.finditer(r"([a-z][a-z0-9-]+) \(step (\d+(?:\.\d+)?)\)", text):
                wf_name, step = m.group(1), m.group(2)
                assert wf_name in steps, f"{d.name}: unknown workflow {wf_name}"
                assert step in steps[wf_name], (
                    f"{d.name}: references {wf_name} step {step}, not defined"
                )

    def test_portfolio_map_references_existing_skills(self, skills_root):
        pmap = skills_root / "PORTFOLIO_MAP.md"
        assert pmap.exists(), "PORTFOLIO_MAP.md missing"
        text = pmap.read_text(encoding="utf-8")
        for m in re.finditer(r"\]\(([a-z][a-z0-9-]*/SKILL\.md)\)", text):
            token = m.group(1).split("/")[0]
            assert (skills_root / token / "SKILL.md").exists(), (
                f"PORTFOLIO_MAP.md references unknown skill {token}"
            )


class TestDeprecatedRouting:
    def test_deprecated_skills_route(self, skills_root):
        deprecated = [
            read_frontmatter(d / "SKILL.md")
            for d in skill_dirs(skills_root)
            if read_frontmatter(d / "SKILL.md").get("deprecated")
        ]
        for fm in deprecated:
            assert fm.get("replaced_by"), f"{fm['name']} missing replaced_by"
            assert (skills_root / fm["replaced_by"] / "SKILL.md").exists(), (
                f"{fm['name']} replaced_by does not resolve"
            )

    def test_source_tier_check_is_deprecated(self, skills_root):
        fm = read_frontmatter(skills_root / "run-source-tier-check" / "SKILL.md")
        assert fm.get("deprecated") is True
        assert fm["replaced_by"] == "audit-decision-evidence"


class TestPortfolioConsistency:
    def test_index_matches_skill_set(self, skills_root):
        index = (skills_root / "INDEX.md").read_text(encoding="utf-8")
        active = [
            read_frontmatter(d / "SKILL.md")["name"]
            for d in skill_dirs(skills_root)
            if not read_frontmatter(d / "SKILL.md").get("deprecated")
        ]
        for name in active:
            assert name in index, f"INDEX.md missing active skill {name}"
        # deprecated skills must appear with a routing note
        for d in skill_dirs(skills_root):
            fm = read_frontmatter(d / "SKILL.md")
            if fm.get("deprecated"):
                assert fm["name"] in index, f"INDEX.md missing deprecated skill {fm['name']}"

    def test_plugin_manifest_matches_skill_set(self, academy_root):
        manifest = academy_root / ".claude-plugin" / "plugin.json"
        plugin = json.loads(manifest.read_text(encoding="utf-8"))
        plugin_skills = {p.split("/")[-1] for p in plugin["skills"] if p.startswith("skills/")}
        active = {
            read_frontmatter(d / "SKILL.md")["name"]
            for d in skill_dirs(academy_root / "skills")
            if not read_frontmatter(d / "SKILL.md").get("deprecated")
        }
        assert plugin_skills == active, (
            f"plugin.json {sorted(plugin_skills - active)} vs active {sorted(active - plugin_skills)}"
        )

    def test_shared_contract_exists(self, skills_root):
        assert (skills_root / "_shared" / "SKILL_CONTRACT.md").exists()

    def test_skill_count_drift(self, skills_root):
        """Every active skill is referenced in the PORTFOLIO_MAP (count consistency)."""
        pmap = (skills_root / "PORTFOLIO_MAP.md").read_text(encoding="utf-8")
        active = [
            read_frontmatter(d / "SKILL.md")["name"]
            for d in skill_dirs(skills_root)
            if not read_frontmatter(d / "SKILL.md").get("deprecated")
        ]
        for name in active:
            assert name in pmap, f"PORTFOLIO_MAP.md missing active skill {name}"


class TestEvaluationSuite:
    def test_at_least_12_scenarios(self, skills_root):
        scenarios = list((skills_root / "evals" / "scenarios").glob("S*.md"))
        assert len(scenarios) >= 12, f"expected >=12 scenarios, found {len(scenarios)}"

    def test_rubric_exists(self, skills_root):
        assert (skills_root / "evals" / "rubric.md").exists()
        assert (skills_root / "evals" / "EVALUATION_REPORT.md").exists()

    def test_audit_exists(self, skills_root):
        assert (skills_root / "quality" / "SKILL_PORTFOLIO_AUDIT.md").exists()


class TestTemplate:
    def test_template_has_required_sections(self, skills_root):
        text = (skills_root / "_template" / "SKILL.md").read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            assert f"## {section}" in text, f"_template missing {section}"
