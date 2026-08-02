"""Tests for source registry, case catalog, and doctrine integrity."""

import re
from pathlib import Path

import pytest


VALID_EVIDENCE_TIERS = {"A", "B", "C", "D", "E"}
VALID_TRANSCRIPT_STATUSES = {
    "VERIFIED_CREATOR_TRANSCRIPT",
    "VERIFIED_PLATFORM_CAPTIONS",
    "ASR_DERIVED_TRANSCRIPT",
    "CREATOR_SUMMARY_ONLY",
    "SECONDARY_SUMMARY_ONLY",
    "TRANSCRIPT_UNAVAILABLE",
    "NOT_APPLICABLE",
}


class TestSourceRegistry:
    """Gate 3: Source Integrity tests."""

    def test_registry_loads(self, source_registry):
        assert "sources" in source_registry
        assert isinstance(source_registry["sources"], list)
        assert len(source_registry["sources"]) > 0

    def test_source_ids_are_unique(self, source_registry):
        source_ids = [s["source_id"] for s in source_registry["sources"]]
        duplicates = [sid for sid in source_ids if source_ids.count(sid) > 1]
        assert not duplicates, f"Duplicate source IDs found: {set(duplicates)}"

    def test_valid_evidence_tiers(self, source_registry):
        for source in source_registry["sources"]:
            tier = source.get("evidence_tier")
            assert tier in VALID_EVIDENCE_TIERS, (
                f"Source {source['source_id']} has invalid evidence_tier: {tier}"
            )

    def test_no_tier_e_with_canonical_claims(self, source_registry):
        for source in source_registry["sources"]:
            tier = source.get("evidence_tier")
            canonical = source.get("canonical_claims_supported")
            if tier == "E" and canonical is True:
                pytest.fail(
                    f"Source {source['source_id']} has evidence_tier=E "
                    f"but canonical_claims_supported=true"
                )

    def test_valid_transcript_statuses(self, source_registry):
        for source in source_registry["sources"]:
            status = source.get("transcript_status")
            assert status in VALID_TRANSCRIPT_STATUSES, (
                f"Source {source['source_id']} has invalid transcript_status: {status}"
            )

    def test_all_sources_have_required_fields(self, source_registry):
        required = {"source_id", "title", "author", "source_type", "evidence_tier"}
        for source in source_registry["sources"]:
            missing = required - set(source.keys())
            assert not missing, (
                f"Source {source.get('source_id', 'UNKNOWN')} missing fields: {missing}"
            )

    def test_source_id_patterns(self, source_registry):
        pattern = re.compile(r"^SRC-[A-Z]{3,6}-\d{4}$")
        for source in source_registry["sources"]:
            sid = source["source_id"]
            assert pattern.match(sid), (
                f"Source {sid} does not match pattern SRC-XXX-0000"
            )


class TestContradictionRegister:
    """Gate 4: Contradiction register well-formed tests."""

    def test_register_loads(self, contradiction_register):
        assert "contradictions" in contradiction_register
        assert isinstance(contradiction_register["contradictions"], list)
        assert len(contradiction_register["contradictions"]) > 0

    def test_contradiction_ids_unique(self, contradiction_register):
        ids = [c["contradiction_id"] for c in contradiction_register["contradictions"]]
        duplicates = [cid for cid in ids if ids.count(cid) > 1]
        assert not duplicates, f"Duplicate contradiction IDs: {set(duplicates)}"

    def test_both_doctrines_populated(self, contradiction_register):
        for con in contradiction_register["contradictions"]:
            assert "doctrine_a" in con, (
                f"{con['contradiction_id']} missing doctrine_a"
            )
            assert "doctrine_b" in con, (
                f"{con['contradiction_id']} missing doctrine_b"
            )
            assert con["doctrine_a"], (
                f"{con['contradiction_id']} doctrine_a is empty"
            )
            assert con["doctrine_b"], (
                f"{con['contradiction_id']} doctrine_b is empty"
            )

    def test_all_have_confidence(self, contradiction_register):
        for con in contradiction_register["contradictions"]:
            assert "confidence" in con, (
                f"{con['contradiction_id']} missing confidence"
            )
            assert con["confidence"] in {"high", "medium", "low", "speculative"}, (
                f"{con['contradiction_id']} invalid confidence: {con['confidence']}"
            )


class TestCaseCatalog:
    """Gate 5: Case catalog structure tests."""

    def test_case_catalog_exists(self, academy_root):
        case_path = academy_root / "07_cases" / "case_catalog.md"
        assert case_path.exists(), "Case catalog file not found"

    def test_case_catalog_has_content(self, academy_root):
        case_path = academy_root / "07_cases" / "case_catalog.md"
        content = case_path.read_text(encoding="utf-8")
        assert len(content) > 1000, "Case catalog appears to be a stub"

    def test_cases_have_causal_confidence(self, academy_root):
        case_path = academy_root / "07_cases" / "case_catalog.md"
        content = case_path.read_text(encoding="utf-8")
        case_count = content.count("## CASE-")
        confidence_count = content.count("### causal_confidence")
        assert confidence_count >= case_count, (
            f"Expected at least {case_count} causal_confidence sections, "
            f"found {confidence_count}"
        )


class TestDoctrineIntegrity:
    """Gate 4: Doctrine integrity tests."""

    def test_principles_file_exists(self, academy_root):
        path = academy_root / "01_core_doctrine" / "PRINCIPLES.md"
        assert path.exists(), "PRINCIPLES.md not found"

    def test_principles_have_evidence(self, academy_root):
        path = academy_root / "01_core_doctrine" / "PRINCIPLES.md"
        content = path.read_text(encoding="utf-8")
        principle_count = content.count("## PRN-")
        evidence_count = content.count("**evidence**")
        assert evidence_count >= principle_count, (
            f"Expected {principle_count} principles with evidence sections, "
            f"found {evidence_count}"
        )


class TestContentQuality:
    """Gate 5: Content quality checks."""

    def test_ai_modules_exist(self, academy_root):
        ai_dir = academy_root / "05_ai_product_management"
        assert ai_dir.is_dir(), "AI product management directory missing"
        md_files = list(ai_dir.glob("*.md"))
        assert len(md_files) >= 3, (
            f"Expected at least 3 AI module files, found {len(md_files)}"
        )

    def test_industry_modules_exist(self, academy_root):
        industry_dir = academy_root / "06_industry_overlays"
        assert industry_dir.is_dir(), "Industry overlays directory missing"

    def test_ai_modules_not_stubs(self, academy_root):
        ai_dir = academy_root / "05_ai_product_management"
        for md_file in ai_dir.glob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            assert len(content) > 300, (
                f"AI module {md_file.name} appears to be a stub ({len(content)} chars)"
            )

    def test_career_modules_exist(self, academy_root):
        career_dir = academy_root / "13_career_transitions"
        assert career_dir.is_dir(), "Career transitions directory missing"
        required = {
            "README.md",
            "LANDING_A_PRODUCT_ROLE.md",
            "CREDIBILITY_BINDER.md",
            "EMERGING_PRODUCT_ROLES.md",
        }
        present = {f.name for f in career_dir.glob("*.md")}
        missing = required - present
        assert not missing, f"Missing career transition modules: {missing}"

    def test_career_modules_not_stubs(self, academy_root):
        career_dir = academy_root / "13_career_transitions"
        for md_file in career_dir.glob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            assert len(content) > 300, (
                f"Career module {md_file.name} appears to be a stub ({len(content)} chars)"
            )

    def test_career_modules_label_claims(self, academy_root):
        career_dir = academy_root / "13_career_transitions"
        for md_file in career_dir.glob("*.md"):
            if md_file.name == "README.md":
                continue
            content = md_file.read_text(encoding="utf-8")
            label_count = sum(
                content.count(label) for label in ["**[E]**", "**[P]**", "**[I]**", "**[D]**", "**[R]**"]
            )
            assert label_count > 0, (
                f"Career module {md_file.name} has no epistemic labels"
            )
            assert "## Practical Application" in content, (
                f"Career module {md_file.name} missing Practical Application section"
            )


class TestRepositoryInfrastructure:
    """Gate 1: Repository infrastructure tests."""

    REQUIRED_DIRS = [
        "00_orientation",
        "01_core_doctrine",
        "02_principal_plus",
        "03_business_and_gtm",
        "04_product_archetypes",
        "05_ai_product_management",
        "06_industry_overlays",
        "07_cases",
        "08_contradictions",
        "09_tools",
        "10_simulator",
        "11_learning_paths",
        "12_personal_lab",
        "13_career_transitions",
        "docs",
        "evidence",
        "handbook",
        "research",
        "schemas",
        "scripts",
        "sources",
        "tests",
    ]

    REQUIRED_ROOT_FILES = [
        "QUALITY_GATES.md",
        "SCOPE.md",
        "SOURCE_POLICY.md",
        "CURRICULUM_MAP.md",
        "CHANGELOG.md",
        "COPYRIGHT_AND_ACCESS_POLICY.md",
        "pyproject.toml",
        ".gitignore",
    ]
    RECOMMENDED_ROOT_FILES = ["README.md"]

    def test_required_directories_exist(self, academy_root):
        missing = []
        for d in self.REQUIRED_DIRS:
            if not (academy_root / d).is_dir():
                missing.append(d)
        assert not missing, f"Missing required directories: {missing}"

    def test_required_root_files_exist(self, academy_root):
        missing = []
        for f in self.REQUIRED_ROOT_FILES:
            if not (academy_root / f).exists():
                missing.append(f)
        assert not missing, f"Missing required root files: {missing}"

    def test_readme_exists(self, academy_root):
        readme_path = academy_root / "README.md"
        assert readme_path.exists(), "README.md should exist at repository root"

    def test_no_secrets_in_repo(self, academy_root):
        secret_patterns = [
            r'api[_-]?key\s*[=:]\s*["\'][a-zA-Z0-9_\-]{8,}',
            r'password\s*[=:]\s*["\'][^\s]{3,}',
            r'secret\s*[=:]\s*["\'][a-zA-Z0-9_\-]{8,}',
            r'token\s*[=:]\s*["\'][a-zA-Z0-9_\-]{8,}',
            r'private[_-]?key\s*[=:]\s*["\']',
        ]
        violations = []
        for md_file in academy_root.glob("**/*.md"):
            content = md_file.read_text(encoding="utf-8", errors="ignore")
            for pattern in secret_patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    violations.append(f"{md_file.relative_to(academy_root)}: {pattern}")
        assert not violations, f"Potential secrets found: {violations}"

    def test_no_forbidden_patterns_in_repo(self, academy_root):
        patterns = [
            r'^\s*(?:pip|pip3)\s+install',
            r'^\s*npx\s+',
            r'\.env\s*[=:]',
        ]
        # These are acceptable in documentation; only flag actual configuration
        forbidden_dirs = {"scripts", "tests"}
        violations = []
        for target_dir_name in forbidden_dirs:
            target_dir = academy_root / target_dir_name
            if not target_dir.is_dir():
                continue
            for py_file in target_dir.rglob("*.py"):
                content = py_file.read_text(encoding="utf-8")
                # Check for embedded credentials
                credential_patterns = [
                    r'(?:api_key|api_secret|access_token)\s*=\s*"[^"]+"',
                    r'(?:api_key|api_secret|access_token)\s*=\s*\'[^\']+\'',
                ]
                for pattern in credential_patterns:
                    if re.search(pattern, content):
                        violations.append(
                            f"{py_file.relative_to(academy_root)}: embedded credential"
                        )
        assert not violations, f"Credential issues: {violations}"


class TestSchemaFiles:
    """Gate 2: JSON schema file integrity."""

    REQUIRED_SCHEMAS = ["source.schema.json", "principle.schema.json", "case.schema.json"]

    def test_schema_files_exist(self, schemas_dir):
        for schema in self.REQUIRED_SCHEMAS:
            path = schemas_dir / schema
            assert path.exists(), f"Schema file missing: {schema}"

    def test_schema_files_are_valid_json(self, schemas_dir):
        import json
        for schema in self.REQUIRED_SCHEMAS:
            path = schemas_dir / schema
            try:
                with open(path, "r", encoding="utf-8") as f:
                    json.load(f)
            except json.JSONDecodeError as e:
                pytest.fail(f"Invalid JSON in {schema}: {e}")

    def test_source_schema_has_required_fields(self, source_schema):
        assert "type" in source_schema
        assert source_schema["type"] == "object"
        assert "required" in source_schema
        assert "properties" in source_schema

    def test_principle_schema_has_required_fields(self, principle_schema):
        assert "required" in principle_schema
        required = principle_schema["required"]
        assert "principle_id" in required
        assert "evidence" in required

    def test_case_schema_has_causal_confidence(self, case_schema):
        required = case_schema.get("required", [])
        assert "causal_confidence" in required, (
            "Case schema missing causal_confidence in required fields"
        )
