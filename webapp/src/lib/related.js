/**
 * Related-item resolution for the Academy.
 *
 * Given a page kind (doc / principle / case / source) plus its content, this
 * returns related principles / cases / tensions / sources based on shared
 * source_ids and on id references inside the body text.
 *
 * Every lookup is guarded: ids that don't resolve are silently dropped, and
 * missing fields (evidence, counterevidence, body, …) are treated as empty.
 */

import { principles } from "../data/principles.json";
import { cases } from "../data/cases.json";
import { contradictions } from "../data/contradictions.json";
import { sources } from "../data/sources.json";
import { prevNextFor } from "./journey.js";

const ID_RE = {
  principle: /PRN-\d{4}/g,
  tension: /CON-\d{4}/g,
  case: /CASE-\d{4}/g,
  source: /SRC-[A-Z]{3,6}-\d{4}/g,
};

const TYPE_LABEL = {
  principle: "Principle",
  tension: "Tension",
  case: "Case",
  source: "Source",
};

const HREF_FOR = {
  principle: (id) => `/principles/${id}/`,
  tension: (id) => `/contradictions/${id}/`,
  case: (id) => `/cases/${id}/`,
  source: (id) => `/sources/${id}/`,
};

const principleIndex = Object.fromEntries(principles.map((p) => [p.id, p]));
const caseIndex = Object.fromEntries(cases.map((c) => [c.id, c]));
const conIndex = Object.fromEntries(contradictions.map((c) => [c.id, c]));
const sourceIndex = Object.fromEntries(sources.map((s) => [s.id, s]));

function extractIds(text, re) {
  if (!text || typeof text !== "string") return [];
  return [...new Set(text.match(re) || [])];
}

function resolveIds(ids, index) {
  return [...new Set(ids)].filter((id) => index[id]);
}

function buildItem(id, kind, index) {
  const entry = index[id];
  if (!entry) return null;
  return {
    id,
    title: entry.title || id,
    href: HREF_FOR[kind](id),
    type: TYPE_LABEL[kind],
  };
}

function buildGroup(key, title, kind, ids, index) {
  const items = resolveIds(ids, index)
    .map((id) => buildItem(id, kind, index))
    .filter(Boolean);
  if (!items.length) return null;
  return { key, title, kind, items };
}

function evidenceSourceIds(principle) {
  return [
    ...(principle.evidence || []).map((e) => e.source_id),
    ...(principle.counterevidence || []).map((e) => e.source_id),
  ].filter(Boolean);
}

function nextFor(url) {
  try {
    const found = url ? prevNextFor(url) : null;
    return found && found.next ? found.next : null;
  } catch {
    return null;
  }
}

/**
 * Compute related groups for a page.
 *
 * @param {object} ctx
 * @param {"doc"|"principle"|"case"|"source"} ctx.kind
 * @param {string} [ctx.url]       canonical page URL (for "next in journey")
 * @param {object} [ctx.principle] principle record (when kind === "principle")
 * @param {object} [ctx.case]      case record (when kind === "case")
 * @param {object} [ctx.source]    source record (when kind === "source")
 * @param {string} [ctx.body]      raw body text (when kind === "doc")
 * @returns {{ groups: Array, next: object|null }}
 */
export function relatedFor(ctx) {
  const groups = [];
  const push = (g) => {
    if (g) groups.push(g);
  };

  switch (ctx.kind) {
    case "doc": {
      const ids = {
        principle: extractIds(ctx.body, ID_RE.principle),
        tension: extractIds(ctx.body, ID_RE.tension),
        case: extractIds(ctx.body, ID_RE.case),
        source: extractIds(ctx.body, ID_RE.source),
      };
      push(buildGroup("principles", "Related principles", "principle", ids.principle, principleIndex));
      push(buildGroup("tensions", "Related tensions", "tension", ids.tension, conIndex));
      push(buildGroup("cases", "Related cases", "case", ids.case, caseIndex));
      push(buildGroup("sources", "Related sources", "source", ids.source, sourceIndex));
      break;
    }
    case "principle": {
      const p = ctx.principle || {};
      const thisSources = new Set(evidenceSourceIds(p));
      const relatedPrinciples = principles.filter(
        (o) =>
          o.id !== p.id &&
          evidenceSourceIds(o).some((sid) => thisSources.has(sid)),
      );
      const tensionIds = [
        ...(p.relatedContradictions || []),
        ...extractIds(p.body, ID_RE.tension),
      ];
      const caseIds = [
        ...cases.filter((c) => (c.body || "").includes(p.id)).map((c) => c.id),
        ...extractIds(p.body, ID_RE.case),
      ];
      const sourceIds = [
        ...thisSources,
        ...extractIds(p.body, ID_RE.source),
      ];
      push(buildGroup("principles", "Related principles", "principle", relatedPrinciples.map((x) => x.id), principleIndex));
      push(buildGroup("tensions", "Related tensions", "tension", tensionIds, conIndex));
      push(buildGroup("cases", "Related cases", "case", caseIds, caseIndex));
      push(buildGroup("sources", "Related sources", "source", sourceIds, sourceIndex));
      break;
    }
    case "case": {
      const c = ctx.case || {};
      const srcIds = extractIds(c.body, ID_RE.source);
      const srcSet = new Set(srcIds);
      const principleIds = principles
        .filter((p) => evidenceSourceIds(p).some((sid) => srcSet.has(sid)))
        .map((p) => p.id);
      push(buildGroup("principles", "Related principles", "principle", principleIds, principleIndex));
      push(buildGroup("sources", "Related sources", "source", [...srcSet], sourceIndex));
      break;
    }
    case "source": {
      const s = ctx.source || {};
      const principleIds = principles
        .filter((p) => evidenceSourceIds(p).includes(s.id))
        .map((p) => p.id);
      const caseIds = cases.filter((c) => (c.body || "").includes(s.id)).map((c) => c.id);
      push(buildGroup("principles", "Related principles", "principle", principleIds, principleIndex));
      push(buildGroup("cases", "Related cases", "case", caseIds, caseIndex));
      break;
    }
    default:
      break;
  }

  return { groups, next: nextFor(ctx.url) };
}
