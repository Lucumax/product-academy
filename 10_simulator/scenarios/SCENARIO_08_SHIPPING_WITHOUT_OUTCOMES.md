# Scenario 08: Shipping Consistently, Outcomes Not Moving

| Field | Value |
|-------|-------|
| **scenario_id** | SIM-008 |
| **title** | Shipping Consistently, Outcomes Not Moving |
| **leadership_level** | Senior PM, Principal PM, Director |
| **primary_tension** | Output vs. outcome |
| **key_capability** | Outcome-oriented thinking and diagnosis |
| **estimated_time** | 40 minutes |
| **related_principles** | PRN-0001 (Empowered Teams), PRN-0004 (PMF as Condition), PRN-0009 (Metrics and Counter-Metrics) |

## Situation

You are a **Director of Product** at **Aptivance**, a B2B SaaS company providing customer education and training software to mid-market companies. The product helps companies create, deliver, and track employee training — compliance training, onboarding, skills development, product education. The company is 180 employees, $32M ARR, growing 8% year-over-year (industry average is 15-20%).

You lead the **Core Learning** product group — 3 product teams (12 engineers, 3 PMs, 3 designers) responsible for the learning management system (course authoring, content delivery, assessment, and reporting). This is the main product surface. You have been in this role for 22 months.

### The Numbers

Over the past 18 months, your teams have been executing well by every operational metric:

| Metric | 18 Months Ago | Today | Change |
|--------|--------------|-------|--------|
| Features shipped per quarter | 8 | 14 | +75% |
| Sprint completion rate | 72% | 91% | +19 pts |
| Bugs resolved within SLA | 78% | 94% | +16 pts |
| Deploy frequency | 2/month | 3/week | 6x |
| Cycle time (idea to ship) | 42 days | 19 days | -55% |
| Engineering satisfaction | 3.8/5 | 4.4/5 | +0.6 |
| Team predictability (on-time delivery) | 68% | 89% | +21 pts |

By any operational standard, this is a high-performing product organization. The teams have good velocity, high quality, strong morale. Your VP of Engineering regularly praises the "engineering culture" and "delivery excellence."

But business outcomes haven't moved:

| Metric | 18 Months Ago | Today | Change |
|--------|--------------|-------|--------|
| Net revenue retention (NRR) | 104% | 103% | -1 pt |
| Logo churn rate | 12% | 14% | +2 pts |
| Average seats per customer | 287 | 291 | +1.4% |
| Feature adoption rate (new features) | — | 22% | (measured last 12 months) |
| NPS | 41 | 39 | -2 pts |
| Win rate (competitive deals) | 34% | 31% | -3 pts |
| Average contract value | $42K | $43K | +2.4% |
| Expansion revenue (% of new ARR) | 28% | 24% | -4 pts |

In 18 months, despite shipping 75% more features with better quality and faster cycle times, the business is in effectively the same place — arguably slightly worse on the metrics that matter most.

### What You've Been Building

Over the past 18 months, your roadmap has been driven primarily by:
- Customer feature requests (top-voted items from the customer ideas portal)
- Competitive parity items ("Competitor X has this, we need it too")
- Sales enablement requests ("We're losing deals because we don't have Y")
- Incremental improvements to existing features (better search, faster loading, richer reports)

You've shipped a lot. But looking back at the last 18 months, you realize something uncomfortable: you can't point to a single feature and say with confidence "this moved the needle on revenue, retention, or adoption."

Some specific examples:
- Q3 last year: Shipped a "course recommendation engine" (based on 214 customer votes on the ideas portal). 22% of customers have enabled it. Of those, average course completions increased 4% — a positive but tiny effect.
- Q4 last year: Shipped "interactive video assessments" (a competitive parity feature). Win rate in deals where this was mentioned increased by 2% — within the margin of error. The feature took 12 person-weeks.
- Q1 this year: Shipped "advanced reporting dashboard" (a top sales request). Sales said it would "unlock enterprise deals." It didn't. The win rate for enterprise deals didn't move.
- Q2 this year: Shipped "bulk user import via API" (top-voted customer request with 312 votes). Adoption is 14%. The customers who use it love it. The customers who don't use it haven't asked for it.

The pattern is becoming visible: the team is building things that people ask for, but the things people ask for are incremental improvements, not drivers of business outcomes. The real problems — why are customers churning? Why is win rate declining? Why isn't expansion revenue growing? — are not being addressed by the roadmap.

### The Discovery Gap

You've started to realize that the team has optimized for delivery but under-invested in discovery. The PMs spend their time:
- Writing detailed specifications and acceptance criteria (60% of time)
- Managing backlog and sprint planning (20% of time)
- Communicating with stakeholders about what's shipping when (15% of time)
- Customer research, problem discovery, outcome definition (5% of time)

Your teams are excellent at building the right thing right (execution), but they're not spending enough time ensuring they're building the right thing (strategy/discovery).

### The Culture Problem

Your CEO, **Maya**, has started asking uncomfortable questions in quarterly business reviews:
- "We shipped 14 features this quarter. Which one moved retention?"
- "Our NPS is flat for 6 quarters. What are we doing about that?"
- "Our win rate against LearnCore is declining. Are we building the wrong things?"

Your peers in the executive team are losing confidence in the product organization. The VP of Sales has started saying things like "we need better features" without being able to articulate what "better" means. The VP of Customer Success has started building workaround solutions for customers because she doesn't trust the product roadmap to address retention problems.

Your PMs feel the pressure but don't know how to respond. They're doing what they've been asked to do — shipping features on time with high quality. They're good at their jobs. The system they're operating in is producing outputs, not outcomes.

### The Deep Question

This scenario is different from others. The question is not a single decision but a diagnosis and a plan:

1. **Diagnosis:** Why is a high-performing delivery organization not producing business outcomes?
2. **Intervention:** What do you change about how the product organization operates?
3. **Measurement:** How will you know if the intervention is working?

## Characters

**Maya (CEO).** Former VP of Customer Success. Knows the business metrics intimately. Increasingly frustrated that product investment isn't translating to business results. Has started asking sharper questions in reviews. Is not yet at the point of considering a change in product leadership, but that point is approaching if the trend continues. Motivated by: business outcomes, board confidence, not presiding over a slow decline.

**Your PM Team (Sandra, Owen, Keisha).** Three capable, hardworking PMs. Sandra is strongest on execution and process. Owen is strongest on stakeholder management. Keisha is strongest on technical depth. None of them has strong discovery skills. All of them are feeling defensive because they're working harder than ever and the feedback they're getting is "it's not enough." Motivated by: doing good work, career growth, not being blamed for systemic problems.

**VP of Engineering (Raj).** Proud of the engineering organization's performance. Points to the operational metrics as proof that engineering is doing its job. Has said: "My team is shipping faster with higher quality than ever. If the business outcomes aren't moving, that's a product strategy problem, not an engineering problem." Motivated by: engineering excellence, protecting his team, not being held accountable for outcomes he doesn't control.

**VP of Sales (Derek).** Sees product as a weapon in competitive deals. Has a mental list of "features we're losing on" but has never tested whether those features actually drive win rates. His requests are well-intentioned but unvalidated. Motivated by: hitting quota, having competitive talking points, closing the quarter.

**VP of Customer Success (Aisha).** Has the closest relationship with churning customers. Knows patterns in why customers leave but hasn't been able to get those patterns onto the product roadmap because they're not as "votable" as feature requests on the ideas portal. Motivated by: retention, customer health, not losing accounts she's worked hard to keep.

**Your Director Counterpart (Marcus, Director of Product for Platform).** Leads the platform and integrations team. His outcomes are slightly better (API adoption is growing, platform reliability is improving). Maya has started comparing your group to his. Motivated by: his own outcomes, not looking like he's part of the problem.

## Constraints

- You have authority over the Core Learning roadmap, team structure, and PM development.
- You cannot fire and replace all your PMs (and you shouldn't want to — they're good people who need different support).
- You have budget for training, tools, or a small headcount addition (e.g., a user researcher).
- The engineering team's delivery machine is working — you don't want to break what's working.
- Maya's patience is finite. You have maybe 2-3 quarters to show a change in trajectory.

## Your Role

You are Director of Product for Core Learning. You report to a VP of Product (who reports to Maya). You manage 3 PMs indirectly (they report to you). You set the roadmap, define the product strategy, and are accountable for the outcomes of your product group. This is your problem to solve.

## Response Format

### Part 1: Assumptions

Key areas: What is the root cause of the output-outcome gap? Is it a discovery problem, a strategy problem, a measurement problem, a team capability problem, or all of the above? Are the features you're building actually the wrong features, or are they the right features with poor go-to-market? What would the PMs say if you asked them "why aren't our features driving outcomes?" What has the organization been rewarding (output or outcome)?

### Part 2: Decision

Describe your plan with:
- **Diagnosis.** What do you believe is the root cause (or causes) of the output-outcome gap? Be specific — "we're not doing enough discovery" is insufficient. What exactly is broken in how the team decides what to build?
- **Intervention.** What specific changes will you make to how the product organization operates? Include: changes to the roadmap process, changes to PM role expectations, changes to success metrics, changes to team rituals.
- **90-day plan.** What happens in the first 90 days? What are you stopping, starting, and continuing?
- **How you'll measure success.** What will tell you in 6 months that the intervention is working?
- **Communication plan.** What do you say to Maya, to your PMs, to Raj, to Derek, to Aisha?

### Part 3: Pre-Mortem

Assume your intervention failed. 18 months from now, business outcomes still haven't moved, and Maya has lost confidence in the product organization. Write a specific pre-mortem. At least 3 distinct failure paths. One must involve the PM team's resistance to change. One must involve organizational dynamics (other departments not adapting). One must involve a flaw in your original diagnosis.

---

## Scoring Rubric (Scenario-Specific)

### Diagnosis Quality

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Surface-level diagnosis: "we're building the wrong things" without explaining why the wrong things are being built. |
| 3 | Identifies specific mechanisms: the roadmap is driven by feature requests (stated needs) rather than outcome discovery (latent needs); PM time allocation is skewed toward delivery over discovery; the organization rewards shipping (output) rather than outcomes. |
| 4 | Diagnoses the system, not just the symptoms: the incentives (PMs are rewarded for on-time delivery, not outcome improvement), the processes (the ideas portal is a demand-capture mechanism, not a discovery mechanism), the capabilities (the PM team has execution skills but not discovery skills). |
| 5 | Identifies the organizational design flaw: the company has built a feature factory. It optimizes for output (features, velocity, quality) and assumes that better output automatically produces better outcomes. The system is working exactly as designed — the design is the problem. |

### Intervention Design

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Proposes adding process: "we'll do more user research," "we'll add OKRs." No structural changes to how decisions are made. |
| 3 | Proposes concrete changes: rebalance PM time toward discovery (e.g., 30% discovery, 50% delivery, 20% stakeholder), introduce outcome-based quarterly planning (teams define success metrics before defining features), add a user researcher to the team. |
| 4 | Redesigns the operating model: shift from feature-request-driven roadmap to outcome-driven roadmap (teams are given outcomes to achieve, not features to build); change PM performance evaluation to include outcome measures; create a continuous discovery practice (weekly customer conversations, not quarterly research projects). |
| 5 | Changes the system at multiple levels: (1) team level — PMs are evaluated on outcome contribution, not feature delivery; (2) process level — the roadmap is organized around business problems, not feature lists; (3) organizational level — product strategy connects team outcomes to business outcomes, the ideas portal is reframed as a problem repository not a voting system, and stakeholder input is structured as outcome definition, not feature specification. |

### Change Management

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Announces changes top-down. Assumes people will adapt. No plan for resistance. |
| 3 | Communicates the "why" behind the change. Involves PMs in designing the new approach. |
| 4 | Anticipates resistance points: PMs may resist because discovery is harder and less comfortable than delivery; Raj may resist because "engineering delivery" was his success story; Derek may resist because outcome-driven roadmaps don't give him specific feature commitments for Q2. Designs specific approaches for each. |
| 5 | Makes the transition itself an outcome-driven experiment: "For the next two quarters, one team will operate in the new model while the other two continue as-is. We'll measure whether the new model produces better outcomes. If it does, we expand. If it doesn't, we learn." This de-risks the change and makes it evidence-based. |

### Metrics Redesign

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Proposes "measure outcomes" without defining what outcomes or how. |
| 3 | Defines specific outcome metrics (NRR, feature adoption depth, time-to-value for new customers) and leading indicators that predict them. |
| 4 | Creates a metrics hierarchy: business outcomes (NRR, win rate) → product outcomes (adoption depth, activation rate) → team metrics (discovery velocity, experiment velocity, decision quality). Each level connects to the level above. |
| 5 | Proposes a measurement system, not just metrics: who owns each metric, how often it's reviewed, what happens when a metric moves in the wrong direction, how the metrics system protects against Goodhart's law (when a measure becomes a target, it ceases to be a good measure). |

---

## Facilitator Notes

**Common traps:**
1. Blaming the PMs. The PMs are doing what the system rewards. If you change the system and they still can't adapt, then it's a people problem. But start with the system.
2. Proposing "we need a better strategy." Strategy matters, but this scenario is testing whether you can diagnose and fix the operating model, not whether you can write a better strategy document.
3. Adding process on top of process. "Mandatory user research for every feature" sounds good but will be gamed and bypassed if the underlying incentives still reward shipping.
4. Ignoring the cultural dimension. The company has celebrated shipping for years. Changing that culture is as important as changing the processes.

**Discussion prompts:**
- How do you know whether the problem is "we're building the wrong things" vs. "we're building good things but not telling a good enough story"?
- What would you do if one of your PMs says "I'm great at delivery and I don't want to do discovery"?
- How do you get Derek (VP Sales) to stop asking for specific features and start telling you about the deals he's losing and why?
- If Maya asks you "what's the single most important thing you're going to change?" — what do you say?
- Is this a product management problem, or is it a product leadership problem?

**Related Academy Content:**
- [PRN-0001](../../01_core_doctrine/PRINCIPLES.md): Empowered teams
- [PRN-0009](../../01_core_doctrine/PRINCIPLES.md): Metrics and counter-metrics
- [Framework 5](../../01_core_doctrine/DECISION_FRAMEWORKS.md): Continuous discovery framework
