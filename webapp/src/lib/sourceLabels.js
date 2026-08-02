export const SOURCE_TAG = {
  book: "Book",
  talk: "Talk",
  video: "Talk",
  podcast: "Talk",
  blog_post: "Article",
  newsletter: "Article",
  article: "Article",
  paper: "Article",
  postmortem: "Article",
  course: "Guide",
  community_discussion: "Guide",
  documentation: "Official docs",
  regulatory_document: "Official docs",
  other: "Source",
};

export function sourceTag(type) {
  return SOURCE_TAG[type] || "Source";
}

export function tierRank(tier) {
  return { A: 0, B: 1, C: 2, E: 3 }[tier] ?? 4;
}
