#!/usr/bin/env node
/**
 * Product Academy content importer.
 *
 * Reads the Product Leadership Academy repository and produces:
 *   - src/content/    — every markdown file, namespaced by track
 *   - src/data/*.json — structured index data
 *
 * Includes:
 *   - tracks, principles, cases, contradictions, sources (with URLs + claims)
 *   - curriculum: learning paths parsed into phases → weeks → steps
 *   - evidence graph: claims by source, principles by contradiction/case
 *
 * Source path: env PRODUCT_ACADEMY_SOURCE or ../product-leadership-academy.
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import YAML from "yaml";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const WEB_ROOT = path.resolve(__dirname, "..");
// Monorepo: webapp/ lives inside the Academy repo, so the content source is
// the repo root (parent of webapp/). Override with PRODUCT_ACADEMY_SOURCE.
const DEFAULT_SOURCE = path.resolve(WEB_ROOT, "..");
const SOURCE = process.env.PRODUCT_ACADEMY_SOURCE || DEFAULT_SOURCE;

const CONTENT_DIR = path.join(WEB_ROOT, "src", "content");
const DATA_DIR = path.join(WEB_ROOT, "src", "data");

function ensureDir(p) {
  fs.mkdirSync(p, { recursive: true });
}

function readText(p) {
  return fs.readFileSync(p, "utf-8");
}

function writeJson(name, obj) {
  fs.writeFileSync(path.join(DATA_DIR, name), JSON.stringify(obj, null, 2), "utf-8");
}

function slugify(s) {
  return s
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

// ---------------------------------------------------------------------------
// Tracks
// ---------------------------------------------------------------------------

const TRACK_DIRS = [
  "00_orientation", "01_core_doctrine", "02_principal_plus", "03_business_and_gtm",
  "04_product_archetypes", "05_ai_product_management", "06_industry_overlays",
  "07_cases", "08_contradictions", "09_tools", "10_simulator", "11_learning_paths",
  "12_personal_lab", "13_career_transitions", "handbook", "docs",
];

const TRACK_TITLES = {
  "00_orientation": "Orientation",
  "01_core_doctrine": "Core Doctrine",
  "02_principal_plus": "Principal Plus",
  "03_business_and_gtm": "Business and Go-to-Market",
  "04_product_archetypes": "Product Archetypes",
  "05_ai_product_management": "AI Product Management",
  "06_industry_overlays": "Industry Overlays",
  "07_cases": "Cases",
  "08_contradictions": "Contradictions",
  "09_tools": "Tools",
  "10_simulator": "Simulator",
  "11_learning_paths": "Learning Paths",
  "12_personal_lab": "Personal Lab",
  "13_career_transitions": "Career Transitions",
  "handbook": "Handbook",
  "docs": "Integration Docs",
};

const HIDE_FROM_TRACK_PAGES = new Set(["handbook", "docs"]);

function walkMd(dirAbs, trackId) {
  const items = [];
  const entries = fs.readdirSync(dirAbs, { withFileTypes: true });
  for (const e of entries) {
    const full = path.join(dirAbs, e.name);
    if (e.isDirectory()) {
      items.push(...walkMd(full, trackId));
    } else if (e.isFile() && e.name.endsWith(".md")) {
      items.push({
        name: e.name,
        path: `${trackId}/${path.relative(path.join(SOURCE, trackId), full).replace(/\\/g, "/")}`,
      });
    }
  }
  return items;
}

function collectTracks() {
  const tracks = [];
  for (const dir of TRACK_DIRS) {
    const abs = path.join(SOURCE, dir);
    if (!fs.existsSync(abs)) continue;
    const items = walkMd(abs, dir);
    if (!items.length) continue;
    tracks.push({
      id: dir,
      number: parseInt(dir.slice(0, 2), 10),
      title: TRACK_TITLES[dir] || dir,
      files: items,
      isTrack: !HIDE_FROM_TRACK_PAGES.has(dir),
    });
  }
  return tracks;
}

function copyMarkdown(tracks) {
  ensureDir(CONTENT_DIR);
  const manifest = [];
  for (const track of tracks) {
    for (const file of track.files) {
      const srcPath = path.join(SOURCE, file.path);
      const dstPath = path.join(CONTENT_DIR, file.path);
      ensureDir(path.dirname(dstPath));
      fs.writeFileSync(dstPath, readText(srcPath), "utf-8");
      manifest.push(file.path);
    }
  }
  return manifest;
}

// ---------------------------------------------------------------------------
// Principles
// ---------------------------------------------------------------------------

function parsePrinciples() {
  const p = path.join(SOURCE, "01_core_doctrine", "PRINCIPLES.md");
  if (!fs.existsSync(p)) return [];
  const text = readText(p);
  const sections = text.split(/^## PRN-/m).slice(1);
  const principles = [];
  for (const sec of sections) {
    const idLine = sec.split("\n")[0].trim();
    const id = "PRN-" + idLine.split(":")[0].trim();
    const field = {};
    const rowRe = /^\|\s*\*\*([a-z_]+)\*\*\s*\|\s*(.+?)\s*\|$/gm;
    let m;
    while ((m = rowRe.exec(sec)) !== null) {
      const val = m[2].trim();
      if (val.startsWith("[") && val.endsWith("]")) {
        try {
          field[m[1]] = YAML.parse(val);
        } catch {
          field[m[1]] = val;
        }
      } else {
        field[m[1]] = val;
      }
    }
    principles.push({
      id,
      title: field.title || "",
      claim: field.claim || "",
      evidence: field.evidence || [],
      counterevidence: field.counterevidence || [],
      applicability: field.applicability_conditions || [],
      nonApplicability: field.non_applicability_conditions || [],
      failureModes: field.failure_modes || [],
      reversalConditions: field.reversal_conditions || [],
      confidence: field.confidence || "",
      relatedContradictions: field.related_contradictions || [],
      practicalTool: field.practical_tool || "",
      lastReviewed: field.last_reviewed || "",
      body: sec.trim(),
    });
  }
  return principles;
}

// ---------------------------------------------------------------------------
// Cases
// ---------------------------------------------------------------------------

function parseCases() {
  const p = path.join(SOURCE, "07_cases", "case_catalog.md");
  if (!fs.existsSync(p)) return [];
  const text = readText(p);
  const sections = text.split(/^## CASE-/m).slice(1);
  const cases = [];
  for (const sec of sections) {
    const idLine = sec.split("\n")[0].trim();
    const id = "CASE-" + idLine.split(":")[0].trim();
    const field = {};
    const rowRe = /^\|\s*\*\*([a-z_]+)\*\*\s*\|\s*(.+?)\s*\|$/gm;
    let m;
    while ((m = rowRe.exec(sec)) !== null) {
      const val = m[2].trim();
      if (val.startsWith("[") && val.endsWith("]")) {
        try {
          field[m[1]] = YAML.parse(val);
        } catch {
          field[m[1]] = val;
        }
      } else {
        field[m[1]] = val;
      }
    }
    const ccMatch = sec.match(/### causal_confidence\s*\n+(.+?)(?=\n### |$)/s);
    const causalConfidence = ccMatch ? ccMatch[1].trim().replace(/\n+/g, " ") : "";
    // pull section headings for TOC + inline anchors
    const headings = [...sec.matchAll(/^### ([a-z_]+)$/gm)].map((x) => x[1]);
    cases.push({
      id,
      title: field.title || "",
      decisionMaker: field.decision_maker || "",
      archetype: field.product_archetype || "",
      industry: field.industry || "",
      stage: field.organizational_stage || "",
      type: field.case_type || "",
      causalConfidence,
      headings,
      body: sec.trim(),
    });
  }
  return cases;
}

// ---------------------------------------------------------------------------
// Contradictions
// ---------------------------------------------------------------------------

function parseContradictions() {
  const p = path.join(SOURCE, "08_contradictions", "register.yaml");
  if (!fs.existsSync(p)) return [];
  try {
    const doc = YAML.parse(readText(p));
    return (doc.contradictions || []).map((c) => {
      const flatten = (d) => {
        if (!d) return "";
        if (typeof d === "string") return d;
        const parts = [];
        if (d.position) parts.push(d.position);
        if (d.description) parts.push(d.description.trim());
        return parts.join(" — ");
      };
      return {
        id: c.contradiction_id,
        title: c.question || c.title || "",
        doctrineA: flatten(c.doctrine_a),
        doctrineB: flatten(c.doctrine_b),
        confidence: c.confidence || "",
        body: "",
      };
    });
  } catch (e) {
    console.warn("  ! contradictions parse failed:", e.message);
    return [];
  }
}

// ---------------------------------------------------------------------------
// Sources + claims graph
// ---------------------------------------------------------------------------

function parseSources() {
  const p = path.join(SOURCE, "sources", "registry.yaml");
  if (!fs.existsSync(p)) return [];
  try {
    const doc = YAML.parse(readText(p));
    return (doc.sources || []).map((s) => ({
      id: s.source_id,
      title: s.title || "",
      author: s.author || "",
      type: s.source_type || "",
      tier: s.evidence_tier || "",
      firstHand: s.firsthand || false,
      canonical: s.canonical_claims_supported || false,
      topics: s.key_topics || [],
      url: s.url || null,
      org: s.organization || null,
      year: s.publication_date || null,
      exactLocation: s.exact_location || "",
      reliability: s.reliability_notes || "",
      transferability: s.transferability_notes || "",
    }));
  } catch (e) {
    console.warn("  ! sources parse failed:", e.message);
    return [];
  }
}

function parseClaims() {
  const p = path.join(SOURCE, "research", "extracted_claims", "claims_inventory.yaml");
  if (!fs.existsSync(p)) return [];
  try {
    const doc = YAML.parse(readText(p));
    return (doc.claims || []).map((c) => ({
      id: c.claim_id,
      statement: c.statement || "",
      evidenceLevel: c.evidence_level || "",
      contested: c.contested || false,
      sourceIds: c.source_ids || [],
      counterSourceIds: c.counter_claim_sources || [],
      corroboration: c.corroboration || "",
      notes: c.notes || "",
    }));
  } catch (e) {
    console.warn("  ! claims parse failed:", e.message);
    return [];
  }
}

// ---------------------------------------------------------------------------
// Curriculum: learning paths → phases → weeks → steps
// ---------------------------------------------------------------------------

function parseLearningPaths(tracks, manifest) {
  const lp = tracks.find((t) => t.id === "11_learning_paths");
  if (!lp) return [];
  const paths = [];
  for (const f of lp.files) {
    if (f.name === "README.md") continue;
    const raw = readText(path.join(SOURCE, f.path));
    const lines = raw.split("\n");
    const pathId = slugify(f.name.replace(".md", ""));
    const title = f.name.replace(".md", "").replace(/_/g, " ");

    const phases = [];
    let currentPhase = null;
    let currentWeek = null;

    for (const line of lines) {
      const phaseMatch = line.match(/^## Phase\s*\d+:\s*(.+)$/i);
      const weekMatch = line.match(/^### Week\s*\d+:\s*(.+)$/i);
      const stepMatch = line.match(/^-\s*\*\*(.+?):\*\*\s*(.+)$/i);
      const readMatch = line.match(/^-\s*Read\s+`([^`]+)`\s*(?:—|–|-)?\s*(.*)$/i);

      if (phaseMatch) {
        currentPhase = { id: `phase-${phases.length + 1}`, title: phaseMatch[1].trim(), weeks: [] };
        phases.push(currentPhase);
        currentWeek = null;
      } else if (weekMatch && currentPhase) {
        currentWeek = {
          id: `week-${phases.length}-${currentPhase.weeks.length + 1}`,
          title: weekMatch[1].trim(),
          steps: [],
        };
        currentPhase.weeks.push(currentWeek);
      } else if (readMatch && currentWeek) {
        const target = readMatch[1].trim();
        currentWeek.steps.push({
          type: "read",
          label: "Read",
          title: readMatch[2].trim() || target,
          target,
          route: routeForTarget(target),
        });
      } else if (stepMatch && currentWeek) {
        const label = stepMatch[1].trim();
        const body = stepMatch[2].trim();
        currentWeek.steps.push({
          type: "do",
          label,
          title: body.slice(0, 90) + (body.length > 90 ? "…" : ""),
          body,
          target: null,
          route: null,
        });
      }
    }
    paths.push({
      id: pathId,
      file: f.path,
      title,
      role: title,
      phases,
      stepCount: phases.reduce(
        (n, ph) => n + ph.weeks.reduce((m, w) => m + w.steps.length, 0),
        0,
      ),
      body: raw,
    });
  }
  return paths;
}

// ---------------------------------------------------------------------------
// Route helper for target paths
// ---------------------------------------------------------------------------

function routeForTarget(target) {
  const t = target.replace(/\.md$/, "");
  const parts = t.split("/");
  const track = parts[0];
  const file = parts.slice(1).join("/") || parts[0];
  const slug = slugify(file);

  // Special structured pages
  if (track === "01_core_doctrine" && file.toLowerCase() === "principles") return "/principles/";
  if (track === "07_cases" && file.toLowerCase() === "case_catalog") return "/cases/";
  if (track === "08_contradictions" && file.toLowerCase() === "register") return "/contradictions/";
  if (track === "00_orientation" && file.toLowerCase() === "readme") return "/";
  if (track === "11_learning_paths" && file.toLowerCase() === "readme") return "/paths/";
  if (track === "10_simulator" && file.toLowerCase() === "readme") return "/tracks/10_simulator/";

  // Directory-level target (e.g. `01_core_doctrine/`) → track page
  if (!file || file === track) {
    return `/tracks/${track}/`;
  }

  if (/^\d{2}_/.test(track)) {
    return `/doc/${track}/${slug}/`;
  }
  return `/doc/${track}/${slug}/`;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

function main() {
  console.log("Product Academy content importer");
  console.log(`  source: ${SOURCE}`);
  if (!fs.existsSync(SOURCE)) {
    console.error("ERROR: source repo not found. Set PRODUCT_ACADEMY_SOURCE.");
    process.exit(1);
  }
  ensureDir(DATA_DIR);
  ensureDir(CONTENT_DIR);

  const tracks = collectTracks();
  const manifest = copyMarkdown(tracks);
  console.log(`  tracks: ${tracks.length} | markdown: ${manifest.length}`);

  const principles = parsePrinciples();
  const cases = parseCases();
  const contradictions = parseContradictions();
  const sources = parseSources();
  const claims = parseClaims();
  const paths = parseLearningPaths(tracks, manifest);
  console.log(
    `  principles: ${principles.length} | cases: ${cases.length} | contradictions: ${contradictions.length}`,
  );
  console.log(`  sources: ${sources.length} | claims: ${claims.length} | paths: ${paths.length}`);

  // claims-by-source index
  const claimsBySource = {};
  for (const c of claims) {
    for (const sid of c.sourceIds) {
      (claimsBySource[sid] = claimsBySource[sid] || []).push({
        id: c.id,
        statement: c.statement,
        level: c.evidenceLevel,
        contested: c.contested,
      });
    }
  }

  writeJson("tracks.json", { generatedAt: new Date().toISOString(), tracks });
  writeJson("principles.json", { generatedAt: new Date().toISOString(), principles });
  writeJson("cases.json", { generatedAt: new Date().toISOString(), cases });
  writeJson("contradictions.json", { generatedAt: new Date().toISOString(), contradictions });
  writeJson("sources.json", { generatedAt: new Date().toISOString(), sources });
  writeJson("claims.json", { generatedAt: new Date().toISOString(), claims, bySource: claimsBySource });
  writeJson("paths.json", { generatedAt: new Date().toISOString(), paths });
  writeJson("manifest.json", { generatedAt: new Date().toISOString(), manifest });

  console.log("  done.");
}

main();
