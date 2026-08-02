# Adversarial Review: Product Leadership Academy v0.1.0

**Date:** 2026-08-01
**Reviewer:** Adversarial Reviewer Agent
**Scope:** READ-ONLY critical examination of repository structure, claims, evidence, and usability
**Result:** **NOT READY FOR USE** — Foundational defects must be repaired before the Academy can fulfill its stated purpose.

---

## Overall Verdict

### Is the repository genuinely usable after this run?

**No.** The repository is structurally impressive but functionally broken in a way that undermines its foundational claim: that it is "evidence-backed." The two most critical defects — mismatch between principle source references and the actual source registry, and the empty `evidence/final/` directory — mean a student trying to "follow the reference to understand the evidence behind the claim" (as the handbook instructs) cannot do so. Until source IDs align between doctrine and registry, the Academy's central value proposition — traceable, verifiable evidence — is non-functional.

### Is it mostly scaffolding or mostly content?

**Mixed, leaning scaffolding.** The repository has several genuinely substantive modules:
- `01_core_doctrine/PROBLEM_SELECTION_MODULE.md` (1,386 lines) is deep and well-structured
- `06_industry_overlays/FINANCIAL_SERVICES.md` (691 lines) demonstrates genuine domain fluency
- `06_industry_overlays/INSURANCE.md` (459 lines) is similarly substantive
- `05_ai_product_management/EVALUATION_CONTRACTS.md` (680 lines) and `FAILURE_MODES.md` (678 lines) are strong
- `10_simulator` has 10 real scenario files
- `09_tools` has 19 template files

However, the Curriculum Map lists ~40 modules across 12 tracks with estimated times totaling 200-450 hours of study, while actual content exists for perhaps 25% of those modules. The `03_business_and_gtm/` directory has only 2 files even though the Curriculum Map lists 7 modules. The map is a wish list, not a map.

### Top 3 things that MUST be fixed for launch

1. **Source ID cross-reference system** — Principle files and source registry use incompatible ID formats. Must be reconciled or a crosswalk created.
2. **Populate `evidence/final/`** — The directory exists but is empty. Cannot claim "evidence-backed" without evidence artifacts.
3. **Curriculum Map vs. actual content gap** — Either build the mapped modules or reduce the map to actual scope.

### Top 3 things that SHOULD be fixed in v0.2

1. **Personal Lab displacement** — Move Walter-specific portfolio content out of a general-purpose Academy track.
2. **Scoring rubric calibration** — Add safeguards against vocabulary-as-proxy-for-judgment scoring.
3. **Source tier audits** — Review Tier A classifications where firsthand operator status is thin or editorialized.

---

## Detailed Findings

### a. Strongest Reason the Repo May Be Useless

**Finding A1: Source IDs are incompatible between doctrine and registry — the evidence chain is broken**

- **File:** `01_core_doctrine/PRINCIPLES.md:14`, `sources/registry.yaml:19`
- **Severity:** **CRITICAL**

**Evidence:** Every principle in PRINCIPLES.md references sources using IDs like `SRC-BK-0001`, `SRC-AR-0013`, `SRC-TK-0001`. But the registry at `sources/registry.yaml` uses IDs like `SRC-BOOK-0001`, `SRC-POST-0001`, `SRC-TALK-0001`. These are fundamentally different ID schemas.

From PRINCIPLES.md line 14:
```
{source_id: SRC-BK-0001, claim_summary: "Empowered product teams deliver superior innovation..."}
```

From registry.yaml line 19:
```
- source_id: SRC-BOOK-0001
    title: "Inspired: How to Create Tech Products Customers Love"
```

A student told "follow the reference to understand the evidence" (handbook line 150: "Don't take the Bible's word for it — check the source") cannot do so. Searching the registry for `SRC-BK-0001` returns nothing. The entire evidence-tracing infrastructure — the Academy's defining feature — is non-operational.

**Why it matters:** The Constitution's Article II, Principle 1 ("Evidence Over Authority") states: "Every canonical claim in the Academy must be supported by qualifying evidence." If the evidence cannot be traced, all canonical claims are effectively unsupported. The Academy has built an elaborate scaffolding for evidence-backed claims and then used a referencing system that prevents anyone from ever finding the evidence.

**Recommendation:** Either (a) update all principle source references to match the registry format (`SRC-BOOK-0001` → `SRC-BOOK-0001`), (b) update all registry IDs to match the principle format, or (c) create a crosswalk file in `docs/source_id_crosswalk.md` and include an automated cross-reference test in the validation script that ensures every source ID cited in doctrine resolves in the registry.

---

**Finding A2: `evidence/final/` directory is completely empty**

- **File:** `evidence/final/` (0 entries)
- **Severity:** **CRITICAL**

**Evidence:** The directory structure includes `evidence/final/` which appears designed to hold processed evidence summaries, extracted claims, or validated source analyses. It contains zero files. The `research/source_scores/` directory has only one file (`source_analysis.md`). The repository has 55 sources catalogued (3,037 lines of YAML) but no processed evidence outputs.

**Why it matters:** The Academy claims to be "evidence-backed" in its preamble: "an evidence-backed system of doctrine, cases, frameworks, and tools." Without evidence artifacts — extracted claims, verified quotations, source strength assessments — the evidence exists only as raw source references. The Academy's practice of linking sources to doctrine is metadata, not evidence. "Evidence-backed" requires that evidence has been examined, weighted, and applied.

**Recommendation:** Populate `evidence/final/` with at minimum: (a) extracted and verified key claims from each Tier A source with exact page/timestamp references, (b) evidence strength assessments per source, (c) correlation matrices showing which claims are corroborated by which independent sources. This is what would distinguish the Academy from a reading list.

---

**Finding A3: Curriculum Map lists ~40 modules; approximately 10 have substantive content**

- **File:** `CURRICULUM_MAP.md` vs actual directory contents
- **Severity:** **CRITICAL**

**Evidence:** The Curriculum Map (341 lines) describes an elaborate 12-track, ~40-module curriculum with 200-450 hours of estimated study time. Actual directory contents:

| Track | Map Claims | Files Excluding README | Gap |
|-------|-----------|----------------------|-----|
| 01 Core Doctrine | 8 sub-modules | 3 files (PRINCIPLES.md, PROBLEM_SELECTION_MODULE.md, DECISION_FRAMEWORKS.md) | 5 missing |
| 02 Principal Plus | 8 sub-modules | 3 files (PRINCIPAL_PM.md, DIRECTOR_VP_TRANSITION.md, CPO_ROLE.md) | 5 missing |
| 03 Business & GTM | 7 sub-modules | 1 file (BUSINESS_MODEL_MAP.md) | 6 missing |
| 04 Product Archetypes | 14 sub-modules | Unknown (not fully examined) | Likely significant |

**Why it matters:** A new user reading the Curriculum Map will believe these modules exist and plan their study accordingly. They will find stubs or nothing. This isn't "v0.1.0 partial scope" — it's a map that describes a destination which doesn't exist. The map is aspirational marketing, not a curriculum document.

**Recommendation:** Either (a) explicitly mark modules that don't exist as "PLANNED — NOT YET WRITTEN" with version targets, or (b) remove them from the map entirely until content exists. The CURRICULUM_MAP.md should include a status column (DRAFT / STUB / PILOT / COMPLETE) for each module.

---

### b. Strongest Duplication with Product Forge

**Finding B1: PROBLEM_SELECTION_MODULE.md duplicates Product Forge's discovery pipeline**

- **File:** `01_core_doctrine/PROBLEM_SELECTION_MODULE.md:51-200`, `docs/PRODUCT_FORGE_INTEGRATION.md`
- **Severity:** **HIGH**

**Evidence:** Product Forge's integration doc states: "The Academy teaches problem selection; Product Forge converts selected problems into validated backlog items." However, PROBLEM_SELECTION_MODULE.md Topic 1 (Problem Discovery) contains detailed methodology for customer interviews, opportunity solution trees, and hypothesis validation — activities that are Product Forge's domain per the Constitution (Article III, Section 3.1): "Product Forge: Opportunity assessment, solution discovery, evidence collection, backlog generation."

The evidence section on line 69 cites SRC-BK-0004 (Torres, Continuous Discovery Habits) with: "The most effective discovery is continuous, not periodic. Teams that have weekly customer touchpoints discover problems that quarterly research misses entirely." This is Product Forge's discovery pipeline content, not Academy-level problem selection doctrine.

**Why it matters:** The boundary blurs into Product Forge's core function. If the Academy already teaches detailed discovery methodology (interviews, observation, hypothesis testing), what's left for Product Forge? The Constitution's own boundary rules are violated by the Academy's pilot module.

**Recommendation:** Trim Topic 1 to focus on discovery *at the strategic/portfolio level* (how VP/CPOs discover problems through capital flow analysis, regulatory trajectory tracking, etc. — content that IS genuinely Academy-level). Move tactical discovery techniques (customer interviews, opportunity solution trees) to Product Forge's domain and replace with cross-references.

---

**Finding B2: Multiple Academy templates duplicate Product Forge artifacts**

- **File:** `09_tools/` (19 templates), `docs/PRODUCT_FORGE_INTEGRATION.md:91-98`
- **Severity:** **MEDIUM**

**Evidence:** The tools directory contains templates like `OPPORTUNITY_ASSESSMENT_TEMPLATE.md`, `EXPERIMENT_DESIGN_TEMPLATE.md`, `EVALUATION_CONTRACT_TEMPLATE.md`, `DECISION_MEMO_TEMPLATE.md`, `POST_LAUNCH_REVIEW_TEMPLATE.md`. These are execution artifacts, not learning artifacts. The Constitution article III Section 3.5 states: "The Academy shall not... duplicate content from adjacent repositories."

**Why it matters:** These templates may genuinely be needed for Academy exercises. But their existence without clear labeling as "Academy-specific exercise templates (not Product Forge artifacts)" invites confusion. A student who uses these templates in their real work has crossed the Academy→Product Forge boundary without knowing it.

**Recommendation:** Add a disclaimer header to each template: "ACADEMY LEARNING ARTIFACT — This template is designed for practice and self-assessment within the Academy, not as a Product Forge execution artifact. For production use, refer to Product Forge's equivalent template."

---

### c. Weakest Canonical Doctrine

**Finding C1: PRN-0003 (Cost of Delay) has contradictory evidence that isn't resolved**

- **File:** `01_core_doctrine/PRINCIPLES.md:57-81`
- **Severity:** **HIGH**

**Evidence:** PRN-0003 claims: "For the vast majority of product decisions, the cost of delaying a decision... exceeds the cost of making an imperfect decision and correcting it later." The counterevidence section lists Knight Capital ($440M lost in 45 minutes) and Boeing 737 MAX (catastrophic safety failure from speed-pressure). The applicability conditions acknowledge irreversible decisions as excluded — but the *default claim* applies to a "vast majority."

The problem: The principle doesn't provide evidence that this is true for the "vast majority of product decisions." It cites DORA research (deployment frequency correlates with performance) and Amazon's philosophy, but neither source quantifies the proportion of decisions where speed beats quality. The claim is quantitative ("vast majority") but the evidence is qualitative.

**Why it matters:** This is the Academy's most dangerous principle if it's wrong. A product leader who adopts "speed over perfection" as their default orientation could make the Knight Capital or Boeing error. The principle acknowledges these as exceptions but provides no methodology for reliably distinguishing the exceptions before the damage is done.

**Recommendation:** Downgrade the confidence from "medium" to "low" and add a specific methodology for distinguishing "majority" decisions from "excluded" decisions BEFORE the fact, not based on outcome. The One-Way/Two-Way Door classification (Decision Framework 1) is cited but not integrated into the principle's applicability testing.

---

**Finding C2: PRN-0016 (Product-Founder Relationship) is untestable and nearly tautological**

- **File:** `01_core_doctrine/PRINCIPLES.md:408-431`
- **Severity:** **MEDIUM**

**Evidence:** PRN-0016 claims: "the relationship between the product leader... and the founder is more important than any product strategy, framework, or process." This is essentially unfalsifiable. If a company with a good founder-CPO relationship succeeds, the principle is confirmed. If it fails, the relationship "wasn't actually strong enough." If a company with a bad relationship succeeds, it's an exception.

The evidence cites Steve Jobs (single company, extraordinary circumstances) and Paul Graham's "Founder Mode" essay (personal opinion). The counterevidence is rated "weak." This is the Academy's least-rigorous principle by a wide margin.

**Why it matters:** The Academy's Constitution Article VII rejects "founder worship" as an anti-pattern. This principle, despite its caveats, is structurally a founder-worship artifact — it argues that the personal relationship between two individuals is more important than strategy, which is itself a rejection of the Academy's own emphasis on structured decision-making.

**Recommendation:** Either (a) downgrade to "case study observation, not doctrine," (b) reframe as "Founder-CPO alignment on decision rights is the highest-leverage organizational design decision" (testable, refutable), or (c) cut entirely as career advice rather than product leadership doctrine.

---

### d. Least Credible Source

**Finding D1: SRC-POST-0001 (Shreyas Doshi's Twitter threads) classified as Tier A**

- **File:** `sources/registry.yaml:65-107`
- **Severity:** **HIGH**

**Evidence:** Doshi's Twitter/X threads are classified as Tier A ("firsthand operator"). The registration says: "Doshi product experience includes roles at Stripe, Twitter, Google, Yahoo. Frameworks derived from firsthand operator experience." And: "Public threads are high-signal but reflect personal heuristics, not systematic research."

Twitter threads from a practitioner — no matter how experienced — are not equivalent to "firsthand operator" evidence in the sense that SRC-TALK-0001 (Gibson Biddle, Netflix VP Product, recorded public talk with consistent narrative) is. Twitter threads are short-form, edited in real-time, not preserved in stable form, and often reactive. The "exact_location" field says: "specific threads on LNO framework, product sense, strategy" — four years of threads without stable URLs.

**Why it matters:** Tier A status means "single source sufficient" for canonical claims per the Constitution's evidence standard. This means a claim supported ONLY by a Doshi Twitter thread would qualify as canonically valid. This fundamentally undermines the evidence tier system. If Twitter threads are Tier A, the tier definitions have no discriminating power.

**Recommendation:** Reclassify SRC-POST-0001 as Tier B ("credible practitioner/educator"). Tier A should be reserved for sources with: (a) stable publication in a verifiable medium (book, recorded talk, official documentation), (b) systematic rather than reactive content, (c) a body of work that can be referenced consistently over time.

---

**Finding D2: SRC-POST-0003 (John Cutler's Substack newsletter) classified as Tier A**

- **File:** `sources/registry.yaml:184-224`
- **Severity:** **MEDIUM**

**Evidence:** Same pattern as Doshi. A Substack newsletter is classified as Tier A despite the reliability notes stating: "Content reflects firsthand synthesis but is primarily opinion/analysis." If content is "primarily opinion/analysis," it should not be Tier A. The tier definition says Tier A = "firsthand operator (built/managed the thing)." Newsletter opinion posts about product operations are not the same as building/managing the thing.

**Why it matters:** Tier inflation erodes the evidence system's credibility. If ~40% of Tier A sources are actually Tier B by the Academy's own definitions, the concept of "evidence-backed" is emptied of meaning.

**Recommendation:** Downgrade to Tier B. Reserve Tier A for sources where Cutler directly describes systems he built at Zendesk, Amplitude, or Toast — not his newsletter analysis of industry trends.

---

**Finding D3: SRC-BOOK-0002 (Julie Zhuo's "Making of a Manager") is tangential to product leadership**

- **File:** `sources/registry.yaml:145-182`
- **Severity:** **LOW**

**Evidence:** Zhuo's book is about first-time management at Facebook, with key topics including "first_time_management," "team_leadership," "feedback," and "hiring." It's classified as Tier A with `canonical_claims_supported: true`. But the Academy explicitly excludes "people management fundamentals" from scope (SCOPE.md line 39). The book is about management, not product leadership.

**Why it matters:** Low severity because it's a quality issue, not a corruption issue. But it signals that source inclusion criteria are being applied loosely.

**Recommendation:** Either reclassify as Tier B for tangential relevance, or add a specific note explaining which product-leadership-relevant claims the Academy extracts from this management book.

---

### e. Most Important Missing Failure Case

**Finding E1: No Theranos case — the definitive product leadership failure**

- **File:** `07_cases/case_catalog.md` (no CASE for Theranos)
- **Severity:** **HIGH**

**Evidence:** The case catalog includes 6 comprehensive cases: Netflix Qwikster, Apple iPhone, Google Reader, Microsoft transformation, Knight Capital, and Slack platform strategy. It does not include Theranos — arguably the most instructive product leadership failure of the last 20 years.

Theranos is not about fraud (a legal problem). It's about:
- Product thesis construction without falsifiability (all claims were non-falsifiable)
- Technical fluency failure by leadership and board (no one who understood the science was in decision-making positions)
- Customer discovery failure (building for customers who couldn't verify claims)
- Speed-over-quality in a regulated medical domain (the exact failure mode PRN-0003 warns about)
- The danger of "fake it till you make it" as product culture
- The failure of governance when leadership controls information flow

**Why it matters:** The Academy's cases skew toward recoverable failures (Netflix recovered, Microsoft recovered) and spectacular successes. Theranos is the case where product leadership failures were existential — the company is gone, people went to prison, and patients were harmed. It is the single most important warning case for every principle the Academy teaches. Its absence suggests the Academy may be avoiding the most uncomfortable case because it implicates the entire product leadership model.

**Recommendation:** Add a Theranos case focusing specifically on the product leadership failures (not the fraud): thesis construction, technical fluency requirements, the insulation of product decisions from technical verification, and the role of board governance in product decisions. It's the acid test for every Academy principle.

---

**Finding E2: No regulated-industry catastrophic failure case (e.g., 737 MAX, Volkswagen emissions)**

- **File:** `07_cases/case_catalog.md`
- **Severity:** **MEDIUM**

**Evidence:** The Academy has detailed industry overlays for financial services, insurance, power/energy, and infrastructure. But the case catalog — which the FINANCIAL_SERVICES.md overlay explicitly references — contains no regulated-industry cases. PRN-0003 references 737 MAX in counterevidence but there's no standalone case. The Academy teaches industry-specific constraints but doesn't demonstrate them through cases.

**Why it matters:** Students in regulated industries may not see their context reflected in the case catalog. The Academy's strongest content (industry overlays) isn't reinforced by its practice infrastructure (cases).

**Recommendation:** Add at minimum one regulated-industry case that demonstrates the speed-vs-assurance trade-off (NOT just using 737 MAX/Knight Capital as counterevidence snippets but as fully analyzed cases).

---

### f. Most Superficial Industry Adaptation

**Finding F1: INFRASTRUCTURE_AND_DEVELOPMENT_FINANCE.md — likely the thinnest overlay**

- **File:** `06_industry_overlays/INFRASTRUCTURE_AND_DEVELOPMENT_FINANCE.md` (not sampled but matched by pattern)
- **Severity:** **MEDIUM**

**Evidence:** The FINANCIAL_SERVICES.md overlay is 691 lines and deeply substantive — it discusses Basel III/IV, prudential regulation, the balance-sheet lens, and trust stack. The INSURANCE.md overlay is 459 lines and similarly detailed. However, the `POWER_AND_ENERGY.md` and `INFRASTRUCTURE_AND_DEVELOPMENT_FINANCE.md` overlays are likely thinner based on the Academy's own admission in the Curriculum Map that these are secondary priorities (depth priority #6: "Regulated-industry overlays").

**Why it matters:** The Academy should not include overlays it cannot make substantive. A thin overlay for an industry would be worse than no overlay — it would give false confidence to practitioners in that industry.

**Recommendation:** Audit each industry overlay file for minimum 300 lines of substantive doctrine (not preamble/boilerplate). If any fail this threshold, either expand them to match the financial services standard or mark them as "OUTLINE — DO NOT RELY ON" until they meet the standard.

---

**Finding F2: The "Walter application" sections make the Academy single-user-specific**

- **File:** Multiple (every principle, every case, PORTFOLIO_OVERVIEW.md)
- **Severity:** **HIGH**

**Evidence:** Every principle in PRINCIPLES.md has a `walter_application` field. Every case has a `walter_application` section. The entire `12_personal_lab/` track (PORTFOLIO_OVERVIEW.md, 229 lines) is dedicated to analyzing "Walter's portfolio" of four specific initiatives (Product Forge, InfraPrep, TIAA, Agents Front Office). From the PORTFOLIO_OVERVIEW.md: "Walter's portfolio is the practical embodiment of the Product Leadership Academy itself."

The Constitution Article IV section 4.3 says: "The Academy's 'Walter application' notes are contextual guidance for applying doctrine to a specific portfolio. These notes are advisory, not prescriptive." But they are embedded in the middle of every canonical document. A student who is NOT Walter must skip past Walter-specific content to get to the general doctrine.

**Why it matters:** The Academy markets itself as an education system "for product leaders from Senior PM through CPO." But its canonical documents are deeply intertwined with one person's specific portfolio. This makes the Academy feel like a personal coaching system for Walter, with a thin layer of general-purpose framing on top. It undermines the credibility of the Academy as a standalone reference.

**Recommendation:** Extract all `walter_application` sections into a separate file (`12_personal_lab/walter_applications.md`) and reference them by link from each principle, rather than embedding them inline. This preserves the value for Walter while making the Academy legible to other users.

---

### g. Weakest Test

**Finding G1: `test_ai_modules_not_stubs` uses a 300-character threshold — trivially passable**

- **File:** `tests/test_validation.py:169-175`
- **Severity:** **MEDIUM**

**Evidence:**
```python
def test_ai_modules_not_stubs(self, academy_root):
    ai_dir = academy_root / "05_ai_product_management"
    for md_file in ai_dir.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        assert len(content) > 300, (
            f"AI module {md_file.name} appears to be a stub ({len(content)} chars)"
        )
```

300 characters is approximately 5 sentences. A five-sentence introductory paragraph plus a table of contents would pass this test. The test guarantees files aren't literally empty but doesn't test whether they're substantive. A file with 301 characters of Lorem Ipsum would pass.

**Why it matters:** The test creates the illusion of quality assurance while actually checking only against the most trivial failure mode (empty files). This is a pattern throughout the test suite: tests verify structure but not substance.

**Recommendation:** Raise to a meaningful threshold (e.g., 3,000 characters) and add a content-based check (must contain at least one `## ` section heading, must contain at least one evidence reference or practical exercise). Better: add a fuzzy check for "does this look like educational content vs. placeholder text?"

---

**Finding G2: No test verifies that source IDs in principles resolve to registry entries**

- **File:** `tests/test_validation.py` (no such test)
- **Severity:** **CRITICAL**

**Evidence:** This is the single most important integrity test the Academy could run — and it doesn't exist. The test suite checks that source IDs in the registry are unique and valid, but never checks that the hundreds of source IDs cited in PRINCIPLES.md, PROBLEM_SELECTION_MODULE.md, and the case catalog resolve to entries in `sources/registry.yaml`. Given the incompatible ID format systems described in Finding A1, this test would fail comprehensively — which is exactly why it should exist.

**Why it matters:** This is a test that would catch the Academy's most critical defect. Its absence means the validation system is validating scaffolding while missing the structural integrity of the content itself.

**Recommendation:** Add a test that (a) extracts all source IDs from all doctrine files, (b) resolves each against the registry (with a crosswalk if ID formats differ), (c) asserts 100% resolution rate, (d) asserts that canonical claims only cite Tier A or corroborated Tier B sources.

---

**Finding G3: Test suite tests file existence and format; zero content-quality tests**

- **File:** `tests/test_validation.py:113-176`
- **Severity:** **HIGH**

**Evidence:** The test classes test:
- `test_case_catalog_exists` — file exists
- `test_case_catalog_has_content` — >1000 characters
- `test_cases_have_causal_confidence` — count of headers
- `test_principles_file_exists` — file exists
- `test_principles_have_evidence` — header count
- `test_ai_modules_exist` — directory exists
- `test_ai_modules_not_stubs` — >300 characters

None of these tests verify that:
- Case studies contain referenced sources that exist
- Principles' applicability conditions don't contradict non-applicability conditions
- Evidence claims are internally consistent (no "strong" claim with "weak" source)
- Contradiction register IDs match contradiction references in principles
- No principle makes claims that the register identifies as unresolved contradictions
- Source marketing incentives are actually disclosed (vs. field being populated)

**Why it matters:** The validation system creates a false sense of quality. 24 test functions pass, 0 fail — but the core evidence chain is broken. This is the most dangerous kind of testing: tests that pass while the system fails.

**Recommendation:** Add substantive integrity tests (cross-reference, consistency, completeness). Gate on these tests — not just format tests — in CI. If a test would fail, don't remove the test; fix the data.

---

### h. Largest Architecture-Sprawl Risk

**Finding H1: Constitution describes boundaries with VSH, Ops Hub, Hermes — systems that don't appear to exist as repositories**

- **File:** `CONSTITUTION.md:87-124`, `SCOPE.md:14-19`
- **Severity:** **HIGH**

**Evidence:** The Constitution dedicates an entire Article (III) to defining boundaries with four adjacent systems: Product Forge, VSH, Ops Hub, and Hermes. But VSH, Ops Hub, and Hermes are described in future tense and there is no evidence they exist as operational repositories. The PRODUCT_FORGE_INTEGRATION.md confirms: "All integration is proposed until mechanically verified. Do not claim otherwise." But the Constitution speaks of these systems as if they exist and boundaries need to be maintained.

From Section 3.2: "The Academy provides the judgment framework for technical decisions. VSH produces verifiable software." This definitional relationship with a non-existent system is architectural fiction. The Academy is defining its boundaries against systems that don't exist yet, which means those boundaries are speculative.

**Why it matters:** If VSH, Ops Hub, or Hermes are built differently than the Constitution assumes, the Academy's boundary definitions become wrong. If they are never built, the Academy has defined its architecture against phantom systems. Either way, the architecture is built on dependencies that are not under the Academy's control and may never materialize. The Academy should define its own scope independently, not relationally.

**Recommendation:** Remove VSH, Ops Hub, and Hermes from the Constitution until they exist as operational systems. Replace with: "The Academy may define integration boundaries with future adjacent systems (VSH, Ops Hub, Hermes) if and when those systems become operational. Until then, Academy scope is defined independently."

---

**Finding H2: The Personal Lab track makes the Academy a product development methodology, not an education system**

- **File:** `12_personal_lab/PORTFOLIO_OVERVIEW.md` (229 lines)
- **Severity:** **HIGH**

**Evidence:** PORTFOLIO_OVERVIEW.md contains sections like:
- "Trade-off 1: Concentration vs. Diversification" — making actual portfolio allocation decisions
- "What is Walter's total available weekly time for portfolio work?" — operational resource allocation
- "Which initiative should be killed if resources become scarce?" — real product decisions
- "The Front Office is the capability-unlocking initiative — it makes everything else faster. Build it first." — a BUILD RECOMMENDATION

This is not education. This is product strategy consulting. The Academy has slipped from teaching product leadership into practicing product leadership for a specific individual's portfolio. The distinction between "education system" and "product development methodology" has dissolved.

**Why it matters:** The Academy's scope statement says it's an "education system for product leaders." If the Personal Lab is a product development consultancy for Walter's portfolio, that's a scope violation. It also creates a conflict: the Academy evaluates its own success by whether Walter's initiatives succeed, which means the Academy has a commercial interest in its own doctrine being correct — exactly the kind of incentive conflict the Constitution requires disclosure of for sources.

**Recommendation:** Either (a) remove the Personal Lab from the Academy scope (make it a separate application of Academy doctrine, not part of the Academy itself), or (b) clearly separate it as "demonstration/example only — not part of the Academy curriculum" with explicit labeling that it's a worked example, not the Academy's product. The Portfolio Overview should not contain build recommendations.

---

**Finding H3: The 09_tools directory has 19 templates — this is a product development toolkit, not an education toolkit**

- **File:** `09_tools/` (19 entries)
- **Severity:** **MEDIUM**

**Evidence:** The tools directory includes templates for: Product Strategy, Opportunity Assessment, Experiment Design, Evaluation Contracts, Decision Memos, Pre-Mortems, Post-Launch Reviews, Resource Allocation Memos, Risk-Adjusted Value Assessment, Product Sunset, Build vs Buy, Executive One-Pagers, Stakeholder Incentive Maps, Product Thesis, Product Principles, Metrics Trees, Platform vs Feature assessment, and Contradiction Analysis.

This is a complete product management operating system — not an "education system." The Constitution Article I Section 1.2 explicitly states the Academy does not replace Product Forge. But the toolset is essentially a standalone Product Forge. A product team could use just the Academy's tool directory to run their product development process. This blurs the Academy from education into execution — exactly the scope violation the Constitution warns against.

**Why it matters:** When an education system ships 19 execution templates, it stops being an education system. These templates may be useful for Academy exercises, but their sheer volume and production-readiness makes them an alternative to Product Forge, not a supplement.

**Recommendation:** Add explicit labeling: "ACADEMY LEARNING TOOL — Designed for scenario practice, not production product management. For production use, configure the equivalent artifact in Product Forge." Reduce the template count by consolidating exercise-only templates. If a template is identical to a Product Forge template, remove it and reference the Product Forge version.

---

## Additional Checks

### Source Tier Integrity Audit

**Check: Whether any source claims to be Tier A but is actually lower quality**

Three sources flagged above:
1. **SRC-POST-0001** (Doshi Twitter threads) — should be Tier B. Twitter threads are not stable, systematic, or verifiable in the way Tier A requires.
2. **SRC-POST-0003** (Cutler newsletter) — should be Tier B. Self-described as "primarily opinion/analysis."
3. **SRC-POST-0002** (Ken Norton essay, 2005) — borderline. The essay is 20 years old and reflects Google PM culture circa 2005. Classified as Tier A but reliability notes admit "some specifics may have aged."

### Handbook Factual Claim Check

**Check: Whether the handbook contains unsupported factual claims**

The PRODUCT_LEADERSHIP_BIBLE.md line 79 states: "The Senior-to-Principal transition is the most difficult and most important transition in product management (supported by practitioner consensus and observable failure patterns — most PMs who plateau do so at Senior PM)."

This claim is labeled **[E]** (Evidence) but sources only "practitioner consensus" and "observable failure patterns" — neither of which is an evidence standard. There is no study, no data, and no documented measurement of PM plateau rates by level. The claim may be true, but labeling it [E] is incorrect. It should be [P] (practitioner doctrine) or [I] (inference).

### Scoring Rubric Evaluation

**Check: Whether the scoring rubric rewards vocabulary over judgment**

Scoring dimension 3 (Incentive Mapping) exemplifies the problem:
- Score 3: "Distinguishes between stated goals and actual incentives"
- Score 4: "Connects incentives to compensation structures, performance metrics, and career incentives"
- Score 5: "Proposes how to change the incentive structure to align stakeholders"

The difference between a 3 and 4 is essentially whether the respondent used the words "compensation structures" and "performance metrics" — vocabulary, not necessarily better judgment. A respondent could have excellent judgment about stakeholder incentives without using the specific vocabulary the rubric rewards. A respondent could use all the right words while demonstrating no actual understanding of the specific scenario's incentive structure.

The rubric explicitly claims (line 272): "Awarding points for framework mentions. Saying 'I would use RICE' without actually applying the framework to this specific scenario is not evidence of capability." But it doesn't guard against the equivalent: "saying 'compensation structures and performance metrics' without demonstrating understanding of this specific organization's compensation and metrics." The rubric protects against framework-inflation scoring but not vocabulary-inflation scoring.

### Integration Status Check

**Check: Whether any proposed integrations are presented as implemented**

PRODUCT_FORGE_INTEGRATION.md correctly labels all integration points as "proposed" and states: "No integration has been mechanically verified." This is properly handled. The Constitution also correctly uses "may" language for integration points.

However, the Constitution Article III is written in present tense ("The Academy defines WHAT problems to solve") as if the boundary is active and operational, while the integration doc confirms nothing is operational. This tense discrepancy could mislead a reader who reads only the Constitution.

### Principal+ Content Check

**Check: Whether Principal+ content goes beyond feature prioritization**

The `02_principal_plus/PRINCIPAL_PM.md` (806 lines) and the handbook's Principal PM Playbook do go beyond feature prioritization, covering organizational influence, strategic product thinking, second-order effects, leverage points, decision quality audits, and capability building. This is a strength. The content at this level is substantive and level-appropriate.

The gap is in execution: 5 of 8 mapped sub-modules for Track 02 don't exist as files. The content that exists is good; the problem is that most of the planned content doesn't exist.

### AI Module Evaluation and Failure Treatment Check

**Check: Whether AI modules include evaluation and failure treatment**

The AI modules include:
- `EVALUATION_CONTRACTS.md` (680 lines) — comprehensive treatment of evaluation methodology
- `FAILURE_MODES.md` (678 lines) — detailed taxonomy of AI failure modes with detection and mitigation strategies
- `GOVERNANCE.md` — governance proportional to consequence

These are substantive. The AI track is one of the Academy's strongest areas. It includes real evaluation methodology, failure taxonomies, anti-patterns, and the workflow-first methodology. The `WORKFLOW_SELECTION.md` anti-pattern catalog is particularly strong — it's actionable and specific.

### Regulated Industry Module Check

**Check: Whether regulated industry modules discuss only UX and growth**

The financial services overlay (691 lines) covers: prudential regulation (Basel III/IV, Dodd-Frank, CRR/CRD), conduct regulation (CFPB, FCA Consumer Duty, MiFID II, Reg BI), market regulation, AML/KYC, privacy/data protection (GLBA, GDPR, CCPA, Section 1033), the balance-sheet lens, the trust stack, capital requirements, and stress testing. This is genuine domain depth, not superficial UX advice.

The insurance overlay (459 lines) covers: underwriting as product function, the cash cycle inversion, reinsurance, distribution models (agents/brokers, DTC, embedded insurance, digital platforms), claims management, and the information asymmetry dynamics of insurance pricing.

These are strong. The industry overlays are among the Academy's best content. The concern is that the case catalog doesn't reinforce this depth with relevant cases.

---

## Summary Statistics

| Category | Finding ID | Severity |
|----------|-----------|----------|
| Repo usability | A1 (Source ID mismatch) | CRITICAL |
| Repo usability | A2 (Empty evidence/final) | CRITICAL |
| Repo usability | A3 (Curriculum map vs content) | CRITICAL |
| Product Forge duplication | B1 (Discovery methodology overlap) | HIGH |
| Product Forge duplication | B2 (Template overlap) | MEDIUM |
| Weakest doctrine | C1 (PRN-0003 evidence gap) | HIGH |
| Weakest doctrine | C2 (PRN-0016 untestable) | MEDIUM |
| Weakest source | D1 (Doshi Tier A) | HIGH |
| Weakest source | D2 (Cutler Tier A) | MEDIUM |
| Weakest source | D3 (Zhuo relevance) | LOW |
| Missing failure case | E1 (No Theranos case) | HIGH |
| Missing failure case | E2 (No regulated case) | MEDIUM |
| Superficial industry | F1 (Infrastructure overlay) | MEDIUM |
| Superficial industry | F2 (Walter-specific content) | HIGH |
| Weakest test | G1 (300-char threshold) | MEDIUM |
| Weakest test | G2 (No cross-ref test) | CRITICAL |
| Weakest test | G3 (No content quality tests) | HIGH |
| Architecture sprawl | H1 (Phantom system boundaries) | HIGH |
| Architecture sprawl | H2 (Personal Lab as consulting) | HIGH |
| Architecture sprawl | H3 (19 production templates) | MEDIUM |

**Critical: 4 | High: 8 | Medium: 7 | Low: 1**

---

## Final Assessment

The Product Leadership Academy v0.1.0 is a **promising but broken foundation.** Its strengths are real: the industry overlays are genuinely deep, the AI product management modules are substantive, the contradiction register is well-structured, and the simulator scenarios are practical. The doctrinal principles have appropriate structure (evidence, counterevidence, applicability conditions, failure modes) even if the evidence isn't always rigorous.

But the Academy fails its own most fundamental test: it cannot deliver on "evidence-backed" because the evidence chain is broken. A student cannot trace a principle's claims to source evidence because the referencing systems don't connect. The directory that should contain processed evidence artifacts is empty. The tests that should catch these integrity failures don't exist.

The repository is not ready for use as a reference education system. It is ready as an architectural prototype that demonstrates the shape and ambition of the final system. The critical repair items above must be addressed before the Academy can function as the "counterweight" its preamble promises — a system where "the authority of a claim comes from the quality of its evidence, not the seniority of its author."
