# Product Leadership Bible

**A coherent, source-linked, context-sensitive reference for product leaders making real decisions.**

**Status:** v0.1.0  
**Evidence taxonomy:** Every claim in this Bible is labeled with its epistemic status:
- **[E]** Evidence — Supported by empirical research, documented outcomes, or verified case data
- **[P]** Practitioner doctrine — Widely held among experienced practitioners but not formally verified
- **[I]** Inference — Reasonable conclusion from available evidence, not directly observed
- **[D]** Open debate — Reasonable practitioners disagree; no settled answer
- **[R]** Practical recommendation — What to do, based on evidence and judgment

---

# Part 1: The Product Leader's Foundation

## 1.1 What Product Leadership Is

Product leadership is the practice of making decisions about what to build, for whom, and why — at levels of consequence that affect organizations, markets, and users. It is distinct from product management (which focuses on individual products) and from general management (which focuses on organizational effectiveness). Product leadership sits at the intersection of:

- **Strategic reasoning** — Which problems are worth solving?
- **Execution architecture** — How do you convert decisions into outcomes?
- **Organizational leverage** — How do you multiply impact through others?
- **Institutional leadership** — How do you shape the system itself?

**[P]** This four-cluster model is the Academy's synthesis of practitioner frameworks (Cagan, Torres, Doshi, Cutler, SVPG, Reforge) into a coherent capability model. It is practitioner doctrine, not empirically verified.

**[E]** The distinction between product leadership and product management is supported by case evidence: the decisions that most affected company outcomes (CASE-0002 iPhone, CASE-0004 Microsoft transformation, CASE-0005 Knight Capital) were leadership decisions, not management decisions. They involved resource allocation, strategic direction, and organizational design — not feature prioritization or backlog management.

## 1.2 The Capability Model Summary

The Academy's capability model (`00_orientation/CAPABILITY_MODEL.md`) organizes product leadership capabilities into four clusters and four levels. Here is the essential summary:

### The Four Clusters

**Cluster 1: Strategic Reasoning** — How you decide what matters
- 1.1 Problem Selection — Choosing the right problems
- 1.2 Product Thesis — Falsifiable theories of value creation
- 1.3 Customer and Domain Understanding — Deep, non-obvious insight
- 1.4 Product Judgment and Taste — Decisions without complete data
- 1.5 Technical Fluency — Engaging with technical systems
- 1.6 Data and Evaluation Fluency — Meaningful measurement
- 1.7 Business Economics — Unit economics, pricing, monetization
- 1.8 Risk Judgment — Decisions under uncertainty
- 1.9 Portfolio Allocation — Resource allocation across opportunities

**Cluster 2: Execution Architecture** — How you convert decisions into outcomes
- 2.1 Strategic Sequencing — Ordering work for compounding advantage
- 2.2 Cross-Functional Influence — Aligning without authority
- 2.3 Executive Communication — Communicating to leadership
- 2.4 Outcome Ownership — Accountability for results

**Cluster 3: Organizational Leverage** — How you multiply impact
- 3.1 Adoption and Change Management — Getting products used
- 3.2 Organizational Multiplication — Making teams more effective
- 3.3 Talent Development — Developing other product leaders
- 3.4 Decision Systems — Building organizational decision-making capability

**Cluster 4: Institutional Leadership** — How you shape the system
- 4.1 Product Strategy — Company-level product direction
- 4.2 Organizational Design — Structuring for product outcomes
- 4.3 Capital Allocation — Deploying financial resources
- 4.4 Board and External Narrative — External product leadership
- 4.5 Product Culture — Shaping how the organization thinks about product

### The Four Levels

| Level | Role | Primary Shift |
|-------|------|---------------|
| **L1: Senior PM** | Individual product leader | From execution to strategy within a bounded context |
| **L2: Principal PM** | Multi-team product leader | From solving defined problems to defining which problems matter |
| **L3: Director** | Portfolio leader | From individual decisions to organizational decision systems |
| **L4: VP/CPO** | Institutional leader | From product decisions to company-defining choices |

**[P]** These level distinctions are the Academy's synthesis. They are observed across the practitioner community but the boundaries between levels vary by organization size, industry, and stage.

## 1.3 Level Distinctions: What Actually Changes

**[E]** The Senior-to-Principal transition is the most difficult and most important transition in product management (supported by practitioner consensus and observable failure patterns — most PMs who plateau do so at Senior PM).

**[P]** What changes at each level:

**Senior PM → Principal PM:** The core shift is from executing strategy to defining strategy. At Senior PM, you receive a problem and solve it. At Principal PM, you define what the problem IS. Your primary output shifts from shipped features to strategic influence and decision quality across organizational boundaries. (See `02_principal_plus/PRINCIPAL_PM.md` for full treatment.)

**Principal PM → Director:** The core shift is from individual influence to organizational systems. At Principal PM, you influence decisions through personal capability. At Director, you design the systems, processes, and culture that produce good decisions without your personal involvement. Your primary output shifts from decisions to decision-making capability.

**Director → VP/CPO:** The core shift is from product leadership to institutional leadership. At Director, you lead product within a bounded domain. At VP/CPO, you define what the company builds, for whom, and why — with board-level accountability. Your primary output shifts from portfolio outcomes to company-level product strategy and organizational design.

**[D]** The question of whether these level transitions are universal or organization-dependent is open. At very small companies, a Director may operate at what would be VP level at a larger company. At very large companies, a Principal PM may have more organizational influence than a Director at a smaller company. The capability model describes capabilities, not titles.

---

# Part 1B: The Evidence Philosophy

## The Academy's Epistemic Stance

**[I]** The Product Leadership Academy takes a specific position on evidence: product leadership is undertheorized and undermeasured relative to its importance. Many "best practices" are practitioner doctrine with no systematic evidence. Some widely held beliefs are wrong. Some counterintuitive approaches are supported by evidence. The Academy's job is to distinguish the known from the believed.

This Bible labels every claim with its epistemic status:

- **[E] Evidence** — Supported by empirical research, documented outcomes, or verified case data. Examples: DORA/Accelerate research on deployment frequency and organizational performance (SRC-BOOK-0027); Knight Capital's documented $440M deployment failure (SRC-POST-0011); Morningstar research on managed account participant outcomes (TIAA application evidence).

- **[P] Practitioner doctrine** — Widely held among experienced practitioners but not formally verified. Most product management "best practices" fall here. The Academy does not dismiss practitioner doctrine — it acknowledges it as potentially valuable but unverified. Examples: The SVPG empowered team model; the Amazon working-backwards process; the Spotify squad model before it was abandoned.

- **[I] Inference** — Reasonable conclusion from available evidence, but not directly observed. The Academy makes inferences explicit so readers can evaluate the chain of reasoning. Examples: "PMF decay is the norm, not the exception" (inferred from the Innovator's Dilemma pattern but not systematically measured); "platform-before-product is the most common platform failure" (inferred from case observation but not quantified).

- **[D] Open debate** — Reasonable practitioners disagree; no settled answer. The contradictions register (`08_contradictions/register.yaml`) collects these. Examples: Empowered teams vs central direction; customer discovery vs strategic conviction; speed vs quality.

- **[R] Practical recommendation** — What to do, based on evidence and judgment. Recommendations are the Academy's output: given what we know (and what we don't), here's what we recommend you do. Recommendations are NOT claims of certainty — they are direction based on the best available evidence.

## How to Evaluate Source Quality

**[R]** Not all sources are equal. The Academy classifies sources by type and strength:

**Source types:**
- **BK (Book):** Practitioner book. Valuable synthesis, not peer-reviewed. Strength varies widely. SRC-BOOK-0015 (Rumelt) and SRC-BOOK-0027 (Forsgren et al.) are evidence-rich. SRC-BOOK-0001 (Cagan) is practitioner doctrine. SRC-BOOK-0021 (Thiel) is philosophical argument.
- **AR (Article/Research):** Varies from peer-reviewed research to blog posts. SRC-POST-0044 (SEC report on Knight Capital) is government investigation. SRC-POST-0009 (Superhuman case) is practitioner blog.
- **TK (Talk/Presentation):** Conference talks, keynotes, interviews. Often the first articulation of practitioner doctrine. SRC-TALK-0005 (Chesky on Airbnb re-centralization) is a CEO describing their own decisions — first-hand account, but self-reported.
- **CS (Case Study):** The Academy's own case studies based on public information. CASE-0001 through CASE-0006. Strength: structured analysis using consistent framework. Limitation: based on public information, not internal data.

**Evidence strength levels:**
- **Strong:** Multiple independent sources, documented outcomes, clear causal chain, replicated across contexts
- **Moderate:** One or two sources, plausible causal chain, consistent with related evidence, not contradicted
- **Weak:** Single source, speculative causal chain, contradicted by other evidence, or anecdotal
- **Correlation only:** Observed relationship without established causality

## What the Academy Does Not Know (And Is Honest About)

**[I]** The Academy identifies significant gaps in the evidence base. These are not failures — they're honest acknowledgments of where the field needs more research:

1. **We don't know the optimal degree of team autonomy at different organizational scales.** CON-0001 captures this, but the specific inflection points are unknown.
2. **We don't know whether AI-assisted development meaningfully changes build-vs-buy economics.** CON-0010 asks this; the evidence isn't in yet.
3. **We don't know the long-term effects of AI on product management as a profession.** Will AI augment PMs or replace significant PM functions? Unknown.
4. **We don't know which pricing models are optimal for different product archetypes.** PRN-0006 identifies pricing as important, but optimal pricing strategy by archetype is underexplored.
5. **We don't know whether "product sense" can be systematically developed or is primarily innate.** CON-0007 touches on this; the answer has major implications for PM hiring and development.
6. **We don't have good metrics for product leadership quality.** We measure product outcomes (revenue, retention, NPS) but can't reliably attribute them to product leadership vs market conditions vs execution quality vs luck.
7. **We don't know the failure rate of product leadership frameworks in practice.** How many "empowered teams" implementations fail? How many "continuous discovery" adoptions produce better products? The evidence is anecdotal.

**[R]** The Academy's position: acknowledging what we don't know is more useful than pretending we know. When you apply Academy doctrine, check: does the doctrine rest on evidence or inference? If inference, what's your plan to validate or invalidate it in your context? The Personal Lab (`12_personal_lab/`) is designed for this — applying doctrine with explicit evidence tracking.

## How to Read Source References in This Bible

**[R]** Throughout this Bible, you'll see source references like SRC-BOOK-0001, CASE-0004, CON-0007. Here's how to trace them:

- **SRC-XX-NNNN:** Source reference. BK = book, AR = article, TK = talk. The complete source catalog with full citations is maintained in the Academy's evidence directory.
- **CASE-NNNN:** Case study from `07_cases/case_catalog.md`. Each case provides situation, analysis, and discussion questions.
- **CON-NNNN:** Contradiction from `08_contradictions/register.yaml`. Each contradiction captures the debate, evidence on both sides, and context factors.
- **PRN-NNNN:** Principle from `01_core_doctrine/PRINCIPLES.md`. Each principle includes the claim, evidence, counterevidence, applicability conditions, and practice exercises.

When a Bible claim cites a source, follow the reference to understand the evidence behind the claim. Don't take the Bible's word for it — check the source. That's the Academy's commitment to evidence-backed product leadership.

*The Academy maintains 14 canonical principles (`01_core_doctrine/PRINCIPLES.md`). This section presents the 12 most important, with evidence assessment and applicability guidance. For full detail including counterevidence, failure modes, and practice exercises, see the principle source files.*

## 2.1 PRN-0001: Empowered Teams Produce Better Outcomes Than Directed Teams — Under Specific Conditions

**The claim:** Cross-functional product teams with clear outcomes, direct customer access, and decision-making authority outperform centrally-directed teams — when specific enabling conditions are met.

**[E]** Evidence strength: **Moderate to Strong**
- Supporting: Cagan's SVPG research (SRC-BOOK-0001, SRC-BOOK-0001), DORA/Accelerate data on elite performers (SRC-BOOK-0027)
- Counter: Airbnb re-centralized product to fix fragmentation (SRC-TALK-0005), Apple's functional organization produces consistently coherent products (SRC-POST-0002)

**[P]** The conditions matter more than the principle. Empowered teams fail without: (1) well-defined bounded contexts, (2) clear strategic context, (3) experienced cross-functional leadership, (4) alignment mechanisms across teams. Empowerment without these conditions is "empowerment theater" — teams are told they're empowered but every decision is second-guessed.

**[R]** Before empowering a team, assess all four conditions. If any score below 3 on a 5-point scale, invest in that condition before granting full decision autonomy. The Team Empowerment Assessment (PRN-0001 practical tool) provides a structured diagnostic.

**[I]** The Academy's inference: this principle is more applicable to growth-stage and mature tech companies than pre-PMF startups (where a single product visionary may outperform distributed decision-making) and more applicable to consumer, enterprise SaaS, and platform products than to safety-critical or highly regulated domains.

## 2.2 PRN-0002: Strategy Is What You Say No To

**The claim:** The defining act of product strategy is saying no to good ideas. A strategy without explicit exclusions is not a strategy — it's a wish list.

**[E]** Evidence strength: **High**
- Supporting: Rumelt's "Good Strategy Bad Strategy" (SRC-BOOK-0015), Amazon's one-way/two-way door framework (SRC-POST-0013)
- Counter: Weak counterevidence only — some practitioners argue strategy must flex with market conditions (SRC-POST-0025)

**[P]** The Strategy Exclusion Test (PRN-0002 practical tool): for any proposed strategy, list 5 specific things the organization will NOT do as a result. If you cannot list 5, the strategy is not specific enough. This test is simple and devastating — most strategy documents fail it.

**[R]** Apply the Strategy Exclusion Test quarterly. Not just to the written strategy document, but to the actual resource allocation. If you're building things your strategy says you won't build, either the strategy is wrong or the resource allocation is wrong. Fix one of them.

**[I]** Non-applicability: Pre-PMF startups (strategy is "find PMF"), monopoly positions, exploratory research phases. In these contexts, exclusion would be premature.

## 2.3 PRN-0003: The Cost of Delay Exceeds the Cost of Imperfection in Most Product Decisions

**The claim:** For most product decisions, delaying costs more than making an imperfect decision and correcting it later.

**[E]** Evidence strength: **Moderate to Strong**
- Supporting: DORA research (SRC-BOOK-0027), Amazon's "Speed Matters" (SRC-POST-0010), Lean Startup Build-Measure-Learn (SRC-BOOK-0014)
- Counter: Knight Capital lost $440M in 45 minutes from a deployment error (SRC-POST-0011), Boeing 737 MAX (SRC-POST-0094) — catastrophic failures from speed without assurance

**[P]** The key distinction is reversibility (PRN-0007). Speed-over-perfection applies to reversible decisions. For irreversible decisions with catastrophic failure modes, assurance must dominate. The One-Way vs Two-Way Door Classification (Decision Framework 1) provides the framework.

**[R]** Classify every significant product decision as Type 1 (one-way door) or Type 2 (two-way door). Type 2 decisions should be made by the person closest to the information within 48 hours. Type 1 decisions require broader input and explicit reversibility planning. Most organizations misclassify Type 2 decisions as Type 1 out of risk aversion.

**[D]** The boundary between Type 1 and Type 2 is contested. What one organization considers irreversible, another considers standard practice. The Knight Capital case is the canonical warning: a decision that was treated as Type 2 (routine deployment) turned out to be Type 1 (existential financial loss).

## 2.4 PRN-0004: Product-Market Fit Is a Condition, Not a Milestone

**The claim:** PMF is not an event you achieve and move past. It's a condition you must maintain as markets, competitors, and customer needs evolve.

**[E]** Evidence strength: **High**
- Supporting: Ries (SRC-BOOK-0014), Christensen's Innovator's Dilemma (SRC-POST-0003), Christensen's "Competing Against Luck" (SRC-BOOK-0021)
- Counter: Some products maintain PMF for decades through incremental improvement (SRC-POST-0017) — but this is weak counterevidence as it doesn't challenge the "condition not milestone" framing

**[P]** The Sean Ellis test remains the most practical PMF diagnostic: survey active users with "How would you feel if you could no longer use [product]?" If fewer than 40% say "very disappointed," PMF is either not achieved or has decayed.

**[R]** Implement a PMF Health Dashboard with leading indicators: Sean Ellis score, organic growth rate, usage depth, competitive win/loss rate, and the qualitative "what would you use instead?" metric. Monitor quarterly. Lagging indicators (revenue, retention) mask PMF decay until it's too late.

**[I]** PMF decay is the norm, not the exception. The most common cause is optimizing for existing customers while missing emerging needs (the Innovator's Dilemma pattern). Products that achieved PMF more than 2 years ago without systematic reassessment are at risk.

## 2.5 PRN-0005: The Product Manager Owns the Problem, Not the Solution

**The claim:** The PM's primary responsibility is defining and validating the problem. Solutions should emerge collaboratively from the cross-functional team.

**[E]** Evidence strength: **Moderate**
- Supporting: Cagan (SRC-BOOK-0001, SRC-BOOK-0001), practitioner evidence on team outcomes (SRC-POST-0029)
- Counter: In highly technical domains, problem definition requires solution knowledge (SRC-POST-0028, SRC-POST-0030)

**[P]** The distinction between "problem definition" and "solution prescription" is the most common failure mode in PM practice. PMs who define problems clearly and enable their teams outperform PMs who define problems vaguely but prescribe solutions precisely. PMs who do both well are rare and valuable.

**[R]** Use the Problem Statement Template as a required artifact for any significant initiative: (1) Who has this problem? (2) What is the current state and why is it painful? (3) What is the desired state? (4) What is the measurable success criterion? (5) What are the constraints? (6) What assumptions must hold?

**[D]** The builder-vs-multiplier tension (CON-0013) directly bears on this principle. Should the PM be deeply involved in solution creation (builder) or enable the team to create solutions (multiplier)? The Academy's position: the answer depends on organizational stage, team capability, and domain complexity. Early-stage and highly technical domains favor builder; mature organizations with strong engineering leadership favor multiplier.

## 2.6 PRN-0006: Pricing Is the Most Powerful and Most Neglected Product Lever

**The claim:** Pricing decisions have larger impact on product outcomes than most feature decisions, yet PMs spend disproportionately little time on pricing.

**[E]** Evidence strength: **High**
- Supporting: PLG pricing optimization research (SRC-BOOK-0023), enterprise SaaS pricing strategy (SRC-BOOK-0024), conversion improvement data from pricing optimization (SRC-POST-0006)
- Counter: In pure enterprise sales with custom-negotiated deals, product-led pricing frameworks are less applicable (SRC-POST-0017)

**[P]** The Value-Based Pricing Canvas (PRN-0006 practical tool): (1) Identify the customer's current alternative, (2) Quantify the cost of that alternative, (3) Quantify your product's value relative to the alternative, (4) Set price as a fraction of the value gap (typically 10-30% for SaaS), (5) Validate with willingness-to-pay research.

**[R]** Conduct a pricing teardown of every product in your portfolio. Products where pricing has not been reviewed in 18+ months are leaving money on the table or blocking adoption — or both. Establish semi-annual pricing reviews. Treat packaging (how features are bundled into plans) as a product design decision, not a sales enablement decision.

**[I]** The most common pricing failure mode is not underpricing or overpricing — it's pricing neglect. PMs spend 10x more time on features than on pricing, even though pricing changes often have 10x the impact on outcomes.

## 2.7 PRN-0007: The Best Product Decisions Are Reversible by Design

**The claim:** When making a decision with uncertain outcomes, invest in making the decision reversible rather than trying to predict the outcome perfectly.

**[E]** Evidence strength: **High**
- Supporting: Amazon's Type 1/Type 2 framework (SRC-POST-0013), elite DevOps performers' use of feature flags and fast rollback (SRC-BOOK-0027)
- Counter: Knight Capital's reversal mechanism (manual shutdown) took 45 minutes while losses accumulated (SRC-POST-0011) — reversibility must be tested, not assumed

**[P]** The Reversibility Assessment (PRN-0007 practical tool) asks: (1) What is the expected cost if we are wrong? (2) What is the probability we are wrong? (3) What would it cost to make this decision reversible? (4) How quickly could we detect we're wrong? (5) How quickly could we reverse? (6) Is reversibility investment less than (cost of wrong × probability of wrong)?

**[R]** For every major product decision, require a Reversibility Assessment. Invest in the infrastructure that makes reversibility cheap: feature flags, versioned APIs, incremental migration paths. Test reversals in non-critical contexts. An untested reversal mechanism is not a mechanism.

**[I]** The most insidious failure mode is "reversibility theater" — building reversal mechanisms but never having the organizational courage to use them. A feature flag that is never turned off is not a reversibility mechanism; it's configuration debt.

## 2.8 PRN-0008: Customer Discovery Produces Better Decisions Than Customer Requests

**The claim:** Systematic investigation of customer problems produces better product decisions than responding to customer feature requests.

**[E]** Evidence strength: **Moderate to Strong**
- Supporting: Torres' Continuous Discovery (SRC-BOOK-0004), Cagan on customer problems vs solutions (SRC-BOOK-0001), Christensen on listening to existing customers leading to disruption vulnerability (SRC-POST-0003)
- Counter: Some breakthrough products were not discoverable through customer research (SRC-BOOK-0021), customer request systems have produced major improvements (SRC-POST-0017)

**[P]** The Discovery Interview Protocol (PRN-0008 practical tool) focuses on specific past experiences, not hypotheticals: "Tell me about the last time you [did X]." "What made that good or bad?" "What have you tried that didn't work?" "If you could wave a magic wand..." "Why is that important?"

**[R]** Establish a minimum discovery cadence: 2 customer touchpoints per PM per week. Review discovery outputs not for "what did customers say?" but "what did we learn that we didn't know before, and what decision does it change?" Prohibit feature requests from entering the backlog without discovery context.

**[D]** The discovery-vs-conviction tension (CON-0002) is unresolved. Continuous discovery excels at incremental improvement. Breakthrough products often come from strategic conviction that no amount of customer interviewing would validate. The Academy's position: discovery should be the default; conviction-driven bets should be the explicit exception, with clear rationale for why discovery is insufficient.

## 2.9 PRN-0009: Platform Decisions Are the Most Consequential Product Decisions

**The claim:** Decisions about what your product IS a platform FOR constrain every subsequent product decision and have network effects that features alone cannot match.

**[E]** Evidence strength: **Moderate to Strong**
- Supporting: Amazon's API Mandate enabling AWS (SRC-POST-0056), Slack's platform strategy determining ecosystem and moat (SRC-POST-0048), platform economics theory (SRC-BOOK-0025)
- Counter: Google Wave was an ambitious platform that failed because it was a platform before it was a product (SRC-POST-0078)

**[P]** The Platform Decision Framework (PRN-0009 practical tool): (1) What is the platform paradigm? (2) Who are the platform's users? (3) What can they build that we shouldn't? (4) What are the platform constraints? (5) How does the platform create switching costs? (6) What is our investment in developer success?

**[R]** If a product has an API but no platform strategy, decide: invest in the platform or deprecate the API. An API without a strategy creates maintenance burden without ecosystem value. This is the worst state for any product with platform characteristics.

**[I]** The most common platform failure mode is building the platform before the product. Developers (internal or external) won't build on a platform that doesn't have proven users. The platform must be extracted from real use cases, not designed in abstraction.

## 2.10 PRN-0010: Organizational Design Is Product Design

**The claim:** The structure of the product organization directly determines the structure of the product. Product leaders at Director+ spend as much time on organizational design as on product design.

**[E]** Evidence strength: **High**
- Supporting: Amazon's simultaneous architecture and org restructuring (SRC-POST-0056), Microsoft's organizational transformation enabling cloud-first strategy (SRC-POST-0041), Facebook's "mobile first" requiring organizational transformation (SRC-POST-0074)
- Counter: Some companies achieve coherence despite fragmentation through strong platform teams and design systems (SRC-POST-0008) — but this is weak counterevidence as it doesn't challenge Conway's Law, just describes mitigation

**[P]** The Conway's Law Design Canvas (PRN-0010 practical tool): map your product architecture and organizational structure side by side. Identify where team boundaries don't match architecture boundaries. For each mismatch, assess whether it's productive or unproductive. Design coordination mechanisms only where structural change is infeasible.

**[R]** Before any major product strategy change, assess whether the current organizational structure can support it. If not, the organizational change should precede or coincide with the product change. The most common strategy failure is launching a new strategic initiative with an org structure designed for the old strategy.

**[I]** Organizational redesign is not a substitute for product strategy. If the strategy is unclear, no org structure will produce good outcomes. The most common org design failure mode is reorganizing too frequently — teams need stability to develop domain expertise and shipping rhythm. Reorganize no more than once per year without exceptional reason.

## 2.11 PRN-0011: Leading Indicators Beat Lagging Indicators for Product Decisions

**The claim:** Revenue, retention, and market share are lagging indicators that reveal problems too late for corrective action. Product decisions should be guided by leading indicators that predict lagging outcomes.

**[E]** Evidence strength: **Moderate to Strong**
- Supporting: General measurement theory (leading vs lagging distinction), product-specific applications in the lean startup and continuous discovery traditions
- Counter: Leading indicators can be gamed more easily than lagging indicators, and their predictive relationship to lagging outcomes may decay over time

**[P]** The distinction between "vanity metrics" (look good, don't predict outcomes) and "actionable metrics" (change behavior, predict outcomes) is fundamental to product management. Most dashboards are filled with vanity metrics.

**[R]** For each product, identify the 3-5 leading indicators that most reliably predict long-term outcomes. Monitor these weekly. If a leading indicator moves, investigate before the lagging indicator confirms the problem. If a leading indicator consistently fails to predict the lagging outcome, replace it.

**[I]** The most common leading indicator failure is optimizing the indicator instead of the outcome (Goodhart's Law: when a measure becomes a target, it ceases to be a good measure). Any leading indicator that becomes a team's primary KPI will eventually become decoupled from the outcome it was supposed to predict.

## 2.12 PRN-0012: The PM's Job Is to Accelerate the Clock Speed of Learning

**The claim:** The PM's fundamental value is reducing the time between "we have an idea" and "we know whether it works." Every product process — planning, discovery, development, launch, measurement — should be evaluated by whether it accelerates or decelerates the learning cycle.

**[E]** Evidence strength: **Moderate**
- Supporting: Lean Startup methodology (SRC-BOOK-0014), DORA/Accelerate on deployment frequency and lead time (SRC-BOOK-0027), Amazon's speed philosophy (SRC-POST-0010)
- Counter: In domains where learning cycles are inherently long (hardware, healthcare, infrastructure), other PM responsibilities may dominate

**[P]** The learning clock speed framework: for any product process, ask "does this help us learn faster about what to build?" If the answer is no, the process is overhead, not product management.

**[R]** Audit your product processes for clock speed impact. Identify the process that most slows the learning cycle. Redesign or eliminate it. The most common clock speed killers: multi-stage approval processes, requirements documents that take longer to write than the feature takes to build, and "strategy reviews" that delay decisions without improving them.

**[D]** The speed-vs-quality tension (CON-0006) is the direct implication. In low-consequence domains, accelerate clock speed aggressively. In high-consequence domains (safety, finance, healthcare), learning speed must be balanced against assurance requirements.

---

# Part 2B: Principle Application — How the Principles Work Together

**[R]** The Academy's 12 principles are not independent. They interact, reinforce, and sometimes constrain each other. Understanding these interactions is as important as understanding each principle individually.

## The Strategy Triad: PRN-0002, PRN-0009, PRN-0010

**[I]** Three principles form the strategic core of product leadership:

- **PRN-0002 (Strategy Is What You Say No To)** defines WHAT you choose
- **PRN-0009 (Platform Decisions Are Most Consequential)** defines HOW your product enables or constrains future choices
- **PRN-0010 (Organizational Design Is Product Design)** defines WHO makes which choices

These three principles must be consistent. A strategy that says "we're an enterprise company" (PRN-0002 exclusion) but has a platform designed for consumer self-serve (PRN-0009) and an org structure that rewards consumer metrics (PRN-0010) will fail. The product and the organization will pull in directions the strategy explicitly excludes.

**[R]** When a product strategy isn't working, diagnose which of the three is misaligned:
1. Is the strategy clear and exclusionary? (PRN-0002) — If not, no amount of platform design or org restructuring will help.
2. Is the platform enabling the strategy? (PRN-0009) — If the platform makes strategic bets harder rather than easier, the platform is wrong.
3. Is the organization structured to produce the strategy? (PRN-0010) — If the org chart rewards behavior the strategy says not to do, the org chart wins every time.

## The Uncertainty Triad: PRN-0003, PRN-0007, PRN-0011

**[I]** Three principles govern decision-making under uncertainty:

- **PRN-0003 (Cost of Delay Exceeds Cost of Imperfection)** governs decision SPEED
- **PRN-0007 (Reversible by Design)** governs decision SAFETY
- **PRN-0011 (Leading Indicators Beat Lagging Indicators)** governs decision FEEDBACK

These three work together: make decisions fast (PRN-0003), design them to be reversible (PRN-0007), and monitor leading indicators to detect when reversal is needed (PRN-0011).

**[R]** The sequence: (1) Classify the decision as Type 1 or Type 2 (one-way/two-way door). (2) If Type 2, decide fast (PRN-0003). (3) Design reversibility (PRN-0007). (4) Define the leading indicators that will tell you if you were wrong (PRN-0011). (5) Monitor the indicators. (6) Reverse if triggered. This sequence turns decision-making from an anxiety-provoking process into a systematic one.

## The Customer Triad: PRN-0004, PRN-0005, PRN-0008

**[I]** Three principles govern customer understanding:

- **PRN-0004 (PMF Is a Condition)** governs the ONGOING relationship with the market
- **PRN-0005 (PM Owns the Problem)** governs the PM's role in defining what to build
- **PRN-0008 (Customer Discovery Produces Better Decisions)** governs how to learn what customers need

**[R]** These three create a continuous cycle: use discovery (PRN-0008) to define problems (PRN-0005), validate that solutions address real problems, monitor PMF continuously (PRN-0004), and when PMF indicators decline, return to discovery to understand why. The cycle never ends — PMF is a condition, not a milestone.

## The Leverage Triad: PRN-0001, PRN-0006, PRN-0012

**[I]** Three principles govern leverage — getting more output from the same input:

- **PRN-0001 (Empowered Teams)** multiplies organizational output through team autonomy
- **PRN-0006 (Pricing Is the Most Powerful Lever)** multiplies commercial output through value capture
- **PRN-0012 (Accelerate Clock Speed of Learning)** multiplies decision quality through faster feedback

**[R]** When you have limited time and resources, which of these three levers should you pull? (1) If you have a working product and haven't reviewed pricing in 18+ months, pricing is probably your highest-leverage lever (PRN-0006). (2) If your teams are micromanaged and slow, team empowerment is probably the lever (PRN-0001). (3) If you're making decisions slowly and learning even slower, clock speed is the lever (PRN-0012). The right lever depends on your constraint.

## Principle Conflicts: When Principles Disagree

**[I]** The Academy's principles are not always consistent. Some create productive tension:

**PRN-0003 (Speed) vs PRN-0007 (Reversibility Design):** Speed says "decide now." Reversibility says "invest in making it reversible first." Resolution: for Type 2 decisions (reversible by nature), speed dominates — just decide. For Type 1 decisions (inherently irreversible), invest in reversibility design first, then decide.

**PRN-0002 (Strategy Is Exclusion) vs PRN-0012 (Accelerate Learning):** Exclusion says "we're not doing that." Learning says "we don't know enough to exclude it." Resolution: exclusion applies to resource allocation (what we invest in), not to learning (what we explore). You can explore without committing resources. The line between "exploring" and "doing" is where most organizations blur exclusion — they call execution "exploration."

**PRN-0001 (Empowered Teams) vs PRN-0010 (Organizational Design):** Empowerment says "teams decide." Org design says "structure determines outcomes." Resolution: org design sets the boundaries; empowerment governs within them. The org design defines what each team owns; within that ownership, teams are empowered. The tension arises when org boundaries don't match product boundaries — which is why they must be designed together.

**PRN-0005 (PM Owns the Problem) vs PRN-0008 (Customer Discovery):** "Own the problem" suggests the PM defines it. "Customer discovery" suggests customers reveal it. Resolution: customers reveal the PROBLEM SPACE; the PM synthesizes and DEFINES the specific problem to solve. Customers provide raw material; the PM provides judgment about which problem to focus on and how to frame it.

## Principle Application Examples

**[R]** These worked examples show how multiple principles apply to single product decisions:

### Example 1: Deciding to Enter the Enterprise Segment

Your consumer product is successful. The board wants enterprise expansion. Before any analysis, apply **PRN-0002 (Strategy Is Exclusion):** Is enterprise within our strategy or explicitly excluded? If our strategy is "consumer-first," the answer may be no — regardless of board pressure. Apply **PRN-0004 (PMF Is a Condition):** Consumer PMF does not transfer. Run the Sean Ellis test separately for enterprise users. Apply **PRN-0006 (Pricing):** Enterprise pricing requires per-seat licensing, procurement, contracts — a fundamentally different model. Apply **PRN-0009 (Platform Decisions):** Enterprise demands SSO, RBAC, audit logs, SLAs — each constrains the consumer product. Apply **PRN-0010 (Org Design):** Can the consumer org serve enterprise? Likely not — Conway's Law says two teams produce two diverging products. Apply **Decision Framework 1:** Enterprise entry is Type 1 (one-way door). Consider: 6-month enterprise experiment with dedicated team before full commitment.

### Example 2: Responding to a Competitor's AI Feature

Competitor launched AI feature. CEO wants response. Apply **Anti-pattern check (Part 6):** Is this Anti-pattern 6 (AI-for-everything)? Apply **PVS Assessment:** What is the real user problem? If PVS < 3.0, the competitor will fail — don't follow. Apply **PRN-0003 (Cost of Delay):** Is there a genuine market window closing, or just press attention? Apply **PRN-0005 (PM Owns the Problem):** Don't define the problem as "match competitor." Define it from customer perspective. The competitor's AI approach may be wrong even if the need is real. Apply **PRN-0009 (Platform Decisions):** Does this AI feature require platform investments that serve multiple use cases, or is it a one-off? One-off AI is expensive. One-off reactive AI is indefensible. Apply **Decision Framework 8 (FMEA):** Pre-mortem — "We built it and it failed. Why?" Most likely: unreliable output, no workflow fit, uneconomical inference costs, or problem not worth solving.

### Example 3: Deciding Whether to Kill a Failing Initiative

Initiative is 12 months in, behind schedule, over budget, weak signals. Apply **PRN-0004 (PMF):** Leading indicators show no PMF emerging. Apply **PRN-0003 (Cost of Delay):** The opportunity cost of continuing exceeds the value of potential future success. Apply **PRN-0011 (Leading Indicators):** They're flat. Don't wait for lagging indicators to confirm failure. Apply **PRN-0007 (Reversibility):** Pause, don't kill. Maintenance mode. Monitor. If no change in 6 months, formal sunset. Apply **Decision Framework 3 (Sunset):** Run the four gates. The blocker is usually Gate 2 (User Impact) — but maintenance mode serves users worse than clean sunset with migration. Apply **Decision Framework 2 (RICE-LM):** Low Strategic Coherence multiplier even if RICE is decent. Apply **CASE-0003 (Google Reader):** Graceful sunset — data export, transition period, honest communication — costs more but preserves trust.

## 3.1 The Nature of Product Uncertainty

**[I]** Product decisions operate under three types of uncertainty:

1. **Market uncertainty:** Will customers want this? Will they pay? How large is the market?
2. **Technical uncertainty:** Can we build this? Will it work at scale? What are the failure modes?
3. **Organizational uncertainty:** Can our organization execute this? Do we have the right people, processes, and culture?

**[E]** The Startup Genome Project and subsequent research found that premature scaling (investing in growth before resolving core uncertainties) is the most common cause of startup failure. This applies to product initiatives within larger organizations as well.

**[P]** The Academy's decision frameworks (`01_core_doctrine/DECISION_FRAMEWORKS.md`) provide eight structured approaches to these uncertainties. The most important for daily use:

### Framework 1: One-Way vs Two-Way Door Classification

**[E]** From Amazon's internal decision framework (SRC-POST-0013).

**Type 1 (One-Way Door):** Irreversible or extremely expensive to reverse.
- Requires broader input, proportional analysis, explicit reversibility design
- Escalate to appropriate level

**Type 2 (Two-Way Door):** Reversible at acceptable cost.
- Make as close to the information as possible
- Spend ≤10% of implementation cost on analysis
- Require reversal plan, not permission

**[R]** The most common organizational failure is treating Type 2 decisions as Type 1 — applying heavy process to reversible decisions. Audit your organization's decision processes. For each process, classify the decisions it governs. If it governs primarily Type 2 decisions, the process is overhead.

### Framework 2: RICE-LM Prioritization

**[P]** Extended from the standard RICE framework (Reach × Impact × Confidence / Effort) with three Principal+ multipliers:

- **Leverage (L):** Does this create capability for future initiatives? (0.5x–2.0x)
- **Market timing (M):** Is there a window driving urgency? (0.5x–2.0x)
- **Strategic coherence (S):** Does this advance the core strategy? (0.5x–2.0x)

**[R]** Final score = Base RICE × L × M × S. The multipliers should be debated, not calculated. Their purpose is to surface strategic considerations that pure RICE misses. A high RICE initiative with 0.5x Strategic Coherence is a trap.

### Framework 8: FMEA for Product Decisions

**[E]** Adapted from engineering Failure Mode and Effects Analysis.

For high-stakes decisions, evaluate: Probability × Severity × Detectability = Risk Priority Number (RPN). Focus mitigation on high-RPN failure modes. Any failure mode with severity 8+ requires mitigation regardless of probability.

**[R]** Before any major product decision, complete a pre-mortem: assume the decision was wrong. What caused the failure? What signals were available? What would you do differently? This exercise surfaces risks that optimistic planning misses.

## 3.2 Pre-Mortems: The Most Cost-Effective Risk Management Tool

**[P]** The pre-mortem (popularized by Gary Klein, adopted by Amazon and many product organizations) is the practice of imagining a future where a decision has failed and working backward to identify causes.

**[R]** For any decision with significant resource commitment or irreversibility:
1. Gather the decision stakeholders
2. Announce: "Assume we are 12 months in the future and this decision was a complete failure. The product failed. The initiative was killed. Write down the reasons why."
3. Collect and discuss: What patterns emerge? What risks were being ignored?
4. For the top 3-5 failure causes, design mitigation or monitoring
5. Document the pre-mortem output alongside the decision

**[I]** Pre-mortems work because they counteract optimism bias (the tendency to underestimate risks in plans we've invested in creating) and groupthink (the tendency for groups to converge on optimistic assessments). They create psychological safety for identifying problems by making the exercise hypothetical.

## 3.3 Reversibility Design and Option Value

**[E]** The concept of option value — the value of keeping future choices open — applies directly to product decisions. Investing in reversibility is essentially purchasing an option to change your mind, and this option has calculable value.

**[P]** For any decision, ask not just "what is the right choice?" but "how do we make this decision easy to reverse?" Techniques include:
- Feature flags (software features can be turned off)
- API versioning (old APIs remain available during migration)
- Phased rollouts (blast radius is limited)
- Data export (users can leave — paradoxically, this increases trust and reduces churn)
- Architecture that supports rollback (tested, not theoretical)

**[R]** The most important question for any high-uncertainty decision is not "are we right?" but "what would we need to see to reverse this decision?" Define the reversal trigger in advance. During a failure is the wrong time to decide who decides to reverse.

## 3.4 When to Escalate vs When to Own

**[P]** The escalation decision is one of the most frequent and least taught product leadership skills. The framework:

**Escalate when:**
- The decision exceeds your decision rights (financial, strategic, or organizational)
- The decision has implications beyond your domain that you cannot fully assess
- You have done the analysis and the recommendation is clear, but you lack the authority to implement it
- The decision involves a risk you are not authorized to accept

**Own when:**
- The decision is within your domain and you have the information to make it
- Escalating would add latency without improving decision quality
- You are the person closest to the relevant information
- The decision is Type 2 (reversible) and you have the reversal plan

**Escalate badly (the most common failure mode):**
- Escalating without a recommendation ("what should we do?")
- Escalating without analysis ("we need a decision on X" without providing the context, alternatives, and trade-offs)
- Escalating to avoid accountability ("I don't want to be responsible if this is wrong")

**[R]** When escalating, always provide: (1) A one-sentence decision statement, (2) The alternatives considered and why some were rejected, (3) Your recommendation, (4) The risks and how they'll be mitigated, (5) What happens if the decision is delayed.

---

# Part 3B: Decision Framework Walkthroughs

*This section provides detailed walkthroughs of the Academy's eight decision frameworks applied to realistic product leadership scenarios. For the framework definitions, see `01_core_doctrine/DECISION_FRAMEWORKS.md`.*

## Framework 1 Walkthrough: One-Way vs Two-Way Door for a Pricing Change

**Decision:** Change pricing from per-seat to usage-based for an enterprise SaaS product.

**Step 1: Classify the decision.** This is Type 1 (one-way door). Existing customers are on per-seat contracts. New customers would sign under usage-based. Reverting would create confusion, trust erosion, and dual pricing models that are expensive to maintain. The reversal cost is high.

**Step 2: Determine the decision process.** Type 1 decisions require broader input, proportional analysis, explicit reversibility design, and escalation to appropriate level. This pricing change should involve finance (revenue modeling), sales (customer impact), engineering (billing system changes), and executive leadership (strategic approval).

**Step 3: Design reversibility.** Can this be more reversible? Phased rollout: start with new customers only. Existing customers grandfathered for 12 months. If usage-based pricing performs worse than per-seat on new customers, revert for new customers with minimal impact. This doesn't make the decision Type 2, but it reduces the blast radius.

**Step 4: Pre-mortem.** "Assume we changed to usage-based pricing and it failed. Why?" Possible causes: customers hated the unpredictability, sales team couldn't explain the model, largest customers saw their bills increase, usage-based pricing encouraged low-usage behavior that reduced product stickiness, billing system couldn't handle the complexity.

**Step 5: Decision.** Decide whether to proceed, with the phased rollout and pre-mortem mitigations.

**Common misclassification:** A team might classify this as Type 2 ("we can always change it back") because the engineering change is reversible. But the customer relationship and trust implications make it Type 1. The reversibility analysis must include customer impact, not just technical reversibility.

## Framework 2 Walkthrough: RICE-LM for an Initiative Portfolio

**Decision:** Prioritize among five proposed initiatives for next quarter's resource allocation.

**Initiatives:**
- A: Build SSO integration (enterprise prospects requesting it)
- B: Improve onboarding completion rate (currently 34% drop-off)
- C: Build public API (platform strategy bet)
- D: Performance optimization (P95 latency from 8s to 2s)
- E: New reporting dashboard (top 3 customers requesting)

**Base RICE scores:**
- A: Reach=5 (enterprise prospects only), Impact=8 (blocking deals), Confidence=90%, Effort=4 person-months → RICE = (5×8×0.9)/4 = 9.0
- B: Reach=8 (all new users), Impact=7 (churn reduction), Confidence=70%, Effort=3 → RICE = (8×7×0.7)/3 = 13.1
- C: Reach=6 (developers), Impact=7 (platform moat), Confidence=50%, Effort=8 → RICE = (6×7×0.5)/8 = 2.6
- D: Reach=10 (all users), Impact=5 (latency improvement), Confidence=95%, Effort=6 → RICE = (10×5×0.95)/6 = 7.9
- E: Reach=3 (power users), Impact=6, Confidence=80%, Effort=4 → RICE = (3×6×0.8)/4 = 3.6

**Apply LM multipliers:**
- A: Leverage=1.0 (point solution), Market Timing=1.5 (blocking enterprise deals now), Strategic Coherence=1.0 → RICE-LM = 9.0 × 1.0 × 1.5 × 1.0 = 13.5
- B: Leverage=1.0, Market Timing=1.0, Strategic Coherence=1.5 (growth strategy) → RICE-LM = 13.1 × 1.0 × 1.0 × 1.5 = 19.7
- C: Leverage=2.0 (platform capability), Market Timing=1.5 (competitor launched API), Strategic Coherence=2.0 (platform strategy) → RICE-LM = 2.6 × 2.0 × 1.5 × 2.0 = 15.6
- D: Leverage=1.0, Market Timing=1.0, Strategic Coherence=1.0 → RICE-LM = 7.9
- E: Leverage=0.5 (one-off), Market Timing=0.5 (not urgent), Strategic Coherence=0.5 (pulls away from platform strategy) → RICE-LM = 3.6 × 0.5 × 0.5 × 0.5 = 0.45

**Result:** B (Onboarding, 19.7) > C (API, 15.6) > A (SSO, 13.5) > D (Performance, 7.9) > E (Dashboard, 0.45)

**Key insight:** Initiative C had the lowest base RICE (2.6) but the highest RICE-LM (15.6) because of leverage, timing, and strategic coherence. Initiative E went from moderate RICE (3.6) to negligible RICE-LM (0.45) because the strategic multipliers revealed it as a distraction. This is why Principal+ PMs use RICE-LM — the multipliers surface strategic considerations that pure RICE misses.

## Framework 3 Walkthrough: Sunset Decision for a Legacy Feature

**Decision:** Whether to sunset an internal analytics dashboard used by 40 people across 3 teams.

**Gate 1: Strategic Fit.** The company is rolling out a new company-wide analytics platform. This dashboard is redundant. Fail Gate 1 — proceed.

**Gate 2: User Impact.** 40 internal users across 3 teams. Usage: 15 daily active, 15 weekly, 10 rarely. Emotional attachment: low — it's a utilitarian tool, not a beloved product. Data export: dashboard supports CSV export, which is sufficient for migration. The new platform covers all use cases. Low impact — proceed.

**Gate 3: Trust Cost.** Internal users — trust cost is low. If the migration path is clearly communicated and the new platform provides equivalent or better functionality, users will adapt. One team lead has expressed concern about "losing historical data" — address with data export tool. Acceptable trust cost — proceed.

**Gate 4: Reversibility.** Code exists but would not be revived if sunset. Migration to new platform is the transition. Recommend: sunset with 60-day notice, data export tool, and migration support for the 3 teams.

**Recommendation:** Sunset. Not maintenance mode — that's the worst outcome (product degrades, resources consumed, no decision made).

## Framework 4 Walkthrough: Build-Buy-Partner for Authentication

**Decision:** Build, buy, or partner for authentication (SSO, MFA, user management) for a growing SaaS product.

**Dimension 1: Strategic Differentiation.** Authentication is NOT differentiating for most SaaS products. Users expect it to work; they don't choose products based on it. Score: Buy.

**Dimension 2: Time-to-Capability.** Enterprise prospects are demanding SSO now. Building would take 3-4 months vs 2-4 weeks to integrate an auth provider. Score: Buy.

**Dimension 3: Build Competence.** The team has no auth/security specialists. Building auth would be a distraction and potentially create security vulnerabilities. Score: Buy.

**Dimension 4: Vendor Risk.** Multiple competitive auth providers (Auth0, Okta, Firebase Auth, Clerk). Switching costs are moderate (user migration) but manageable. Score: Buy.

**Dimension 5: Long-Term Optionality.** Auth is unlikely to become differentiating. If it does, switch later. Score: Buy.

**Recommendation:** Buy. All five dimensions favor buying. Select a provider based on enterprise feature support, pricing model, and integration complexity. Review annually — if the auth provider is acquired or changes pricing dramatically, revisit.

## Framework 5 Walkthrough: Strategy Cascade for a New Initiative

**Situation:** A company providing workflow automation wants to enter the HR workflow space.

**Level 1 — Company Strategy:** "Become the leading workflow automation platform for mid-market enterprises (500-5000 employees). Differentiate on no-code workflow builder. Explicitly not serving: custom enterprise under 500 employees, CRM workflows, consumer automation."

**Level 2 — Product Strategy:** "For HR workflows, focus on onboarding and employee self-service. These are the highest-frequency, highest-pain workflows in mid-market HR. Differentiate on HRIS integration depth (vs competitors' shallow integrations). Explicitly not serving: payroll processing, benefits administration, compliance reporting."

**Level 3 — Product Area Strategy (HR Workflows Area):** "Build the HR workflow engine that integrates deeply with top 3 mid-market HRIS platforms. Outcomes: (a) HR workflows can be built in <1 day by HR managers (no IT involvement), (b) HRIS data sync is real-time with <0.1% error rate, (c) 3 reference workflows available out-of-box (onboarding, PTO, employee data changes)."

**Level 4 — Team Objectives:** "Objective 1: Build HRIS integration framework supporting BambooHR, Gusto, and Namely. Objective 2: Ship onboarding workflow template that 80% of trial users complete setup within 1 hour. Objective 3: Achieve <5% data sync error rate on employee record updates."

**Level 5 — Team Backlog:** Initiative items that trace to objectives. If a backlog item can't trace to an objective, it shouldn't be in the backlog.

**Cascade Test:** At each level, can a reasonable person at the level below make different decisions with this guidance than without it? If Level 3 adds no specificity beyond Level 2, it's not doing its job. The HR Workflows Area strategy adds: which workflows, which HRIS platforms, which outcomes.

## Framework 6 Walkthrough: Product-Organization Co-Design

**Situation:** A product with web app, mobile app, and API — each with duplicated backend logic.

**Step 1 — Desired Architecture:** Shared backend services with three thin presentation layers that call the same services. Core business logic in shared services; web, mobile, and API are presentation-only.

**Step 2 — Organizational Structure:** Move from surface-based teams (Web Team, Mobile Team, API Team) to capability-based teams: Core Services Team (owns backend), Web Experience Team, Mobile Experience Team, API Experience Team.

**Step 3 — Coordination Mechanisms:** Core Services provides APIs with SLAs. Experience teams consume APIs. Coordination through API contracts, not meetings. Weekly architecture sync for API changes.

**Step 4 — Transition Plan:** 3-month transition. Month 1: Core Services formed, extracts shared logic. Month 2: Experience teams formed, migrate to Core Services APIs. Month 3: Old surface teams dissolved. Expect 30% velocity reduction during transition.

**Key decision:** This restructuring is painful but necessary. The alternative — maintaining surface-based teams — means every new feature requires coordination across 3 teams and is built 3 times. The transition cost is high but the status quo cost is higher.

## Framework 7 Walkthrough: Stakeholder Alignment for a Build-vs-Buy Decision

**Decision:** Whether to build an internal experimentation platform or buy an existing solution.

**Step 1 — Stakeholder Map:**
- VP Data Science: Cares about experimentation velocity. Fears: buying locks them into a platform that doesn't support their methods. Influencer on CEO.
- VP Engineering: Cares about team focus. Fears: building takes 2+ quarters of engineering time. Blocker — controls engineering resources.
- CFO: Cares about cost. Fears: buying is expensive ($200K+/year). Blocker — controls budget.
- Head of Product (you): Recommending buy with a 1-year contract. Influencer on all stakeholders.
- CEO: Will make final decision based on VP alignment. Decision-maker.

**Step 2 — Pre-Alignment:**
- Meet VP Data Science: Address their concern about platform lock-in with a 1-year contract (easy to switch). Show that the platform supports their statistical methods.
- Meet VP Engineering: Address their concern about engineering time. "If we buy, your team saves 2 quarters. If we build, we need 2 senior engineers for 2 quarters — and then maintenance forever."
- Meet CFO: Present TCO comparison. Buy: $200K year 1, $220K year 2. Build: $400K+ year 1 (engineering), $100K+ annual maintenance. Break-even at year 3+.

**Step 3 — Decision Memo:** Circulate 48 hours before meeting. Include all stakeholder concerns and how addressed.

**Step 4 — Decision Meeting:** 35 minutes. Decision: Buy with 1-year contract, re-evaluate at month 9.

## Framework 8 Walkthrough: FMEA for a Data Migration Decision

**Decision:** Migrate from PostgreSQL to a time-series database for analytics data.

**Failure Mode 1: Data corruption or loss during migration.** Probability: 3 (complex but tested). Severity: 10 (data loss catastrophic). Detectability: 5 (corruption not immediately visible). RPN: 150. Mitigation: Run databases in parallel for 30 days with automated validation. Reversal trigger: divergence >0.01% and cannot resolve within 4 hours.

**Failure Mode 2: Query performance degrades for complex analytics.** Probability: 6 (time-series DBs not optimized for complex joins). Severity: 5 (slower but not broken). Detectability: 3 (gradual, users may not report). RPN: 90. Mitigation: Performance benchmarks for top 20 query patterns, monitored continuously. Rollback: keep PostgreSQL as analytics replica for 6 months.

**Failure Mode 3: Team lacks time-series DB expertise.** Probability: 7 (new technology). Severity: 4 (can hire or train). Detectability: 2 (skill gaps emerge slowly). RPN: 56. Mitigation: Hire or contract time-series DB specialist before migration begins. Training for existing team.

**Decision:** Proceed with migration, with all mitigations in place. RPNs are moderate and mitigations reduce residual risk to acceptable levels.

## 4.1 The Resource Allocation Problem

**[E]** Resource allocation — deciding where to deploy capital, headcount, and attention — is the highest-leverage activity for product leaders at Director level and above. The quality of allocation decisions determines portfolio outcomes more than the quality of execution within any individual initiative.

**[P]** The Academy's resource allocation framework (Capability 1.9 in `00_orientation/CAPABILITY_MODEL.md`):

**Senior PM:** Allocates own time across competing demands. Makes roadmap tradeoffs within a bounded context.

**Principal PM:** Allocates resources across multiple initiatives. Identifies when emerging evidence calls for reallocation. Optimizes at the portfolio level, not locally.

**Director:** Owns headcount, budget, and attention allocation across a product area. Makes explicit investment theses. Reallocates as evidence accumulates — not just during annual planning.

**VP/CPO:** Allocates total product investment across the company. Balances core, adjacent, and transformational bets. Manages the exploration-exploitation tradeoff.

**[I]** The most common resource allocation failure is not wrong allocation — it's NO allocation. Resources are distributed by organizational momentum ("this is what we've always funded"), by political power ("this is what the most powerful executive wants"), or by false fairness (equal allocation across initiatives). Explicit allocation — where every funded initiative has an investment thesis and every unfunded initiative has an explicit rejection — is rare.

## 4.2 Capital Allocation: The Exploration-Exploitation Balance

**[E]** From organizational learning theory (March, 1991) and its application to product management: organizations must balance exploration (searching for new opportunities) and exploitation (optimizing existing ones). The optimal balance depends on market dynamics, organizational stage, and competitive position.

**[P]** A useful heuristic for product portfolio allocation:

| Horizon | Allocation | Focus | Decision Cycle |
|---------|------------|-------|----------------|
| **H1: Core** | 60-70% | Optimize and scale existing products | Quarterly |
| **H2: Adjacent** | 20-30% | Extend into new segments, features, or markets | Semi-annual |
| **H3: Transformational** | 5-10% | Explore fundamentally new product directions | Annual |

**[R]** This allocation is a starting point, not a rule. Early-stage companies should tilt toward H2/H3. Mature companies in stable markets should tilt toward H1. Companies facing disruption should dramatically increase H3.

**[I]** The allocation should shift over time based on evidence, not calendar. The most common failure mode is H1 consuming H2 and H3 resources ("the core business needs us right now" — it always will). Protect H3 allocation explicitly; it will always lose to H1 in a fair fight.

## 4.3 Headcount Allocation: The Neglected Lever

**[P]** Headcount allocation — who works on what — is more consequential than budget allocation for most product organizations. The quality of the team determines outcomes more than the quantity of funding.

**[R]** Principles for headcount allocation:
1. **Concentrate, don't spread.** A team of 5 on one initiative beats 5 teams of 1 on five initiatives.
2. **Allocate teams, not individuals.** Cross-functional teams (PM + Engineering + Design) should move together. Splitting a team across multiple initiatives produces half-hearted work on all.
3. **Reallocate based on evidence, not calendar.** If an initiative is showing strong signals, increase headcount immediately — don't wait for the next planning cycle.
4. **Kill to reallocate.** The only way to fund new initiatives is to stop funding existing ones. If you can't kill anything, you can't start anything.
5. **Allocate for learning, not just delivery.** Teams that are learning faster should get more resources, even if their current output is lower.

## 4.4 Attention Allocation: The Ultimate Scarce Resource

**[P]** Leadership attention is the scarcest resource in any product organization. Where the leader spends attention determines what the organization values, regardless of what the strategy document says.

**[R]** Audit your attention allocation: for two weeks, track where you spend your time. Categorize by initiative. Compare to your stated strategic priorities. The gap between stated priorities and attention allocation is the true strategy.

**[I]** The most common attention allocation failure: spending time on the most urgent (not most important) initiative. Urgent problems demand attention; important opportunities must be given attention deliberately. The discipline of protecting time for important, non-urgent work is a Principal+ capability.

---

# Part 5: Product Archetypes

*The Academy's archetype catalog (`04_product_archetypes/archetype_catalog.md`) describes 13 archetypes with distinctive characteristics, leadership demands, and failure modes. This section provides the key distinctions and implications for each. For full detail, see the catalog.*

## 5.1 The Archetype Framework

**[P]** Product archetypes are patterns of product characteristics that shape what product leadership means in practice. The same PM skills apply differently across archetypes. A great consumer PM may fail in enterprise; a great platform PM may fail in marketplace. Recognizing which archetype you're operating in — and which mental model you're applying — is a Principal+ capability.

**[R]** For any product decision, first identify: (1) Which archetype am I operating in? (2) Which mental model am I applying? (3) Is the mental model appropriate for this archetype? The most common archetype failure is applying the wrong mental model — consumer thinking to enterprise, platform thinking to consumer, AI thinking to hardware.

### Archetype Summary Table

| # | Archetype | Key Distinction | PM's Hardest Skill | Commonest Failure Mode |
|---|-----------|-----------------|-------------------|----------------------|
| 1 | Consumer/Social | User = customer | Product judgment and taste | Optimizing engagement at expense of well-being |
| 2 | Enterprise B2B SaaS | Buyer/user split | Cross-functional influence (esp. sales) | Building for buyer, ignoring user |
| 3 | Platform/Infrastructure | Value is indirect | Technical fluency | Building platform before use case |
| 4 | Marketplace/Network | Two-sided dynamics | Business economics (marketplace) | Chicken-and-egg paralysis |
| 5 | AI/ML Products | Probabilistic behavior | Evaluation design | Shipping a model, not a product |
| 6 | Developer Tools | Users are developers | Technical fluency + DX judgment | Bad documentation |
| 7 | Hardware/Physical | Irreversible decisions | Strategic sequencing | Software PMs applying software logic to hardware |
| 8 | Fintech/Financial | Trust is foundation | Risk judgment | "Move fast and break things" in finance |
| 9 | Healthcare/Healthtech | Patient safety ultimate constraint | Domain expertise | Consumer PMs applying consumer logic to healthcare |
| 10 | Edtech/Education | Learning outcomes hardest to measure | Evaluation fluency | Optimizing for engagement over learning |
| 11 | Gaming/Entertainment | Product is experience, not tool | Product judgment and taste | Data-driven design destroying creative quality |
| 12 | Market Data/Analytics | Insight delivery | Data and evaluation fluency | Confusing data volume with insight quality |
| 13 | Internal Tools/Ops | Internal customers | Organizational influence | Building what stakeholders ask for, not what they need |

## 5.2 Archetype Transitions

**[P]** Moving between archetypes is one of the hardest product leadership challenges. PMs who excel in one archetype often fail in another because they apply the wrong mental model. The catalog describes archetype transition failure modes (Case 07.7 in `07_cases/case_catalog.md`).

**[R]** When transitioning between archetypes:
1. **Acknowledge the difference.** Don't assume "product management is product management." It's not.
2. **Identify the new archetype's hardest skill.** If you're weak in it, develop it explicitly or ensure someone on the team is strong in it.
3. **Watch for the old archetype's mental model.** Consumer PMs in enterprise will underinvest in sales partnership. Enterprise PMs in consumer will overinvest in feature breadth.
4. **Learn from the failure modes.** The archetype catalog's failure modes are a checklist: "Am I doing any of these?"

## 5.3 Detailed Archetype Analysis

### Archetype 1: Consumer / Social

**[P]** Consumer products succeed or fail on the quality of micro-decisions about interaction design, visual polish, and experience coherence. The user IS the customer — no buyer/user split. Engagement depth matters more than feature breadth. Distribution is a product problem: growth mechanics (viral loops, network invites, content-driven acquisition) are product features, not marketing activities.

**[E]** Key failure modes with case evidence:
- **Optimizing engagement at expense of well-being** — What drives metrics may harm users. Eventually users or regulators notice (CASE-0003 Google Reader: usage decline masked an influential user base Google underestimated).
- **Feature creep destroying simplicity** — Each feature adds cognitive load. Accumulated complexity kills the experience.
- **Growth hacking without product value** — Users arrive and leave. Growth numbers look good for a quarter, then collapse.
- **Confusing A/B test wins with product improvement** — Optimizing a local metric while degrading holistic experience.

**[R]** The PM's hardest skill is product judgment and taste. Must make decisions about interaction design, visual polish, and experience coherence that cannot be A/B tested. The PM who optimizes for metrics at the expense of quality produces a product that is locally optimized and globally mediocre.

### Archetype 2: Enterprise / B2B SaaS

**[P]** Enterprise products face a fundamental structure that consumer products don't: the buyer is not the user. The person who signs the contract (economic buyer, procurement, IT) is different from the person who uses the product daily. Both must be served, and their needs frequently conflict. Additional complexity: administrators, IT/security teams, and executives each have distinct evaluation criteria.

**[E]** Key failure modes with case evidence:
- **Building for buyer, ignoring user** — Products that win RFPs but fail in daily use. The procurement checklist is satisfied; the user experience is miserable.
- **Building for user, ignoring buyer** — Products users love but can't pass security review or procurement (CASE-0006 Slack: balanced bot-first developer adoption with enterprise buyer needs).
- **Sales-driven roadmap** — Building whatever the largest customer demands. Product becomes a collection of custom features with no coherent strategy.
- **Customization death spiral** — Building custom features for individual customers until the product is unmaintainable and engineering is burned out.
- **Pricing that kills adoption or leaves money on the table** — The right price captures value without preventing growth. Fee compression in financial services (see TIAA application) is a case study.

**[R]** The PM's hardest skill is cross-functional influence — particularly with sales. The PM who can't partner with sales will be bypassed. The PM captured by sales will build a feature factory. The right balance: sales informs but doesn't dictate the roadmap. Design the product for adoptability (training, migration tools, administrator experience are product features). Treat pricing and packaging as product decisions, not sales enablement.

### Archetype 3: Platform / Infrastructure

**[P]** Platform value is indirect — it enables other products. Measuring platform value requires understanding the products built on top. Adoption has long time constants; the investment profile differs fundamentally from consumer or enterprise products. Breaking changes are extremely expensive — once adopted, platform APIs become contracts.

**[E]** Key failure modes with case evidence:
- **Building platform before the use case** — "If we build it, they will come." They won't (CASE-0006 Slack: built platform capabilities only after the product had proven demand. CASE-0004 Microsoft: Azure grew from proven infrastructure needs, not speculative platform design).
- **Over-generalizing too early** — Building for hypothetical future use cases instead of concrete current ones.
- **Ignoring the adoption experience** — Building powerful capabilities with unusable interfaces, incomplete documentation, painful migration paths. Technical excellence doesn't matter if no one can use it.
- **The platform team as bottleneck** — Every team must go through platform team for everything. The platform that should accelerate slows down.

**[R]** The PM's hardest skill is technical fluency — the highest requirement of any archetype. Must understand distributed systems, API design, scalability, reliability engineering. The platform PM who can't earn engineering respect will be irrelevant. Strategic sequencing is critical: building platform capabilities before teams are ready is wasted investment. The platform must be extracted from real, proven use cases.

### Archetype 4: Marketplace / Network

**[P]** Marketplace products balance two-sided (or multi-sided) dynamics. Changes that benefit one side often harm the other. Liquidity is the fundamental metric — without sufficient supply there's no demand; without demand, supply leaves. Network effects create winner-take-most dynamics. Trust and safety are existential — marketplaces intermediate between strangers.

**[E]** Key failure modes:
- **Chicken-and-egg paralysis** — Waiting for supply before attracting demand, and demand before supply. Marketplaces must be hacked into existence through deliberate subsidy, single-player mode, or piggybacking on existing networks.
- **Premature scaling** — Expanding to new geographies or categories before achieving liquidity in the core. The marketplace collapses everywhere.
- **Over-optimizing one side** — Making supply so happy demand suffers (or vice versa). The optimal marketplace is slightly uncomfortable for both sides.
- **Losing trust** — Safety incidents, fraud, quality problems. Once lost, marketplace trust is extraordinarily hard to regain.

**[R]** The PM's hardest skill is business economics — marketplace economics are complex. Cross-side effects, liquidity thresholds, take rate optimization, subsidy strategy require economic thinking, not just product thinking. Must balance supply-side and demand-side investments dynamically as the marketplace matures.

### Archetype 5: AI/ML Products

**[P]** See Part 6 (AI Product Leadership) for comprehensive treatment. Key characteristics: model capability uncertainty, probabilistic behavior with unpredictable failure modes, data flywheels as durable moats, evaluation as a first-class product problem, safety as product requirement, and cost structure fundamentally different from traditional software.

**[R]** The PM's hardest skill is evaluation design — how to know if the model is good enough for the product. The PM who can't design evaluation frameworks can't ship AI products safely.

### Archetype 6: Developer Tools

**[P]** Users are developers — technically sophisticated, opinionated, skeptical. They evaluate products on technical merit, not marketing. Documentation quality IS feature quality. Developer experience (DX) is the UX: API design, SDK ergonomics, CLI usability, error message quality, getting-started time.

**[E]** Key failure modes:
- **Bad documentation** — The most common and most fatal developer tool failure. The product is powerful but unusable.
- **API inconsistency** — Different patterns, naming conventions, behaviors across endpoints. Developers must learn each individually rather than applying a consistent mental model.
- **Ignoring the getting-started experience** — Time from "I want to try this" to "I've done something useful" is the most important metric.
- **Enterprise sales motion applied to developer adoption** — Top-down sales doesn't work for developer tools. Developers must want to use the product first.

**[R]** The PM must use the product as a developer would. Dogfooding is not optional. Must understand API design tradeoffs and earn credibility with a highly technical user base.

### Archetype 7: Hardware / Physical Products

**[P]** Hardware's defining characteristic: decisions are irreversible. Component choices and manufacturing decisions made today will be in customers' hands for years. Development cycles are orders of magnitude slower than software. Manufacturing, supply chain, and regulatory constraints are product constraints.

**[E]** Key failure modes:
- **Software PMs applying software logic to hardware** — Optimizing for iteration speed in a domain where iteration is slow and expensive.
- **Feature creep during development** — Adding features after tooling has begun. Each addition costs months and millions.
- **Supply chain optimism** — Assuming components will be available, yields will be high, and manufacturing will go smoothly.

**[R]** The PM's hardest skill is strategic sequencing — decisions made early constrain options later. The cost of a sequencing error is measured in years and millions.

### Archetype 8: Fintech / Financial Services

**[P]** Trust is the foundation — financial products handle people's money. Trust is earned slowly, lost instantly. Regulatory constraints are pervasive; compliance is a product requirement, not a separate function. Transaction integrity is non-negotiable; "eventually consistent" is not acceptable. Fraud and security are existential threats from day one.

**[E]** Key failure modes with case evidence:
- **"Move fast and break things" in finance** — Breaking things means losing money, violating regulations, enabling fraud (CASE-0005: Knight Capital lost $440M in 45 minutes — the canonical example).
- **Compliance as afterthought** — Building first, asking compliance to approve later. They won't. The product must be redesigned.
- **Underestimating fraud** — Every financial product that gains traction will be targeted.
- **Opaque pricing** — Hidden fees destroy trust. Transparency is a competitive advantage, not a compliance obligation.

**[R]** The PM's hardest skill is risk judgment — financial risk, fraud risk, regulatory risk, reputational risk at sophistication beyond other archetypes. Must partner with compliance as a design partner, not a reviewer. See `12_personal_lab/TIAA_APPLICATION.md` for a worked example.

### Archetype 9: Healthcare / Healthtech

**[P]** Patient safety is the ultimate constraint — products can harm or kill people. Multi-stakeholder complexity involves patients, providers, payers, regulators, and pharmaceutical companies with conflicting incentives. Regulatory pathways (FDA, HIPAA) are long and expensive. Clinical evidence requirements mean RCTs and real-world evidence are part of product development.

**[E]** Key failure modes:
- **Consumer PMs applying consumer logic to healthcare** — "Move fast, validate with A/B tests." Some things can't be A/B tested because downside risk is patient harm.
- **Ignoring clinical workflow** — Products that are medically sound but don't fit how clinicians work. Clinicians won't use products that slow them down.
- **Building for the wrong stakeholder** — Optimizing for patients when payers decide; optimizing for providers when patients choose.
- **AI-specific** — Clinical AI without rigorous validation. Algorithmic bias in healthcare AI has life-or-death consequences.

**[R]** Healthcare domain expertise is not optional. Generalist PMs without healthcare experience will make dangerous mistakes.

### Archetype 10: Edtech / Education

**[P]** Learning outcomes are the ultimate metric and the hardest to measure. Engagement is easy; learning is hard. Products that optimize for engagement may not produce learning. Pedagogy matters — educational products must be built on sound learning science. Institutional adoption involves long procurement cycles (12-24 months for schools/universities).

**[E]** Key failure modes:
- **Optimizing for engagement at expense of learning** — The Edtech unicorn graveyard is full of engaging products with zero learning efficacy.
- **Building for students, ignoring teachers** — Teachers are gatekeepers; alienating them guarantees failure.
- **Content as an afterthought** — Content quality determines educational effectiveness.

**[R]** The PM must balance engagement and learning outcomes. Gamification without pedagogy is entertainment, not education. Desirable difficulty is a product design principle.

### Archetype 11: Gaming / Entertainment

**[P]** The product is an experience, not a tool. Creative production (writers, designers, artists, composers) is part of product development. Communities are part of the product — they must be nurtured, and they can turn toxic. Monetization has ethical dimensions: loot boxes, battle passes, microtransactions raise questions about addiction and exploitation.

**[E]** Key failure modes:
- **Data-driven design destroying creative quality** — Optimizing by A/B testing every element. Produces a local maximum that's globally mediocre.
- **Monetization that feels exploitative** — Pay-to-win, predatory loot boxes, aggressive advertising.
- **Live service burnout** — Games-as-a-service that demand constant engagement. Players burn out from the product designed for retention.

**[R]** Data informs creative decisions; it doesn't make them. Product judgment and taste are paramount. The PM must bridge creative and technical functions with different cultures, values, and success metrics.

### Archetype 12: Market Data / Analytics

**[P]** Data products deliver insight, not just data. Key characteristics: data quality and freshness as product requirements, the market for "data products" spans from raw APIs to packaged insights, and the value proposition is "better decisions through better information."

**[E]** Key failure mode: confusing data volume with insight quality. Providing more data without helping users extract meaning. The product that shows everything shows nothing.

**[R]** The PM must understand both the data (sources, quality, freshness, coverage) and the decision the data supports. The hardest skill: designing products that answer the question the user actually has, not the question the data can answer.

### Archetype 13: Internal Tools / Operations

**[P]** Internal products serve internal customers — employees, not external users. Productivity measurement is harder than revenue measurement. The build-vs-buy decision is constant: should we buy a tool or build it internally? Organizational influence is the dominant skill — understanding internal needs without being captured by feature requests.

**[E]** Key failure modes:
- **Building what stakeholders ask for, not what they need** — Internal customers are poor designers of their own tools, just like external customers.
- **Platform team as bottleneck** — Internal tools team becomes the gatekeeper for all requests.
- **Measuring output not outcomes** — Counting features shipped, not productivity improved.

**[R]** The PM's hardest skill is organizational influence. Must conduct discovery with internal users (they have problems they can articulate but solutions they design poorly). Must measure productivity improvement, not just feature delivery.

---

## 5.4 Archetype-Specific Leadership Demand Weights

**[I]** The Academy's inference: the capabilities in the capability model have different importance weights across archetypes. Technical fluency is paramount for Platform and Developer Tools; much less so for Consumer. Risk judgment is paramount for Fintech and Healthcare; much less so for Gaming. The capability model describes WHAT capabilities matter; the archetype catalog describes WHICH capabilities matter most for a given product type. The PM transitioning between archetypes must identify which capabilities are weighted differently and develop accordingly.

---

# Part 6: AI Product Leadership

*This is a summary. For full treatment, see `handbook/AI_PM_PLAYBOOK.md` and Track 05 (`05_ai_product_management/`).*

## 6.1 The AI Product Leadership Mandate

**[E]** AI product management is not a specialization — it's becoming a core competency. Every product leader will make AI-related product decisions within the next 3 years, whether they choose to or not. The question is not "should we use AI?" but "where should we use AI, how do we evaluate it, and how do we govern it?"

**[P]** The Academy's AI product management framework (Track 05) rests on four pillars:
1. **Workflow Selection** — Is this workflow appropriate for AI? (Most failures trace to poor workflow selection.)
2. **Evaluation** — How do you know the AI is good enough? (The hardest unsolved problem.)
3. **System Design** — The system matters more than the model. (Prompts are fragile; system design is durable.)
4. **Governance** — Governance proportional to consequence. (Not all AI decisions carry the same risk.)

## 6.2 Workflow-First Methodology

**[E]** The most common AI product mistake is model-centric thinking: "Model X can do Y, let's build a product." The Academy's counter: workflow-centric thinking. Start from the human workflow, decompose it into subtasks, classify each by AI suitability.

**[R]** Before any AI product decision, complete the Workflow Description (Module 05, Part 1):
- Who: [user role]
- What: [task they're trying to accomplish]
- Input: [what they start with]
- Output: [what they produce]
- Constraint: [time, quality, regulatory]
- Current performance: [how well it works today, measured]

Then decompose into subtasks and score each on determinism, error tolerance, and automation value. The subtask matrix tells you which parts of the workflow are appropriate for AI. Most workflows have 20-40% of subtasks that are high-suitability for AI; 60-80% that should remain human or deterministic.

## 6.3 Evaluation Contracts

**[E]** Evaluation is the hardest unsolved problem in AI product management. Model benchmarks (MMLU, HumanEval, etc.) correlate weakly with product performance. The only reliable evaluation is against your specific workflow with your specific users.

**[R]** The Evaluation Contract (`05_ai_product_management/EVALUATION_CONTRACTS.md`) defines:
1. **Task success criteria** — What does "correct" mean for your workflow?
2. **Error severity classification** — Not all errors are equal
3. **Acceptance thresholds** — What error rate is acceptable?
4. **Test dataset** — Representative of real-world inputs, not curated
5. **Evaluation cadence** — How often and by whom?

**[I]** The most common evaluation failure is testing on the data you trained on (or prompted against). This produces inflated performance estimates. The test dataset must be held out, constructed before evaluation, and representative of the long tail of real inputs — not just the common cases.

## 6.4 AI Failure Modes

**[E]** AI products have failure modes that deterministic software doesn't. The Academy's failure mode catalog (`05_ai_product_management/FAILURE_MODES.md`) identifies 15 categories. The most important:

1. **Hallucination** — The model confidently produces incorrect output
2. **Brittleness** — Small input changes produce large output changes
3. **Distribution shift** — Model performance degrades on real-world data vs training/test distribution
4. **Mode collapse** — Output variety decreases over time or across users
5. **Bias amplification** — Model amplifies biases present in training data
6. **Overreliance** — Users trust AI output too much and stop exercising judgment
7. **Cost overrun** — Inference costs exceed planned budget or project revenue
8. **Prompt fragility** — Carefully crafted prompts break when the model is updated

**[R]** Before shipping any AI feature, complete the Failure Mode checklist. For each failure mode, assess probability, severity, detectability, and mitigation. The checklist is not optional — it's the minimum viable safety analysis.

## 6.5 Governance Proportional to Consequence

**[E]** Not all AI uses carry the same risk. The EU AI Act's risk-tiered approach (unacceptable, high, limited, minimal) provides a useful framework, even for non-EU products.

**[R]** The Academy's governance framework (`05_ai_product_management/GOVERNANCE.md`):
- **High-consequence domains** (healthcare, finance, safety, legal, hiring): Human-in-the-loop required. Evaluation contracts mandatory. External audit recommended.
- **Medium-consequence domains** (customer-facing recommendations, content generation, code generation): Human review for edge cases. Automated testing for known failure modes. User feedback mechanism.
- **Low-consequence domains** (internal tools, summarization, classification for non-critical use): Automated evaluation sufficient. Lightweight governance.

**[I]** The governance framework should be applied proportionally. The most common governance failure is applying the same governance to all AI uses — either over-governing low-consequence uses (slowing everything down) or under-governing high-consequence uses (creating unacceptable risk).

## 6.6 Build vs Buy vs Provider for AI

**[D]** The AI build-vs-buy decision is different from traditional software (CON-0010):
- **Build** (train or fine-tune your own model): Necessary when differentiation depends on model behavior, when you have unique data, or when off-the-shelf models don't meet your quality requirements. Highest cost, highest control.
- **Buy** (use a model API like OpenAI, Anthropic, Google): Appropriate for most use cases. Lower cost, lower control, dependency on provider.
- **Provider** (use an AI-powered product that includes the AI): Appropriate when the AI is not differentiating. Lowest cost, lowest control.

**[R]** The Academy's recommendation: default to "Buy" (model API) unless differentiation requires "Build" or non-differentiation allows "Provider." Most organizations overestimate how differentiating their AI use case is.

## 6.7 AI Product Leadership in Practice: Case-Integrated Lessons

**[E]** The Academy's case catalog provides lessons that directly apply to AI product leadership:

**From CASE-0005 (Knight Capital): The AI Parallel.** Knight Capital lost $440M in 45 minutes from a deployment error involving dormant code and no circuit breakers. The AI parallel: AI systems make decisions at scale with similar blast radius. Circuit breakers are mandatory — confidence thresholds that trigger human review, rate limits on automated decisions, automatic shutdown if error rates exceed thresholds. Dormant capabilities are technical debt — model capabilities you haven't tested can activate unexpectedly. Reversal mechanisms must be tested, not assumed — your AI's "human override" needs a tested speed of activation.

**From CASE-0004 (Microsoft Transformation): The AI Platform Shift.** Microsoft transformed from Windows-first to cloud-first by killing legacy strategy, embracing competitors' platforms, and cultural transformation. Organizations adding AI face a similar shift: stop optimizing for the old product model and build AI-native capabilities (evaluation, data flywheels, trust architecture). Embrace AI providers as partners even if they compete in some areas. Transform culture, not just technology — PMs who can't evaluate AI output cannot lead AI products.

**From CASE-0006 (Slack Platform Strategy): The AI Paradigm Decision.** Slack chose bot-first over directory-first, defining their platform paradigm. AI product leaders face a similar choice: is your AI paradigm agent-first (AI takes action) or assistant-first (AI suggests, human decides)? The paradigm decision determines evaluation approach, trust architecture, governance requirements, and user experience. Make it explicitly, not by default.

**From CASE-0003 (Google Reader): The AI Sunset Parallel.** Google's Reader sunset damaged trust for a decade. When you deprecate an AI feature or change model behavior, the trust cost can exceed the engineering savings. Users who built workflows around your AI's behavior will be disrupted. Graceful AI deprecation: communicate changes, provide transition periods, explain why, maintain backward compatibility where possible.

## 6.8 AI Product Leadership: Skills Portfolio by Level

**[R]** AI competency development by role level:

**Senior PM — AI Literacy:** Can complete Workflow Selection methodology for proposed AI features. Can write evaluation contracts. Understands the 8 anti-patterns. Can articulate AI cost structure. Understands governance tier for their domain.

**Principal PM — AI Strategy:** Can identify AI-appropriate workflows across multiple areas. Can design evaluation systems. Can make build-vs-buy-vs-provider decisions. Understands strategic implications of AI for the product domain. Can influence organizational AI governance.

**Director — AI Portfolio Management:** Can allocate across AI and non-AI investments. Can design AI development processes (evaluation gates, governance reviews). Can build organizational AI capability. Can manage AI vendor relationships. Can communicate AI strategy and risk to executives.

**VP/CPO — AI Institutional Leadership:** Can define company AI strategy. Can represent AI decisions to the board. Can navigate regulatory environment. Can build AI product culture across the organization. Can make build-vs-partner decisions for AI infrastructure.

## 6.9 The AI Product Leader's Decision Framework

**[R]** A consolidated view of the AI product leadership frameworks from this Part and the AI PM Playbook:

| Stage | Framework | Key Question | Output |
|-------|-----------|-------------|--------|
| 1. Problem | PVS Assessment | Is this problem worth solving? | PVS score (≥4.0 proceed) |
| 2. AI Suitability | Workflow Selection | Should AI do this? | Subtask suitability matrix |
| 3. Anti-Pattern | 8 Anti-Patterns | Why NOT use AI? | Anti-pattern clearance |
| 4. Feasibility | TNA Assessment | Can AI do this well enough? | TNA score (≥3.0 proceed) |
| 5. Decision | PVS-TNA Matrix | Combined assessment | Build/Investigate/Monitor/Don't Build |
| 6. Quality | Evaluation Contract | How do we know it's good? | Contract document |
| 7. Safety | Failure Mode Assessment | What could go wrong? | RPN scores + mitigations |
| 8. Sourcing | Build-Buy-Provider | How do we get it? | Sourcing recommendation |
| 9. Governance | Governance Tiers | What oversight? | Tier 1/2/3 classification |
| 10. Adoption | Trust Architecture | How will users trust it? | Trust design elements |

**[R]** Skipping stages is the most common AI product failure pattern. The most skipped: Stage 3 (Anti-Pattern Check), Stage 6 (Evaluation Contract), Stage 7 (Failure Mode Assessment), and Stage 10 (Trust Architecture). These four stages separate AI products from AI demos.

---

# Part 7: Industry Contexts

*This section summarizes the Academy's industry overlays (Track 06). For full detail, see `06_industry_overlays/`.*

## 7.1 Financial Services

**[E]** Financial services is the most heavily regulated industry for product management. The key constraints:

- **Trust is existential.** Financial products handle people's money. Trust is earned slowly, lost instantly.
- **Regulatory constraints are pervasive.** Compliance shapes what can and cannot be built. It is not a separate function — it's a product requirement.
- **Transaction integrity is non-negotiable.** Money must move correctly every time. "Eventually consistent" is not acceptable.
- **Fraud and security threats are relentless.** Financial products are high-value targets from day one.
- **Complex stakeholder landscape.** Regulators, banking partners, compliance, risk managers, legal — all have veto power.

**[R]** For PMs in financial services:
- Compliance is a design partner, not a reviewer. Involve compliance in product discovery, not just product approval.
- The cost of being wrong is measured in lost money, lost trust, and regulatory action — not just lost users.
- "Move fast and break things" is never appropriate. The appropriate framework is "move deliberately and build things right."
- Financial products that feel trustworthy (transparency, control, clear communication) outperform products that feel clever.

**Related:** See Fintech archetype (Archetype 8) in Part 5. See CASE-0005 (Knight Capital) for the canonical failure. See TIAA application in `12_personal_lab/TIAA_APPLICATION.md`.

## 7.2 Insurance

**[E]** Insurance product management adds distinctive constraints beyond financial services:
- Actuarial science meets product management — pricing is based on risk models, not willingness to pay
- Claims experience determines customer satisfaction — the moment of truth is when something goes wrong
- Moral hazard and adverse selection are product design problems — not just actuarial problems
- Regulatory framework varies by state/province and country — more fragmented than banking regulation
- Legacy technology stacks are the norm — innovation must work within and around decades-old systems

**[R]** For PMs in insurance:
- The claims experience IS the product experience. Design it as carefully as the purchase experience.
- Product decisions have actuarial implications. Partner with actuarial teams; don't make pricing or coverage decisions without them.
- Innovation in insurance is more often about distribution, claims, and customer experience than about new risk products.

## 7.3 Power and Energy

**[E]** Energy product management operates at the intersection of physical infrastructure, regulatory markets, and environmental constraints:
- Physical infrastructure has multi-decade lifecycles — product decisions today affect operations for 30+ years
- Regulatory markets (not competitive markets) determine pricing and product viability in many jurisdictions
- Environmental and social impact are product requirements, not externalities
- Grid interconnection and reliability requirements create hard technical constraints
- Capital intensity means financing is a product variable — the cost of capital shapes what can be built

**[R]** For PMs in energy:
- Regulatory strategy is product strategy. You cannot separate product decisions from the regulatory framework.
- The time horizon for product decisions is measured in years or decades, not quarters.
- Stakeholder management includes communities, environmental groups, and regulators — not just customers and shareholders.
- Technology risk (does it work?) and market risk (will people buy?) are joined by regulatory risk (will it be approved?) and financing risk (can it be funded?).

## 7.4 Infrastructure

**[E]** Infrastructure product management involves:
- Public-sector buyers with procurement processes that shape what can be built and sold
- Multi-stakeholder complexity: governments, financiers, communities, contractors, operators
- Long development cycles with high upfront costs and delayed revenue
- Political risk — changes in government can reshape the infrastructure landscape
- Evidence standards are high and contested — projects must be "bankable," not just desirable

**[R]** For PMs in infrastructure:
- Procurement understanding is as important as customer understanding. You must know how your buyer buys.
- The development cycle (concept → feasibility → design → finance → build → operate) is a product lifecycle. Each phase has different product leadership demands.
- Public-private partnership models create unique product constraints and opportunities.
- Infrastructure products that reduce development cycle time or improve evidence quality are valuable even if they don't change the physical output.

**Related:** See InfraPrep application in `12_personal_lab/INFRAPREP_APPLICATION.md`.

## 7.5 General Industry Patterns

### The Regulated Industry Pattern

**[I]** Products in regulated industries (finance, healthcare, insurance, infrastructure, energy) share common patterns despite different regulations:

1. **Compliance is a product requirement, not a review step.** The PM who treats compliance as a post-design gate will redo the design. The PM who partners with compliance from discovery onward ships on schedule.
2. **Trust architecture is essential.** In regulated industries, trust is not assumed — it must be designed into the product. Transparency, control, explainability, and recourse mechanisms are product features.
3. **The cost of being wrong is higher.** The speed-assurance trade-off (CON-0006) tilts strongly toward assurance. Not infinitely — the cost of delay still matters — but the minimum bar for quality is higher.
4. **Stakeholder landscape includes regulators.** You cannot ignore them or hope they don't notice. Regulatory strategy is product strategy.
5. **Innovation occurs within constraints, not by ignoring them.** The most innovative regulated-industry products work within the regulatory framework, not around it. Regulatory arbitrage as strategy (exploiting gaps) is temporary; regulators eventually catch up.

### The High-Growth Startup Pattern

**[I]** Products in high-growth startups face:
1. **Runway constraints dominate resource allocation.** Strategy must account for funding milestones. The sequence must produce fundable evidence at the right moments.
2. **Speed matters more than process.** Pre-PMF startups should bias toward speed (PRN-0003 applicability). Process that slows learning without improving decisions is lethal.
3. **The PM IS the builder.** At early stage, the PM-builder model (CON-0013 position A) is appropriate. You cannot be a multiplier when there's nothing to multiply.
4. **Strategy is "find PMF."** Exclusion (PRN-0002) would be premature.
5. **The team IS the strategy.** Early-stage product success depends heavily on the specific people, not just the market opportunity.

### The Public Company Pattern

**[I]** Products in public companies face:
1. **Quarterly earnings create pressure toward short-term optimization.** Resisting this is a leadership skill.
2. **Analyst expectations shape product perception.** The product narrative must be legible to people who don't use the product.
3. **Materiality standards apply to communication.** What you say about the product has legal and market implications.
4. **Resource allocation is more political.** Budgets have more stakeholders and more inertia.
5. **The existing business constrains innovation.** New products must coexist with, not cannibalize, the revenue streams that fund the company (CASE-0004: Microsoft managed this; many fail).

### The Turnaround Pattern

**[I]** Products in turnaround situations face:
1. **Centralized direction may be necessary.** Team autonomy (PRN-0001) may need to be suspended for coordinated, rapid action.
2. **Hard decisions must be made fast.** The cost of delay in a turnaround is existential.
3. **Trust must be rebuilt.** Internal trust (employees) and external trust (customers) have typically been damaged.
4. **Legacy products must be managed down while new products are built up.** The Microsoft pattern (CASE-0004) applies.
5. **Culture change is product strategy.** The culture that produced the crisis must change for the turnaround to sustain.

---

# Part 7B: Product Leadership Across Organizational Stages

**[P]** Product leadership demands vary not just by industry and archetype, but by organizational stage. The PM operating model that works at a 10-person startup fails at a 10,000-person enterprise — and vice versa. This section describes the distinctive product leadership challenges at each stage.

## Pre-Product / Seed Stage (1-10 people)

**[I]** At this stage, there is no product, no users, and no revenue. The only thing that matters is finding product-market fit. Strategy documents, process frameworks, and organizational design are premature — even harmful.

**What product leadership means at this stage:**
- The PM (often the founder) IS the builder. There is no organizational leverage to apply — you must do the work yourself (CON-0013, Position A).
- Speed dominates. The cost of delay is existential (PRN-0003).
- Strategy is "find PMF by trying things." Exclusion would be premature (PRN-0002 non-applicability).
- The team IS the strategy. The specific people matter more than any document.
- Customer discovery is the core activity — but it's discovery by building and shipping, not discovery by interviewing. You learn by putting things in front of users.

**Key risks:**
- Building infrastructure before validating demand
- Optimizing for investor appeal rather than user value
- Over-indexing on the first 10 users (they're not representative)
- Failing to pivot when evidence says the current direction isn't working

**Academy doctrine most relevant:** PRN-0003, PRN-0004 (finding PMF, not maintaining it), PRN-0008, AI_PM_PLAYBOOK workflow selection (for AI-first products)

## Growth Stage (10-200 people)

**[P]** PMF has been found. The challenge shifts from "does anyone want this?" to "how do we scale this without breaking it?" This is the most chaotic stage — the organization is growing faster than its processes can keep up.

**What product leadership means at this stage:**
- Begin transitioning from builder to multiplier. You cannot touch every decision. You must develop other PMs and trust their judgment.
- Process emerges from need, not from design. Add process only when the absence of process is causing visible failures.
- Team structures form around product boundaries. Conway's Law becomes relevant for the first time (PRN-0010).
- Resource allocation becomes a conscious activity, not a default (Part 4). You now have more opportunities than resources.
- Strategy begins to require explicit exclusion (PRN-0002). Before this stage, everything was worth trying. Now, choices must be made.

**Key risks:**
- The founder bottleneck — the person who made every decision at 10 people can't make every decision at 100
- Premature process — adding process because it feels responsible, not because it's needed
- Hiring generalists when you need specialists (or vice versa)
- Losing product culture as the organization grows (new hires don't have the context the early team had)

**Academy doctrine most relevant:** PRN-0001 (empowered teams start to become relevant), PRN-0002, PRN-0010, PRN-0012, Principal PM Playbook (for the Senior-to-Principal transition happening at this stage)

## Scale Stage (200-1000+ people)

**[P]** The organization has product lines, multiple teams, and established processes. The challenge shifts from "how do we scale?" to "how do we maintain velocity, quality, and innovation as we grow?" This is where organizational design becomes a primary product leadership activity.

**What product leadership means at this stage:**
- The Principal PM role becomes essential. Senior PMs execute within bounded contexts; Principal PMs define the boundaries and maintain strategic coherence across them.
- Decision systems matter more than individual decisions. You cannot be in every decision meeting. You must design HOW decisions are made (Decision Framework 7).
- Organizational design IS product design (PRN-0010). Team structure shapes product architecture. Platform teams, shared services, and API contracts become the coordination mechanisms.
- Strategy must cascade from company level to team backlogs (Decision Framework 5). The "missing middle" — strategy that exists at the top and bottom but not in between — is the most common failure.
- Product culture must be actively maintained. It no longer transmits automatically through proximity to the founder or early team.

**Key risks:**
- The Innovator's Dilemma — optimizing for existing customers while missing emerging needs (PRN-0004)
- Process accumulation — each crisis adds a process; eventually the organization is crushed by process
- The middle-management bulge — Directors who add process without adding strategic value
- Cross-team coordination costs growing faster than team output (diseconomies of scale in product development)

**Academy doctrine most relevant:** PRN-0001, PRN-0009, PRN-0010, Decision Framework 6 (Product-Org Co-Design), Part 8 (Principal+ Leadership), CON-0001 (Autonomy vs Central Direction)

## Mature / Public Company Stage

**[P]** The product portfolio is established. Revenue is substantial. The organization is optimized for the current business model. The challenge shifts from "how do we grow?" to "how do we avoid being disrupted while continuing to deliver?"

**What product leadership means at this stage:**
- Portfolio allocation (Part 4) is the primary activity. How much to invest in the core business vs adjacent expansion vs transformational bets.
- The board narrative matters. Product strategy must be legible to people who don't use the product.
- Legacy products must be managed — not just built (Sunset Decision Framework, CASE-0003).
- Innovation must be structurally protected from the core business (the "ambitious startup vs well-funded incumbent" dynamic playing out internally).

**Key risks:**
- Short-term optimization — quarterly earnings pressure driving decisions that sacrifice long-term value
- Innovation theater — funding "innovation labs" that produce press releases, not products
- The core business consuming all resources — "we'll invest in new things next quarter" (and next quarter, and next quarter)
- Losing touch with the product — VP/CPO becoming pure organizational leaders

**Academy doctrine most relevant:** CASE-0004 (Microsoft transformation), Industry overlay 06.3 (Public Companies), Part 4 (Resource Allocation), Part 8 (VP/CPO Leadership), CON-0009 (Short-term vs Long-term)

## Transformation / Turnaround Stage

**[P]** The organization is in crisis — declining revenue, competitive displacement, cultural dysfunction, or technological obsolescence. The challenge shifts from "how do we optimize?" to "how do we survive and redirect?"

**What product leadership means at this stage:**
- Centralized direction may be temporarily necessary. Team autonomy (PRN-0001) may need to be suspended for coordinated, rapid action.
- Hard decisions must be made fast. The cost of delay in a turnaround is existential (PRN-0003 applies with extreme force).
- Legacy assets must be managed down while new direction is built up (CASE-0004).
- Trust must be rebuilt — internal (employees) and external (customers).

**Key risks:**
- Transformation theater — announcing change without changing incentives, structure, or resource allocation
- Killing the legacy business too fast — the revenue from legacy products funds the transformation
- Cultural resistance — the organization that needs to change is composed of people who were successful under the old model
- Half-measures — trying to transform while preserving all existing commitments

**Academy doctrine most relevant:** CASE-0004 (Microsoft transformation), CASE-0001 (Netflix Qwikster — managed decline of DVD business), Industry overlay 06.9 (Turnarounds), CON-0003 (Founder vs Professional — turnarounds often require a different leader)

*This is a summary. For full treatment, see `handbook/PRINCIPAL_PM_PLAYBOOK.md` and Track 02 (`02_principal_plus/`).*

## 8.1 What Actually Changes at Principal Level

**[P]** The Senior-to-Principal transition is the most difficult in product management. Most PMs who plateau do so at Senior PM — not because they lack execution skills, but because Principal capabilities are qualitatively different.

The core shift is from execution to strategy:

| Dimension | Senior PM | Principal PM |
|-----------|-----------|--------------|
| Primary output | Shipped features and measured outcomes | Strategy, organizational influence, decision quality at scale |
| Scope | Single product or feature area | Product domain or multiple related products |
| Time horizon | Current quarter to 6 months | 6-18 months |
| Decision authority | Within defined product area | Across product boundaries; must influence without authority |
| Information quality | Defined problem, defined constraints | Ambiguous problem, ambiguous constraints — must define both |
| Failure mode | Wrong feature, wrong priority | Wrong strategy, wrong resource allocation, wrong problem definition |

**[R]** If you're a Senior PM aspiring to Principal, the single most important capability to develop is Problem Definition Under Ambiguity (Capability 2.1 in `02_principal_plus/PRINCIPAL_PM.md`). Practice: take a vague directive ("improve developer experience") and produce a one-page problem definition with specific customer segment, quantified current state, measurable desired state, constraints, and assumptions — in 4 hours, not 4 weeks.

## 8.2 Director: From Influence to Systems

**[P]** The Director transition is from personal influence to organizational systems. At Principal PM, you influence through personal capability. At Director, you design the systems that produce good decisions without your personal involvement.

Key Director capabilities:
- Designing decision rights, planning cadences, and review forums (Decision Systems, Capability 3.4)
- Ensuring the organization has adoption capability, not just delivery capability (Adoption Architecture)
- Building the coaching and development infrastructure for PMs (Talent Development)
- Managing the tension between team autonomy and organizational coherence (CON-0001)

## 8.3 VP/CPO: Institutional Leadership

**[P]** The VP/CPO transition is from product leadership to institutional leadership. You are now accountable for product outcomes to the board, investors, and market — not just to your organization.

Key VP/CPO capabilities:
- Board-level narrative construction (Capability 4.4)
- Capital allocation across the portfolio (Capability 4.3)
- Defining the company-level product strategy (what markets, what differentiation, what exclusion)
- Organizational design that produces the desired product (PRN-0010)
- Maintaining product culture as the organization scales

**[I]** The CPO role is the least standardized in product management. CPOs at different companies do fundamentally different jobs depending on company stage, founder involvement, industry, and organizational structure. The Academy's CPO capability model is a synthesis of observed practice, not a standardized role description.

## 8.4 The Failure Modes at Each Level

**[P]** Level-specific failure modes:

**Senior PM failure modes:**
- Optimizing for output (features shipped) rather than outcomes (problems solved)
- Building what's requested rather than discovering what's needed
- Avoiding difficult stakeholder conversations
- Treating the roadmap as a promise rather than a hypothesis

**Principal PM failure modes:**
- Still operating as a Senior PM — defining solutions instead of defining problems
- Influence without substance — trying to influence decisions without bringing data or insight
- Strategic thinking without execution — spending so much time on strategy that you stop shipping
- The ghost influencer — influencing behind the scenes so quietly that nobody knows you did it

**Director failure modes:**
- Micromanaging PMs instead of developing their capability
- Designing process for its own sake — process that adds overhead without improving decisions
- Avoiding resource allocation decisions — maintaining status quo allocations
- Confusing organizational activity (meetings, reviews, planning cycles) with organizational effectiveness

**VP/CPO failure modes:**
- Losing touch with the product — becoming a pure organizational leader
- Board narrative that diverges from operational reality
- Strategy that is aspirational without being actionable — no cascading through the organization
- Hiring CPO-level talent (Principal, Director) but operating them as Senior PMs

---

# Part 8: Principal+ Leadership

*This is a summary. For full treatment, see `handbook/PRINCIPAL_PM_PLAYBOOK.md` and Track 02 (`02_principal_plus/`).*

## 8.1 What Actually Changes at Principal Level

**[P]** The Senior-to-Principal transition is the most difficult in product management. Most PMs who plateau do so at Senior PM — not because they lack execution skills, but because Principal capabilities are qualitatively different.

The core shift is from execution to strategy:

| Dimension | Senior PM | Principal PM |
|-----------|-----------|--------------|
| Primary output | Shipped features and measured outcomes | Strategy, organizational influence, decision quality at scale |
| Scope | Single product or feature area | Product domain or multiple related products |
| Time horizon | Current quarter to 6 months | 6-18 months |
| Decision authority | Within defined product area | Across product boundaries; must influence without authority |
| Information quality | Defined problem, defined constraints | Ambiguous problem, ambiguous constraints — must define both |
| Failure mode | Wrong feature, wrong priority | Wrong strategy, wrong resource allocation, wrong problem definition |

**[R]** The single most important capability to develop: Problem Definition Under Ambiguity (see `02_principal_plus/PRINCIPAL_PM.md`, Capability 1). Practice: take a vague directive and produce a one-page problem definition with specific customer segment, quantified current state, measurable desired state, constraints, and assumptions — in 4 hours, not 4 weeks. Share with someone who would know if it's wrong. Revise.

## 8.2 The Five Principal PM Capabilities

From `02_principal_plus/PRINCIPAL_PM.md`:

**Capability 1: Problem Definition Under Ambiguity:** You receive vague strategic direction and must decompose it into specific problems, customer segments, and success criteria. The problem definition IS the deliverable.

**Capability 2: Organizational Influence Without Authority:** You influence decisions you cannot make directly. The key shift: you no longer have authority over the people whose decisions you need to influence. The toolkit includes framing decisions, building coalitions, making partners successful, documenting decisions, and knowing when to escalate vs accept.

**Capability 3: Decision-Making Under Uncertainty:** At Senior PM, you make decisions with data. At Principal PM, you make decisions before data exists. The key framework: identify what you need to believe, identify key uncertainties, design the cheapest test, set a time limit, design the reversal condition.

**Capability 4: Strategic Product Thinking:** Seeing the system, not just the part. The second-order drill uncovers effects beyond the immediate decision — system effects, signal effects, and commitment effects that first-order thinking misses.

**Capability 5: Cross-Team Product Thesis:** Theses that span multiple product areas. Not just what you believe, but what evidence would change your mind. The thesis must be falsifiable and specific — not aspirational.

## 8.3 Director: From Influence to Systems

**[P]** The Director transition shifts from personal influence to organizational systems. At Principal PM, you influence through personal capability. At Director, you design systems that produce good decisions without your personal involvement. You shift from making decisions to building decision-making capability in others.

**Key Director capabilities:**
- Designing decision systems — decision rights, planning cadences, review forums, information flows
- Building organizational adoption capability — ensuring the org has skills for adoption architecture, not just delivery
- Talent development — coaching PMs, building hiring and development infrastructure
- Organizational design — structuring teams to produce the desired product architecture (PRN-0010)
- Managing the autonomy-coherence tension (CON-0001, CON-0008)

**The Director failure mode:** Micromanaging PMs instead of developing them. The Director who reviews every PRD is operating as a "Super Principal PM." The job is to make the organization capable without you.

## 8.4 VP/CPO: Institutional Leadership

**[P]** The VP/CPO transition moves from product leadership to institutional leadership. You are accountable for product outcomes to the board, investors, and market — not just your organization. You define what the company builds, for whom, and why, with board-level accountability.

**Key VP/CPO capabilities:**
- Company-level product strategy — what markets, what differentiation, what exclusion (Capability 4.1)
- Capital allocation — allocating total product investment across the portfolio (Capability 4.3)
- Board narrative — constructing and maintaining the product narrative for the board (Capability 4.4)
- Organizational design at scale — Conway's Law applied deliberately (Capability 4.2)
- Product culture — shaping how the organization thinks about product (Capability 4.5)

**The VP/CPO failure mode:** Losing touch with the product. Becoming a pure organizational leader who spends all time on board decks and organizational design while losing the product judgment that made them effective. The best VP/CPOs maintain direct product engagement.

## 8.5 The Failure Modes at Each Level — With Detection and Correction

**[P]** Level-specific failure modes — not just what they are, but how to detect and correct them:

**Senior PM failure modes:**
- **Output-over-outcome:** Measuring features shipped, not problems solved. *Detection:* Your review lists features, not outcomes. *Correction:* For each feature, ask "What outcome did this produce? How do we know?"
- **Building what's requested:** Responding to feature requests without discovery. *Detection:* Backlog items don't trace to discovered problems. *Correction:* For each item, trace it to customer discovery.
- **Roadmap as promise:** Treating roadmap as commitment, not hypothesis. *Detection:* You feel stressed when it changes. *Correction:* Label items with confidence levels. Communicate as "current best plan."

**Principal PM failure modes:**
- **The Super Senior PM:** Still doing Senior work at higher volume. *Detection:* Calendar full of roadmap reviews, feature decisions. *Correction:* Delegate one Senior PM task this week.
- **The Strategist's Trap:** Strategy without execution. *Detection:* Haven't influenced a shippable decision in two weeks. *Correction:* Find one tactical decision and contribute to it today.
- **The Ghost Influencer:** Influence without visibility. *Detection:* Manager can't name three decisions you influenced. *Correction:* Write and circulate a decision memo.
- **The Influence-Only PM:** Influence without substance. *Detection:* In every meeting but no decisions changed. *Correction:* Prepare new data/analysis before your next influence conversation.

**Director failure modes:**
- **Micromanaging PMs:** Reviewing every PRD. *Detection:* PMs wait for your approval. *Correction:* For one decision this week, tell a PM "You decide. Let me know what and why."
- **Process building:** Creating process for every friction. *Detection:* Two+ new recurring meetings this quarter. *Correction:* Before adding process, ask "Can I fix this by talking to the people involved?"
- **Status quo allocation:** Resources unchanged for two+ quarters. *Detection:* No initiative killed or reallocated. *Correction:* Identify lowest-impact initiative. Propose killing it.

**VP/CPO failure modes:**
- **Board narrative divorced from reality:** Telling the board what they want to hear. *Detection:* Anxious before board meetings. *Correction:* One bad-news item per board meeting, with analysis and plan.
- **Strategy as aspiration:** Company strategy that excludes nothing. *Detection:* Can't list 5 things the strategy says you won't do. *Correction:* Explicitly list exclusions. Socialize them.
- **Losing product touch:** Pure organizational leader. *Detection:* Haven't used product as a user in past week. *Correction:* Block 2 hours/week for product engagement. Don't let it be consumed.

## 8.6 The Product Leader's Reading Path by Level

**[R]**

**Senior PM → Principal PM:**
1. `02_principal_plus/PRINCIPAL_PM.md` (entire document)
2. `handbook/PRINCIPAL_PM_PLAYBOOK.md` (entire document)
3. Principles: PRN-0001, PRN-0002, PRN-0005, PRN-0009, PRN-0010, PRN-0012
4. Decision Frameworks: 1, 2, 7, 8
5. Contradictions: CON-0001, CON-0007, CON-0013
6. Cases: CASE-0001, CASE-0004, CASE-0006

**Principal PM → Director:**
7. `02_principal_plus/DIRECTOR_VP_TRANSITION.md`
8. Bible Parts 4, 7, 8
9. Decision Frameworks: 3, 4, 5, 6
10. All contradictions
11. Cases: CASE-0003, CASE-0005

**Director → VP/CPO:**
12. `02_principal_plus/CPO_ROLE.md`
13. Bible Parts 4, 6, 7, 8, 9 — full depth
14. All remaining cases
15. AI Strategy modules (05.7)

---

# Part 9: Contradictions and Open Questions

*The Academy maintains a register of 13 unresolved product leadership contradictions (`08_contradictions/register.yaml`). This section summarizes the most important and their practical implications.*

## 9.1 The Contradictions Register Summary

**[D]** These are questions where reasonable, experienced product leaders disagree — and where the "right" answer depends on context. The Academy's position: acknowledging uncertainty is better than asserting false certainty.

### CON-0001: Empowered Teams vs Central Direction

*Should product teams set their own direction, or should central leadership define the strategy?*

**Position A (Empowered teams):** Cross-functional teams with customer access and decision authority outperform centrally-directed teams. Autonomy increases motivation, speeds decision cycles, and produces solutions that fit local context better than top-down mandates. *Key proponents: Marty Cagan, Spotify model, Teresa Torres.*

**Position B (Central direction):** Without strong centralized direction, teams optimize locally, produce fragmented experiences, duplicate effort, and fail to make platform-level bets. The most consequential decisions cannot be delegated without losing coherence. *Key proponents: Steve Jobs, Apple, Brian Chesky (Airbnb re-centralization).*

**[E]** Evidence: Position A supported by SVPG research (SRC-BOOK-0001, SRC-BOOK-0001), DORA data (SRC-BOOK-0027). Position B supported by Airbnb case (SRC-TALK-0005), Apple's functional organization (SRC-POST-0002).

**[R]** Context A stronger: Mature product with stable architecture and strong teams. Context B stronger: Early-stage seeking PMF, platforms requiring cross-surface integration, turnaround situations. The worst state is the "messy middle" — neither fully empowered nor fully directed.

### CON-0002: Customer Discovery vs Strategic Conviction

*Should product decisions be driven by continuous customer research or concentrated strategic conviction?*

**Position A (Continuous discovery):** Regular, structured customer interaction produces better decisions than periodic strategic planning. Markets move too fast for annual strategy cycles. *Key proponents: Teresa Torres, Jeff Gothelf, Eric Ries.*

**Position B (Strategic conviction):** Customers cannot tell you what they will want. Breakthrough products come from singular vision that no amount of interviewing would validate. *Key proponents: Steve Jobs, Peter Thiel.*

**[E]** Evidence: Position A supported by Continuous Discovery methodology (SRC-BOOK-0004), Lean Startup (SRC-BOOK-0014). Position B supported by Innovator's Dilemma insight (SRC-POST-0003), Zero to One (SRC-BOOK-0021).

**[R]** Discovery should be the default. Conviction-driven bets should be the explicit exception, with clear rationale for why discovery is insufficient. The failure modes are symmetric: "discovery theater" (interviewing but only hearing what confirms beliefs) vs "strategic LARPing" (claiming conviction when unwilling to do discovery work).

### CON-0003: Founder-Led vs Professional Product Organization

*Should product leadership stay with the founder or transition to professional product leadership at scale?*

**[E]** Evidence: Position A (founder-led) supported by Founder Mode essay (SRC-POST-0004), The Hard Thing About Hard Things (SRC-BOOK-0003). Position B (professional) supported by Blitzscaling (SRC-BOOK-0022), various founder-to-CPO transition cases (SRC-POST-0005).

**[R]** Context A stronger: Pre-PMF companies, companies under 150 people, companies where founder IS the product visionary. Context B stronger: Multi-product companies 500+ people, regulated industries requiring systematic compliance, companies where founder instinct has produced multiple failed bets.

**[D]** The open question: "Is there a durable 'founder product partner' model that preserves founder vision while adding professional capacity?" This question is unresolved in practice.

### CON-0004: Product-Led Growth vs Sales-Led Growth

*Should growth be driven by the product itself or by enterprise sales?*

**[E]** Evidence: PLG supported by OpenView research (SRC-BOOK-0023, SRC-POST-0006). Sales-led supported by enterprise SaaS benchmarks (SRC-POST-0007), Predictable Revenue methodology (SRC-BOOK-0024).

**[R]** Context A stronger: SMB products, self-serve evaluation, developer tools. Context B stronger: Enterprise with organizational behavior change requirements, regulated industries, high-ACV products. The most common failure: "PLG cargo cult" — adding a free tier and calling it PLG without product-led adoption architecture.

### CON-0005: General Platform vs Opinionated Workflow

*Should products be general platforms that users configure, or opinionated workflows that enforce a specific approach?*

**[E]** Evidence: Platform approach supported by AWS strategy (SRC-POST-0008), platform economics theory (SRC-BOOK-0025). Opinionated workflow supported by Basecamp/37signals philosophy (SRC-BOOK-0026), Superhuman, Linear cases (SRC-POST-0009).

**[R]** Context A stronger: Developer tools, enterprise products serving heterogeneous workflows. Context B stronger: Specific workflow with known best practice, consumer products where simplicity is core value, early-stage products needing to prove value before adding flexibility.

### CON-0006: Speed vs Quality and Assurance

*Should product organizations prioritize speed of delivery or assurance of quality?*

**[E]** Evidence: Speed supported by DORA research showing elite performers ship faster AND more reliably (SRC-BOOK-0027), Amazon speed philosophy (SRC-POST-0010). Quality/assurance supported by Google SRE approach (SRC-BOOK-0028), Knight Capital incident (SRC-POST-0011).

**[R]** Speed-appropriate contexts: Pre-PMF, consumer software, internal tools. Quality-appropriate contexts: Safety-critical (medical, aviation, autonomous), financial systems, regulated, sensitive data. The DORA finding that elite performers achieve BOTH speed and stability is the aspiration, but requires significant investment in CI/CD, feature flags, and operational capability.

### CON-0007: Experimentation vs Judgment

*Should product decisions be driven by structured experimentation or experienced judgment?*

**[E]** Evidence: Experimentation supported by Kohavi's research (SRC-BOOK-0029), Booking.com culture (SRC-POST-0012). Judgment supported by Amazon's one-way door framework (SRC-POST-0013), Shreyas Doshi on product sense (SRC-POST-0014).

**[R]** Key insight: most important decisions (market entry, platform architecture, product sunsetting) cannot be A/B tested. They are one-way doors requiring judgment. Experimentation works for optimization within a strategic frame, not for choosing the frame itself.

### CON-0008: Local Team Autonomy vs Enterprise Architecture

*Should teams have full decision autonomy or should enterprise architecture govern cross-team decisions?*

**[E]** Evidence: Autonomy supported by evolutionary architecture (SRC-BOOK-0030), Netflix culture (SRC-POST-0015). Governance supported by architecture governance tradeoffs (SRC-BOOK-0031), Amazon API Mandate (SRC-POST-0016).

**[R]** The Amazon resolution: one centralized architecture decision (all teams communicate through APIs) that ENABLES team autonomy. The right approach is not autonomy OR governance but governance at the interface layer that enables autonomy within bounded contexts.

### CON-0009: Customer Responsiveness vs Product Vision

*Should product organizations be highly responsive to customer requests or protect a coherent vision?*

**[E]** Evidence: Responsiveness supported by Salesforce IdeaExchange (SRC-POST-0017), customer success economics (SRC-BOOK-0032). Vision supported by Intercom's saying-no philosophy (SRC-POST-0018), Good Strategy Bad Strategy (SRC-BOOK-0015).

**[R]** The Jobs-to-be-Done framework offers a potential bridge: focus on the customer's underlying job (which they can articulate), not their requested solution (which they design poorly). This honors customer input without producing feature swamps.

### CON-0010: Build vs Buy vs Partner

*Should teams build custom solutions or buy and integrate third-party products?*

**[E]** Evidence: Default-to-buy supported by enterprise architecture best practices (SRC-POST-0019), API economy (SRC-POST-0020). Build-for-control supported by 37signals philosophy (SRC-BOOK-0033), Netflix CDN build (SRC-POST-0021).

**[R]** Default to buy unless the capability IS the differentiation. The most undervalued factor: the total cost of ownership for built capabilities is typically 3-5x the initial build cost over 5 years. The most overvalued factor: many organizations claim differentiation to justify building non-differentiating capabilities.

### CON-0011: Human-in-the-Loop vs Full Automation

*Should AI workflows keep humans in the loop or automate fully?*

**[E]** Evidence: Human-in-the-loop supported by AI safety research (SRC-POST-0022), FDA framework (SRC-POST-0023). Full automation supported by Stripe philosophy (SRC-POST-0024), subscription business case (SRC-BOOK-0034).

**[R]** Context A stronger: High-stakes decisions (medical, credit, criminal justice), edge-case-rich domains, regulated industries. Context B stronger: High-volume low-stakes (spam filtering, recommendations), operations with clear correctness criteria, systems that measurably outperform humans. This is the most urgent contradiction for AI product leaders — see `handbook/AI_PM_PLAYBOOK.md` Section 6.

### CON-0012: One Roadmap vs Independent Team Roadmaps

*Should the organization operate from a single roadmap or team-level roadmaps?*

**[E]** Evidence: Single roadmap supported by portfolio prioritization best practices (SRC-POST-0025), Escaping the Build Trap (SRC-BOOK-0008). Independent roadmaps supported by Cagan on roadmap myths (SRC-POST-0026), Spotify squad model (SRC-POST-0027).

**[R]** The "roadmap hierarchy" model: strategic themes at the top (company-level, "we're investing in X, Y, Z"), team roadmaps at the bottom (specific initiatives). Themes provide coherence without false precision. Teams own execution within thematic bounds.

### CON-0013: PM as Builder vs PM as Multiplier

*Is the PM primarily a builder deeply involved in creation, or a multiplier who enables others?*

**[E]** Evidence: Builder model supported by Shreyas Doshi on PM craft (SRC-POST-0028), Lenny's Podcast interviews (SRC-POST-0029). Multiplier model supported by Cagan on cross-functional teams (SRC-BOOK-0001), John Cutler on PM leverage (SRC-POST-0030).

**[R]** The Academy's provisional position: this IS a career stage progression. PMs start as builders (early career, small teams, technical products). As they advance to Principal+, they shift toward multiplier while retaining enough builder capability to maintain credibility. The failure modes are symmetric: "builder bottleneck" (PM doing work engineers should own) vs "facilitator emptiness" (PM adding no unique value beyond meeting scheduling). See `handbook/PRINCIPAL_PM_PLAYBOOK.md` Section 1.2.

## 9.2 How to Use the Contradictions

**[R]** The contradictions are not intellectual exercises. They are practical decision frameworks:

1. **When facing a decision that fits a contradiction:** Identify which contradiction applies. Identify whether your context more closely matches Context A or Context B. That gives you a provisional direction.
2. **When the context is ambiguous:** Invest in clarifying the context before committing to a direction. The contradiction tells you what context variables matter.
3. **When you're persistently on one side of a contradiction:** Ask whether you're applying the right framework for your context or applying your preferred framework regardless of context.
4. **When the organization is stuck:** The contradiction may explain the stuckness — different stakeholders are operating from different sides of the same tension without acknowledging it. Making the tension explicit can unlock progress.

## 9.4 Case-Specific Applications of the Contradictions

**[R]** The contradictions are best understood through cases. The Academy's case catalog (`07_cases/case_catalog.md`) provides detailed analysis. Key case-contradiction mappings:

| Case | Primary Contradiction | What the Case Teaches |
|------|----------------------|-----------------------|
| CASE-0001 (Netflix Qwikster) | CON-0002 (Discovery vs Conviction) | Hastings's strategic conviction about DVD/streaming unbundling was conceptually correct but executionally wrong — the customer's mental model mattered more than strategic logic |
| CASE-0002 (iPhone) | CON-0002 (Discovery vs Conviction), CON-0007 (Experimentation vs Judgment) | Jobs's conviction produced the iPhone — no amount of customer discovery would have revealed the opportunity. But this is the exception, not the rule |
| CASE-0003 (Google Reader) | CON-0009 (Responsiveness vs Vision) | Google's strategic focus ("more wood behind fewer arrows") led to killing a beloved product. The tension: serving a passionate user base vs serving strategic priorities |
| CASE-0004 (Microsoft Transformation) | CON-0003 (Founder vs Professional), CON-0006 (Speed vs Quality) | Nadella's professional product leadership reversed 30 years of founder-era strategy. The transformation required both speed (kill Windows Phone) and quality (rebuild developer trust) |
| CASE-0005 (Knight Capital) | CON-0006 (Speed vs Quality), CON-0011 (Human-in-Loop) | The definitive case for why speed without assurance kills. In financial systems, quality IS speed — one catastrophic failure erases all speed advantages |
| CASE-0006 (Slack Platform) | CON-0005 (Platform vs Workflow) | Slack chose bot-first over directory-first platform paradigm — an opinionated platform approach that proved commercially successful |

## 9.5 How the Contradictions Evolve

**[I]** The contradictions register is not static. As the field evolves, some contradictions may resolve:

- **CON-0006 (Speed vs Quality)** may partially resolve as AI-assisted testing and deployment reduce the cost of assurance, making the elite performer pattern (fast AND stable) more achievable
- **CON-0013 (Builder vs Multiplier)** may resolve as the field converges on a career-stage model: builder early, multiplier later, with the best product leaders retaining builder capability at any level
- **CON-0011 (Human-in-the-Loop)** will evolve rapidly as AI capabilities improve and governance frameworks mature — the boundary between "needs a human" and "safe to automate" shifts with model capability

**[R]** The Academy reviews the contradictions register quarterly. When a contradiction shows signs of resolution (consensus emerging, evidence accumulating on one side), the register is updated to reflect the shift from open debate toward settled doctrine.

**[D]** Beyond the contradictions register, the Academy identifies open questions that the field has not settled:

1. At what organizational scale does the balance tip from empowered teams to central direction? (CON-0001)
2. Can "Founder Mode" (Paul Graham, 2024) be systematized for non-founders? (CON-0003)
3. What is the right framework for determining acceptable error rates for full AI automation by domain? (CON-0011)
4. Can AI-assisted testing and review meaningfully reduce the speed-assurance trade-off? (CON-0006)
5. How do you develop product judgment systematically rather than relying on innate ability? (CON-0007)
6. How does the build-vs-buy calculus change with AI-assisted development reducing build costs? (CON-0010)
7. Is the builder-multiplier tension actually a career stage progression? (CON-0013)

**[R]** The Academy does not claim to answer these questions. It frames them so that practitioners can answer them for their specific context — and contribute their answers back to the evidence base.

---

# Part 10: Personal Application

## 10.1 How to Use This Bible

**[R]** The Product Leadership Bible is designed as a reference, not a textbook. You should not read it cover to cover. You should reach for it when you face a specific product leadership challenge.

**For decision-making:** Start with Part 2 (Core Doctrine) to identify which principles apply to your decision. Then Part 3 (Decision-Making Under Uncertainty) for the frameworks. Then Part 5 (Product Archetypes) if your product context matters.

**For capability development:** Start with Part 1 (Foundation) to understand your level. Then Part 8 (Principal+ Leadership) if you're making a level transition. Then the level-specific playbooks (`PRINCIPAL_PM_PLAYBOOK.md`, `AI_PM_PLAYBOOK.md`).

**For strategic questions:** Start with Part 4 (Resource Allocation) if you're allocating resources. Part 9 (Contradictions) if you're navigating a tension. Part 7 (Industry Contexts) if your industry creates specific constraints.

**For personal application:** Use the Personal Lab (`12_personal_lab/`) to apply doctrine to your own initiatives. The Bible provides the doctrine; the Lab provides the application.

## 10.2 Decision Walkthroughs: Using the Bible in Practice

### Walkthrough 1: Deciding Whether to Enter a New Market

**Situation:** Your product is successful in the US mid-market. The board is asking whether you should enter the European market. This is a Type 1 decision (one-way door — entering a market is hard to reverse).

**Bible-guided approach:**

1. **PRN-0002 (Strategy Is Exclusion):** Is "enter Europe" within your strategy or does it dilute it? Apply the Strategy Exclusion Test: what would you NOT do to fund European expansion? If the answer is "nothing — we'd stop nothing," the strategy doesn't have real exclusion.

2. **PRN-0003 (Cost of Delay):** Is there a market window closing? If yes, speed matters. If no, thorough analysis is appropriate for this Type 1 decision.

3. **PRN-0004 (PMF Is a Condition):** Do you have evidence that the European market needs your product? PMF in the US does not guarantee PMF in Europe. The product, pricing, and go-to-market may need significant adaptation.

4. **PRN-0007 (Reversible by Design):** Can you enter Europe in a way that's reversible? Partner with a local distributor rather than building your own sales team? Launch in one country rather than the whole continent? Phased entry creates optionality.

5. **PRN-0010 (Org Design Is Product Design):** Does your current organizational structure support European expansion? Do you have people who understand European markets, regulations, and customer behavior? If not, the organizational change must precede or coincide with the market entry.

6. **Decision Framework 1 (One-Way/Two-Way Door):** Classify sub-decisions. "Enter Europe" is Type 1. "Which country first?" is Type 1. "What pricing model?" is Type 2 (can be changed). "What marketing message?" is Type 2.

7. **Decision Framework 8 (FMEA):** Pre-mortem — "We entered Europe and failed. Why?" List failure modes: regulatory complexity underestimated, localization costs exceeded budget, European competitors responded aggressively, US-centric product didn't meet European needs, currency fluctuation, GDPR compliance costs.

8. **Industry Overlays (Part 7):** If your product falls under EU regulations (GDPR, EU AI Act, Digital Services Act), regulatory compliance is a product requirement, not an afterthought.

9. **Contradictions (Part 9):** CON-0001 (Autonomy vs Central Direction) — does the European team get full autonomy or operate under US direction? CON-0010 (Build vs Buy) — do you build a European operation or acquire/partner?

**Bible-guided output:** A decision memo covering: recommended approach (country-by-country phased entry with local partner), risks (regulatory, competitive, cultural), mitigations (hire local leadership before launch, partner for distribution, regulatory audit before committing), success criteria (3-country pilot with revenue targets), reversal trigger (if 2 of 3 pilot countries fail to achieve targets within 12 months, reconsider European strategy).

### Walkthrough 2: Deciding Whether to Sunset a Product

**Situation:** You have a product with 2,000 active users, declining 15% year-over-year. It consumes 3 engineers at 40% each for maintenance. New strategic initiatives need those engineers.

**Bible-guided approach:**

1. **PRN-0002 (Strategy Is Exclusion):** Is this product part of your strategy? If you were starting from scratch today, would you build it? If not, it's a sunset candidate.

2. **PRN-0004 (PMF Is a Condition):** Has this product lost PMF? Calculate the Sean Ellis score ("very disappointed" if unavailable). If below 40%, PMF has decayed.

3. **Decision Framework 3 (Sunset Decision Framework):** Run through the four gates:
   - Gate 1 (Strategic Fit): Does this serve current strategy? (Probably no)
   - Gate 2 (User Impact): 2,000 users. What's their profile? (Emotionally attached power users? Utility users with no loyalty?)
   - Gate 3 (Trust Cost): Will killing this product damage trust in your OTHER products? (CASE-0003: Google Reader teaches that trust damage can outlast the product)
   - Gate 4 (Reversibility): Can you transition rather than kill? (Open-source, transfer to partner, maintenance mode?)

4. **PRN-0007 (Reversible by Design):** Even sunsetting should be designed for reversibility. Keep the code. Keep the data export capability. If market conditions change, you want the option to revive — even if you never use it.

5. **Decision Framework 5 (Strategy Cascade):** If this product is sunset, what happens to the users' workflow? Is there a migration path? If not, you're leaving users stranded — trust cost is high.

6. **CASE-0003 (Google Reader):** What did Google do wrong that you should do right? Graceful sunset: data export, extended transition period, migration path to alternatives, honest communication about why. Google did none of these — and the trust damage persists a decade later.

**Bible-guided output:** A sunset plan covering: transition timeline (6 months), data export tool (1 month to build), recommended alternatives (identify 3 products users can migrate to), communication plan (explain the "why" not just the "when"), trust preservation measures (this doesn't mean we'll kill other products), and the explicit decision that makes the resource trade-off visible.

### Walkthrough 3: Deciding on an AI Feature

**Situation:** Your enterprise SaaS product has a feature request backlog of 200+ items. The CTO wants to "use AI to auto-triage and prioritize feature requests based on customer impact."

**Bible-guided approach:**

1. **Part 6 (AI Product Leadership) and AI_PM_PLAYBOOK.md:** Apply the AI Decision Sequence (Section 9.2).

2. **Workflow Selection:** Describe the workflow without AI. Who does triage? Product managers. What do they do? Read feature requests, assess customer impact, estimate effort, align with strategy, prioritize. This is LOW determinism (requires strategic judgment), MEDIUM error tolerance (wrong prioritization wastes engineering time but isn't catastrophic), HIGH automation value (200+ requests, PM time is expensive). AI is in the DANGER ZONE for this workflow — low determinism but high automation value is tempting and risky.

3. **Anti-pattern check (AI PM Playbook Section 2.2):** Anti-pattern 4 — the task requires causal reasoning, not pattern matching. Prioritization requires understanding strategy (what are we NOT building?), competitive dynamics, and organizational constraints. AI can pattern-match ("similar requests were prioritized in the past") but cannot reason strategically.

4. **PVS-TNA Assessment:** PVS is likely high (frequent, painful, strategically aligned). But TNA is low — this is a low-determinism task. The PVS-TNA matrix says this is a HIGH-RISK BET — only proceed with exceptional PVS and credible research path.

5. **Better approach:** Don't use AI to prioritize. Use AI to AUGMENT the PM's prioritization process: summarize and cluster similar requests, surface requests from high-value customers, identify requests that touch strategic product areas, estimate engineering effort based on similar past work. The AI is an input to PM judgment, not a replacement for it.

6. **Evaluation contract:** If you proceed, define success not as "did the AI prioritize correctly?" (you can't measure that) but as "did the PM make better prioritization decisions with AI assistance than without?" Measure: decision time, decision consistency across PMs, retrospective accuracy (were the AI-flagged high-impact requests actually high-impact?).

7. **Trust architecture (AI PM Playbook Section 7):** PMs need to trust the AI's input without over-relying. Show the AI's confidence in each recommendation. Show the reasoning behind each recommendation. Let PMs override. Track override rate — if it's high, the AI isn't adding value.

**Bible-guided output:** Recommend AGAINST AI-driven prioritization (low determinism, high strategic judgment requirement). Recommend FOR AI-assisted prioritization (clustering, impact estimation, effort estimation). Build as a decision support tool, not a decision-making tool.

## 10.3 The Evidence Taxonomy in Practice

**[R]** Every claim in this Bible is labeled. When you apply it to a decision:

- **[E]** claims are the most reliable — but check whether the evidence applies to your context
- **[P]** claims are widely held but not verified — test them in your context before betting on them
- **[I]** claims are reasonable but unproven — treat them as hypotheses, not facts
- **[D]** claims have no settled answer — you must decide for your context
- **[R]** claims are practical recommendations — apply with judgment, not as rules

The most common Bible misuse is treating [P] or [I] claims as [E] claims — assuming practitioner consensus or logical inference is the same as verified evidence. The second most common: treating all [E] claims as universally applicable. Evidence from consumer products may not apply to enterprise. Evidence from US markets may not apply to European. Evidence from 2020 may not apply in 2026 with different technology and market conditions.

## 10.4 How to Read the Evidence Labels Critically

**[R]** When you see an [E] label, ask:
1. What is the source? (Book? Academic paper? Case study? Industry report?)
2. What is the context? (Company stage, industry, product type, geography, era)
3. How strong is the evidence? (Correlation or causation? Sample size? Replication?)
4. Does the evidence transfer to my context? (Same stage? Same industry? Same constraints?)

When you see a [P] label, ask:
1. How wide is the consensus? (One prominent voice? General agreement? Contested?)
2. What incentives might shape this consensus? (Are practitioners incentivized to believe this?)
3. Has anyone systematically tested this practitioner belief?

When you see an [I] label, ask:
1. What is the chain of reasoning? (Is each step valid?)
2. What alternative inference could explain the same evidence?
3. What would need to be true for this inference to be wrong?

When you see a [D] label, ask:
1. What would resolve this debate? (What evidence would both sides accept?)
2. What's my context, and which side does it favor?
3. Am I defaulting to one side for reasons other than my context? (Personal preference, organizational culture, career incentives)

## 10.5 Integration with the Academy

**[R]** This Bible is the synthesis layer of the Academy. It references but does not replace:

- **Core Doctrine** (`01_core_doctrine/`) — Full principle definitions with practice exercises
- **Decision Frameworks** (`01_core_doctrine/DECISION_FRAMEWORKS.md`) — Detailed framework instructions
- **Principal+** (`02_principal_plus/`) — Level-specific capability development
- **Archetype Catalog** (`04_product_archetypes/archetype_catalog.md`) — Full archetype descriptions
- **AI Product Management** (`05_ai_product_management/`) — Detailed AI methodology
- **Industry Overlays** (`06_industry_overlays/`) — Industry-specific guidance
- **Cases** (`07_cases/case_catalog.md`) — Decision case studies
- **Contradictions** (`08_contradictions/register.yaml`) — Full contradiction register
- **Personal Lab** (`12_personal_lab/`) — Portfolio application

Use the Bible to navigate the Academy. When a topic requires deeper treatment, follow the references to the source modules.

## 10.6 The Bible as a Living Document

**[R]** This Bible is not static. It should be updated:

- **Quarterly:** Review for new evidence, new cases, and refined doctrine
- **When a contradiction resolves:** If the field reaches consensus on a previously open question, update Part 9
- **When a principle is revised:** If evidence or practice shifts, update Part 2
- **When a new industry overlay is added:** Update Part 7
- **When the Personal Lab applications reveal patterns:** Update Part 10
- **When a new major case is documented:** Add to the case catalog and cross-reference in relevant sections

**[I]** The Bible's update cadence reflects the Academy's evidence philosophy: doctrine should evolve as evidence accumulates. A Bible that doesn't reflect current evidence is worse than no Bible — it provides false confidence. The most dangerous product leadership resource is an outdated one.

## 10.7 Contributing to the Bible

**[R]** If you apply Bible doctrine and discover something that contradicts, extends, or refines it:

1. Document the finding with: (a) What doctrine was applied, (b) What context (company, product, stage, industry), (c) What happened, (d) What was learned
2. Classify the evidence strength: case study (n=1), pattern (n=3+), systematic observation (n=20+)
3. Submit through the Academy's Contribution Protocol (`12_personal_lab/`, module 12.7)

The Academy's doctrine improves through application. The Bible is the synthesis of what the Academy knows; the contribution protocol is how the Academy learns.

---

*The Product Leadership Bible was synthesized from the Product Leadership Academy's full doctrine as of 2026-08-01. It reflects the Academy's commitment to distinguishing evidence from inference, certainty from debate, and principles from preferences. Use it to make better product decisions — and to know when you don't know enough to decide.*
