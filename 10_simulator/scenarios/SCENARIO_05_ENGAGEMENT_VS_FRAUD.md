# Scenario 05: Engagement Up 40%. Fraud Up 15%. Now What?

| Field | Value |
|-------|-------|
| **scenario_id** | SIM-005 |
| **title** | Engagement Up 40%. Fraud Up 15%. Now What? |
| **leadership_level** | Senior PM, Principal PM, Director |
| **primary_tension** | Growth metric vs. risk metric |
| **key_capability** | Systems-level trade-offs |
| **estimated_time** | 40 minutes |
| **related_principles** | PRN-0005 (Platform Thinking), PRN-0009 (Metrics and Counter-Metrics), PRN-0011 (Ethics in Product Leadership) |

## Situation

You are **Director of Product for Consumer Payments** at **WavePay**, a fintech company providing person-to-person (P2P) payments, bill pay, and a digital wallet to 12 million active users. The company is Series D, valued at $2.1B, with $180M ARR. You lead a team of 5 PMs across the consumer product surface.

Six months ago, your team launched a major UX redesign of the P2P payment flow. The previous flow required 7 steps to send money to a friend (select recipient, enter amount, select funding source, review, confirm, authenticate, confirm again). The new flow reduced this to 3 steps (select recipient, enter amount, swipe to send). The redesign was a bet that reducing friction would increase engagement and transaction volume.

### The Numbers

The redesign has produced strong engagement metrics:
- **40% increase** in weekly active senders (people who send money at least once per week)
- **28% increase** in total P2P transaction volume (dollar amount)
- **35% increase** in daily active users of the payment feature
- **NPS improved** from 42 to 58
- User research shows customers describe the new flow as "effortless," "exactly what I wanted," and "finally, it just works"

The product team celebrated. The CEO highlighted the results at the last board meeting. The redesign was declared a success.

### The Other Numbers

Last week, your Risk and Compliance team delivered their quarterly fraud review. The results are concerning:

- **15% increase** in successful P2P fraud transactions (unauthorized transfers from compromised accounts)
- **22% increase** in social engineering fraud (scams where users are tricked into sending money — "friends and family" scams, fake seller scams, impersonation scams)
- **8% increase** in account takeover attempts
- **Fraud loss rate** increased from 0.32% of transaction volume to 0.41% — still within industry benchmarks (0.3-0.5% for P2P payments), but the trend is clear and accelerating
- The fraud operations team has grown from 12 to 18 analysts in 6 months just to keep up with case volume

The Risk team's analysis draws a direct causal link: the friction that was removed to improve engagement — the extra confirmation steps, the review screen, the second authentication — was also the friction that prevented fraud. Users who were slowed down by confirmation steps were more likely to notice they were being scammed. Fraudsters who had to bypass multiple security layers found the old flow harder to exploit.

Your Head of Risk, **Naomi Okonkwo**, put it bluntly: "You made it easier for everyone to send money. That includes fraudsters. The same friction you removed for legitimate users was protecting vulnerable users from themselves."

Naomi has proposed re-introducing friction for "high-risk transactions" — first-time sends to new recipients, transactions above $200, transactions initiated from new devices, and transactions that match known fraud patterns. Her proposal would:
- Re-introduce a confirmation step for high-risk transactions
- Add a delay (30-60 seconds) before high-risk transactions complete
- Display fraud warnings based on transaction characteristics
- Estimated to reduce fraud by approximately 30-40%
- Estimated to reduce engagement gains by approximately 5-10%

### The Deeper Tension

The VP of Growth, **Tomás Reyes**, is adamant that any re-introduction of friction is a mistake: "We spent 18 months fighting for this redesign. The engagement numbers are the best we've ever seen. If we start adding steps back, we're going to lose the momentum. Fraud is a cost of doing business — every payment company deals with it. Our fraud rate is still within industry benchmarks. We should invest in better fraud detection on the backend, not add friction back to the user experience."

Tomás has a point. The industry does accept a certain fraud rate as normal. And the backend fraud detection could be improved — your ML team has been asking for more investment in real-time fraud scoring models, which could catch fraud without adding user-facing friction.

But Naomi has a point too. The fraud that increased is not random — it disproportionately affects:
- Elderly users (3x more likely to be victims of social engineering fraud)
- New immigrants (targeted by impersonation scams claiming to be from immigration authorities)
- Financially vulnerable users (people living paycheck to paycheck for whom a $500 fraud loss is catastrophic)
- Non-native English speakers (who may not understand fraud warnings even when they are displayed)

Your user research team conducted follow-up interviews with 12 fraud victims. The stories are hard to read:
- A 74-year-old grandmother who lost $3,000 to a "grandparent scam" because the new flow was fast enough that she didn't have time to call her grandson and verify
- A recent immigrant who lost $800 to someone claiming to be from USCIS — in the old flow, the confirmation screen would have given him time to reconsider
- A college student who lost her rent money ($1,200) to a fake apartment listing — she said "it happened so fast I didn't even realize until the money was gone"

### The Organizational Context

- Tomás (VP Growth) is measured on engagement, transaction volume, and active users. The redesign is his signature achievement. His compensation is tied to growth metrics.
- Naomi (Head of Risk) is measured on fraud loss rate, regulatory compliance, and operational risk indicators. She has been warning about this since before the redesign launched.
- Your CEO, **Elena**, has been publicly championing the redesign. At the last all-hands, she called it "proof that we can innovate on experience while maintaining trust."
- The board has been pushing for growth metrics in preparation for a potential IPO in 24 months.
- Regulators (CFPB) have been increasingly focused on P2P fraud, especially scams. A consent order or enforcement action would be devastating to the IPO timeline.

## Characters

**Tomás Reyes (VP Growth).** Led the redesign. Sees it as his career-defining work. Views fraud as a "risk management problem, not a product problem." Believes growth momentum is fragile and must be protected. Motivated by: growth metrics, career advancement, being right about the redesign.

**Naomi Okonkwo (Head of Risk).** Former fraud investigator at a major bank. Has seen what happens when growth outpaces risk controls. Is not alarmist — her proposals are data-driven and measured. But she is increasingly frustrated that risk concerns are treated as obstacles rather than design constraints. Motivated by: protecting users, regulatory compliance, being taken seriously.

**Elena (CEO).** Former product leader. Wants both growth and safety. Has not yet internalized that the redesign traded one for the other. Motivated by: IPO readiness, board confidence, company reputation.

**Your PM for Consumer Payments (Alex).** Built the redesign. Is proud of it but also disturbed by the fraud data. Caught between his achievement and his conscience. Has been unusually quiet in the last two team meetings. Motivated by: building things that help people, not building things that hurt them.

**Your User Research Lead (Jamila).** Conducted the victim interviews. Has the qualitative data that makes the fraud statistics human. Advocates for vulnerable user protection. Motivated by: user advocacy, research integrity.

## Constraints

- The redesign is live. Rolling it back would be a major reversal and a public admission that the redesign had negative consequences.
- Both engagement and fraud are trending. Waiting means more growth AND more fraud — the question is whether the growth is worth the fraud.
- Backend fraud detection improvements are possible but take 6-9 months to build and tune. They don't solve the problem of users being tricked into authorizing legitimate-seeming transactions.
- Regulatory risk is real but not immediate. CFPB actions take years. But once started, they are expensive and distracting.
- User trust, once lost, is very hard to recover.

## Your Role

You are Director of Product for Consumer Payments. You report to the VP of Product (who reports to the CEO). Tomás (VP Growth) and Naomi (Head of Risk) are your peers. You own the product surface — the UX, the flow, the feature set. You do not own fraud operations or growth marketing, but you are accountable for the outcomes of the product you manage.

## Response Format

### Part 1: Assumptions

Key areas: Can backend fraud detection adequately substitute for UX friction? Is the fraud increase temporary (fraudsters adapt, then defenses catch up) or permanent (the new attack surface is structural)? How many users are being harmed vs. how many are benefiting? What is the actual regulatory risk timeline? What would Tomás need to see to change his position?

### Part 2: Decision

Describe your decision with:
- **What you will do.** Specific product changes, timeline, measurement plan.
- **What you will NOT do.** What trade-offs you're explicitly making — e.g., "we will accept that engagement growth slows from 40% to 30%."
- **How you will resolve the Growth vs. Risk tension.** Not just "we'll compromise" but a specific mechanism for deciding what level of fraud is acceptable and what level is not.
- **Communication plan.** What you say to Tomás, Naomi, Elena, and your team.

### Part 3: Pre-Mortem

Assume your decision failed. 12 months later, it's worse. Write a pre-mortem with at least 3 distinct failure paths. Include at least one path where you over-corrected (added so much friction that engagement collapsed) and one where you under-corrected (the fraud rate kept climbing and CFPB opened an investigation).

---

## Scoring Rubric (Scenario-Specific)

### Systems-Level Thinking

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Treats engagement and fraud as separate problems. Proposes "improve fraud detection" without recognizing that the UX design IS the fraud surface. |
| 3 | Recognizes the trade-off: the friction that was removed was serving a risk function. Proposes a balanced approach with both UX changes and backend improvements. |
| 4 | Thinks in systems: the UX redesign changed the equilibrium between growth and risk. The new equilibrium has higher engagement AND higher fraud. The question is whether the new equilibrium is acceptable and sustainable, not whether we can tweak a button. |
| 5 | Identifies the incentive structures that created this situation: Tomás was rewarded for engagement, Naomi was measured on fraud but not included in the redesign, and nobody owned the trade-off. Proposes structural changes (a Growth+Risk product review, shared metrics between Growth and Risk teams, user vulnerability impact assessments for major UX changes). |

### Metrics and Counter-Metrics

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Focuses only on engagement metrics or only on fraud metrics. No attempt to define the acceptable trade-off space. |
| 3 | Defines both success metrics (fraud reduction) and counter-metrics (engagement preservation). Defines acceptable ranges for both. |
| 4 | Defines segment-specific metrics: the aggregate fraud rate may be acceptable, but the fraud rate for vulnerable user segments may be unacceptably high. Proposes segment-level monitoring and thresholds. |
| 5 | Designs a composite metric that captures the trade-off (e.g., "net user value" = engagement gain minus fraud loss, both in dollar terms, with fraud loss weighted higher for vulnerable segments). Defines ownership for each metric and an escalation path if thresholds are breached. |

### Ethical Reasoning (Who Bears the Risk?)

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Treats fraud as a statistical cost. "0.41% is within industry benchmarks" — ignores that the 0.41% is concentrated on vulnerable users. |
| 3 | Recognizes the distribution problem: aggregate metrics hide that harm is concentrated on specific populations. Proposes interventions targeted at those populations. |
| 4 | Engages with the ethical question directly: "When we reduce friction, we distribute the benefit broadly and the harm narrowly. When a redesign helps 4 million users save 10 seconds each but costs 500 vulnerable users their rent money, is that a good trade-off?" Does not assume the answer is obvious. |
| 5 | Proposes a framework for making this type of trade-off systematically: user vulnerability impact assessment as part of the design process, a "do no harm" threshold for vulnerable user segments that overrides aggregate metrics, and a governance mechanism (not a PM's judgment call) for deciding when the trade-off is acceptable. |

### Stakeholder Communication

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Frames the problem as "Tomás vs. Naomi" — picks a side and argues for it. |
| 3 | Brings Tomás and Naomi together with data. Presents both perspectives and facilitates a decision. |
| 4 | Reframes the conversation from "growth vs. risk" to "what kind of product are we building and for whom?" Positions the vulnerable user data not as an attack on the redesign but as information that can make the redesign better. |
| 5 | Prepares a recommendation for Elena that makes the trade-off visible at the CEO level: "Elena, we can have 40% higher engagement with current fraud levels, or 30% higher engagement with 25% lower fraud. This is a strategic choice about what kind of company we are. You need to make it, because it affects IPO readiness, regulatory risk, and brand positioning." |

---

## Facilitator Notes

**Common traps:**
1. Proposing "better fraud detection on the backend" as the sole solution — this ignores that many fraud types (social engineering, impersonation) involve users who are authorizing transactions they believe are legitimate. No backend system can detect that a user is being lied to on the phone.
2. Treating the fraud victims as "acceptable losses" because the numbers look good overall.
3. Proposing a full rollback — the redesign has real benefits for millions of users. The answer is likely more nuanced than "undo it."
4. Ignoring the regulatory dimension. The CFPB doesn't care about your engagement metrics. They care that vulnerable consumers are being harmed at increased rates.

**Discussion prompts:**
- Is there a level of fraud that would make you roll back the redesign entirely? What number?
- If you were one of the fraud victims, what would you want WavePay to do?
- How would you design the same 3-step flow if you had included Naomi's team from the beginning?
- Tomás says "fraud is a cost of doing business." Is he right? Under what conditions?
- What obligation does a payment product have to protect users from themselves?

**Related Academy Content:**
- [PRN-0009](../../01_core_doctrine/PRINCIPLES.md): Metrics and counter-metrics
- [PRN-0011](../../01_core_doctrine/PRINCIPLES.md): Ethics in product leadership
- [Framework 3](../../01_core_doctrine/DECISION_FRAMEWORKS.md): Pre-mortem protocol
