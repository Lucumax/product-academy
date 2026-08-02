# Experiment Design Template

## Purpose

An experiment design template structures product experiments so they produce reliable, actionable evidence. It ensures you've defined the hypothesis, success criteria, statistical considerations, and decision framework BEFORE running the experiment — preventing the most common failure mode (deciding the experiment was a success because you want it to be, regardless of what the data says).

This template is for product experiments (A/B tests, feature flags, phased rollouts, MVP tests). It is NOT for user research studies or qualitative discovery (those have different design considerations).

## When to Use

- You're about to run an A/B test on a product change
- You're shipping a feature behind a feature flag and want to measure its impact
- You're piloting a new product or feature with a subset of users
- You're testing a pricing change, UX change, or algorithm change
- Any situation where you're making a product change and need to know if it worked

## Template Structure

### 1. Experiment Summary

- **Experiment name:** Specific, descriptive, findable later
- **Hypothesis:** "We believe that [change] will cause [outcome] for [population] because [reasoning]."
- **Primary metric:** The ONE metric that determines success or failure
- **Decision:** What decision will this experiment inform?

The hypothesis is the most important field. A weak hypothesis: "The new onboarding will improve conversion." A strong hypothesis: "We believe that reducing onboarding from 7 steps to 3 steps will increase signup-to-activation rate by 15% for new team accounts because user research shows that 40% of drop-offs occur at steps 4-5, which we are eliminating."

### 2. Experiment Design

- **Population:** Who is included? Who is excluded? (New users only? All users? Specific segment?)
- **Treatment:** What exactly changes for the treatment group? Be specific — "new onboarding flow" is insufficient. Describe the exact experience.
- **Control:** What does the control group experience? (Current experience, or a different variant?)
- **Randomization:** How are users assigned to treatment vs. control? Is the unit of randomization the user, the team, the workspace?
- **Ramp plan:** What % of users see the treatment initially? How does this increase? What is the gate for increasing?
- **Duration:** How long does the experiment run? Why that duration? (Must account for: learning effects, weekly seasonality, enough sample size)

### 3. Success Criteria

- **Primary metric target:** The specific value that constitutes success. "Increase activation by 15%" not "improve activation."
- **Minimum detectable effect (MDE):** The smallest effect you care about. If the treatment produces a 0.5% improvement, is that worth shipping? Probably not. Define the MDE.
- **Statistical significance threshold:** Typically 95% (p < 0.05). State it explicitly.
- **Statistical power:** Typically 80%. State it explicitly.
- **Required sample size:** Based on MDE, significance, power, and baseline conversion rate — how many users are needed in each arm?

### 4. Guardrail Metrics (Counter-Metrics)

What metrics should NOT degrade as a result of the experiment?
- **Primary guardrail:** Metric that would cause you to stop the experiment immediately if it degrades significantly (e.g., "if fraud rate increases by >5%, stop immediately")
- **Secondary guardrails:** Metrics you'll monitor but that won't cause immediate stop (e.g., "if page load time increases by >500ms, investigate before ramping")

### 5. Decision Framework

Before running the experiment, define exactly what you'll do given each possible outcome:

| Outcome | Decision |
|---------|----------|
| Primary metric shows statistically significant improvement >MDE, no guardrail violations | Ship to 100% |
| Primary metric shows statistically significant improvement >MDE, but guardrail violation | Do not ship. Investigate guardrail. |
| Primary metric shows improvement but not statistically significant | Extend experiment duration OR increase sample size |
| Primary metric shows no meaningful change (within MDE) | Do not ship. Hypothesis not supported. |
| Primary metric shows statistically significant degradation | Stop experiment immediately. Revert. |

This is the most important section. If you don't define the decision framework before seeing the data, you'll interpret the data to support what you already wanted to do.

### 6. Analysis Plan

- **Segmentation:** What segments will you analyze beyond the primary population? (e.g., new vs. existing users, mobile vs. desktop, by plan tier)
- **Time-based analysis:** Will you look at effects over time? (Learning effects, novelty effects, decay)
- **Statistical method:** What test will you use? (T-test, chi-square, Bayesian, etc. — should be determined by your data characteristics)
- **Confidence intervals:** Report confidence intervals, not just point estimates

### 7. Shipping Criteria

Beyond the statistical outcome, what else must be true to ship?
- **Engineering readiness:** Performance, scalability, error rates
- **Operational readiness:** Support team trained, documentation updated, sales team briefed
- **Customer readiness:** Any customer communication needed?
- **Rollback plan:** If we need to revert after shipping to 100%, how do we do it?

### 8. Learnings Capture

Regardless of outcome, what will you document?
- **What we learned about the hypothesis:** Was it supported or not?
- **What we learned about the metric:** Did it behave as expected?
- **What we learned about the population:** Did segments respond differently?
- **What we learned about experimentation:** What would we do differently next time?

---

## Filled Example: Payment Flow Redesign

### 1. Experiment Summary
- **Experiment name:** P2P Payment Flow Redesign — 3-Step Flow vs. 7-Step Flow
- **Hypothesis:** We believe that reducing the P2P payment flow from 7 steps to 3 steps will increase the weekly active sender rate by 15% because (a) user research shows 40% of drop-offs occur at steps 4-5 (review and confirm screens), which we are consolidating, and (b) reducing friction should increase completion rate, especially for repeat senders who find the current multi-step confirmation unnecessary.
- **Primary metric:** Weekly active senders (users who send ≥1 P2P payment in a trailing 7-day period)
- **Decision:** Whether to replace the current 7-step flow with the new 3-step flow for all users.

### 2. Experiment Design
- **Population:** All users who have completed ≥1 P2P payment in the past 90 days (experienced senders). Excludes: new users who have never sent a payment (separate new-user experiment required — the flow is different for first-time senders).
- **Treatment:** 3-step flow: (1) Select recipient + enter amount on same screen, (2) Swipe to confirm (replaces review + confirm + authenticate steps — authentication happens via biometrics during swipe), (3) Confirmation animation with receipt.
- **Control:** Current 7-step flow: Select recipient, Enter amount, Select funding source, Review, Confirm, Authenticate (FaceID/PIN), Confirmation.
- **Randomization:** User-level randomization. Users assigned to treatment or control based on user ID hash (50/50 split). Assignment is persistent — a user stays in their arm for the experiment duration.
- **Ramp plan:** 10% of eligible users for first 7 days (safety check). If no guardrail violations, ramp to 50% for days 8-21. Full analysis at day 21.
- **Duration:** 21 days minimum. Must capture at least 2 full weekend cycles (P2P payment behavior is different on weekends) and account for novelty effect (users may send more initially because it's new, then revert).

### 3. Success Criteria
- **Primary metric target:** 15% increase in weekly active senders (relative increase) in treatment vs. control.
- **MDE:** 5% relative increase — below 5%, the change is not worth the engineering investment and UX disruption.
- **Significance:** 95% (p < 0.05, two-tailed)
- **Power:** 80%
- **Required sample size:** 12,400 users per arm (based on: baseline weekly active sender rate = 22%, MDE = 5% relative = 1.1 percentage points absolute, alpha = 0.05, beta = 0.2). Our eligible population is ~180,000 users — we have adequate sample.

### 4. Guardrail Metrics

| Guardrail | Threshold | Action if Violated |
|-----------|-----------|-------------------|
| Fraud rate (successful fraud / transaction volume) | >10% relative increase | Stop experiment immediately |
| Customer support contacts per transaction | >20% relative increase | Investigate before ramping |
| Transaction completion rate (all users, including drop-offs) | <5% relative decrease | Investigate before ramping |
| App crash rate during payment flow | >1% absolute increase | Stop experiment immediately |

### 5. Decision Framework

| Outcome | Decision |
|---------|----------|
| Weekly active senders ↑ ≥15% (stat sig), no guardrail violations | Ship to 100% of experienced senders. Plan new-user experiment. |
| Weekly active senders ↑ ≥15% (stat sig), but fraud rate ↑ >10% | Do not ship. Investigate fraud mechanism. Consider re-adding friction for high-risk transactions specifically. |
| Weekly active senders ↑ 5-15% (stat sig), no guardrail violations | Ship to 100%. Marginal improvement still worthwhile given low engineering cost of maintaining old flow. |
| Weekly active senders change within ±5% (not stat sig) | Do not ship. Consider variant experiments (2-step? 4-step? Different confirmation mechanism?). |
| Weekly active senders ↓ (stat sig) | Stop experiment. Investigate what about the new flow is worse. Qualitative research with users in treatment group. |

### 6. Analysis Plan
- **Segmentation:** Analyze by: (a) sender frequency — heavy senders (>5/week), moderate (1-5/week), light (<1/week), (b) device — iOS vs. Android, (c) transaction amount — <$50, $50-$200, >$200, (d) recipient relationship — first-time recipient vs. repeat recipient.
- **Time-based:** Compare Week 1 vs. Week 3 to detect novelty effects. If Week 1 shows +25% and Week 3 shows +5%, the effect is decaying.
- **Statistical method:** Two-tailed t-test for continuous metrics, chi-square for proportions. Report 95% confidence intervals.
- **Expected confounders:** Holiday periods, app version updates, concurrent marketing campaigns. Control for these in analysis.

### 7. Shipping Criteria
- **Engineering:** P95 latency < 500ms for the 3-step flow. Error rate < 0.1% on payment completion. Rollback requires feature flag toggle — can revert in <15 minutes.
- **Operational:** Support team trained on new flow and common issues. Help center updated with new flow screenshots. Fraud team briefed on changes to authentication model (biometric during swipe vs. separate authentication step).
- **Customer:** No proactive communication for existing users (the change is self-explanatory). New-user onboarding updated to reflect 3-step flow.
- **Rollback:** Feature flag toggle reverts all users to 7-step flow within 15 minutes. Database transactions during the 3-step experiment are compatible with the 7-step flow (no data migration needed for rollback).

### 8. Learnings Capture
- **Hypothesis:** Weekly active senders increased by 18% (p < 0.01, 95% CI: 14-22%). Hypothesis supported.
- **Metric:** Treatment effect was strongest for heavy senders (+28%) and moderate senders (+17%). Light senders showed no significant change. The effect was consistent across Weeks 1-3 (no novelty decay), suggesting sustained behavior change.
- **Population:** iOS users showed +22% vs. Android +12% — likely because FaceID makes the swipe-to-authenticate experience seamless while Android fingerprint/PIN is less fluid.
- **Experimentation:** The 10% safety ramp was important — we detected a bug in the Android implementation on Day 3 that would have affected all users if we had ramped to 50% immediately. Ramp plans are not optional.

---

## Common Mistakes

1. **Peeking.** Checking results daily and stopping when they look good. This inflates false positive rates dramatically. Define the analysis date in advance and don't make decisions before it.
2. **No MDE or sample size calculation.** Running an experiment without knowing if you have enough sample to detect the effect you care about is wasting time.
3. **Experiment as rubber stamp.** Running an experiment but having already decided to ship regardless of results. If you're going to ignore the data, don't run the experiment — it's disrespectful to the team's time.
4. **No guardrails.** Optimizing for one metric without monitoring what else breaks. Every A/B test winner that degraded the product in a way nobody measured.
5. **Novelty effects misinterpreted as sustained effects.** New things often perform better initially because they're new, not because they're better. Run experiments long enough to see if the effect sustains.
6. **Multiple comparisons without correction.** If you check 20 metrics and one is significant at p < 0.05, that's expected by chance. Define your primary metric before the experiment and don't cherry-pick significant results.

## Dependencies

- [Metrics Tree Template](METRICS_TREE_TEMPLATE.md): Your experiment's primary metric should come from your metrics tree.
- [Pre-Mortem Template](PRE_MORTEM_TEMPLATE.md): Pre-mortem the experiment design before launching — what could go wrong with the experiment itself?
- [Post-Launch Review Template](POST_LAUNCH_REVIEW_TEMPLATE.md): After shipping based on experiment results, review what happened.
- [Core Doctrine: PRN-0003](../01_core_doctrine/PRINCIPLES.md): Cost of delay vs. imperfection — how long should you run the experiment vs. shipping and learning?
