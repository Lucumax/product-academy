"""Tests for the webapp /skills/ SEO surface: pages, config, metadata, and data pipeline."""

import json
import re
import subprocess
import sys
from pathlib import Path

import pytest


@pytest.fixture(scope="module")
def webapp_root(academy_root):
    return academy_root / "webapp"


@pytest.fixture(scope="module")
def skills_root(academy_root):
    return academy_root / "skills"


class TestSkillPagesExist:
    def test_skills_pages_present(self, webapp_root):
        pages = webapp_root / "src" / "pages"
        for rel in [
            "skills/index.astro",
            "skills/[id].astro",
            "skills/install.astro",
            "skills/workflows/index.astro",
            "skills/workflows/[id].astro",
            "404.astro",
        ]:
            assert (pages / rel).exists(), f"missing page {rel}"

    def test_every_active_skill_has_a_route(self, webapp_root, skills_root):
        """The per-skill page must cover every active skill id."""
        active = []
        for d in skills_root.iterdir():
            if not d.is_dir() or d.name.startswith("_") or d.name in {"quality", "evals", "workflows"}:
                continue
            fm_file = d / "SKILL.md"
            if not fm_file.exists():
                continue
            text = fm_file.read_text(encoding="utf-8")
            if "deprecated: true" in text:
                continue
            active.append(d.name)
        page = (webapp_root / "src" / "pages" / "skills" / "[id].astro").read_text(encoding="utf-8")
        assert len(active) >= 12, "expected at least 12 active skills"
        # getStaticPaths iterates over the parsed skills data, so the id set is driven by data.
        assert "getStaticPaths" in page and "params: { id: s.id }" in page


class TestConfigAndMetadata:
    def test_site_config_not_placeholder(self, webapp_root):
        cfg = (webapp_root / "astro.config.mjs").read_text(encoding="utf-8")
        assert "product-academy.example.com" not in cfg, "placeholder site config must be gone"
        assert "site:" in cfg and "lucumax.github.io" in cfg
        assert 'base: "/product-academy"' in cfg
        assert "sitemap" in cfg, "sitemap integration missing"

    def test_robots_txt_declares_sitemap(self, webapp_root):
        robots = (webapp_root / "public" / "robots.txt").read_text(encoding="utf-8")
        assert "User-agent: *" in robots
        assert "Allow: /" in robots
        assert "Sitemap: https://lucumax.github.io/product-academy/sitemap-index.xml" in robots

    def test_base_layout_has_seo_head(self, webapp_root):
        base = (webapp_root / "src" / "layouts" / "Base.astro").read_text(encoding="utf-8")
        for token in [
            '<link rel="canonical"',
            'property="og:title"',
            'property="og:description"',
            'property="og:image"',
            'name="twitter:card"',
            'name="twitter:title"',
            'name="robots"',
            'rel="icon"',
            'href: "/skills/"',
        ]:
            assert token in base, f"Base.astro missing {token}"

    def test_canonical_does_not_double_the_base(self, webapp_root):
        """Canonical must be origin + pathname (pathname already includes /product-academy/)."""
        base = (webapp_root / "src" / "layouts" / "Base.astro").read_text(encoding="utf-8")
        assert "new URL(Astro.url.pathname, origin).href" in base, "canonical must use origin, not site+base"

    def test_nav_is_base_prefixed(self, webapp_root):
        """Internal nav must be prefixed with the Astro base so it works under the Pages subpath."""
        base = (webapp_root / "src" / "layouts" / "Base.astro").read_text(encoding="utf-8")
        assert "const base = Astro.base || \"/\";" in base
        assert "const b = (path) => base + path.replace(/^\\//, \"\");" in base
        assert "href={b(item.href)}" in base, "nav links must be base-prefixed"

    def test_no_noindex_by_default(self, webapp_root):
        base = (webapp_root / "src" / "layouts" / "Base.astro").read_text(encoding="utf-8")
        # noindex is opt-in via prop, not default
        assert "noindex" in base

    def test_homepage_links_to_skills(self, webapp_root):
        home = (webapp_root / "src" / "pages" / "index.astro").read_text(encoding="utf-8")
        assert "/skills/" in home


class TestImportPipeline:
    def test_content_import_produces_skill_data(self, webapp_root, skills_root):
        """Run the importer and assert data counts match the active skill set."""
        node = subprocess.run(
            [sys.executable and "node", "scripts/import-content.mjs"],
            cwd=str(webapp_root),
            capture_output=True,
            text=True,
        )
        assert node.returncode == 0, f"importer failed: {node.stderr[:500]}"
        data = json.loads((webapp_root / "src" / "data" / "skills.json").read_text(encoding="utf-8"))
        wf = json.loads((webapp_root / "src" / "data" / "skillWorkflows.json").read_text(encoding="utf-8"))
        active = [
            d.name
            for d in skills_root.iterdir()
            if d.is_dir()
            and not d.name.startswith("_")
            and d.name not in {"quality", "evals", "workflows"}
            and (d / "SKILL.md").exists()
            and "deprecated: true" not in (d / "SKILL.md").read_text(encoding="utf-8")
        ]
        assert len(data["skills"]) == len(active), (
            f"imported {len(data['skills'])} skills, expected {len(active)}"
        )
        assert len(wf["workflows"]) == 4
        for s in data["skills"]:
            assert s["id"] in active
            assert s["purpose"], f"{s['id']} missing purpose"
            assert s["verdict"], f"{s['id']} missing verdict"
        for w in wf["workflows"]:
            assert w["entryConditions"], f"workflow {w['id']} missing entry conditions"
            assert w["finalOutput"], f"workflow {w['id']} missing final output"

    def test_skill_pages_cover_all_imported_skills(self, webapp_root):
        data = json.loads((webapp_root / "src" / "data" / "skills.json").read_text(encoding="utf-8"))
        landing = (webapp_root / "src" / "pages" / "skills" / "index.astro").read_text(encoding="utf-8")
        for s in data["skills"]:
            assert s["id"] in landing, f"landing page missing skill {s['id']}"
