import { sources } from "../data/sources.json";
import { tierRank } from "./sourceLabels.js";

const CURATED = {
  "00_orientation/": [],
  "01_core_doctrine/": [
    "SRC-BOOK-0001",
    "SRC-BOOK-0004",
    "SRC-BOOK-0020",
    "SRC-TALK-0002",
    "SRC-TALK-0003",
    "SRC-POST-0014",
  ],
  "02_principal_plus/": [
    "SRC-BOOK-0001",
    "SRC-BOOK-0003",
    "SRC-BOOK-0015",
    "SRC-POST-0002",
    "SRC-POST-0003",
    "SRC-POST-0030",
  ],
  "03_business_and_gtm/": [
    "SRC-BOOK-0015",
    "SRC-BOOK-0024",
    "SRC-BOOK-0011",
    "SRC-BOOK-0034",
    "SRC-TALK-0001",
    "SRC-POST-0021",
  ],
  "04_product_archetypes/": [
    "SRC-BOOK-0010",
    "SRC-BOOK-0011",
    "SRC-BOOK-0014",
    "SRC-BOOK-0025",
    "SRC-BOOK-0034",
  ],
  "05_ai_product_management/": [
    "SRC-POST-0006",
    "SRC-PAPER-0001",
    "SRC-DOC-0008",
    "SRC-DOC-0009",
    "SRC-DOC-0010",
    "SRC-DOC-0011",
    "SRC-POST-0023",
  ],
  "08_contradictions/": [
    "SRC-BOOK-0003",
    "SRC-BOOK-0007",
    "SRC-BOOK-0010",
    "SRC-BOOK-0035",
    "SRC-POST-0027",
  ],
  "09_tools/": [
    "SRC-BOOK-0004",
    "SRC-BOOK-0012",
    "SRC-BOOK-0017",
    "SRC-BOOK-0018",
    "SRC-POST-0030",
  ],
};

const byId = Object.fromEntries(sources.map((s) => [s.id, s]));

const MAX_PER_WEEK = 6;

export function sourcesForTrack(track) {
  return (CURATED[track] || [])
    .map((id) => byId[id])
    .filter((s) => s && s.url);
}

export function goDeeperSources(targets) {
  const seen = new Set();
  const out = [];
  for (const t of targets || []) {
    if (!t) continue;
    const track = t.split("/")[0] + "/";
    for (const s of sourcesForTrack(track)) {
      if (seen.has(s.id)) continue;
      seen.add(s.id);
      out.push(s);
    }
  }
  out.sort((a, b) => tierRank(a.tier) - tierRank(b.tier));
  return out.slice(0, MAX_PER_WEEK);
}
