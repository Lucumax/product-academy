# Contradiction Analysis Template

## Purpose

A contradiction analysis addresses a situation where two valid product leadership principles or goals are in irresolvable tension — where you cannot fully satisfy both and must navigate the tension rather than resolve it. It answers: "What do I do when the right principles point in opposite directions?"

The Academy's contradiction catalog documents known tensions (e.g., "customer revenue vs. product strategy," "speed vs. quality," "empowerment vs. coherence"). This template helps you apply those contradictions to your specific situation and design a navigation strategy.

## When to Use

- You're facing a decision where two "right" answers conflict
- Stakeholders are divided along principled lines (not just preferences)
- You're experiencing the tension between short-term and long-term optimization
- A framework or principle you believe in is leading you to a conclusion that feels wrong in this context
- You're designing an organizational process that must balance competing values

## Template Structure

### 1. The Tension

- **What are the two poles?** Describe the tension in specific terms: "The tension between [Principle A / Goal A / Value A] and [Principle B / Goal B / Value B]."
- **Why is this a genuine tension?** Why can't you fully satisfy both? (Resource constraints, time constraints, physics, organizational reality, market dynamics)
- **What makes this tension relevant now?** What specific situation or decision has surfaced the tension?

### 2. The Case for Pole A

Why would a reasonable, principled product leader choose Pole A?
- What principle, goal, or value does it serve?
- What evidence supports this choice?
- What are the stakes of NOT choosing Pole A?
- Who in the organization advocates for Pole A and why?

### 3. The Case for Pole B

Same structure as Pole A. The goal is to articulate BOTH positions as strongly as possible — if one side sounds like a straw man, you haven't understood the tension.

### 4. Why This Tension Cannot Be Resolved

- Why is there no permanent resolution? (The tension is structural, not temporary)
- What makes this a "polarity to manage" rather than a "problem to solve"?
- What happens if you optimize exclusively for one pole over an extended period?

### 5. Navigation Strategy

How will you navigate this tension in your specific situation?

- **Where on the spectrum do you position for NOW?** Not "balance" — a specific position with rationale. "In this quarter, we position at 70% toward Pole A because [specific reason]."
- **Under what conditions do you shift toward the other pole?** What triggers a repositioning?
- **What organizational mechanisms maintain the tension?** How do you prevent drift toward either extreme? (e.g., "The Risk team has veto power over changes that increase fraud by >5%" or "Every QBR includes a 'strategy coherence check' that reviews decisions against the product strategy.")
- **Who is the guardian of each pole?** Which person or team is responsible for advocating for each side of the tension? (Tensions managed by one person tend to collapse toward one pole over time.)

### 6. Communication Strategy

- **How do you communicate the navigation decision to stakeholders who advocate for the other pole?** What do you say to someone who believes you should have chosen differently?
- **How do you prevent the tension from becoming a factional conflict?** (Us vs. them dynamics)

### 7. Monitoring and Adjustment

- **What metrics indicate you're too far toward one pole?** Leading indicators of imbalance
- **What is the review cadence?** When do you re-evaluate the positioning?
- **What would cause a fundamental re-evaluation of the tension itself?** (Market shift, organizational change, new evidence)

---

## Filled Example: Speed vs. Safety in Payment Product

### 1. The Tension
- **The two poles:** Speed to market (shipping features quickly to maintain competitive velocity and growth) vs. Safety and trust (ensuring features do not increase fraud risk or harm vulnerable users).
- **Why genuine:** The UX changes that improve engagement (reducing friction, removing steps, simplifying flows) are often the same changes that reduce protective friction (confirmation screens, warnings, delays). You cannot fully optimize for both speed/engagement and safety/fraud prevention simultaneously — they trade off.
- **Why relevant now:** Our P2P payment flow redesign increased weekly active senders by 18% but also increased fraud by 15%. The Growth team wants to preserve the gains. The Risk team wants to add friction back. Both are right. Neither is wrong.

### 2. The Case for Speed/Growth
A reasonable product leader would prioritize growth because:
- We are in a competitive market where speed of innovation determines market share. Competitors (Venmo, Cash App) are shipping new features quarterly.
- The 18% increase in weekly active senders represents real value for millions of users — faster, easier payments improve their lives.
- Fraud at 0.41% of transaction volume is within industry benchmarks (0.3-0.5%). The absolute fraud loss ($X/year) is less than the revenue gain from increased engagement ($Y/year).
- Growth metrics are what the board and investors care about in preparation for IPO.
- Advocate: Tomás (VP Growth), measured on engagement and transaction volume.

### 3. The Case for Safety/Trust
A reasonable product leader would prioritize safety because:
- The 15% fraud increase is not randomly distributed — it disproportionately harms vulnerable users (elderly, immigrants, low-income). Aggregate metrics hide this concentration of harm.
- User trust, once lost, is very hard to recover. A single high-profile fraud incident can damage the brand more than 18% engagement helps.
- Regulatory risk: CFPB is increasingly focused on P2P fraud. A consent order or enforcement action would be devastating to the IPO timeline.
- "Industry benchmark" fraud rates are not a moral justification — they're an average of companies that may also be under-investing in safety.
- Advocate: Naomi (Head of Risk), measured on fraud loss rate and regulatory compliance.

### 4. Why This Tension Cannot Be Resolved
This is not a temporary problem where we can "fix fraud and then go back to growth." Every future UX change that reduces friction will create this same tension. The core dynamic — what makes the product better for legitimate users also makes it better for fraudsters — is structural to any payment product. We cannot "solve" fraud and then ignore it. We cannot "solve" growth and then ignore it. The tension is permanent.

If we optimize exclusively for growth: fraud rate climbs, vulnerable users are harmed, regulators intervene, trust erodes, growth reverses. (See: multiple fintech companies that grew fast and imploded from fraud/regulatory issues.)
If we optimize exclusively for safety: UX becomes slow and burdensome, competitors with better UX take market share, growth stalls, IPO becomes impossible.

### 5. Navigation Strategy
- **Position for now (next 2 quarters):** 60% toward Safety, 40% toward Growth. Rationale: The fraud increase from the redesign is a new, un-modeled risk that needs immediate containment. We must demonstrate to ourselves, our customers, and potentially regulators that we can manage the risk before we push for more growth. Once we have proven fraud controls that work in the low-friction UX, we can shift toward Growth.
- **Shift conditions:** Shift to 50/50 when: (a) fraud rate returns to pre-redesign levels (0.32%) for 2 consecutive quarters, (b) fraud controls are proven to work without degrading UX for legitimate users by >5%, (c) no regulatory inquiries are active.
- **Organizational mechanisms:**
  - Monthly "Growth + Risk" review: Tomás and Naomi jointly review engagement and fraud metrics. Both must agree before any major UX change that removes friction.
  - Fraud guardrail: Any UX change affecting the payment flow must include a fraud impact assessment. If projected fraud increase exceeds 5%, the change requires VP Product approval.
  - Vulnerable user monitoring: Fraud metrics are segmented by vulnerability indicators (age, account age, transaction patterns). Thresholds are lower for vulnerable segments.
- **Guardians:** Tomás is the guardian of Growth. Naomi is the guardian of Safety. Both have explicit authority to escalate to the CEO if they believe the balance has shifted too far.

### 6. Communication Strategy
- **To Tomás:** "The 18% engagement gain proves the redesign works. Now we need to prove it works safely. Think of this as Phase 2 — we protect the gains by building the safety infrastructure that makes the growth sustainable. Growth without safety is temporary. Growth with safety is permanent. You and Naomi are partners in this, not opponents."
- **To Naomi:** "You were right that the redesign increased fraud, and your concerns are validated. Now we need your expertise to design fraud controls that work within the new UX paradigm — not just adding the old friction back, but inventing new, more targeted protections. You're not the obstacle to growth — you're the architect of sustainable growth."
- **Preventing factional conflict:** Tomás and Naomi will co-present the "Growth + Risk" review to the executive team quarterly. They share ownership of the outcome, not just their respective metrics. Neither can "win" at the expense of the other — their success is measured jointly.

### 7. Monitoring and Adjustment
- **Too far toward Growth:** Fraud rate exceeds 0.45% for 2 consecutive months. Vulnerable user fraud rate increases >20% quarter-over-quarter. Customer trust survey shows declining "I trust WavePay with my money" score.
- **Too far toward Safety:** Weekly active sender growth drops below 5% quarter-over-quarter. Transaction completion rate decreases >10%. User research reports "this is getting slow again."
- **Review cadence:** Monthly "Growth + Risk" review. Quarterly strategic re-evaluation of the 60/40 positioning.
- **Fundamental re-evaluation:** If a competitor launches a product that achieves BOTH higher engagement AND lower fraud (using AI/ML fraud detection that doesn't require UX friction), the tension itself may shift — safety may no longer require sacrificing speed. This would be a technological breakthrough, not a strategy change.

---

## Common Mistakes

1. **Framing one pole as bad.** If you describe Pole A as "the right thing to do" and Pole B as "what short-sighted people want," you haven't understood the tension. Both poles exist because they serve legitimate values held by reasonable people.
2. **Seeking permanent resolution.** Some tensions cannot be resolved — they must be managed. Trying to "solve" a permanent tension leads to oscillating between extremes (optimize for growth for 18 months, then panic and optimize for safety for 18 months, repeat).
3. **Fence-sitting as strategy.** "We'll balance speed and safety" is not a strategy — it's an aspiration. Strategy is deciding where on the spectrum you position NOW, under what conditions you shift, and what mechanisms prevent drift.
4. **No guardians.** Tensions managed by one person or one team tend to collapse toward one pole. Each pole needs an advocate with real authority — not a veto, but a voice that must be heard.
5. **Ignoring the organizational dynamics.** The tension isn't just philosophical — there are real people with real incentives on each side. If Tomás is compensated on growth and Naomi is compensated on safety, they will naturally pull in opposite directions. Acknowledging the incentive structure is more effective than wishing it away.

## Dependencies

- [Contradiction Catalog](../08_contradictions/): The Academy's catalog of known product leadership tensions.
- [Stakeholder Incentive Map](STAKEHOLDER_INCENTIVE_MAP.md): Understanding who advocates for which pole and why.
- [Decision Memo Template](DECISION_MEMO_TEMPLATE.md): For documenting the navigation decision.
- [Core Doctrine: Multiple principles](../01_core_doctrine/PRINCIPLES.md): Many Academy principles exist in tension with each other.
