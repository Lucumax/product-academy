/**
 * Markdown rendering with epistemic-label styling.
 *
 * Uses markdown-it for spec-compliant rendering, then post-processes
 * the HTML to wrap Academy epistemic labels ([E], [P], [I], [D], [R])
 * in styled spans and linkify internal references (PRN-, CON-, CASE-,
 * SRC- ids) to their detail pages.
 */

import MarkdownIt from "markdown-it";

const md = new MarkdownIt({
  html: false,
  linkify: true,
  typographer: false,
});

// Epistemic labels arrive as **[E]** which markdown-it renders to
// <strong>[E]</strong>. We tokenize them in the raw source first so
// they survive rendering unchanged, then style them in HTML. The token
// uses @@ which contains no markdown-significant characters.
const LABEL_TOKEN_RE = /\*\*\[([EPIDR])\]\*\*/g;
const LABEL_HTML_RE = /@@EP_([EPIDR])@@/g;

// Internal reference ids
const REF_RE =
  /\b(SRC-[A-Z]{3,6}-\d{4}|PRN-\d{4}|CON-\d{4}|CASE-\d{4})\b/g;

const LABEL_NAMES = {
  E: "Evidence",
  P: "Practitioner doctrine",
  I: "Inference",
  D: "Open debate",
  R: "Recommendation",
};

function routeFor(ref) {
  if (ref.startsWith("PRN-")) return "/principles/" + ref + "/";
  if (ref.startsWith("CON-")) return "/contradictions/" + ref + "/";
  if (ref.startsWith("CASE-")) return "/cases/" + ref + "/";
  if (ref.startsWith("SRC-")) return "/sources/" + ref + "/";
  return null;
}

function tokenizeLabels(markdown) {
  return markdown.replace(LABEL_TOKEN_RE, (_m, letter) => `@@EP_${letter}@@`);
}

function styleLabels(html) {
  return html.replace(LABEL_HTML_RE, (_m, letter) => {
    const name = LABEL_NAMES[letter];
    return `<span class="ep-inline ep-inline-${letter}" title="${name}">[${letter}]</span>`;
  });
}

function linkifyRefs(html) {
  return html.replace(REF_RE, (ref) => {
    const route = routeFor(ref);
    if (!route) return ref;
    return `<a href="${route}" class="ref-link">${ref}</a>`;
  });
}

export function renderMarkdown(markdown) {
  let source = tokenizeLabels(markdown);
  let html = md.render(source);
  html = styleLabels(html);
  html = linkifyRefs(html);
  return html;
}

/** Strip HTML for search/index excerpts. */
export function plainText(markdown) {
  const source = tokenizeLabels(markdown);
  const html = md.render(source);
  return html
    .replace(/<[^>]+>/g, " ")
    .replace(/@@EP_[EPIDR]@@/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}
