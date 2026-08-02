# Changelog

## v0.3.0 (2026-08-02)

### Added
- Evidence chain repaired: 107 missing source records added (registry now 180 sources); every cited source ID in doctrine/handbook/case resolves
- Cross-reference test (G2) enforcing that all cited IDs resolve and canonical claims use qualifying sources
- `evidence/final/` populated: Claims Ledger, Source Evidence Strength, Corroboration Matrix (35 claims from real claims inventory)
- Theranos case (CASE-0019) — the canonical non-falsifiable-thesis failure
- CC BY 4.0 LICENSE; Academy's own content licensed, distinct from third-party source material
- Curriculum map now has an honest Status column (COMPLETE/COVERED/PARTIAL/PLANNED) per module

### Fixed
- Source tier inflation: Doshi (SRC-POST-0001), Cutler (SRC-POST-0003), Zhuo (SRC-BOOK-0002) reclassified to Tier B with `canonical_claims_supported: false`
- Innovator's Dilemma citations corrected from the colliding SRC-POST-0003 to SRC-BOOK-0010 (Christensen)
- Weak test thresholds: AI module stub test raised from 300 to 3000 chars + structural check
- Walter-specific application notes extracted from canonical doctrine into a gitignored personal file

### Known Limitations
- Several curriculum modules remain PLANNED (marked honestly in the Status column)
- Walter-specific application files are gitignored; personal-lab README remains public

## v0.2.0 (2026-08-02)

### Added
- Track 13: Career Transitions (`13_career_transitions/`)
  - `LANDING_A_PRODUCT_ROLE.md` — hiring as an evidence system; landing product roles by seniority
  - `CREDIBILITY_BINDER.md` — durable public evidence of product judgment (writing, portfolios, artifacts)
  - `EMERGING_PRODUCT_ROLES.md` — AI product management and the evolving product role
- Career navigation brought in scope via SCOPE.md update (bounded to doctrine/playbooks, not personalized coaching)
- Automated tests for career module presence, substance, and epistemic labeling

### Known Limitations
- Career module claims are predominantly practitioner doctrine and inference; empirical evidence is sparse and labeled as such
- Source corpus remains v0.1 depth; career module cites external works by name without registry records

## v0.1.0 (2026-08-01)

Initial bounded release of the Product Leadership Academy.

### Deliverables
- Product leadership capability model (Senior PM through CPO)
- Structured curriculum framework
- Source and evidence registry with 50+ verified source records
- Doctrine and contradiction register (13 seed contradictions)
- Case-study system with 15 cases including failures and reversals
- Product-archetype modules (13 archetypes)
- Industry overlays (financial services, insurance, power/energy, infrastructure/development finance)
- AI Product Management module with evaluation contracts
- Principal+ decision and allocation material
- Practice simulations (10 scenarios with scoring rubrics)
- Reusable decision tools (18 templates)
- Personal application layer (5 portfolio applications)
- Product Forge integration boundary documentation
- Ecosystem map of adjacent systems
- Automated validation suite (schemas, source IDs, links, metadata)
- Generated Product Leadership Bible, Principal PM Playbook, AI PM Playbook
- Deep pilot curriculum: Selecting Problems and Allocating Scarce Resources Under Uncertainty

### Known Limitations
- Source corpus is v0.1 depth (50+ records with 20+ deep analyses); planned expansion in v0.2
- Industry overlay for healthcare is structural only; requires subject-matter expansion
- Product Forge integration is documented but not mechanically verified
- Some source records have ACCESS_REQUIRED status pending credential acquisition
- Scenario library covers 10 scenarios; planned expansion to 25+

### Next Session
- Bounded corpus expansion using enforced source schemas and quality gates
- Deepen healthcare industry overlay
- Expand case library to 30+
- Build first mechanically integrated Product Forge handoff
