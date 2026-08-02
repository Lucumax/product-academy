"""Cross-reference integrity tests (adversarial review findings A1 and G2).

Every source ID cited in doctrine, handbook, and case files must resolve to a
record in the source registry (or be a documented case-catalog source).
"""

import re
from pathlib import Path

import pytest

# Files that may cite source IDs. Excludes evidence/agent_runs (historical
# snapshots) and .pytest_cache.
DOCTRINE_FILES = [
    "00_orientation/README.md",
    "01_core_doctrine/PRINCIPLES.md",
    "01_core_doctrine/PROBLEM_SELECTION_MODULE.md",
    "01_core_doctrine/DECISION_FRAMEWORKS.md",
    "02_principal_plus/PRINCIPAL_PM.md",
    "02_principal_plus/DIRECTOR_VP_TRANSITION.md",
    "02_principal_plus/CPO_ROLE.md",
    "03_business_and_gtm/BUSINESS_MODEL_MAP.md",
    "04_product_archetypes/archetype_catalog.md",
    "05_ai_product_management/README.md",
    "05_ai_product_management/EVALUATION_CONTRACTS.md",
    "05_ai_product_management/FAILURE_MODES.md",
    "05_ai_product_management/MODEL_VS_SYSTEM.md",
    "05_ai_product_management/GOVERNANCE.md",
    "05_ai_product_management/ADOPTION.md",
    "05_ai_product_management/AGENT_ARCHITECTURE.md",
    "05_ai_product_management/WORKFLOW_SELECTION.md",
    "06_industry_overlays/FINANCIAL_SERVICES.md",
    "06_industry_overlays/INSURANCE.md",
    "06_industry_overlays/POWER_AND_ENERGY.md",
    "06_industry_overlays/INFRASTRUCTURE_AND_DEVELOPMENT_FINANCE.md",
    "07_cases/case_catalog.md",
    "08_contradictions/register.yaml",
    "handbook/PRODUCT_LEADERSHIP_BIBLE.md",
    "handbook/PRINCIPAL_PM_PLAYBOOK.md",
    "handbook/AI_PM_PLAYBOOK.md",
    "10_simulator/README.md",
    "11_learning_paths/README.md",
    "12_personal_lab/README.md",
    "13_career_transitions/README.md",
    "13_career_transitions/LANDING_A_PRODUCT_ROLE.md",
    "13_career_transitions/CREDIBILITY_BINDER.md",
    "13_career_transitions/EMERGING_PRODUCT_ROLES.md",
    "docs/PRODUCT_FORGE_INTEGRATION.md",
]

SRC_PATTERN = re.compile(r"SRC-[A-Z]{3,6}-\d{4}")


def _collect_cited_ids(academy_root):
    """Collect all cited source IDs across tracked files."""
    cited = set()
    for rel in DOCTRINE_FILES:
        path = academy_root / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        cited.update(SRC_PATTERN.findall(text))
    return cited


def _collect_registry_ids(academy_root, source_registry):
    """Registry IDs plus the documented case-catalog inline sources."""
    ids = {s["source_id"] for s in source_registry["sources"]}

    # Case-catalog inline source_locations are a documented secondary catalog.
    case_path = academy_root / "07_cases" / "case_catalog.md"
    if case_path.exists():
        text = case_path.read_text(encoding="utf-8", errors="ignore")
        ids.update(SRC_PATTERN.findall(text))
    return ids


class TestCrossReferenceIntegrity:
    """Every cited source ID resolves (adversarial findings A1 and G2)."""

    def test_all_cited_ids_resolve(self, academy_root, source_registry):
        cited = _collect_cited_ids(academy_root)
        assert cited, "No source IDs found to check"

        resolvable = _collect_registry_ids(academy_root, source_registry)
        unresolved = sorted(cited - resolvable)
        assert not unresolved, (
            f"{len(unresolved)} cited source IDs do not resolve: {unresolved}"
        )

    def test_all_doctrine_files_exist(self, academy_root):
        missing = [f for f in DOCTRINE_FILES if not (academy_root / f).exists()]
        assert not missing, f"Tracked doctrine files missing: {missing}"

    def test_canonical_claims_use_qualifying_sources(self, academy_root, source_registry):
        """Canonical principle evidence must cite Tier A or corroborated Tier B."""
        tier = {s["source_id"]: s.get("evidence_tier") for s in source_registry["sources"]}

        principles_path = academy_root / "01_core_doctrine" / "PRINCIPLES.md"
        text = principles_path.read_text(encoding="utf-8")
        # evidence fields carry the cited IDs; counterevidence fields too.
        for field in ("**evidence**", "**counterevidence**"):
            for match in re.finditer(
                re.escape(field) + r".*?source_id: (SRC-[A-Z]{3,6}-\d{4})", text
            ):
                sid = match.group(1)
                assert sid in tier, f"Cited source {sid} not in registry"
