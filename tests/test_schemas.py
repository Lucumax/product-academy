"""Schema-specific tests with jsonschema validation where available."""

import json
from pathlib import Path

import pytest

try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


class TestSourceSchemaValidation:
    """Validate source registry records against source.schema.json."""

    @pytest.mark.skipif(not HAS_JSONSCHEMA, reason="jsonschema not installed")
    def test_source_records_validate_against_schema(self, source_registry, source_schema):
        for source in source_registry["sources"]:
            try:
                jsonschema.validate(instance=source, schema=source_schema)
            except jsonschema.ValidationError as e:
                pytest.fail(
                    f"Source {source.get('source_id', 'UNKNOWN')} "
                    f"fails schema validation: {e.message}"
                )

    @pytest.mark.skipif(not HAS_JSONSCHEMA, reason="jsonschema not installed")
    def test_source_schema_itself_is_valid(self, source_schema):
        jsonschema.Draft7Validator.check_schema(source_schema)

    def test_source_schema_has_expected_properties(self, source_schema):
        props = source_schema.get("properties", {})
        assert "source_id" in props
        assert "evidence_tier" in props
        assert "transcript_status" in props
        assert "canonical_claims_supported" in props

    def test_evidence_tier_enum_values(self, source_schema):
        tier_enum = source_schema["properties"]["evidence_tier"]["enum"]
        assert "A" in tier_enum
        assert "E" in tier_enum
        assert len(tier_enum) == 5
        assert set(tier_enum) == {"A", "B", "C", "D", "E"}

    def test_transcript_status_enum_values(self, source_schema):
        status_enum = source_schema["properties"]["transcript_status"]["enum"]
        assert "VERIFIED_CREATOR_TRANSCRIPT" in status_enum
        assert "NOT_APPLICABLE" in status_enum
        assert len(status_enum) == 7


class TestPrincipleSchemaValidation:
    """Validate principle schema structure."""

    def test_principle_schema_requires_evidence(self, principle_schema):
        required = principle_schema.get("required", [])
        assert "evidence" in required, "Principle schema must require evidence"

    def test_principle_schema_requires_counterevidence(self, principle_schema):
        required = principle_schema.get("required", [])
        assert "counterevidence" in required, (
            "Principle schema must require counterevidence"
        )

    @pytest.mark.skipif(not HAS_JSONSCHEMA, reason="jsonschema not installed")
    def test_principle_schema_itself_is_valid(self, principle_schema):
        jsonschema.Draft7Validator.check_schema(principle_schema)

    def test_principle_confidence_enum_values(self, principle_schema):
        conf_enum = principle_schema["properties"]["confidence"]["enum"]
        assert "high" in conf_enum
        assert "speculative" in conf_enum
        assert len(conf_enum) == 4


class TestCaseSchemaValidation:
    """Validate case schema structure."""

    def test_case_schema_requires_causal_confidence(self, case_schema):
        required = case_schema.get("required", [])
        assert "causal_confidence" in required

    def test_case_schema_causal_confidence_enum(self, case_schema):
        conf_enum = case_schema["properties"]["causal_confidence"]["enum"]
        assert "high" in conf_enum
        assert "correlation_only" in conf_enum
        assert "retrospective_narrative" in conf_enum

    @pytest.mark.skipif(not HAS_JSONSCHEMA, reason="jsonschema not installed")
    def test_case_schema_itself_is_valid(self, case_schema):
        jsonschema.Draft7Validator.check_schema(case_schema)


class TestYAMLFiles:
    """Validate all YAML files parse correctly."""

    def test_registry_yaml_parses(self, source_registry):
        assert isinstance(source_registry, dict)
        assert "sources" in source_registry

    def test_contradictions_yaml_parses(self, contradiction_register):
        assert isinstance(contradiction_register, dict)
        assert "contradictions" in contradiction_register

    def test_claims_inventory_yaml_parses(self, academy_root):
        if not HAS_YAML:
            pytest.skip("pyyaml not installed")
        claims_path = academy_root / "research" / "extracted_claims" / "claims_inventory.yaml"
        if claims_path.exists():
            with open(claims_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            assert isinstance(data, dict)
            assert "claims" in data


class TestConflictSchemaCompliance:
    """Manual structural validation when jsonschema is not available."""

    def test_source_schema_structure_manual(self):
        """Even without jsonschema, verify basic JSON structure."""
        schemas_dir = Path(__file__).resolve().parent.parent / "schemas"
        for schema_name in ["source.schema.json", "principle.schema.json", "case.schema.json"]:
            path = schemas_dir / schema_name
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            assert "$schema" in data, f"{schema_name} missing $schema"
            assert "type" in data, f"{schema_name} missing type"
            assert data["type"] == "object", (
                f"{schema_name} type is not object"
            )
            assert "properties" in data, f"{schema_name} missing properties"


class TestJSONFilesAreValid:
    """Validate all JSON files in schemas and sources directories."""

    def test_schema_json_files_parse(self, academy_root):
        schemas_dir = academy_root / "schemas"
        for json_file in sorted(schemas_dir.glob("*.json")):
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    json.load(f)
            except json.JSONDecodeError as e:
                pytest.fail(f"Invalid JSON in {json_file.name}: {e}")

    def test_source_json_files_parse(self, academy_root):
        sources_dir = academy_root / "sources"
        for json_file in sorted(sources_dir.glob("*.json")):
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    json.load(f)
            except json.JSONDecodeError as e:
                pytest.fail(f"Invalid JSON in sources/{json_file.name}: {e}")
