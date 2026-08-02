# Product Strategy Template

## Purpose

A product strategy defines where you play, how you win, and why now — for a product, product line, or portfolio. It is the answer to: "Given our resources, capabilities, and market position, what is the coherent set of choices that maximizes our probability of achieving our goals?"

This is NOT a roadmap (which shows what you'll build and when) or a vision (which shows the aspirational future state). Strategy is the connective tissue between vision and execution — it explains WHY certain choices and NOT others.

## When to Use

- Defining strategy for a new product or major initiative
- Annual strategy refresh
- Responding to a significant market or competitive shift
- Aligning a team or organization around strategic choices
- Preparing for a board presentation or funding round
- When you realize your "strategy" is actually a prioritized feature list

## Template Structure

### 1. Strategy on One Page

Start with the answer, not the analysis. In 5-7 bullet points, state your strategy. Each bullet should be a choice:
- **Where we play:** Which markets, segments, and use cases?
- **Where we do NOT play:** Which markets, segments, and use cases are we explicitly excluding?
- **How we win:** What is our competitive advantage?
- **What we will NOT do:** What are we explicitly sacrificing?
- **Why now:** What makes this the right strategy at this moment?
- **Key metrics:** How will we know the strategy is working?

If you cannot summarize your strategy in 5-7 bullet points, it's not concise enough. If any bullet is vague ("we will be the best"), it's not specific enough.

### 2. Market and Competitive Context

- **Market structure:** What does the market look like? (Size, growth, concentration, buyer dynamics, value chain)
- **Competitive landscape:** Who competes? How? With what advantages?
- **Market shifts:** What is changing? (Technology, regulation, customer behavior, competitive dynamics)
- **Implications:** What do these shifts mean for our strategic choices?

### 3. Strategic Diagnosis

What is the fundamental challenge or opportunity the strategy must address? This is the "problem behind the problem." Examples:
- "We have strong product-market fit with SMB but cannot grow revenue per customer fast enough to support our cost structure."
- "Our core market is mature and growth has slowed to single digits. We need to find a second growth engine."
- "A well-funded competitor is entering our market with a platform play. We have 18-24 months before they become a credible threat."

A good diagnosis is specific, evidence-based, and creates clarity about what the strategy must accomplish. A bad diagnosis is generic ("we need to grow faster").

### 4. Strategic Choices

For each strategic dimension, state your choice and the alternatives you rejected:

**Where to Play:**
- Target customers: Who exactly? (Segment, size, industry, role, behavior)
- Use cases: What problems do we solve? What problems do we explicitly NOT solve?
- Geography: Which markets?
- Channel: Direct sales, self-serve, partnerships, marketplace?

**How to Win:**
- Value proposition: Why do customers choose us over alternatives?
- Competitive moat: What protects us? (Technology, network effects, data, brand, switching costs, scale economics, regulatory advantage)
- Key capabilities: What must we be excellent at? What can we be adequate at?

**What to Sacrifice:**
- Explicitly excluded: Customers, use cases, features, markets, revenue opportunities
- Why: The strategy logic for each exclusion

### 5. Coherence Logic

How do the strategic choices reinforce each other? A good strategy has internal coherence — the choices fit together and amplify each other. A bad strategy is a collection of independent choices that don't connect.

Example of coherence: "We target mid-market compliance teams (where to play) with AI-powered automation (how to win) because our AI capabilities enable us to deliver enterprise-grade compliance at mid-market prices, which competitors can't match (coherence). We explicitly do NOT target enterprise compliance teams because their requirements (on-premise deployment, custom integrations, dedicated support) would require capabilities that conflict with our AI-first, self-serve model (sacrifice + coherence)."

### 6. Phasing and Sequencing

Strategy is not just what you do — it's what you do FIRST:
- **Phase 1 (Now to X months):** What must be true before we can do Phase 2?
- **Phase 2 (X to Y months):** What does Phase 1 enable?
- **Phase 3 (Y to Z months):** What does Phase 2 enable?
- **Triggers between phases:** What determines when we move from one phase to the next?

### 7. Resource Allocation

What resources does this strategy require? What trade-offs does it force?
- Investment priorities vs. current allocation
- What stops or slows down
- Key hires needed
- Capital requirements

### 8. Risks and Reversal Conditions

- **Key assumptions:** What must be true for this strategy to work?
- **Biggest risks:** What could cause the strategy to fail?
- **Reversal conditions:** What evidence would cause us to change the strategy?
- **Monitoring plan:** How will we detect strategy failure early?

### 9. Communication Narrative

How do you communicate this strategy to different audiences?
- **To the team:** What does this mean for their work?
- **To executives/board:** What bet are we making and why?
- **To customers:** What does this mean for them?
- **To the market:** How do we position against competitors?

---

## Filled Example: MediCore Cloud Strategy

### 1. Strategy on One Page
- **Where we play:** Independent physician practices (5-50 physicians) in the United States seeking to modernize from legacy EHR systems or adopt their first integrated EHR + practice management platform.
- **Where we do NOT play:** Hospital systems (already served by Epic/Cerner), solo practitioners on Classic (we will maintain Classic for them but not invest in new features), international markets (regulatory complexity exceeds our current capabilities).
- **How we win:** AI-powered clinical workflow automation that reduces documentation time by 40% — the #1 pain point for independent practices — combined with an open API ecosystem that enables third-party innovation.
- **What we will NOT do:** Build every feature ourselves (platform strategy). Compete on price (premium positioning). Maintain feature parity with Classic (different products for different needs).
- **Why now:** Three tailwinds: (1) physician burnout from EHR documentation is at an all-time high, (2) AI capabilities for clinical documentation have matured rapidly in the past 18 months, (3) regulatory mandates (information blocking rules) are forcing practices to seek modern, interoperable systems.
- **Key metrics:** NRR >115%, NPS >55, Cloud ARR >$50M within 3 years.

### 2. Market and Competitive Context
- **Market:** 95,000 independent physician practices in the US. Total EHR market $15B, growing 5-7% annually. Independent practice segment is ~$4B, growing slowly but with high churn from legacy systems.
- **Competitors:** Epic and Cerner dominate hospitals. Athenahealth is the leading cloud EHR for independent practices (with 140K providers). Kareo and DrChrono serve smaller practices. Practice Fusion (now Veradigm) serves solo practices.
- **Shifts:** AI in clinical workflows, FHIR interoperability mandates, physician burnout driving demand for automation, consolidation of independent practices into larger groups.
- **Implications:** The window for establishing a modern, AI-first EHR platform is now. The competitors are either legacy (Epic/Cerner), mid-transition (Athenahealth), or under-invested (smaller players). A clear AI-first positioning can differentiate.

### 3. Strategic Diagnosis
MediCore has a profitable legacy product (Classic) that generates $40M ARR but is technologically obsolete and shrinking at 5% annually. We have a modern platform (Cloud) growing at 40% annually but at $18M ARR. The fundamental challenge: transition from a legacy cash-cow model to a modern growth platform without losing the revenue that funds the transition. The window is 3-5 years — after that, Classic's technology becomes unmaintainable and Cloud must be self-sustaining.

### 4. Strategic Choices

**Where to Play:**
- Target: Independent practices (5-50 physicians) who are either on a legacy EHR and actively seeking to switch OR new practices being formed (by younger physicians who expect modern UX)
- Use cases: Core clinical workflow (documentation, e-prescribing, lab orders, clinical decision support) + practice management (scheduling, billing, patient communications). Excluded: hospital workflow, specialty-specific workflows (beyond what the platform supports with configuration), revenue cycle management as a standalone service
- Geography: US only (regulatory complexity makes international expansion unattractive in the next 3 years)
- Channel: Direct sales (for practices >10 physicians) + self-serve (for practices 1-10 physicians) + channel partnerships with practice management consultants

**How to Win:**
- Value proposition: "The EHR that writes itself." AI-powered documentation that reduces physician documentation time by 40% — addressing the #1 cause of physician burnout.
- Competitive moat: (1) AI models trained on proprietary clinical documentation data from 25 years of Classic usage (anonymized, with customer consent), (2) Open API ecosystem — third-party developers build on our platform, creating switching costs, (3) Integrated practice management — unlike point solutions, we cover clinical AND financial workflow.
- Key capabilities: AI/ML for clinical documentation (must be excellent), EHR core workflow (must be excellent), practice management (must be good), patient engagement (can be adequate — leverage API ecosystem).

**What to Sacrifice:**
- Classic feature parity: Cloud will NOT replicate all 200+ niche Classic features. Practices that depend on niche Classic features will either adapt or stay on Classic.
- Solo practitioners: Cloud pricing ($600+/month) is 3x Classic pricing ($200/month). Solo practitioners who won't pay Cloud pricing stay on Classic.
- International: No international expansion for 3 years.
- Enterprise (hospital) sales: We will not build the on-premise deployment, custom integration, and dedicated support that enterprise hospital sales require.

### 5. Coherence Logic
Our AI-first strategy works because: (1) we have proprietary training data from 25 years of Classic usage that competitors cannot replicate, (2) independent practices feel the documentation burden most acutely (they don't have scribes or large support staff), (3) our open API ecosystem means we don't need to build every feature — third parties fill gaps, making the platform stickier, (4) our integrated clinical + practice management creates a data flywheel (clinical documentation improves billing accuracy, billing data improves clinical decision support).

### 6. Phasing and Sequencing
- **Phase 1 (Year 1): AI Documentation MVP.** Ship AI-powered clinical documentation (ambient listening + automated note generation). Target: 20 Cloud customers, 40% documentation time reduction. Requires: AI team hiring, clinical data access agreements, physician advisory board.
- **Phase 2 (Year 2): Platform Ecosystem.** Ship open API and app marketplace. Recruit 10+ third-party developers. Target: 50 Cloud customers, 5+ popular marketplace apps.
- **Phase 3 (Year 3): Migration Acceleration.** Ship Classic-to-Cloud migration tooling. Target: migrate 500 Classic customers. Classic revenue begins meaningful transition to Cloud.

### 7. Resource Allocation
- Year 1 investment: $8M incremental (AI team, cloud infrastructure, clinical validation)
- What slows down: Classic feature development (maintenance only), practice management enhancements (deferred to Year 2)
- Key hires: VP of AI/ML, 3 ML engineers, 2 clinical informaticists, Head of Platform Partnerships

### 8. Risks and Reversal Conditions
- **Key assumptions:** AI documentation can achieve 40% time reduction (medium confidence — prototype promising but not validated at scale). Independent practices will pay premium pricing for AI-powered EHR (medium confidence — early pilots positive but sample small). Third-party developers will build on our platform (low confidence — unvalidated assumption).
- **Biggest risks:** AI accuracy is insufficient for clinical use (patient safety risk). Cloud growth rate doesn't accelerate fast enough to offset Classic decline. Competitor (Athenahealth) launches comparable AI features.
- **Reversal conditions:** If AI documentation doesn't achieve >25% time reduction in 6-month pilot, reconsider AI-first positioning. If Cloud ARR growth rate drops below 30%, re-evaluate investment level. If Classic churn accelerates >10%/year, accelerate migration timeline.
- **Monitoring plan:** Monthly: Cloud ARR growth rate, Classic churn rate, AI documentation accuracy metrics. Quarterly: competitive intelligence review, strategy reassessment.

### 9. Communication Narrative
- **To the team:** "We're building the EHR of the future — one that reduces physician burnout instead of causing it. Our AI-first strategy is the biggest bet in the company's history. Here's what it means for your work..."
- **To the board:** "We have a 3-year window to transition from a legacy cash-cow model to a modern growth platform. Our AI-first strategy leverages our unique data advantage and addresses the #1 pain point in our market. The investment is $8M for $50M+ ARR potential."
- **To Classic customers:** "We are continuing to support and maintain Classic. For practices that want modern capabilities, Cloud now includes AI-powered documentation that reduces charting time by 40%. We'll help you migrate when you're ready."
- **To the market:** "MediCore is the first EHR with an AI that writes itself — because physicians should spend time with patients, not screens."

---

## Common Mistakes

1. **Strategy as vision statement.** "We will be the leading platform for X" is a goal, not a strategy. Strategy is about choices — where, how, what not to do.
2. **Strategy as feature list.** "We will build A, B, C" is a roadmap, not a strategy. Strategy explains WHY A and not D.
3. **No explicit exclusions.** A strategy that doesn't say what you're NOT doing is not specific enough. The test: can a PM use the strategy to say no to a good idea?
4. **Strategy as annual ritual.** Strategy that is written in January and never revisited is worse than no strategy because it gives the illusion of direction without the substance.
5. **Coherence by accident.** A list of independent choices is not a strategy — it's a preference list. The choices must amplify each other.
6. **Audience of one.** Strategy that only makes sense to the author is not useful. It must be communicable to the team, executives, and (in adapted form) customers.

## Dependencies

- [Product Thesis Template](PRODUCT_THESIS_TEMPLATE.md): Your thesis is a bet about the market. Strategy is the plan for winning the bet.
- [Resource Allocation Memo](RESOURCE_ALLOCATION_MEMO.md): Strategy drives allocation. Without resource allocation, strategy is aspiration.
- [Metrics Tree Template](METRICS_TREE_TEMPLATE.md): Strategy defines what success looks like. The metrics tree operationalizes it.
- [Executive One-Pager Template](EXECUTIVE_ONE_PAGER_TEMPLATE.md): For communicating strategy to executives concisely.
