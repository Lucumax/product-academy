# Product Leadership Academy — Source Collection

## Version
v0.1 — 2026-08-01

## Overview

The Academy source corpus provides the evidence foundation for all claims, principles, and doctrine in the Product Leadership Academy. Every canonical claim must be traceable to a documented source with a defensible evidence tier.

This collection contains **73 source records** across 10 categories.

---

## Source Tiers

| Tier | Definition | Count | % |
|------|-----------|-------|---|
| **A** | Primary operator evidence; firsthand operator account; official product/company documentation; regulatory source | 43 | 59% |
| **B** | Credible practitioner or educator; transparent reasoning with strong credibility | 23 | 32% |
| **C** | Practitioner community discussion; weakly verified experiential evidence | 5 | 7% |
| **D** | Commercial or promotional source | 0 | 0% |
| **E** | Unverifiable / pending verification | 2 | 3% |

**Key:** Only Tier A sources may support canonical doctrine alone. Tier B requires corroboration. Tier C generates hypotheses only. Tier D/E are excluded from doctrine.

---

## Source Categories

### Books (SRC-BOOK)
20 records — Foundational texts in product management, strategy, leadership, and related disciplines. Authors include Marty Cagan, Ben Horowitz, Julie Zhuo, Eric Ries, Clayton Christensen, Geoffrey Moore, Don Norman, and others.

### Blog Posts & Articles (SRC-POST)
12 records — Public writing by product operators and practitioners. Includes Shreyas Doshi's product strategy threads, Ken Norton's hiring essay, John Cutler's Beautiful Mess newsletter, and Paul Graham's startup essays.

### Company & Platform Documentation (SRC-DOC)
18 records — Official documentation from technology companies and platforms. Includes Google AI Principles, Apple HIG, Stripe API docs, Netflix culture deck, Slack and Airbnb engineering blogs, Material Design, Kubernetes docs, and regulated product frameworks.

### Courses & Syllabi (SRC-COURSE)
5 records — University and professional education sources. Includes Stanford MS&E 472, MIT Product Design and Development, UVA Darden Digital Product Management on Coursera, CMU Web Application Development, and Reforge programs.

### Postmortems & Case Studies (SRC-CASE)
7 records — Documented product failures and reversals. Includes Google product shutdowns, Google Glass, Quibi, Amazon Fire Phone, Clubhouse, Microsoft Zune, and New Coke.

### Talks & Presentations (SRC-TALK)
4 records — Recorded presentations by product operators. Includes Gibson Biddle (Netflix), Melissa Perri (Build Trap), Kevin Hale (YC), and Rich Mironov (Art of Product Management).

### Community Discussions (SRC-COMM)
4 records — Practitioner community sources. Includes r/ProductManagement, Mind the Product, Lenny's Podcast, and Blind.

### Research Papers (SRC-PAPER)
1 record — Academic/research publication. Includes the Model Cards for Model Reporting paper (FAccT 2019).

### Regulatory Documents (SRC-DOC)
Included in SRC-DOC — FDA SaMD Guidance, HIPAA, GDPR, PCI DSS, SOC 2.

---

## Coverage by Category Requirement

| Requirement | Target | Actual | Status |
|-------------|--------|--------|--------|
| Firsthand product-operator sources (Tier A) | 8+ | 20+ | Exceeded |
| Credible educational/syllabus sources (Tier B) | 5 | 5 | Met |
| Company or platform cases | 5 | 10 | Exceeded |
| Failure/reversal/postmortem cases | 5 | 7 | Exceeded |
| AI product development/evaluation sources | 5 | 6 | Met |
| Regulated product sources | 5 | 5 | Met |
| Public practitioner-community sources | 3 | 4 | Met |
| Credible opposing/contrarian sources | 3 | 4 | Met |

---

## Methodology

### Source Selection Criteria
1. **Defensible description:** Every source included can be described based on its actual published content. No source details are fabricated or inferred.
2. **Verifiable existence:** Sources have verifiable publication records (ISBN, URL, conference proceedings, official documentation).
3. **Operator credibility:** Firsthand sources are from individuals with documented, verifiable roles at named organizations.
4. **Uncertainty marked:** Sources with uncertain details are marked conservatively with pending verification status.
5. **Commercial incentive recorded:** All commercial relationships are disclosed in source records.

### Sources Not Included
- Course syllabi where only public descriptions (not detailed content) could be verified
- Interviews where exact content could not be confirmed
- Blog posts from unverifiable sources
- Paywalled content where access was not held
- Internal company documents not publicly accessible

### What This Collection Is NOT
- A comprehensive bibliography of all product management literature
- An endorsement of every included source's claims
- A substitute for reading the actual sources
- A popularity ranking (see SOURCE_POLICY.md: popularity is not evidence)

---

## Key Files

| File | Description |
|------|-------------|
| `registry.yaml` | Master source registry with all 73 records |
| `../research/source_scores/source_analysis.md` | Deep analysis of 18 strongest sources |
| `../research/extracted_claims/claims_inventory.yaml` | 35 key claims extracted from sources |
| `../schemas/source.schema.json` | Schema for source records |
| `../SOURCE_POLICY.md` | Source collection and evidence tier policy |
| `../COPYRIGHT_AND_ACCESS_POLICY.md` | Copyright and access rules |

---

## Source ID Format

Sources use the pattern `SRC-{CATEGORY}-{NNNN}`:

| Prefix | Category | Example |
|--------|----------|---------|
| SRC-BOOK | Books | SRC-BOOK-0001 |
| SRC-POST | Blog posts, articles, newsletters | SRC-POST-0001 |
| SRC-DOC | Documentation, regulatory docs | SRC-DOC-0001 |
| SRC-TALK | Talks, presentations | SRC-TALK-0001 |
| SRC-COURSE | Courses, syllabi | SRC-COURSE-0001 |
| SRC-CASE | Case studies, postmortems | SRC-CASE-0001 |
| SRC-COMM | Community discussions | SRC-COMM-0001 |
| SRC-PAPER | Research papers | SRC-PAPER-0001 |
| SRC-INTV | Interviews (reserved) | SRC-INTV-0001 |

---

## Quality Notes

### Strengths
- High proportion of Tier A firsthand operator sources (59%)
- Broad coverage across product archetypes and organizational stages
- Commercial incentives explicitly documented
- Transcript statuses accurately recorded
- Both mainstream and contrarian perspectives included
- Regulatory framework sources included for regulated industry coverage

### Limitations
- Heavy skew to U.S. West Coast technology companies
- Limited representation of non-English and non-U.S. perspectives
- Most sources are experience-based, not empirical research
- Retrospective bias in firsthand accounts
- Founder/CEO perspective overrepresented relative to PM-level practitioners
- Limited hardware product management sources
- Limited pre-2000s product management practice sources

### Planned Additions (v0.2)
- Non-U.S. product leadership sources
- Regulated industry operator firsthand accounts
- Hardware product management sources
- Academic research evaluating PM practices
- More pre-internet product management history
- Enterprise sales-led PM experiences

---

## Contributing

Source additions must follow the schema (`schemas/source.schema.json`) and the source policy (`SOURCE_POLICY.md`). Key requirements:

1. Every field must be defensible based on actual source content
2. Never fabricate URLs, dates, or content
3. Mark uncertain sources conservatively
4. Disclose commercial incentives
5. Use accurate transcript statuses
6. Only Tier A sources can support canonical doctrine

---

**Last Updated:** 2026-08-01
**Maintained by:** Product Leadership Academy Research Function
