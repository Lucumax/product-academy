# Source Policy

## Purpose

Every claim in the Product Leadership Academy must be traceable to a documented source. This policy defines how sources are collected, classified, stored, and cited.

## Source Tiers

### Tier A — Primary Operator Evidence
Firsthand operator account with concrete decisions and outcomes. Official product or company documentation. Rigorous case or postmortem. Primary regulatory or technical source.

**May support canonical doctrine.** Must be the strongest evidence for any canonical claim.

### Tier B — Credible Practitioner Evidence
Experienced practitioner or educator with transparent reasoning, concrete examples, and strong professional credibility.

**May support doctrine with corroboration.** A Tier B source alone is insufficient for a canonical claim.

### Tier C — Practitioner Discussion
Community discussion, conference talk, podcast anecdote. Useful but weakly verified experiential evidence.

**May generate hypotheses and case leads.** Cannot support canonical doctrine alone.

### Tier D — Commercial or Promotional
Influencer summary, coaching funnel, promotional framework, content marketing.

**Discovery only** unless independently corroborated by Tier A or B sources.

### Tier E — Unverifiable
Anonymous unsupported assertion, AI-generated reconstruction, unverifiable aggregation, invented or uncertain transcript.

**Exclude from canonical doctrine.** May be recorded for transparency.

## Required Source Metadata

Every source record must include:

- `source_id` — Stable unique identifier
- `title` — Source title
- `author` — Author or speaker name
- `organization` — Publishing organization
- `source_type` — Type (book, interview, course, talk, article, paper, documentation, community_discussion, case_study, etc.)
- `url` — URL or local path
- `publication_date` — When known
- `access_date` — Date the source was accessed or reviewed
- `level` — Product leadership level addressed (senior_pm, principal_pm, director, vp_product, cpo, founder)
- `product_archetypes` — Relevant archetypes
- `industries` — Relevant industries
- `organizational_stage` — Relevant organizational stages
- `firsthand` — Whether the source is a firsthand operator account (true/false)
- `evidence_tier` — Tier A through E
- `commercial_incentive` — Description of any commercial incentive
- `transcript_status` — One of the allowed transcript statuses
- `exact_location` — Timestamp, page, section, or heading for key claims
- `key_topics` — Array of key topics covered
- `reliability_notes` — Notes on source reliability
- `transferability_notes` — Notes on where claims do and do not transfer
- `copyright_access_status` — Copyright and access status
- `canonical_claims_supported` — Whether canonical claims may rely on this source
- `last_reviewed` — Date last reviewed

## Transcript Integrity

Never invent, reconstruct, or fabricate a transcript. Use only these statuses:

- `VERIFIED_CREATOR_TRANSCRIPT` — Transcript provided by the content creator
- `VERIFIED_PLATFORM_CAPTIONS` — Platform-provided captions or subtitles
- `ASR_DERIVED_TRANSCRIPT` — Automatically generated transcript (must be labelled)
- `CREATOR_SUMMARY_ONLY` — Only a creator-provided summary is available
- `SECONDARY_SUMMARY_ONLY` — Only secondary summaries are available
- `TRANSCRIPT_UNAVAILABLE` — No transcript is available

### Transcript Rules
1. Exact quotations require a verifiable source location.
2. YouTube-derived claims require timestamps where available.
3. ASR-derived text must be labelled.
4. Spot-check ASR against the source.
5. Never represent a paraphrase as a quotation.
6. Do not infer a video's detailed content from its title or thumbnail.
7. Do not fabricate course syllabi or lesson contents.

## Access Policy

1. Do not bypass access controls.
2. Do not scrape private communities.
3. Do not circumvent paywalls.
4. Do not download or reproduce entire copyrighted works.
5. Prefer source metadata, timestamped analytical notes, limited quotations, and original synthesis.
6. Index inaccessible but valuable sources as `ACCESS_REQUIRED`.
7. When a transcript is unavailable, record the source and move on.
8. The repository stores derived learning, not copied media.

## Popularity

Popularity is not evidence. A widely-cited framework, viral talk, or best-selling book does not automatically qualify as a Tier A source. Evaluate content, not reach.
