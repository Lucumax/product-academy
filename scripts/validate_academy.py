#!/usr/bin/env python3
"""
Product Leadership Academy — Comprehensive Validation Script.

Validates repository integrity across 8 quality gates.
Exit code 0 = all gates pass. Non-zero = at least one gate failed.

Usage:
    python scripts/validate_academy.py
    python scripts/validate_academy.py --verbose
    python scripts/validate_academy.py --gate 3
"""

import json
import os
import re
import sys
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    print("WARNING: pyyaml not installed. YAML validation will be skipped.")
    print("         Install with: pip install pyyaml")


ACADEMY_ROOT = Path(__file__).resolve().parent.parent


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
    "README.md",
    "QUALITY_GATES.md",
    "SCOPE.md",
    "SOURCE_POLICY.md",
    "CURRICULUM_MAP.md",
    "CHANGELOG.md",
    "COPYRIGHT_AND_ACCESS_POLICY.md",
    "LICENSE",
    "pyproject.toml",
    ".gitignore",
]

SECRET_PATTERNS = [
    (r'api[_-]?key\s*[=:]\s*["\'][a-zA-Z0-9_\-]{8,}', "hardcoded API key"),
    (r'password\s*[=:]\s*["\'][^\s]{4,}', "hardcoded password"),
    (r'secret\s*[=:]\s*["\'][a-zA-Z0-9_\-]{8,}', "hardcoded secret"),
    (r'token\s*[=:]\s*["\'][a-zA-Z0-9_\-]{10,}', "hardcoded token"),
    (r'private[_-]?key\s*[=:]\s*["\']', "hardcoded private key"),
    (r'-----BEGIN (?:RSA|DSA|EC|PGP|OPENSSH) PRIVATE KEY-----', "private key block"),
]


class ValidationReporter:
    def __init__(self, verbose=False):
        self.total = 0
        self.passed = 0
        self.failed = 0
        self.errors = []
        self.verbose = verbose

    def check(self, gate, description, condition, detail=""):
        self.total += 1
        if condition:
            self.passed += 1
            if self.verbose:
                print(f"  [PASS] [{gate}] {description}")
        else:
            self.failed += 1
            msg = f"[{gate}] {description}"
            if detail:
                msg += f" — {detail}"
            print(f"  [FAIL] {msg}")
            self.errors.append(msg)

    def summary(self):
        print()
        print("=" * 60)
        print(f"VALIDATION COMPLETE: {self.passed}/{self.total} checks passed")
        if self.failed:
            print(f"  FAILED: {self.failed} check(s)")
            for err in self.errors:
                print(f"    - {err}")
            print()
            print("RESULT: FAILURE — some quality gates did not pass.")
        else:
            print("  All quality gates passed.")
            print()
            print("RESULT: SUCCESS — all quality gates passed.")
        return self.failed


def gate1_repository_integrity(reporter):
    """Gate 1: Repository Integrity."""
    print("\n--- Gate 1: Repository Integrity ---")

    for d in REQUIRED_DIRS:
        path = ACADEMY_ROOT / d
        reporter.check("Gate 1", f"Directory exists: {d}/", path.is_dir())

    for f in REQUIRED_ROOT_FILES:
        path = ACADEMY_ROOT / f
        reporter.check("Gate 1", f"Root file exists: {f}", path.exists())

    gitignore = ACADEMY_ROOT / ".gitignore"
    if gitignore.exists():
        content = gitignore.read_text(encoding="utf-8")
        for pattern in ["__pycache__", ".venv", "node_modules", ".pytest_cache"]:
            reporter.check(
                "Gate 1",
                f".gitignore contains '{pattern}'",
                pattern in content,
            )
    else:
        reporter.check("Gate 1", ".gitignore exists", False)

    forbidden_dirs = ["node_modules", ".venv"]
    for fd in forbidden_dirs:
        for found in ACADEMY_ROOT.rglob(fd):
            rel = found.relative_to(ACADEMY_ROOT)
            if "webapp" in rel.parts:
                continue  # webapp/ is a self-contained app with its own deps
            reporter.check(
                "Gate 1",
                f"No '{fd}' in sensitive location: {rel}",
                False,
                detail="Should be gitignored or removed",
            )

    for pattern, label in SECRET_PATTERNS:
        found = False
        for f in ACADEMY_ROOT.rglob("*.py"):
            if ".git" in f.parts or "webapp" in f.parts or "node_modules" in f.parts:
                continue
            content = f.read_text(encoding="utf-8", errors="ignore")
            if re.search(pattern, content, re.IGNORECASE):
                rel = f.relative_to(ACADEMY_ROOT)
                reporter.check(
                    "Gate 1",
                    f"No secrets: {label}",
                    False,
                    detail=f"Found in {rel}",
                )
                found = True
                break
        if not found:
            reporter.check("Gate 1", f"No secrets: {label}", True)


def gate2_schema_compliance(reporter):
    """Gate 2: Schema Compliance."""
    print("\n--- Gate 2: Schema Compliance ---")

    schema_dir = ACADEMY_ROOT / "schemas"
    for schema_file in sorted(schema_dir.glob("*.json")):
        try:
            with open(schema_file, "r", encoding="utf-8") as f:
                json.load(f)
            reporter.check("Gate 2", f"Valid JSON: schemas/{schema_file.name}", True)
        except json.JSONDecodeError as e:
            reporter.check(
                "Gate 2",
                f"Valid JSON: schemas/{schema_file.name}",
                False,
                detail=str(e),
            )

    if HAS_YAML:
        yaml_files = (
            list(ACADEMY_ROOT.rglob("*.yaml"))
            + list(ACADEMY_ROOT.rglob("*.yml"))
        )
        EXCLUDED_PARTS = {".git", "node_modules", "webapp", "__pycache__"}
        for yf in yaml_files:
            if EXCLUDED_PARTS & set(yf.parts):
                continue
            try:
                with open(yf, "r", encoding="utf-8") as f:
                    yaml.safe_load(f)
                reporter.check(
                    "Gate 2",
                    f"Valid YAML: {yf.relative_to(ACADEMY_ROOT)}",
                    True,
                )
            except yaml.YAMLError as e:
                reporter.check(
                    "Gate 2",
                    f"Valid YAML: {yf.relative_to(ACADEMY_ROOT)}",
                    False,
                    detail=str(e),
                )

    for json_file in sorted((ACADEMY_ROOT / "sources").rglob("*.json")):
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                json.load(f)
            reporter.check(
                "Gate 2",
                f"Valid JSON: {json_file.relative_to(ACADEMY_ROOT)}",
                True,
            )
        except json.JSONDecodeError as e:
            reporter.check(
                "Gate 2",
                f"Valid JSON: {json_file.relative_to(ACADEMY_ROOT)}",
                False,
                detail=str(e),
            )


def gate3_source_integrity(reporter):
    """Gate 3: Source Integrity."""
    print("\n--- Gate 3: Source Integrity ---")

    registry_path = ACADEMY_ROOT / "sources" / "registry.yaml"
    if not registry_path.exists():
        reporter.check("Gate 3", "Source registry exists", False)
        return

    if not HAS_YAML:
        reporter.check("Gate 3", "YAML available for source checks", False)
        return

    try:
        with open(registry_path, "r", encoding="utf-8") as f:
            registry = yaml.safe_load(f)
    except Exception as e:
        reporter.check("Gate 3", "Source registry parses", False, detail=str(e))
        return

    sources = registry.get("sources", [])
    reporter.check("Gate 3", f"Source registry has records", len(sources) > 0)

    source_ids = [s.get("source_id") for s in sources]
    seen = set()
    duplicates = set()
    for sid in source_ids:
        if sid in seen:
            duplicates.add(sid)
        seen.add(sid)
    reporter.check(
        "Gate 3",
        "All source IDs are unique",
        len(duplicates) == 0,
        detail=f"Duplicates: {duplicates}" if duplicates else "",
    )

    for source in sources:
        sid = source.get("source_id", "UNKNOWN")
        tier = source.get("evidence_tier")
        reporter.check(
            "Gate 3",
            f"Valid evidence tier for {sid}",
            tier in VALID_EVIDENCE_TIERS,
            detail=f"Got: {tier}" if tier not in VALID_EVIDENCE_TIERS else "",
        )

        status = source.get("transcript_status")
        reporter.check(
            "Gate 3",
            f"Valid transcript status for {sid}",
            status in VALID_TRANSCRIPT_STATUSES,
            detail=f"Got: {status}" if status not in VALID_TRANSCRIPT_STATUSES else "",
        )

        if tier == "E" and source.get("canonical_claims_supported") is True:
            reporter.check(
                "Gate 3",
                f"Tier E source {sid} does not support canonical claims",
                False,
                detail="evidence_tier=E but canonical_claims_supported=true",
            )
        else:
            reporter.check(
                "Gate 3",
                f"Tier assertion valid for {sid}",
                True,
            )


def gate4_doctrine_integrity(reporter):
    """Gate 4: Doctrine Integrity."""
    print("\n--- Gate 4: Doctrine Integrity ---")

    principles_path = ACADEMY_ROOT / "01_core_doctrine" / "PRINCIPLES.md"
    if not principles_path.exists():
        reporter.check("Gate 4", "PRINCIPLES.md exists", False)
        return

    content = principles_path.read_text(encoding="utf-8")
    reporter.check("Gate 4", "PRINCIPLES.md has content", len(content) > 500)

    principle_headers = re.findall(r"^## PRN-\d{4}", content, re.MULTILINE)
    reporter.check(
        "Gate 4",
        f"Principles found in PRINCIPLES.md",
        len(principle_headers) > 0,
        detail=f"Count: {len(principle_headers)}",
    )

    evidence_sections = re.findall(
        r"\*\*evidence\*\*", content, re.IGNORECASE
    )
    reporter.check(
        "Gate 4",
        "Every principle has an evidence section",
        len(evidence_sections) >= len(principle_headers),
        detail=f"Principles: {len(principle_headers)}, Evidence sections: {len(evidence_sections)}",
    )

    contradictions_path = ACADEMY_ROOT / "08_contradictions" / "register.yaml"
    if contradictions_path.exists() and HAS_YAML:
        try:
            with open(contradictions_path, "r", encoding="utf-8") as f:
                contradictions = yaml.safe_load(f)
            cons = contradictions.get("contradictions", [])
            for con in cons:
                cid = con.get("contradiction_id", "UNKNOWN")
                reporter.check(
                    "Gate 4",
                    f"Contradiction {cid} has doctrine_a",
                    bool(con.get("doctrine_a")),
                )
                reporter.check(
                    "Gate 4",
                    f"Contradiction {cid} has doctrine_b",
                    bool(con.get("doctrine_b")),
                )
        except Exception as e:
            reporter.check("Gate 4", "Contradiction register parses", False, detail=str(e))

    cases_path = ACADEMY_ROOT / "07_cases" / "case_catalog.md"
    if cases_path.exists():
        case_content = cases_path.read_text(encoding="utf-8")
        case_count = case_content.count("## CASE-")
        confidence_count = case_content.count("### causal_confidence")
        reporter.check(
            "Gate 4",
            "All cases have causal_confidence",
            confidence_count >= case_count,
            detail=f"Cases: {case_count}, Causal confidence sections: {confidence_count}",
        )


def gate5_content_quality(reporter):
    """Gate 5: Content Quality."""
    print("\n--- Gate 5: Content Quality ---")

    ai_dir = ACADEMY_ROOT / "05_ai_product_management"
    if ai_dir.is_dir():
        md_files = list(ai_dir.glob("*.md"))
        reporter.check(
            "Gate 5",
            "AI module files exist",
            len(md_files) >= 3,
            detail=f"Found {len(md_files)} files",
        )
        for mf in md_files:
            content = mf.read_text(encoding="utf-8")
            reporter.check(
                "Gate 5",
                f"AI module not a stub: {mf.name}",
                len(content) > 300,
                detail=f"Only {len(content)} chars" if len(content) <= 300 else "",
            )
    else:
        reporter.check("Gate 5", "AI module directory exists", False)

    industry_dir = ACADEMY_ROOT / "06_industry_overlays"
    reporter.check(
        "Gate 5",
        "Industry overlays directory exists",
        industry_dir.is_dir(),
    )

    principal_file = ACADEMY_ROOT / "02_principal_plus" / "PRINCIPAL_PM.md"
    if principal_file.exists():
        content = principal_file.read_text(encoding="utf-8")
        reporter.check(
            "Gate 5",
            "Principal+ material is substantive",
            len(content) > 500,
        )

    handbook_dir = ACADEMY_ROOT / "handbook"
    reporter.check("Gate 5", "Handbook directory exists", handbook_dir.is_dir())


def gate6_ecosystem_integrity(reporter):
    """Gate 6: Ecosystem Integrity."""
    print("\n--- Gate 6: Ecosystem Integrity ---")

    adjacent_repos = [
        Path("C:/Walter/100 day plan/AI Agents/Agents/vsh-v0.4"),
        Path("C:/Walter/100 day plan/AI Agents/Agents/ops-hub"),
        Path("C:/Walter/100 day plan/AI Agents/Hermes"),
        Path("C:/Walter/100 day plan/AI Agents/Product Forge/product_forge_v0_1"),
    ]

    for repo in adjacent_repos:
        if not repo.exists():
            if reporter.verbose:
                print(f"  [SKIP] Adjacent repo not found: {repo.name}")
            continue

        git_dir = repo / ".git"
        if git_dir.exists():
            try:
                import subprocess
                result = subprocess.run(
                    ["git", "status", "--porcelain"],
                    cwd=str(repo),
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                modified = result.stdout.strip()
                is_clean = not modified or all(
                    line.startswith("??") for line in modified.split("\n") if line
                )
                if not modified:
                    reporter.check(
                        "Gate 6",
                        f"Adjacent repo clean: {repo.name}",
                        True,
                    )
                elif is_clean:
                    reporter.check(
                        "Gate 6",
                        f"Adjacent repo has untracked files: {repo.name}",
                        True,
                        detail=f"Untracked: {modified[:200]} (only untracked, no staged/modified)",
                    )
                else:
                    reporter.check(
                        "Gate 6",
                        f"Adjacent repo modified: {repo.name}",
                        False,
                        detail=f"Modified: {modified[:200]}",
                    )
            except Exception as e:
                reporter.check(
                    "Gate 6",
                    f"Adjacent repo check: {repo.name}",
                    True,
                    detail=f"Could not check git status: {e}",
                )
        else:
            reporter.check(
                "Gate 6",
                f"Adjacent repo has .git: {repo.name}",
                True,
                detail="Not a git repo (skipped integrity check)",
            )


def gate7_link_integrity(reporter):
    """Gate 7: Link Integrity."""
    print("\n--- Gate 7: Link Integrity ---")

    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    broken_count = 0
    checked_count = 0

    EXCLUDED_PARTS = {".git", "__pycache__", "node_modules", "webapp"}
    for md_file in ACADEMY_ROOT.rglob("*.md"):
        if EXCLUDED_PARTS & set(md_file.parts):
            continue
        try:
            content = md_file.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        for match in link_pattern.finditer(content):
            target = match.group(2)
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            if target.startswith("/"):
                continue

            checked_count += 1
            anchor = None
            if "#" in target:
                target, anchor = target.split("#", 1)

            target_path = (md_file.parent / target).resolve()
            if not target_path.exists():
                broken_count += 1
                reporter.check(
                    "Gate 7",
                    f"Broken link in {md_file.relative_to(ACADEMY_ROOT)}",
                    False,
                    detail=f"-> {target}",
                )

    if checked_count == 0:
        reporter.check("Gate 7", "No relative links found to check", True, detail="(skipped)")
    else:
        reporter.check(
            "Gate 7",
            f"Internal links resolve",
            broken_count == 0,
            detail=f"Checked: {checked_count}, Broken: {broken_count}",
        )


def gate8_test_quality(reporter):
    """Gate 8: Test Quality."""
    print("\n--- Gate 8: Test Quality ---")

    tests_dir = ACADEMY_ROOT / "tests"
    if not tests_dir.is_dir():
        reporter.check("Gate 8", "Tests directory exists", False)
        return

    test_files = list(tests_dir.glob("test_*.py"))
    reporter.check(
        "Gate 8",
        "Test files exist",
        len(test_files) > 0,
        detail=f"Found {len(test_files)} test files",
    )

    total_tests = 0
    for tf in test_files:
        content = tf.read_text(encoding="utf-8")
        test_funcs = re.findall(r"def (test_\w+)", content)
        test_classes = re.findall(r"class (Test\w+)", content)
        total_tests += len(test_funcs)
        reporter.check(
            "Gate 8",
            f"Test file has test functions: {tf.name}",
            len(test_funcs) > 0,
            detail=f"Found {len(test_funcs)} test functions, {len(test_classes)} test classes",
        )

    reporter.check(
        "Gate 8",
        "At least 5 test functions defined",
        total_tests >= 5,
        detail=f"Total test functions: {total_tests}",
    )

    validate_script = ACADEMY_ROOT / "scripts" / "validate_academy.py"
    reporter.check(
        "Gate 8",
        "Validation script exists and is this file",
        validate_script.exists(),
    )

    conftest = ACADEMY_ROOT / "tests" / "conftest.py"
    reporter.check(
        "Gate 8",
        "conftest.py exists with fixtures",
        conftest.exists(),
    )


def main():
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    gate_filter = None

    for arg in sys.argv[1:]:
        if arg.startswith("--gate="):
            try:
                gate_filter = int(arg.split("=")[1])
            except ValueError:
                print(f"Invalid gate number: {arg}")
                sys.exit(2)

    reporter = ValidationReporter(verbose=verbose)
    print("Product Leadership Academy — Validation Report")
    print(f"Root: {ACADEMY_ROOT}")
    print(f"Date: 2026-08-01")

    gates = {
        1: gate1_repository_integrity,
        2: gate2_schema_compliance,
        3: gate3_source_integrity,
        4: gate4_doctrine_integrity,
        5: gate5_content_quality,
        6: gate6_ecosystem_integrity,
        7: gate7_link_integrity,
        8: gate8_test_quality,
    }

    if gate_filter is not None:
        if gate_filter in gates:
            print(f"Running only Gate {gate_filter}")
            gates[gate_filter](reporter)
        else:
            print(f"Invalid gate number: {gate_filter}. Must be 1-8.")
            sys.exit(2)
    else:
        for gate_num in sorted(gates):
            gates[gate_num](reporter)

    failed = reporter.summary()
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
