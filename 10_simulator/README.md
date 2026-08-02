# Practice Simulator

## Purpose

The Academy simulator puts you in real product leadership situations where there is no textbook answer. Each scenario presents a constraint-rich, context-sensitive dilemma that tests not whether you know frameworks, but whether you can exercise judgment under uncertainty.

## How the Simulator Works

### Scenario Structure

Each scenario file follows a fixed structure:

1. **Situation.** The context, company stage, product details, and the specific dilemma you face.
2. **Characters.** The people involved — their roles, goals, incentives, and relationships.
3. **Constraints.** Hard constraints (regulatory deadlines, runway, contracts) and soft constraints (team morale, organizational politics, technical debt).
4. **Your Role.** The position you occupy and the authority/limits that come with it.
5. **Response Format.** Every scenario expects the same three-part response.

### Three-Part Response Format

Every scenario response must include:

**Part 1 — Assumptions.** What you are assuming that is not explicitly stated. Good assumptions are specific, falsifiable, and labeled with confidence (high/medium/low). Poor assumptions are generic (e.g., "the team is competent"). Strong assumptions connect to the situation: "I'm assuming the regulatory deadline is non-extendable because fining authority has escalated twice in the past 18 months. Confidence: high."

**Part 2 — Decision.** What you will do, in what sequence, with what resources, over what timeframe. A decision is not a goal — it is an allocation of resources against a specific plan with a rationale for why this plan, not the alternatives. Weak decisions describe aspirations ("we'll balance both priorities"). Strong decisions describe commitments with trade-offs ("we will defer the migration for 8 weeks to meet the regulatory deadline, accepting that this delays platform velocity by one quarter, and we will communicate this cost to the executive team before the decision is final").

**Part 3 — Pre-Mortem.** Assume your decision was implemented and 12 months later it failed. What went wrong? Be specific about failure mechanisms, not vague ("the market changed"). The pre-mortem must identify at least 3 specific failure paths with early warning signals you would monitor.

### How to Use Scenarios for Deliberate Practice

**Solo practice (30-45 minutes per scenario):**

1. Read the scenario without looking at the rubric.
2. Write your three-part response. Time-box: 10 minutes for assumptions, 15 minutes for decision, 10 minutes for pre-mortem.
3. Score yourself against the rubric (see `SCORING_RUBRIC.md`).
4. Identify the specific capability dimension where you scored lowest.
5. Write a one-paragraph improvement plan for that dimension.
6. Re-do the scenario 2 weeks later and compare your responses.

**Pair practice (60 minutes):**

1. Both participants read the scenario independently and write responses.
2. Exchange responses and score each other's.
3. Discuss where scores diverged and why.
4. The conversation about scoring disagreements is often more valuable than the scenario itself.

**Group practice (90 minutes):**

1. Assign roles to participants (the PM, the VP, the CEO, the customer). Each participant reads the scenario from their character's perspective.
2. The PM presents their three-part response.
3. Each role-player challenges the response from their character's incentives.
4. The group scores the final response against the rubric.
5. Debrief: what did the role-playing reveal that the solo response missed?

**Cadence recommendation:**
- 1 scenario per week for Senior PMs building toward Principal
- 2 scenarios per week for Principal+ levels
- Rotate through all 10 scenarios, then re-do the lowest-scoring ones

### How the Scoring Rubrics Work

Each scenario includes a level-specific scoring rubric. The rubric evaluates your response across 11 dimensions (see `SCORING_RUBRIC.md` for full definitions):

| Dimension | What It Measures |
|-----------|-----------------|
| Problem Framing | Can you define the real problem, not just the presenting symptoms? |
| Stakeholder Analysis | Can you map who has power, who has interest, and who will resist? |
| Incentive Mapping | Can you articulate what each stakeholder wants and fears? |
| Alternatives Generation | Can you generate and evaluate multiple distinct options, not just two? |
| Evidence Planning | Can you specify what evidence would change your mind and how you'd get it? |
| Decision Quality | Is the decision specific, allocative, and connected to a rationale? |
| Resource Allocation | Does the decision specify who does what, when, and what they stop doing? |
| Metrics and Counter-Metrics | Do you define success AND failure signals, not just success? |
| Pre-Mortem Quality | Are the failure paths specific, mechanistic, and monitorable? |
| Reversal Conditions | Do you specify what evidence would trigger a change in approach? |
| Executive Communication | Can you communicate the decision's logic and trade-offs concisely? |

Each dimension is scored on a 1-5 scale, with the total score mapped to leadership levels:

| Score Range | Level | Interpretation |
|-------------|-------|---------------|
| 11-22 | Structured but shallow | Applies frameworks mechanically without contextual depth |
| 23-33 | Strong Senior PM | Shows context sensitivity, good alternatives, clear rationale |
| 34-44 | Principal | Demonstrates systems thinking, incentive depth, strong pre-mortem |
| 45-50 | Director | Shows organizational strategy, resource trade-offs across teams, executive communication |
| 51-55 | Executive | Orchestrates multi-stakeholder outcomes, creates strategic options, communicates upward effectively |

### What the Simulator Is and Is Not

The simulator IS:
- A tool for practicing judgment under uncertainty
- A way to surface your blind spots and default patterns
- A forcing function for structured thinking
- A conversation starter for mentoring relationships

The simulator is NOT:
- A certification or assessment tool
- A replacement for real experience
- A personality test
- A framework that always produces the "right" answer

There is no single correct answer to any scenario. The rubric rewards the quality of reasoning, not a particular outcome. Two opposite decisions can both score well if the reasoning is sound and the trade-offs are explicit.

## Scenario Catalog

| # | Scenario | Primary Tension | Key Capability Tested |
|---|----------|----------------|----------------------|
| 01 | Two Engineers, Three Demands | Resource scarcity vs. strategic trade-offs | Triage under constraint |
| 02 | Enterprise Request | Revenue vs. platform integrity | Strategic coherence |
| 03 | AI Severe Failures | Performance vs. harm in edge cases | Ethical trade-off reasoning |
| 04 | Sales Promise | Committed revenue vs. architectural reality | Cross-functional negotiation |
| 05 | Engagement vs. Fraud | Growth metric vs. risk metric | Systems-level trade-offs |
| 06 | Infrastructure Procurement | Runway vs. long sales cycles | Founder resource allocation |
| 07 | CEO AI Demand | Executive pressure vs. validated need | Upward management and influence |
| 08 | Shipping Without Outcomes | Output vs. outcome | Outcome-oriented thinking |
| 09 | Legacy Product Blocker | Profitable legacy vs. platform modernization | Platform strategy and migration |
| 10 | Services vs. Product | Short-term revenue vs. long-term defensibility | Founder/product strategy |

## Scenarios by Leadership Level

| Level | Primary Scenarios | Stretch Scenarios |
|-------|-------------------|-------------------|
| Senior PM | 01, 03, 05, 08 | 02, 07 |
| Principal PM | 01, 02, 03, 08 | 07, 09 |
| Director | 02, 05, 07, 08, 09 | 04, 10 |
| VP Product | 04, 07, 09, 10 | 06 |
| CPO/Founder | 06, 09, 10 | All |

## Related Academy Modules

- [Core Doctrine](../01_core_doctrine/PRINCIPLES.md) — foundational principles that inform scenario responses
- [Decision Frameworks](../01_core_doctrine/DECISION_FRAMEWORKS.md) — structured frameworks applicable to scenarios
- [Contradictions](../08_contradictions/) — unresolved tensions that appear across multiple scenarios
- [Cases](../07_cases/case_catalog.md) — real-world case studies that parallel these scenarios
