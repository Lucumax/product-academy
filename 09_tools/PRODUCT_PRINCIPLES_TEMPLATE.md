# Product Principles Template

## Purpose

Product principles are the decision-making values that guide how a product organization makes choices. They are the answer to: "When we face a difficult trade-off with no obviously right answer, what values guide our decision?" Good principles are specific, actionable, and help teams resolve conflicts. Bad principles are generic ("we are customer-obsessed") and provide no decision guidance.

This template helps you define, pressure-test, and operationalize product principles for a team, product, or organization.

## When to Use

- Defining principles for a new product or team
- Refreshing principles that have become generic or ignored
- Aligning a growing organization around shared decision-making values
- Onboarding new team members (principles encode decision-making culture)
- Resolving recurring conflicts (good principles prevent the same disagreement from happening repeatedly)
- Scaling decision-making (principles enable teams to make aligned decisions without escalation)

## Template Structure

### 1. The Principle

State the principle as a specific, decision-guiding statement, not a value:
- **Good:** "We ship when the feature solves the customer's problem, not when it has every edge case covered. We fix edge cases based on data, not speculation."
- **Bad:** "We value speed."

### 2. What It Means

Explain the principle in practical terms. What behavior does it encourage? What behavior does it discourage? Provide 2-3 concrete scenarios where the principle would guide a decision.

### 3. What It Does NOT Mean

Every principle can be misinterpreted or taken to an extreme. Explicitly state what the principle does NOT mean:
- "This does NOT mean we ship broken software."
- "This does NOT mean we ignore edge cases — it means we prioritize the ones with evidence of impact."

### 4. The Trade-Off It Resolves

Every good principle exists because of a recurring tension. State the tension explicitly:
- "This principle resolves the tension between shipping quickly and shipping completely."
- "This principle resolves the tension between serving existing customers and pursuing new markets."

### 5. How to Apply It

Provide a decision-making heuristic:
- "When faced with a choice between [Option A] and [Option B], apply the principle by asking: [specific question]."
- "Before making a decision this principle would guide, consider: [specific factors]."

### 6. How We Know We're Violating It

What are the symptoms that we've drifted from this principle?
- Specific, observable signals (not "we're moving too slow" but "cycle time from spec to ship has increased >2x in the past 3 quarters")

### 7. Reversal Conditions

Under what conditions would this principle no longer apply?
- Market changes, product stage changes, organizational changes
- "This principle applies while we are pre-PMF. After PMF, it shifts to [modified version]."

### 8. Related Principles

How does this principle relate to other principles in your set? Are there tensions between principles? (If two principles conflict, that's a sign you need more specific guidance on how to resolve the conflict.)

---

## Filled Example: Product Principles for a Growth-Stage B2B SaaS Company

### Principle 1: Solve the Problem, Not the Request

**What it means:** When a customer or stakeholder asks for a feature, our job is to understand the underlying problem they're trying to solve — and then solve THAT problem in the best way we can, which may be different from what they requested. We don't say "no" to customers — we understand what they need and deliver value, even if the solution doesn't look like what they asked for.

**What it does NOT mean:**
- This does NOT mean we ignore customer requests. We take every request seriously as a signal of an underlying need.
- This does NOT mean we always build something different from what was requested. Sometimes the customer's requested solution IS the best solution.
- This does NOT mean we substitute our judgment for the customer's without validating. We test our interpretation with the customer before building.

**The trade-off it resolves:** The tension between being customer-responsive (building what customers ask for) and being strategically coherent (building a product with a clear value proposition, not a collection of requested features).

**How to apply it:** For every feature request, ask three questions: (1) What problem is the customer trying to solve? (2) Is this problem shared by other customers or segments? (3) What's the best way to solve this problem, given our product strategy and capabilities?

**How we know we're violating it:** The roadmap is a list of top-voted feature requests from the customer ideas portal. PMs describe their work as "building what customers asked for." Nobody can explain WHY a feature was prioritized beyond "customers wanted it."

**Reversal conditions:** If we enter a market where customer requirements are standardized (e.g., compliance features where the requirement IS the feature — "we need SOC 2 evidence collection"), the distinction between problem and request narrows. The principle still applies but the solution space is more constrained.

---

### Principle 2: Data Informs, Judgment Decides

**What it means:** We use data to understand what's happening, generate hypotheses, and evaluate outcomes. But data alone never makes the decision — human judgment, informed by data, does. We don't use data as a substitute for thinking, and we don't ignore data when it contradicts our intuition.

**What it does NOT mean:**
- This does NOT mean we can ignore data we don't like.
- This does NOT mean "we need more data" is a valid reason to delay a decision indefinitely.
- This does NOT mean every decision requires an A/B test. Some decisions are judgment calls informed by qualitative data, competitive context, and strategic reasoning.

**The trade-off it resolves:** The tension between data-driven decision-making (which can become analysis paralysis) and intuition-driven decision-making (which can become HIPPO — Highest Paid Person's Opinion).

**How to apply it:** Before making a decision, identify: (1) What data do we have? (2) What data would we LIKE to have? (3) What's the cost of waiting for more data vs. making the decision now? If the cost of waiting exceeds the value of the additional data, decide now and revisit when new data is available.

**How we know we're violating it:** Decisions are being made based on "I think" without reference to evidence. OR decisions are being delayed because "we need more data" when the data being requested would not actually change the decision. OR teams run A/B tests for decisions that could be made faster with qualitative research and judgment.

**Reversal conditions:** If we enter a market with severe information asymmetry (we know very little), data becomes more important relative to judgment. The principle shifts toward "prioritize data generation over judgment" until we have enough understanding for judgment to be reliable.

---

### Principle 3: Speed With Standards

**What it means:** We move fast, but we have non-negotiable quality standards that speed cannot override. For every project, we define the minimum quality bar before we start — and we don't ship below that bar, regardless of timeline pressure. The art is setting the right bar for each project: higher for irreversible decisions, lower for reversible experiments.

**What it does NOT mean:**
- This does NOT mean everything must be perfect before shipping.
- This does NOT mean quality standards are uniform — a payment security feature has different standards than a UI color change.
- This does NOT mean speed is more important than standards. The principle is that BOTH matter and the tension must be managed deliberately.

**The trade-off it resolves:** The tension between shipping quickly (competitive velocity, learning, momentum) and shipping safely (quality, reliability, trust).

**How to apply it:** For every project, define: (1) What is the minimum quality bar? (Performance, error rate, accessibility, security, UX consistency.) (2) Why this bar and not higher or lower? (3) Who approves shipping below the bar? (Requires explicit exception.)

**How we know we're violating it:** We're shipping features with known bugs that affect >5% of users. OR we're delaying launches by 3+ weeks for edge cases affecting <1% of users. The key signal is that nobody can articulate WHY the quality bar is set where it is — it's either "always this high" or "whatever we can get done by the deadline."

**Reversal conditions:** If we move into a regulated domain (healthcare, finance, compliance), the minimum quality bar rises across the board. The burden of proof shifts: we must justify why the bar is LOWER, not why it's higher.

---

### Principle 4: Own the Outcome, Not the Feature

**What it means:** Product teams are accountable for achieving outcomes (metrics that measure customer and business value), not for shipping features. A team that ships 10 features but moves no outcomes has failed. A team that ships 1 feature and moves the outcome has succeeded. We reward outcome achievement, not feature output.

**What it does NOT mean:**
- This does NOT mean features don't matter. Features are HOW we achieve outcomes. They're necessary but not sufficient.
- This does NOT mean teams are accountable for outcomes they cannot influence. A team's outcome must be something they can affect through their work.
- This does NOT mean teams are penalized for outcomes that don't move despite good decisions. We distinguish between "good decision, bad outcome" (learning, not failure) and "bad decision, bad outcome" (failure).

**The trade-off it resolves:** The tension between measuring what's easy (features shipped, velocity, on-time delivery) and measuring what matters (customer value, business impact, outcome movement).

**How to apply it:** Every project starts with an outcome hypothesis: "We believe that [feature/change] will cause [outcome metric] to move from [baseline] to [target] within [timeframe]." The project is evaluated on whether the outcome moved, not whether the feature shipped.

**How we know we're violating it:** Quarterly reviews focus on "what we shipped" rather than "what changed." PMs describe their impact in terms of features launched, not outcomes achieved. Teams are celebrated for shipping on time even when the feature had no measurable impact.

**Reversal conditions:** For infrastructure, platform, or technical quality work, the "outcome" may be internal (e.g., "reduce deployment time from 4 hours to 10 minutes") rather than customer-facing. The principle still applies — define the outcome, measure it, own it.

---

### Principle 5: Diversity of Input, Unity of Decision

**What it means:** We seek broad input before making decisions — from customers, cross-functional partners, team members with different perspectives. But once a decision is made, we commit to it fully. We don't re-litigate decisions unless new information emerges that would have changed the decision. We disagree and commit.

**What it does NOT mean:**
- This does NOT mean decisions are made by consensus. The decider (clearly identified) makes the decision after hearing input.
- This does NOT mean decisions are permanent. They should be revisited when new information emerges.
- This does NOT mean people who disagree should pretend they agree. "I disagree with the decision but I commit to making it work" is the expected behavior.

**The trade-off it resolves:** The tension between inclusive decision-making (which produces better decisions through diverse perspectives) and decisive execution (which requires commitment and alignment).

**How to apply it:** For every significant decision, answer three questions before the decision is made: (1) Who is the decider? (2) Who must be consulted before the decision? (3) What is the deadline for input? After the decision: (1) Who needs to be informed? (2) Under what conditions would we revisit this decision?

**How we know we're violating it:** Decisions are made by the highest-paid person without input. OR decisions are endlessly discussed without anyone making a call. OR decisions are made but people continue to argue about them in hallways and Slack channels. OR decisions are revisited at the first sign of difficulty rather than when new information emerges.

**Reversal conditions:** In crisis situations (security incident, major outage, regulatory deadline), the "diversity of input" phase compresses or is skipped. Unity of decision becomes even more important.

---

## Common Mistakes

1. **Principles as aspirations, not decision tools.** "We are customer-obsessed" doesn't help anyone make a decision. "When customer requests conflict with product strategy, we prioritize strategy because serving a focused set of customers well is better than serving everyone poorly" actually guides decisions.
2. **Too many principles.** If you have 10+ principles, nobody remembers them. Aim for 4-6 principles that cover the most common tensions your organization faces.
3. **Principles without tensions.** A principle that everyone agrees with is probably too generic. Good principles are slightly uncomfortable — they force a choice that some people would rather avoid.
4. **Principles as wall art.** Principles that are written once and never referenced in decisions are decoration. Reference principles in design reviews, decision memos, and retrospectives.
5. **Principles that conflict without resolution guidance.** If Principle A says "move fast" and Principle B says "be thorough," and there's no guidance on how to resolve the conflict, you haven't created principles — you've documented a contradiction without helping anyone navigate it.
6. **One set of principles for everything.** Principles may need to vary by product stage, team maturity, or market context. A pre-PMF startup has different decision principles than a mature enterprise product.

## Dependencies

- [Product Strategy Template](PRODUCT_STRATEGY_TEMPLATE.md): Principles should align with and support the strategy.
- [Contradiction Analysis Template](CONTRADICTION_ANALYSIS_TEMPLATE.md): Principles help navigate contradictions. Use contradiction analysis for tensions that principles don't resolve.
- [Evaluation Contract Template](EVALUATION_CONTRACT_TEMPLATE.md): Principles inform how teams are evaluated.
- [Core Doctrine: PRN-0001, PRN-0002, PRN-0003](../01_core_doctrine/PRINCIPLES.md): Many Academy principles can be adapted as organizational product principles.
