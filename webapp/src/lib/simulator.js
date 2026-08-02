/**
 * Simulator helpers: scenario markdown parsing + journey routing.
 *
 * Scenarios live in src/content/10_simulator/scenarios/*.md and follow a
 * fixed structure (see 10_simulator/README.md):
 *   - a `| **field** | value |` metadata table
 *   - `## Situation / Characters / Constraints / Your Role`
 *   - `## Response Format` (three parts)
 *   - `## Scoring Rubric (Scenario-Specific)` with `### <Dimension>` tables
 *   - `## Facilitator Notes`
 */

/** Eagerly loaded scenario markdown sources (raw strings keyed by file path). */
export const scenarioModules = import.meta.glob("../content/10_simulator/scenarios/*.md", {
  query: "?raw",
  import: "default",
  eager: true,
});

const FIELD_RE = /^\|\s*\*\*([a-z_]+)\*\*\s*\|\s*(.*?)\s*\|$/i;
const H2_RE = /^##\s+(.+?)\s*$/;
const H3_RE = /^###\s+(.+?)\s*$/;

/** Stable route id for a scenario file path (e.g. `scenario-01-two-engineers`). */
export function scenarioFileId(path) {
  const file = path.split("/").pop() || path;
  return file
    .replace(/\.md$/i, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

/** Parse the `| **field** | value |` metadata table at the top of a scenario. */
export function parseMetaTable(markdown) {
  const meta = {};
  for (const line of markdown.split("\n")) {
    const m = line.match(FIELD_RE);
    if (m) meta[m[1].trim()] = m[2].trim();
  }
  return meta;
}

/** Split markdown into `## ` sections keyed by heading text. */
export function parseSections(markdown) {
  const sections = {};
  let current = null;
  const buf = [];
  const flush = () => {
    if (current !== null) sections[current] = buf.join("\n").trim();
  };
  for (const line of markdown.split("\n")) {
    const m = line.match(H2_RE);
    if (m) {
      flush();
      current = m[1].trim();
      buf.length = 0;
    } else if (current !== null) {
      buf.push(line);
    }
  }
  flush();
  return sections;
}

/** Parse `### <Dimension>` sub-sections from a rubric section (each a markdown table). */
export function parseRubricDimensions(rubricSection) {
  const dims = [];
  let current = null;
  const buf = [];
  const flush = () => {
    if (current !== null) dims.push({ name: current, table: buf.join("\n").trim() });
  };
  for (const line of (rubricSection || "").split("\n")) {
    const m = line.match(H3_RE);
    if (m) {
      flush();
      current = m[1].trim();
      buf.length = 0;
    } else if (current !== null) {
      buf.push(line);
    }
  }
  flush();
  return dims;
}

/** Full parse of a scenario document. */
export function parseScenario(markdown) {
  const meta = parseMetaTable(markdown);
  const sections = parseSections(markdown);
  const rubric = parseRubricDimensions(sections["Scoring Rubric (Scenario-Specific)"] || "");
  return { meta, sections, rubric };
}

/**
 * Link a learning-path step to the simulator when its target points at
 * simulator content. Falls back to the simulator index for non-scenario
 * targets (e.g. the track README).
 */
export function scenarioRouteForTarget(target, knownIds) {
  if (!target) return null;
  if (target.startsWith("10_simulator/")) {
    const id = scenarioFileId(target);
    if (!knownIds || knownIds.has(id)) return `/simulator/${id}/`;
    return "/simulator/";
  }
  return null;
}
