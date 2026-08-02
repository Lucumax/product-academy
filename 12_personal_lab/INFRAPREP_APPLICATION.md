# InfraPrep — Academy Application

**Date:** 2026-08-01  
**Evidence labels applied throughout**

---

## 1. Product or Initiative

**InfraPrep** — A Managed Agentic Infrastructure Preparation Facility + Platform, currently at v0.1. Its first commercial wedge: early-stage energy and climate infrastructure pipeline preparation in Latin America and the Caribbean. *(Local-source fact: from InfraPrep/README.md)*

The initiative must prove 5 things before expanding: (1) a repeatable buyer problem, (2) expert-grade evidence quality, (3) measurable preparation value, (4) paid demand, and (5) renewal or expansion. *(Local-source fact)*

**State transition the product targets:** `Unstructured project pipeline → evidence-backed advance / hold / redesign / stop recommendation`

---

## 2. Product Archetype

**Primary:** Platform / Infrastructure (Archetype 3 in `archetype_catalog.md`) — but an unusual variant.

**Why Platform/Infrastructure:**
- The value is indirect (enables better infrastructure investment decisions, not directly consumed) *(Inference)*
- Customers are sophisticated (development finance institutions, infrastructure developers, government agencies) *(Inference)*
- Adoption has a long time constant (infrastructure projects have multi-year lifecycles) *(External fact)*
- Build-vs-buy is a constant tension for potential customers (why use InfraPrep vs hire consultants?) *(Inference)*

**Secondary:** AI-Enabled Workflow Product (Archetype 5)
- The core workflow (pipeline → recommendation) is AI-assisted *(Local-source fact)*
- Evaluation of output quality is the hardest product problem *(Inference, from Academy 05_ai_product_management)*

**Secondary:** Market Data / Analytics (Archetype 12)
- The product produces evidence-backed recommendations, essentially a data product *(Inference)*

**Archetype-specific doctrine that applies:**
- Platform product leadership demands from `archetype_catalog.md`: Technical fluency (highest requirement), Strategic sequencing (building before teams are ready = wasted investment), Adoption architecture (platforms require developer relations, documentation, migration support) *(External fact)*

---

## 3. Industry

**Primary:** Infrastructure / Development Finance / Energy

**Key industry characteristics:**
- Highly regulated, multi-jurisdictional *(External fact)*
- Capital-intensive with long development cycles *(External fact)*
- Multiple stakeholders with conflicting interests (developers, financiers, governments, communities) *(External fact)*
- Decision quality has real-world consequences — a bad recommendation could waste millions or cause environmental/social harm *(Inference)*
- Evidence standards are high and contested — what counts as "expert-grade"? *(Unknown)*

**Academy industry overlays that apply (Track 06):**
- `INFRASTRUCTURE_AND_DEVELOPMENT_FINANCE.md` *(External fact, from file existence in 06_industry_overlays/)*
- `POWER_AND_ENERGY.md` *(External fact)*
- The industry overlay for regulated industries (06.1) applies due to multi-jurisdictional regulatory frameworks

---

## 4. Organizational Stage

**Seed-stage / Pre-product** — The InfraPrep facility framework exists (governance, product, architecture, gates, manifests, prompts, templates, validation) but the product has not been built or sold. *(Local-source fact)*

**The README explicit constraint:** "The initiative is not authorized to begin as a broad SaaS platform, horizontal agent framework, or autonomous project-finance adviser." *(Local-source fact)*

This is unusual: the governance structure is more established than the product. The platform thinking precedes the product thinking. *(Inference)*

**Stage-specific Academy doctrine:**
- Pre-PMF: "strategy is 'find PMF by trying things' and exclusion would be premature" (PRN-0002 non-applicability)
- First commercial wedge is correctly defined (energy and climate infrastructure in LAC)
- The gate structure (5 gates from 00_governance through 07_validation) provides clear progression but may be premature structure for pre-PMF

---

## 5. Current User

**No current users** — The facility framework exists but has not been deployed against a real customer. *(Local-source fact)*

**Target users (inferred from README):**
- Infrastructure developers with project pipelines in energy and climate *(Inference)*
- Development finance institutions evaluating portfolios *(Inference)*
- Government agencies managing infrastructure prioritization *(Inference)*

**User characteristics that matter:**
- Highly sophisticated domain experts (they know infrastructure better than any AI tool) *(External fact)*
- Will judge output on expert standards, not consumer standards *(Inference)*
- Slow to adopt new tools; relationship-based decision-making *(Inference)*
- The tool must earn trust by demonstrating competence, not claiming it *(Recommendation)*

---

## 6. Buyer

**Unvalidated** — The README specifies "paid demand" as one of the five things to prove. *(Local-source fact)*

**Potential buyers (inferred):**
- Development finance institutions (DFIs like IDB, World Bank, CAF, etc.) — have budgets for project preparation, need to demonstrate portfolio quality to their own boards *(Inference)*
- Infrastructure developers — need to advance projects from concept to bankability efficiently *(Inference)*
- Government infrastructure agencies — mandated to prioritize and prepare projects *(Inference)*

**Buyer/user split:** Likely. The buyer (institutional budget holder) is different from the user (analyst reviewing project pipelines). This creates the classic enterprise product challenge (Archetype 2). *(Inference)*

**CRITICAL UNKNOWN:** Who actually pays for infrastructure project preparation? The answer determines the commercial viability of the entire initiative. *(Unknown)*

---

## 7. Problem Thesis

**Claim:** Early-stage infrastructure projects (particularly in emerging markets) suffer from insufficient, inconsistent, or biased preparation analysis. This causes good projects to go unfunded and bad projects to waste preparation resources. A structured, agentic preparation facility can produce faster, more consistent, and higher-quality preparation analysis than current methods — reducing the cost and time from pipeline identification to investment decision. *(Inference)*

**The thesis decomposes into sub-claims:**

1. **Problem existence:** Infrastructure preparation analysis is currently insufficient/biased → **Moderate evidence** (general industry knowledge, but not specific to the LAC energy/climate wedge) *(External fact)*
2. **Problem magnitude:** The cost of bad preparation decisions is large enough to justify a new tool → **Unknown** (not quantified for the target market)
3. **Solution fit:** Agentic analysis can match or exceed human expert quality → **Unknown** (no benchmark data)
4. **Economic viability:** The cost of running InfraPrep is less than the value of improved decisions → **Unknown** (neither cost nor value has been measured)
5. **Buyer willingness:** Someone will pay for this → **Unknown** (the README lists this as something to prove)

---

## 8. Evidence Status

**What we know (Local-source fact):**
- The facility framework defines governance, product, architecture, gates, manifests, prompts, templates, and validation
- The launch sequence is defined: Ops Hub registers → PAL authorizes → Product Forge runs discovery → Benchmark proves workflow → Independent expert adjudicates → Paid sprint proves commercial value → VSH builds minimum workspace
- The first wedge is "energy and climate infrastructure pipeline preparation in Latin America and the Caribbean"
- Explicit non-goals include: replacing engineers/lawyers/environmental specialists, declaring projects bankable, automating investment approval, building a general-purpose platform
- The routing table in README.md defines clear boundaries between ecosystem components

**What we know (External fact):**
- Infrastructure project preparation is a recognized bottleneck in development finance
- Climate infrastructure investment needs to scale dramatically (trillions in gap)
- Emerging market infrastructure faces higher preparation costs and longer timelines
- AI/agentic tools for infrastructure analysis are an emerging category

**What we don't know (Unknown):**
- Whether the public-data benchmark will produce expert-grade quality
- Whether independent experts will adjudicate results positively
- Whether there is a buyer willing to pay for the Portfolio Readiness Sprint
- What "measurable preparation value" looks like in practice
- Whether the agentic workflow can handle domain complexity in infrastructure
- What the competitive landscape looks like (are DFIs developing internal tools?)

---

## 9. Product-Leadership Questions

**From Academy industry overlays:**
- What regulatory frameworks govern infrastructure preparation advice? Is there liability for wrong recommendations? *(Unknown)*
- Does InfraPrep need to be physically co-located with projects or can it operate remotely? *(Unknown)*
- What data sources are available for public-data benchmarks in LAC energy infrastructure? *(Recommendation — investigate)*

**From PRN-0009 (Platform Decisions):**
- Is InfraPrep a facility (service), a platform (extensible), or a product (standalone)? The naming suggests all three. *(Recommendation — pick one)*
- What is the platform paradigm? The README discusses Domain OS, which implies platform, but the gate structure implies service. *(Inference)*

**From PRN-0005 (PM Owns the Problem):**
- Does InfraPrep solve a problem infrastructure professionals know they have, or a problem Walter hypothesizes they have? *(Unknown)*
- Have any potential customers been interviewed about their preparation workflows? *(Unknown)*

**From AI Workflow Selection (Module 05):**
- What is the error tolerance for infrastructure preparation recommendations? (Error severity: recommending a bad project for investment has massive financial and social consequences) *(Inference)*
- Should the AI be an advisor (with human decision) or an analyst (with human review)? *(Recommendation — advisor only, given error severity)*

**From CON-0011 (Human-in-the-Loop):**
- The README non-goals say "replacing engineers, lawyers, environmental specialists" — where exactly does human judgment end and agentic analysis begin?
- CON-0011 context_where_a_stronger: high-stakes decisions, edge-case-rich domains, regulated industries — all apply to infrastructure

---

## 10. Principal-Level Trade-offs

**Trade-off 1: Expert Quality vs. Speed/Cost**
- Infrastructure experts (engineers, financial analysts, environmental specialists) produce high-quality preparation analysis but are expensive, scarce, and slow
- Agentic analysis is faster and cheaper but quality is unproven
- The optimal solution may be agentic first pass + expert review, but this might not reduce cost enough to justify
- *(Recommendation):* Benchmark agentic quality against expert quality before selling. The public-data benchmark in the launch sequence is the right approach (Module 05, Part 4 — Product Performance Model)

**Trade-off 2: Narrow Wedge vs. Ambitious Vision**
- The energy/climate infrastructure wedge in LAC is appropriately narrow for proving commercial viability
- But the governance structure (Domain OS, routing table, 7 directory layers) implies ambitions far beyond the wedge
- The risk is building a governance framework for a platform that may never have users (the "platform before product" failure mode from archetype_catalog.md Platform archetype failure mode #1)
- *(Recommendation):* Gate everything behind the first paid customer. The platform architecture can be designed but not built until Gate 4.

**Trade-off 3: Transparency of Methodology vs. Proprietary Advantage**
- Infrastructure preparation typically involves proprietary methodologies (consulting firms' "secret sauce")
- InfraPrep is built on open Academy doctrine — methodology is transparent
- Transparent methodology builds trust with expert users but reduces competitive moat
- *(Recommendation):* Methodology transparency is a differentiator in infrastructure (experts will want to see the work). The moat is execution quality, not methodological secrecy.

**Trade-off 4: Agent Autonomy vs. Human Oversight**
- The routing table gives Hermes orchestration authority and Walter final human approval
- As the system proves itself, should agent autonomy increase?
- Infrastructure decisions are CON-0011 context_where_a_stronger (high stakes, regulated) — maintain human oversight as a permanent feature, not a transitional state
- *(Recommendation):* Human-in-the-loop should be a product feature, not a temporary limitation. Market it as "expert-augmented AI" not "AI replacing experts."

---

## 11. Risks

**Risk 1: Expert Rejection (High probability, High severity)**
- Infrastructure professionals dismiss agentic analysis as insufficiently rigorous
- The tool produces analysis that looks credible to non-experts but is recognized as flawed by domain experts
- *Mitigation:* Independent expert adjudication (step 5 of launch sequence) is the right mechanism. But it must be genuine — the experts must be able to fail the work, and that failure must be accepted.

**Risk 2: Liability Exposure (Medium probability, High severity)**
- If InfraPrep recommends advancing a project and the project fails, who is liable?
- The README non-goals attempt to manage this ("not declaring projects bankable," "not automating investment approval")
- But in practice, the line between "recommendation" and "advice" is thin
- *Mitigation:* Legal review of liability before any commercial engagement. Disclaimer architecture as a product requirement.

**Risk 3: Data Scarcity in Target Market (Medium probability, Medium severity)**
- LAC energy infrastructure data may not be available at sufficient quality for agentic analysis
- Public data sources may be incomplete, outdated, or biased
- *Mitigation:* The public-data benchmark (step 4 of launch sequence) must explicitly test data availability and quality. If the data isn't there, the thesis is falsified.

**Risk 4: Platform Before Product (Medium probability, Medium severity)**
- The extensive governance structure (7 directory layers) risks building a platform before anyone needs it
- This is failure mode #1 for the Platform archetype in the Academy catalog
- *Mitigation:* Strictly enforce the gate structure. No platform architecture beyond what's needed for Gate 0-1. VSH builds only "the minimum reusable workspace justified by repeated workflow."

**Risk 5: Mission Drift into Consultancy (Low probability, Medium severity)**
- If agentic analysis isn't sufficient, the natural evolution is toward human consulting (Walter doing infrastructure preparation manually)
- This would violate the explicit non-goals and turn InfraPrep into a services business
- *Mitigation:* Clear metrics distinguishing product revenue from services revenue. If services revenue exceeds product revenue, the initiative has drifted.

---

## 12. Missing Validation

**Critical unknowns ranked by importance:**

1. **Buyer existence:** Is there anyone willing to pay for infrastructure preparation analysis? *(Recommendation):* 5 customer discovery interviews with potential buyers before any product development.
2. **Expert quality threshold:** What quality level do infrastructure experts consider "good enough" for a recommendation? *(Recommendation):* Define quality criteria with domain experts before building. Use the Academy Evaluation Contracts framework (05_ai_product_management/EVALUATION_CONTRACTS.md).
3. **Data availability:** Can a public-data benchmark actually be constructed for the target market? *(Recommendation):* Attempt to construct the benchmark dataset before building any analysis pipeline. If the data doesn't exist, stop.
4. **Workflow decomposition:** What exactly do infrastructure preparers do? *(Recommendation):* Apply the Academy Workflow Selection methodology (Module 05, Part 1) — describe the workflow without mentioning AI, decompose into subtasks, classify each by AI suitability.
5. **Competitive landscape:** Are DFIs, consulting firms, or other organizations already building this? *(Unknown)*

---

## 13. Most Useful Academy Doctrine

| Doctrine | Relevance | Application |
|----------|-----------|-------------|
| **Industry overlay: Infrastructure & Development Finance** (06_industry_overlays/) | Critical | Domain-specific constraints on evidence, regulation, stakeholder complexity |
| **Industry overlay: Power & Energy** (06_industry_overlays/) | High | Energy sector-specific product leadership constraints |
| **PRN-0008** (Customer Discovery) | Critical | Before building, must discover whether infrastructure professionals have this problem |
| **PRN-0004** (PMF Is a Condition) | High | Must maintain PMF as the wedge widens; what works for energy in LAC may not work for transport in Africa |
| **PRN-0009** (Platform Decisions) | High | The platform vs product tension is central to InfraPrep's design |
| **PRN-0003** (Cost of Delay vs Imperfection) | High | In infrastructure, decisions are high-stakes; the cost of being wrong may exceed the benefit of being fast |
| **PRN-0010** (Org Design Is Product Design) | Medium | The ecosystem routing table is an organizational design decision that shapes the product |
| **AI Workflow Selection** (Module 05) | Critical | Which parts of infrastructure preparation are appropriate for AI? |
| **AI Evaluation Contracts** (Module 05) | Critical | How to define and measure "expert-grade" quality for infrastructure analysis |
| **AI Failure Modes** (Module 05) | High | Infrastructure-specific failure modes for AI analysis |
| **AI Governance** (Module 05) | High | Governance proportional to consequence — infrastructure consequence is high |
| **CASE-0005** (Knight Capital) | High | The cost of automation failure in high-stakes domains |
| **CON-0011** (Human-in-the-Loop) | Critical | Infrastructure analysis is context_where_a_stronger — keep humans in the loop |
| **CON-0006** (Speed vs Quality) | High | In infrastructure, the quality/assurance bar must be higher than consumer products |
| **Decision Framework 4** (Build-Buy-Partner) | Medium | How much of the analysis infrastructure should be built vs bought? |

---

## 14. Cheapest Decisive Test

**Test:** Conduct 5 structured customer discovery interviews with potential buyers of infrastructure preparation services (DFI program officers, infrastructure fund analysts, government infrastructure planners).

**Protocol:** Academy Discovery Interview Protocol (from PRN-0008 practical tool):
1. "Tell me about the last time you had to prepare an infrastructure project for investment decision."
2. "What made that experience good or bad?"
3. "What do you do today to prepare projects? What tools, consultants, processes?"
4. "What have you tried that didn't work?"
5. "If you could wave a magic wand, what would ideal infrastructure preparation look like?"
6. "Why is that important to you?"

**Cost:** ~10 hours total (scheduling, conducting, analyzing 5 interviews)

**Decisive if:**
- All 5 interviewees say they have no problem with current preparation → problem thesis is falsified
- All 5 interviewees describe the same pain point → strong problem validation
- Interviewees mention specific budgets for preparation tools → buyer validation

**If the test is ambiguous:** Run the public-data benchmark (step 4 of launch sequence) as the next test. If the benchmark shows that agentic analysis cannot match expert quality on real infrastructure data, stop.

---

## 15. What Would Reverse the Current View

**Current view:** InfraPrep is a promising application of agentic analysis to a real infrastructure problem, worth exploring through the gate structure defined in the README. *(Recommendation)*

**The view should be reversed if:**
1. Customer discovery reveals no willingness to pay for infrastructure preparation analysis
2. The public-data benchmark shows agentic analysis quality is below expert threshold and improving it requires domain expertise the system cannot acquire
3. Data availability in the target market is insufficient for meaningful analysis
4. Liability concerns make the product commercially unviable
5. A competitor (DFI internal tool, consulting firm product) already dominates the niche
6. Gate 0 (governance approval) or Gate 1 (permissions) cannot be completed within 90 days — indicating the ecosystem overhead exceeds the initiative's value

**The view should be strengthened if:**
1. Customer discovery reveals specific, painful preparation workflows with budget attached
2. The public-data benchmark produces analysis that independent experts rate as "useful" or "comparable to junior analyst"
3. A paid Portfolio Readiness Sprint converts a prospect
4. The first customer renews or expands

---

*This application should be revisited after completing customer discovery (5 interviews) and the public-data benchmark. The prevalence of "Unknown" labels indicates this is an early-stage initiative with more questions than answers — which is appropriate for the current gate.*
