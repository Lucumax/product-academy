# Post-Launch Review Template

## Purpose

A post-launch review extracts learnings from a completed launch — whether successful or not — and converts those learnings into organizational improvement. Unlike a retrospective (which focuses on process improvement) or a post-mortem (which focuses on failure), a post-launch review evaluates the full outcome: what we expected, what actually happened, why the gap exists, and what we'll do differently next time.

The primary audience is the product organization (PMs, engineering, design, leadership). The secondary audience is future teams who will make similar decisions and should benefit from your learnings.

## When to Use

- After a major feature, product, or initiative launch (any launch that consumed >10% of team capacity for >1 month)
- After a launch that significantly exceeded or missed expectations (both outcomes are learning opportunities)
- After a strategic bet, experiment, or pilot that was intended to inform future decisions
- Quarterly or annually as a portfolio review of launches
- When onboarding new team members (past post-launch reviews are excellent context)

## Template Structure

### 1. Launch Summary

- **What launched:** Specific description (not "the new onboarding" but "the 3-step P2P payment flow for experienced senders")
- **Launch date:** When it went to 100% of target users
- **Team:** Who built and launched it
- **Investment:** Approximate person-weeks and calendar time
- **Strategic intent:** Why we built this (the hypothesis or bet)

### 2. Expectations vs. Reality

The core of the review. Compare what you expected to what actually happened:

| Dimension | Expected | Actual | Gap | Explanation |
|-----------|----------|--------|-----|-------------|
| Primary metric | Target value and timeline | Actual value and timeline | Difference | Why the gap exists |
| Adoption/Usage | Expected adoption rate and pattern | Actual adoption rate and pattern | Difference | Why the gap exists |
| Quality/Reliability | Expected error rate, performance | Actual error rate, performance | Difference | Why the gap exists |
| Customer feedback | Expected sentiment and themes | Actual sentiment and themes | Difference | Why the gap exists |
| Business impact | Expected revenue/retention impact | Actual revenue/retention impact | Difference | Why the gap exists |

For each gap, distinguish between:
- **Estimation error:** We were wrong about the magnitude of the effect
- **Causal error:** We were wrong about what would cause the effect
- **Execution error:** We built the right thing but didn't execute well
- **Environmental change:** Something changed in the market or organization that affected the outcome

### 3. What We Got Right

What worked well? Be specific — not "the team did a great job" but "the decision to use a feature flag for the rollout allowed us to detect and fix a platform-specific bug before it affected all users." Include:
- Product decisions that proved correct
- Process decisions that enabled success
- Technical decisions that held up well
- Unexpected positive outcomes

### 4. What We Got Wrong

What didn't work? Be honest — this is where the learning happens. Include:
- Product decisions that proved incorrect
- Assumptions that turned out to be false
- Process breakdowns or inefficiencies
- Unexpected negative outcomes

### 5. Surprises

What happened that neither the optimists nor pessimists predicted?
- Positive surprises (things that went better than anyone expected)
- Negative surprises (things that went worse than anyone expected)
- Neutral surprises (things that were different in ways that didn't affect the outcome but are interesting)

### 6. Customer Impact

Beyond metrics, how did customers actually experience the launch?
- What did customers say? (Quotes from support tickets, social media, reviews, sales conversations)
- What did customers do? (Behavioral changes beyond the primary metric)
- Who benefited most? (Which customer segments saw the most value?)
- Who was negatively affected? (Which segments saw regression or confusion?)

### 7. Key Learnings

Distill the most important lessons — the ones that should change behavior on future launches:
- **Product learnings:** About the customer, the problem, the solution
- **Process learnings:** About how we build and launch
- **Organizational learnings:** About how we work across teams and functions
- **Strategic learnings:** About the market, competition, or business model

Each learning should be specific and actionable. "We should involve design earlier" is weak. "For any project where UX is a primary lever, the designer must be staffed from Day 0, not Day 14 — on this project, the late design involvement added 3 weeks of rework" is strong.

### 8. What We'll Do Differently

For each key learning, define a specific change:
- **What we'll change:** Specific change to process, practice, or policy
- **Who owns it:** Named person
- **By when:** Specific date or event
- **How we'll know it worked:** Success criteria for the change

### 9. Artifacts for Future Teams

What should future teams know about this launch?
- Key documents (decision memos, design docs, experiment results)
- People with institutional knowledge (who to talk to)
- Pitfalls to avoid (specific, not generic)
- Patterns that worked (specific, reusable)

---

## Filled Example: P2P Payment Flow Redesign

### 1. Launch Summary
- **What launched:** 3-step P2P payment flow replacing the 7-step flow for experienced senders (users with ≥1 prior P2P payment)
- **Launch date:** March 15, 2026 (ramp to 10% on Feb 22, 50% on March 1, 100% on March 15)
- **Team:** Consumer Payments squad (1 PM, 4 engineers, 1 designer, 1 user researcher)
- **Investment:** 18 person-weeks over 14 weeks (design: 4 weeks, engineering: 10 weeks, launch: 4 weeks guarded rollout)
- **Strategic intent:** Reduce payment friction to increase weekly active sender rate by 15%, based on user research showing 40% of drop-offs at steps 4-5

### 2. Expectations vs. Reality

| Dimension | Expected | Actual | Gap | Explanation |
|-----------|----------|--------|-----|-------------|
| Weekly active senders | +15% relative increase | +18% (first 90 days) | +3 pts above target | Stronger than expected due to: (a) repeat sender boost was larger than anticipated, (b) social sharing of "this is so fast now" drove word-of-mouth adoption. Estimation error — our survey-based estimates underestimated the behavioral effect. |
| Fraud rate | No significant change expected | +15% relative increase in successful fraud transactions | -15 pts below expectation (worse) | Causal error — we assumed the removed confirmation steps were cosmetic, but they were providing decision-making friction for fraud victims. We did not model fraud impact in the experiment design. |
| Customer support contacts | No significant change expected | +8% (transaction confusion, not fraud-related) | -8 pts below expectation | Mixed. Increase was from users confused by the new swipe gesture. Decreased over time as users learned the interaction. |
| NPS | +5 points expected | +16 points (42 → 58) | +11 pts above target | Estimation error — NPS impact was 3x our estimate. Customers describe the new flow as "effortless" — this word appears in 40% of positive NPS comments. |
| Time-to-send | -60% expected (45 seconds → 18 seconds) | -71% (45 seconds → 13 seconds) | -11 pts above target | Execution exceeded expectations — the FaceID integration during swipe was faster than our prototype estimates. |

### 3. What We Got Right
- **Feature flag rollout:** The ramped rollout (10% → 50% → 100%) caught an Android-specific swipe gesture bug on Day 3 of 10% phase. Without the ramp, this would have affected all Android users (40% of base) and potentially caused a rollback.
- **Decision to scope to experienced senders:** Focusing the redesign on users who already knew how to send money avoided the confusion that new users would have experienced. The new-user flow should be designed separately.
- **User research informing design:** The research finding that users found the "review" and "confirm" steps redundant was validated — those steps were the primary source of drop-off, and removing them drove the behavior change.
- **Swipe gesture choice:** The decision to use "swipe to send" rather than another button press was controversial during design (some stakeholders wanted a button for consistency). The swipe created a distinct, satisfying interaction that users describe as "fun."

### 4. What We Got Wrong
- **Fraud impact was not modeled:** The experiment design measured engagement and quality metrics but did not include fraud as a guardrail metric. By the time the Risk team flagged the fraud increase (Week 9 post-launch), the pattern was established and rolling back would have been disruptive. We are now adding friction back for high-risk transactions — effectively re-building some of what we removed.
- **Android gesture implementation was under-tested:** The swipe gesture worked perfectly on iOS (FaceID integration was seamless) but was choppy on Android devices with fingerprint sensors. We spent the first 2 weeks of the 50% ramp fixing Android-specific issues. Cost: ~40 person-days of rework and a subpar experience for Android users during those 2 weeks.
- **New-user flow was deferred:** We knew the redesign didn't address new users but didn't prioritize the new-user flow. Three months post-launch, new users are still on the 7-step flow while experienced users are on the 3-step flow — creating a confusing "why is my experience different?" moment that support has to explain.
- **Fraud team was not involved early:** The Risk team was consulted during design but their input focused on authentication security, not social engineering fraud prevention. A fraud specialist in the design review might have flagged the risk of removing confirmation steps for high-risk transactions.

### 5. Surprises
- **Positive:** The "swipe to send" became a minor social phenomenon. Users posted about it on social media. "This app lets me send money with a swipe — it's like magic" became an unexpected acquisition channel.
- **Negative:** The fraud increase was concentrated among elderly users (3x more likely to be victims after the redesign). This was not predicted by anyone on the team and only became visible when the Risk team segmented fraud data by age.
- **Neutral:** Users on older Android devices (4+ years old) had significantly worse swipe performance. This wasn't a design flaw — it was hardware limitations — but it created a two-tier experience we hadn't anticipated.

### 6. Customer Impact
- **What customers said:** "Finally, it just works." "I used to dread sending money because it took forever. Now it's one swipe." "This is the best Venmo alternative I've used." (From App Store reviews)
- **Negative quotes:** "I accidentally sent money to the wrong person because it was too fast." "My grandmother got scammed because it didn't ask her to confirm." "Why did you make it so easy to send money to scammers?" (From support tickets and social media)
- **Behavioral changes:** Repeat senders increased from 2.1 sends/week to 2.9 sends/week (+38%). First-time recipient sends (sending to someone you've never sent to before) increased by 22% — these transactions have higher fraud risk, which we should have anticipated.
- **Who benefited most:** Heavy senders (>5/week, +28%), moderate senders (1-5/week, +17%), iOS users (+22%). Light senders (<1/week) and Android users showed smaller gains.
- **Who was negatively affected:** Fraud victims (elderly, new immigrants, non-native English speakers) who lost the protective friction of confirmation steps.

### 7. Key Learnings
- **Product learning:** Friction serves multiple functions — removing friction improves engagement but may remove protective friction (fraud prevention, error correction). Every UX change that reduces friction should include a "what protective function did this friction serve?" analysis.
- **Process learning:** Fraud/risk stakeholders must be in design reviews for any UX change that affects money movement, not just authentication or security. Risk impact modeling should be a standard part of experiment design.
- **Organizational learning:** The Growth team (measured on engagement) and the Risk team (measured on fraud) had no shared forum before this launch. We need a cross-functional "Growth + Risk" review for changes that affect both metrics.
- **Strategic learning:** "Move fast and reduce friction" is a valid strategy for engagement, but it must be paired with "protect vulnerable users" as a design constraint. These are not opposing goals — they're co-requirements for a fintech product that serves diverse populations.

### 8. What We'll Do Differently

| Learning | Change | Owner | By When | Success Criteria |
|----------|--------|-------|---------|-----------------|
| Fraud impact not modeled | Add "Fraud/Risk impact assessment" to experiment design template | Head of Experimentation | End of Q2 | 100% of payment flow experiments include fraud guardrail metrics |
| Fraud team not involved early | Risk team participates in design reviews for any UX change affecting money movement | PM, Consumer Payments | Immediately (next design review) | Risk team has veto on changes that increase fraud risk for vulnerable populations |
| No cross-functional Growth+Risk forum | Establish monthly "Growth + Risk" review to discuss metrics and trade-offs | VP Product + Head of Risk | End of Q1 | First review held. Both teams report improved coordination. |
| Android under-tested | Add "platform parity testing" phase to QA process for multi-platform features | Engineering Manager, Consumer Payments | End of Q2 | Android and iOS metrics within 10% of each other at launch |

### 9. Artifacts for Future Teams
- **Key documents:** [Experiment Design: 3-Step Payment Flow], [User Research: Payment Flow Friction Points], [Fraud Impact Analysis (post-launch)], [Decision Memo: Adding Friction for High-Risk Transactions]
- **People with knowledge:** PM (Alex Chen) — product decisions and fraud trade-offs. Staff Engineer (Maria) — Android implementation challenges. User Researcher (Jamila) — fraud victim interviews.
- **Pitfalls:** (1) Don't remove confirmation steps without modeling fraud impact. (2) Test swipe/gesture interactions on older devices — they perform differently. (3) New-user flow should be designed concurrently, not deferred.
- **Patterns that worked:** (1) Ramped rollout with guardrail monitoring. (2) Scoping to a specific user segment (experienced senders) before expanding. (3) User research driving design decisions (the "review" and "confirm" redundancy finding).

---

## Common Mistakes

1. **Review as celebration or blame.** A good review is honest about both successes and failures. "Everything went great" reviews are useless. "Everything went wrong" reviews are demoralizing and miss the learnings from what did work.
2. **No gap analysis.** Listing what happened without comparing to what was expected misses the point. The gap between expectation and reality is where the learning lives.
3. **Generic learnings.** "We should communicate better" is not a learning — it's a cliche. A learning should be specific, causal, and produce a behavior change.
4. **No accountability for changes.** Learnings without owners and deadlines are wishes, not organizational improvements.
5. **Review filed and forgotten.** The review is not complete when it's written — it's complete when the changes have been implemented and validated.
6. **Delayed review.** The review should happen within 4-8 weeks of launch. After that, memories fade, team members move on, and learnings are lost.

## Dependencies

- [Experiment Design Template](EXPERIMENT_DESIGN_TEMPLATE.md): If the launch was based on an experiment, the experiment results are inputs to the review.
- [Metrics Tree Template](METRICS_TREE_TEMPLATE.md): The metrics you should be evaluating come from your metrics tree.
- [Pre-Mortem Template](PRE_MORTEM_TEMPLATE.md): Compare the post-launch reality to the pre-launch pre-mortem — did any of the failure modes materialize? Were there failure modes you didn't anticipate?
- [Decision Memo Template](DECISION_MEMO_TEMPLATE.md): The launch decision should have been documented. The review evaluates whether the decision was right.
