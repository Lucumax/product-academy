"""Pytest fixtures for Product Leadership Academy tests."""

import json
import os
import sys
from pathlib import Path

import pytest

try:
    import yaml
except ImportError:
    yaml = None


ACADEMY_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="session")
def academy_root():
    return ACADEMY_ROOT


@pytest.fixture(scope="session")
def scripts_dir(academy_root):
    return academy_root / "scripts"


@pytest.fixture(scope="session")
def schemas_dir(academy_root):
    return academy_root / "schemas"


@pytest.fixture(scope="session")
def sources_dir(academy_root):
    return academy_root / "sources"


def _load_yaml(path):
    if yaml is None:
        pytest.skip("pyyaml not installed")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def load_yaml():
    return _load_yaml


@pytest.fixture(scope="session")
def load_json():
    return _load_json


@pytest.fixture(scope="session")
def source_registry(academy_root):
    path = academy_root / "sources" / "registry.yaml"
    return _load_yaml(path)


@pytest.fixture(scope="session")
def contradiction_register(academy_root):
    path = academy_root / "08_contradictions" / "register.yaml"
    return _load_yaml(path)


@pytest.fixture(scope="session")
def source_schema(academy_root):
    path = academy_root / "schemas" / "source.schema.json"
    return _load_json(path)


@pytest.fixture(scope="session")
def principle_schema(academy_root):
    path = academy_root / "schemas" / "principle.schema.json"
    return _load_json(path)


@pytest.fixture(scope="session")
def case_schema(academy_root):
    path = academy_root / "schemas" / "case.schema.json"
    return _load_json(path)


@pytest.fixture(scope="session")
def all_md_files(academy_root):
    return list(academy_root.rglob("*.md"))


@pytest.fixture(scope="session")
def all_yaml_files(academy_root):
    return list(academy_root.rglob("*.yaml")) + list(academy_root.rglob("*.yml"))


@pytest.fixture(scope="session")
def all_json_files(academy_root):
    return list(academy_root.rglob("*.json"))
