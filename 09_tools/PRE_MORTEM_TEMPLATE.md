# Pre-Mortem Template

## Purpose

A pre-mortem is a structured exercise where you imagine a decision, project, or initiative has failed — and then work backward to identify what went wrong. Unlike risk assessment (which asks "what could go wrong?"), a pre-mortem asks "it went wrong — why?" This shift in framing overcomes optimism bias and surfaces failure modes that standard risk analysis misses because they feel "unlikely."

The pre-mortem's primary output is not a list of risks — it's a set of early warning signals and mitigation actions that reduce the probability and impact of failure.

## When to Use

- Before making a significant commitment (major project, strategic bet, organizational change)
- Before launching a product or feature
- Before starting a quarter or planning cycle
- When a decision has high irreversibility (Type 1 decision)
- When a team is overly confident (the pre-mortem is a bias-correction tool)
- As a regular ritual (quarterly pre-mortems for the roadmap, pre-launch pre-mortems for major features)

## Template Structure

### 1. The Scenario

Define what you're pre-morteming: "It is [date, typically 12-18 months from now]. We [made this decision / launched this product / executed this plan]. It failed. The failure was visible to [stakeholders]. The consequences included [specific consequences]."

The scenario should be specific enough that participants can vividly imagine the failure. Vague scenarios produce vague pre-mortems.

### 2. Failure Narratives (3-5)

For each failure narrative:
- **Headline:** One-sentence summary of what went wrong
- **Causal chain:** Step-by-step description of how the failure unfolded. Start with the root cause and trace forward to the visible failure.
- **Why we didn't see it coming:** What blind spot, assumption, or organizational dynamic prevented early detection.
- **Who was affected:** Which stakeholders, customers, or metrics were impacted?
- **Severity:** On a scale of 1-5, how bad was this failure?

Each narrative should be specific to the situation. "The project was late" is not a failure narrative — "The compliance work uncovered a data model dependency that required 3 weeks of architectural refactoring, which delayed the RegionalOne feature by 5 weeks, which triggered the customer to open a formal RFP process with a competitor" is a failure narrative.

### 3. Common Root Causes

Pattern-match the failure narratives to identify common root causes:
- Was there a recurring assumption that appears in multiple narratives? (e.g., "we assumed the team could parallelize work that turned out to be sequential")
- Was there a recurring organizational dynamic? (e.g., "in each narrative, leadership pressure to ship caused the team to skip quality checks")
- Was there a recurring external dependency? (e.g., "in each narrative, a third-party API or partner was the point of failure")

### 4. Early Warning Signals

For each failure narrative, identify what you could have observed 4-8 weeks before the failure became obvious:
- **Leading metric:** What metric would have moved first? (e.g., "cycle time increasing from 12 days to 18 days")
- **Qualitative signal:** What would people have been saying? (e.g., "engineers reporting context-switching overhead")
- **External signal:** What would have happened outside the team? (e.g., "customer email response times increasing")

The goal is to identify signals that are observable, specific, and early enough to act on.

### 5. Mitigation Actions

For each early warning signal, define:
- **What we will monitor:** Specific metric or signal
- **How often we review it:** Cadence
- **Who owns it:** Named person
- **What triggers action:** Threshold or condition
- **What action we take:** Specific response

### 6. Assumption Inversion

For each key assumption in your plan:
- **Assumption:** What you're assuming will be true
- **Inversion:** What if the opposite is true?
- **Impact:** What happens to the plan if this assumption is wrong?
- **Detection:** How would you know the assumption is wrong? How quickly?

### 7. Reversibility Assessment

- What parts of this decision are reversible? At what cost?
- What parts are irreversible? Why?
- Can we make any irreversible parts more reversible? How?
- What is the "point of no return" — the moment after which reversal becomes prohibitively expensive?

---

## Filled Example: FinClear Platform Migration Pre-Mortem

### 1. The Scenario
It is March 2027 (15 months from now). We made the decision to defer the platform migration to Q4 2026 while prioritizing PSD3 compliance and the RegionalOne feature. The migration started in Q4 as planned but failed to deliver. The CTO has lost confidence in the platform modernization strategy. Two key engineers (Alex and one Cloud engineer) have left. Real-time processing is still not available, and 3 prospects who required it have chosen competitors. The migration is now estimated at "another 9-12 months" and the CEO has asked whether we should abandon the migration entirely and "just make the monolith work."

### 2. Failure Narratives

**Narrative 1: The Single Point of Failure Realized**
- **Headline:** Alex resigned 3 weeks into the migration after receiving an offer from a FAANG company, leaving no one who understood the reconciliation algorithm well enough to complete the migration.
- **Causal chain:** Alex had been working 55-hour weeks for 6 months (compliance → RegionalOne → migration). He was the only person who understood the matching algorithm. The migration required his deep expertise for the data model transformation. When he gave notice, we had no knowledge transfer plan because we had never treated his departure as a realistic scenario. The migration stalled for 8 weeks while we tried to hire a replacement. By the time a new senior engineer joined (10 weeks later), the migration context was lost and required 4 additional weeks of ramp-up. The migration timeline slipped by 4 months.
- **Why we didn't see it:** We treated Alex's retention as a "people problem" not a "business continuity risk." We had no bus factor mitigation plan. Alex had expressed frustration about context-switching but we interpreted it as normal engineer grumbling, not a retention signal.
- **Who was affected:** Engineering (lost institutional knowledge), CTO (migration delayed), prospects (real-time processing still not available), CEO (credibility with board).
- **Severity:** 5 (existential to the migration timeline)

**Narrative 2: Scope Creep Consumes the Migration**
- **Headline:** The migration scope expanded from "event-driven architecture for reconciliation" to "complete platform rewrite" as the architecture team identified additional modernization opportunities, turning a 4-month project into an undefined multi-quarter initiative.
- **Causal chain:** The CTO, frustrated by 18 months of deferred migration, treated the Q4 start as the opportunity to fix everything — not just the event system but also the API layer, the database schema, the deployment pipeline, and the monitoring infrastructure. Each addition was individually justified ("we're already touching this code, might as well fix it") but collectively they turned a focused migration into a platform rewrite. By month 3, the scope was 3x the original estimate and the end was not in sight.
- **Why we didn't see it:** The CTO's scope expansion was gradual and each addition seemed reasonable in isolation. The PM (you) was focused on RegionalOne delivery and didn't have bandwidth to push back on migration scope. The engineering team was excited about the modernization and didn't want to be the ones saying "no" to improvements.
- **Who was affected:** CTO (migration delivered nothing because it tried to deliver everything), engineering team (burnout from endless migration), prospects and customers (no value delivered).
- **Severity:** 4 (the migration consumed resources without producing outcomes)

**Narrative 3: The Migration Broke the Existing System**
- **Headline:** The migration's event-driven architecture introduced a subtle timing bug in the reconciliation algorithm that caused 0.3% of transactions to be double-counted, which was not detected for 6 weeks, resulting in $120K in customer billing errors and a loss of trust from the largest customers.
- **Causal chain:** The reconciliation algorithm had implicit timing assumptions that were encoded in the monolith's synchronous processing model. When ported to an event-driven architecture, transactions that arrived within 50ms of each other (previously serialized by the monolith) were processed concurrently, creating race conditions in the matching logic. The bug was subtle — it only affected transactions that met specific timing and data conditions (<0.5% of volume). Standard testing didn't catch it because test data didn't replicate production timing patterns. It was detected when a customer's finance team noticed discrepancies in their monthly reconciliation report.
- **Why we didn't see it:** The reconciliation algorithm's timing assumptions were implicit — they weren't documented because they were "obvious" to Alex (who wrote them) but invisible to the migration team. The testing environment didn't replicate production concurrency patterns.
- **Who was affected:** Customers (billing errors, trust erosion), finance team (120 hours of manual reconciliation to fix), engineering (credibility damage), sales (customer conversations about reliability).
- **Severity:** 4 (reputational damage and financial cost)

### 3. Common Root Causes
- **Alex as single point of failure:** Appears in Narratives 1 and 3. The team's knowledge was concentrated in one person. No mitigation plan existed.
- **Scope discipline failure:** Appears in Narrative 2. The migration was framed as "the big fix" rather than a focused, phased investment.
- **Implicit knowledge not made explicit:** Appears in Narratives 1 and 3. Critical system behavior was encoded in Alex's intuition, not in documentation or tests.
- **Success theater:** The organization had celebrated "committing to the migration" without investing in the conditions for its success (knowledge transfer, scope discipline, testing infrastructure).

### 4. Early Warning Signals

| Failure Narrative | Leading Metric Signal | Qualitative Signal | When It Would Have Been Visible |
|-------------------|----------------------|-------------------|----------------------------------|
| Alex resignation | Alex's working hours consistently >50/week for 8+ weeks | Alex says "I'm tired" or stops volunteering for new work | 4-6 weeks before resignation |
| Scope creep | Migration Jira tickets growing faster than completion rate | Engineers say "the scope keeps expanding" in retrospectives | 2-3 weeks into migration |
| Reconciliation bug | Reconciliation accuracy monitoring shows >0.1% anomalous results in staging | QA team reports "weird" edge cases that are hard to reproduce | 2-3 weeks after migration start (in staging) |

### 5. Mitigation Actions

| Early Warning | Monitor | Cadence | Owner | Trigger | Action |
|--------------|---------|---------|-------|---------|--------|
| Alex burnout risk | Weekly working hours, 1:1 sentiment | Weekly | PM | >50 hours/week for 4+ weeks, or negative sentiment in 2 consecutive 1:1s | Reduce Alex's active project load. Initiate knowledge transfer sessions (Alex → Jordan). Alert CEO. |
| Migration scope creep | Jira: tickets opened vs. closed per week, estimated vs. actual scope | Weekly | CTO + PM | Tickets opened >1.5x tickets closed for 3+ weeks | Scope freeze. CTO and PM jointly review all new tickets. Defer non-critical items to Phase 2. |
| Reconciliation accuracy | Automated reconciliation accuracy tests in staging (production-like concurrency) | Daily (automated) | Staff Engineer (or Alex replacement) | Accuracy <99.9% on any test run | Stop migration work. Investigate accuracy regression. Do not deploy to production until root cause identified and fixed. |

### 6. Assumption Inversion

| Assumption | Inversion | Impact if Wrong | Detection |
|------------|-----------|-----------------|-----------|
| Alex will stay through the migration | Alex leaves during the migration | Migration stalls, timeline slips 3-4 months | Weekly 1:1s, retention risk signals |
| The migration scope can be contained to 4 months | The migration scope expands to 8+ months | Resources consumed without outcomes; CTO credibility damaged | Weekly scope vs. progress tracking |
| The reconciliation algorithm ports cleanly to event-driven architecture | Implicit timing assumptions create subtle bugs | Customer-facing errors, trust damage | Production-like staging environment with concurrency testing |
| Jordan can ramp up on the migration architecture | Jordan lacks the systems architecture experience for event-driven design | Migration quality suffers; Alex overload increases | Jordan's velocity and code review feedback quality |

### 7. Reversibility Assessment
- **Reversible:** The migration is software — we can roll back to the monolith at any point. But the cost increases over time (the longer the migration runs, the more systems depend on the new architecture).
- **Irreversible:** The opportunity cost of the migration time (person-weeks spent on migration cannot be recovered). Customer trust if the migration causes errors (Narrative 3). Engineer burnout and potential attrition (Narrative 1).
- **Point of no return:** When the first customer-facing feature is built on the new event-driven architecture. Before that point, rollback is engineering work. After that point, rollback requires feature deprecation and customer migration. Define this point explicitly before the migration starts.
- **Reversibility improvement:** Phase the migration so no customer-facing features depend on the new architecture until Phase 2 (after the event system is proven stable). This keeps the point of no return in the future.

---

## Common Mistakes

1. **Pre-mortem as generic risk list.** "The project was late" is not a pre-mortem. It's a risk category. A pre-mortem tells a specific story with named characters, specific decisions, and causal chains.
2. **Pre-mortem as doom session.** The goal is not to feel bad about the plan — it's to identify specific, actionable mitigations. Every failure narrative should produce at least one early warning signal and one mitigation action.
3. **Only technical failure modes.** The best pre-mortems include organizational, political, and market failure modes — not just technical ones. "The VP of Sales promised a timeline we couldn't meet" is as valid as "the database migration caused data corruption."
4. **Pre-mortem without follow-through.** Identifying early warning signals is useless if nobody monitors them. The pre-mortem MUST produce an ongoing monitoring plan with named owners.
5. **One-time exercise.** A pre-mortem done once and filed away is useless. The early warning signals should be reviewed regularly. When signals trigger, the pre-mortem's mitigation actions should be executed.

## Dependencies

- [Decision Memo Template](DECISION_MEMO_TEMPLATE.md): The pre-mortem should be done before finalizing a decision memo.
- [Risk-Adjusted Value Assessment](RISK_ADJUSTED_VALUE_ASSESSMENT.md): Pre-mortem outputs feed into risk assessment.
- [Experiment Design Template](EXPERIMENT_DESIGN_TEMPLATE.md): Pre-mortem the experiment design before launching.
- [Framework 3: Pre-Mortem Protocol](../01_core_doctrine/DECISION_FRAMEWORKS.md): The Academy's canonical pre-mortem framework.
