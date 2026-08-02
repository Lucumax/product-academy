/**
 * Slugify a document path into its route id. Used by the doc page and
 * the track pages so links always match.
 */
export function docSlug(path) {
  return path
    .split("/")
    .slice(1) // drop the track segment
    .join("/")
    .replace(".md", "")
    .replace(/[^a-z0-9]+/gi, "-")
    .replace(/^-+|-+$/g, "")
    .toLowerCase();
}

/** Documents that get dedicated structured pages, never raw doc routes. */
export const DOC_SKIP = new Set([
  "01_core_doctrine/PRINCIPLES.md",
  "07_cases/case_catalog.md",
  "08_contradictions/register.yaml",
  "sources/registry.yaml",
  "00_orientation/README.md",
  "11_learning_paths/README.md",
  "10_simulator/README.md",
]);

/** Track id from a document path. */
export function docTrack(path) {
  return path.split("/")[0];
}

/** Human title from a document path. */
export function docTitle(path) {
  return path.split("/").pop().replace(".md", "").replace(/_/g, " ");
}

