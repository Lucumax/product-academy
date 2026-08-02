# Risk-Adjusted Value Assessment

## Purpose

A risk-adjusted value assessment compares multiple initiatives with different risk profiles, time horizons, and value potential using a consistent framework. It answers: "Given that these options have different chances of success, different potential upsides, and different failure costs — which one creates the most expected value?" This is a tool for comparing investments, not for making the final decision. Judgment is still required.

## When to Use

- Comparing multiple initiatives competing for the same resources
- Evaluating a portfolio of product bets
- Making a build vs. buy vs. partner decision
- Quarterly or annual planning when prioritizing across options
- Making the case for (or against) a speculative investment
- Communicating investment decisions to executives or the board

## Template Structure

### 1. The Options

List each option with a brief description. Be specific about what each option entails in terms of scope, timeline, and resource commitment.

### 2. Value Estimation

For each option, estimate the expected value:

| Option | Best Case Value | Best Case Probability | Expected Case Value | Expected Case Probability | Worst Case Value | Worst Case Probability |
|--------|----------------|----------------------|--------------------|--------------------------|-----------------|----------------------|
| A | $X | Y% | $X | Y% | $X | Y% |
| B | $X | Y% | $X | Y% | $X | Y% |

**Expected Value = (Best Case × Best Prob) + (Expected Case × Expected Prob) + (Worst Case × Worst Prob)**

Where probabilities must sum to 100% for each option.

**Important:**
- Value should be expressed in consistent terms across options (revenue dollars, contribution margin, or a strategic value score)
- Probabilities should be calibrated — use historical data, reference classes, or explicit assumptions. Avoid "50% for everything because I'm uncertain" — differentiate based on what you actually know.
- The worst case is NOT "this fails completely and we get zero value." It should account for partial value, learnings, and salvageable assets.

### 3. Cost Estimation

| Option | Build Cost (one-time) | Annual Cost (ongoing) | Time to First Value | Full Value Timeline |
|--------|----------------------|----------------------|--------------------|--------------------|
| A | $X / Y person-weeks | $X/year | Z months | Z months |
| B | $X / Y person-weeks | $X/year | Z months | Z months |

### 4. Risk Adjustment Factors

Beyond probability-weighted value, adjust for:

**Risk of Complete Failure (0-100%):**
The probability that the option produces ZERO value (not just less than expected). This is different from the "worst case" in the value estimation — worst case assumes the project completes but produces less value. Complete failure means the project is abandoned or never ships usable value.

**Reversibility (1-5 scale):**
- 5: Fully reversible at low cost (e.g., A/B test that can be rolled back)
- 1: Impossible to reverse (e.g., architecture migration, pricing change, brand change)

**Optionality Value (1-5 scale):**
- 5: Creates significant future options regardless of direct outcome (e.g., builds a reusable platform, enters a strategic market)
- 1: Creates no future options beyond the direct outcome (e.g., one-off feature for a single customer)

**Learning Value (1-5 scale):**
- 5: Produces critical learning regardless of outcome (e.g., validates a key assumption, tests a new market)
- 1: Produces no significant learning (e.g., routine feature with known ROI)

### 5. Adjusted Value Score

Combine expected value with risk adjustments:

**Adjusted Score = Expected Value × (1 - Failure Risk) × Reversibility Multiplier × Optionality Multiplier × Learning Multiplier**

Where multipliers range from 0.5 (penalty) to 1.5 (bonus):
- Reversibility: 1 = reversible at medium cost. >1 for highly reversible. <1 for irreversible.
- Optionality: 1 = standard. >1 for high optionality. <1 for no optionality.
- Learning: 1 = standard. >1 for high learning value. <1 for no learning value.

The adjusted score is NOT a precise number. It's a way to make risk adjustments explicit and comparable. The conversation about what multipliers to use is often more valuable than the final number.

### 6. Non-Quantifiable Factors

What matters that cannot be captured in the model?
- Strategic coherence (does this reinforce or dilute the strategy?)
- Talent implications (does this attract, retain, or risk talent?)
- Brand and reputation (what signal does this send?)
- Competitive dynamics (how do competitors react?)
- Organizational capability building (does this build muscle for future work?)

These factors can override the quantitative analysis. The model is an input to judgment, not a substitute for it.

### 7. Portfolio Considerations

- **Correlation:** Are the options correlated? (e.g., Options A and B both depend on the same key assumption — if that assumption is wrong, both fail.) A portfolio of uncorrelated bets is more robust.
- **Sequencing:** Should we do some options sequentially rather than in parallel? (e.g., Option A builds the platform that Option B needs.)
- **Diversification:** Are we over-concentrated in one type of bet (e.g., all high-risk/high-reward, or all low-risk/incremental)?

### 8. Recommendation

- **Recommended option(s):** Based on the full analysis
- **Key trade-offs:** What are we gaining and sacrificing?
- **Sequencing or phasing:** If multiple options, in what order?
- **What we'll learn:** What key uncertainty will be resolved, and by when?

---

## Filled Example: Comparing Three Growth Initiatives

### 1. The Options
- **Option A: AI Documentation Assistant.** Build AI-powered clinical documentation that reduces physician charting time by 40%. Target: 50 Cloud customers in Year 1. Estimated $2.5M incremental ARR.
- **Option B: Classic Migration Tooling.** Build automated migration tools to move Classic customers to Cloud. Target: 500 migrations in Year 1. Estimated $3M retained ARR (preventing churn) + $1.5M incremental ARR (upgrade pricing).
- **Option C: Practice Management Enhancements.** Improve Cloud's billing and scheduling modules to compete with dedicated practice management solutions. Target: 100 new customers in Year 1. Estimated $1.8M incremental ARR.

### 2. Value Estimation (3-Year ARR Impact)

**Option A: AI Documentation Assistant**

| Scenario | 3-Year ARR Impact | Probability |
|----------|-------------------|-------------|
| Best Case | $12M (200 customers, AI becomes core differentiator, 20% market share gain) | 20% |
| Expected Case | $5M (100 customers, solid adoption, meaningful differentiator) | 50% |
| Worst Case | $0.5M (AI accuracy insufficient, limited adoption, but technology learnings salvageable) | 30% |

Expected Value: ($12M × 0.20) + ($5M × 0.50) + ($0.5M × 0.30) = $2.4M + $2.5M + $0.15M = $5.05M

**Option B: Classic Migration Tooling**

| Scenario | 3-Year ARR Impact | Probability |
|----------|-------------------|-------------|
| Best Case | $10M (80% of Classic base migrates, churn minimized, upgrade pricing captured) | 15% |
| Expected Case | $4.5M (50% migrate, some churn, partial upgrade capture) | 60% |
| Worst Case | $1M (20% migrate, high churn, migration tool issues) | 25% |

Expected Value: ($10M × 0.15) + ($4.5M × 0.60) + ($1M × 0.25) = $1.5M + $2.7M + $0.25M = $4.45M

**Option C: Practice Management Enhancements**

| Scenario | 3-Year ARR Impact | Probability |
|----------|-------------------|-------------|
| Best Case | $6M (displaces dedicated PM solutions, 150 new customers) | 25% |
| Expected Case | $3M (solid improvements, 100 new customers) | 55% |
| Worst Case | $0.5M (improvements insufficient vs. dedicated PM solutions) | 20% |

Expected Value: ($6M × 0.25) + ($3M × 0.55) + ($0.5M × 0.20) = $1.5M + $1.65M + $0.1M = $3.25M

### 3. Cost Estimation

| Option | Build Cost | Annual Cost | Time to First Value | Full Value Timeline |
|--------|-----------|-------------|--------------------|--------------------|
| A: AI Assistant | $3.2M (12 months, ML team) | $800K/year (ML ops, cloud) | 12 months (beta) | 24 months |
| B: Migration Tooling | $1.8M (9 months) | $300K/year (support) | 9 months (MVP) | 18 months |
| C: PM Enhancements | $1.2M (6 months) | $150K/year | 6 months | 12 months |

### 4. Risk Adjustment Factors

| Factor | A: AI Assistant | B: Migration | C: PM Enhancements |
|--------|----------------|-------------|-------------------|
| Failure Risk | 35% (AI accuracy may not meet clinical bar) | 15% (proven migration patterns, lower technical risk) | 10% (known domain, well-understood) |
| Reversibility | 3 (can pivot AI approach, but sunk cost is high) | 4 (migration tool doesn't change core product) | 5 (feature improvements, reversible) |
| Optionality | 5 (AI capability applies to all future products) | 3 (enables Cloud consolidation strategy) | 2 (point improvements, limited optionality) |
| Learning Value | 5 (validates AI strategy, informs future AI investments) | 3 (learns about customer migration behavior) | 2 (routine features, limited learning) |

### 5. Adjusted Value Score

Using multipliers: Reversibility (3=1.0, >3 bonus, <3 penalty), Optionality (3=1.0), Learning (3=1.0)

**Option A:** $5.05M × (1 - 0.35) × 1.1 × 1.3 × 1.3 = $5.05M × 0.65 × 1.1 × 1.3 × 1.3 = $6.11M adjusted
**Option B:** $4.45M × (1 - 0.15) × 1.1 × 1.0 × 1.0 = $4.45M × 0.85 × 1.1 = $4.16M adjusted
**Option C:** $3.25M × (1 - 0.10) × 1.3 × 0.8 × 0.8 = $3.25M × 0.90 × 1.3 × 0.8 × 0.8 = $2.43M adjusted

### 6. Non-Quantifiable Factors
- **Strategic coherence:** Option A (AI) is the core differentiator in our strategy. Option B (Migration) enables the strategy by consolidating the customer base. Option C (PM Enhancements) is table-stakes — necessary but not differentiating.
- **Talent:** Option A requires hiring ML engineers (competitive market, may fail). Option B and C use existing talent.
- **Competitive dynamics:** Athenahealth is also investing in AI. If we don't move on Option A, we lose the "first AI-powered EHR" positioning. But if we move and fail, we've spent $3.2M on a capability we couldn't deliver.
- **Organizational capability:** Option A builds AI muscle that serves the entire product portfolio for years. Options B and C are one-time investments.

### 7. Portfolio Considerations
- **Correlation:** Options A and B are correlated — both depend on Cloud being a viable growth platform. If Cloud fails to grow, both A and B lose value.
- **Sequencing:** Option B (Migration) should PRECEDE Option A (AI). AI features are more valuable when the customer base is consolidated on Cloud. A phased approach: B in Year 1 (build the consolidated base), A in Year 2 (add AI differentiation on top).
- **Diversification:** Option C is a lower-risk complement to the higher-risk A and B. It provides steady, predictable growth while A and B are speculative.

### 8. Recommendation
- **Recommended:** Phase B (Migration) → A (AI), with C (PM Enhancements) as a parallel lower-investment track.
- **Year 1:** Migration Tooling (Option B) + PM Enhancements (Option C, scaled to 50% of proposed scope). Investment: $2.4M. Expected 3-year value: $4.16M + $1.2M = $5.36M.
- **Year 2:** AI Documentation Assistant (Option A), building on the consolidated Cloud customer base from Year 1 migration. Investment: $3.2M. Expected 3-year value (from Year 2 start): $6.11M.
- **Key trade-off:** AI is deferred by one year, risking "first-mover" positioning. But it launches to a larger consolidated customer base, making it more valuable when it does launch. The migration-first approach de-risks the AI investment.
- **What we'll learn:** Year 1 migration results validate whether Classic customers will actually move to Cloud (key assumption for the entire strategy). If migration fails, AI investment is re-evaluated.

---

## Common Mistakes

1. **False precision.** Modeling expected value to two decimal places suggests more certainty than exists. Use ranges and scenarios, not point estimates. The output is a conversation starter, not a calculator result.
2. **Probability calibration neglect.** Most people are overconfident — they assign 70-80% probability to expected cases and 5-10% to worst cases. Use reference classes (how often do similar projects succeed?) and historical data to calibrate.
3. **Ignoring correlation.** If your "portfolio" is three bets that all depend on the same assumption (e.g., "AI adoption in healthcare accelerates"), you don't have a diversified portfolio — you have one bet expressed three ways.
4. **Worst case as zero.** Even failed projects produce learnings, reusable code, or market insights. The worst case should account for salvageable value.
5. **Non-quantifiable factors as tiebreakers.** The non-quantifiable section should be as rigorous as the quantitative section. "This feels strategic" is not analysis. "This advances our strategy because it specifically enables X, Y, and Z that are currently blocked" is analysis.
6. **Analysis as decision.** The model informs judgment but does not replace it. If the model says Option A but your judgment says Option B, interrogate both — the model may be wrong, or your judgment may be biased.

## Dependencies

- [Product Strategy Template](PRODUCT_STRATEGY_TEMPLATE.md): Strategy defines what types of bets align with your direction.
- [Resource Allocation Memo](RESOURCE_ALLOCATION_MEMO.md): The options compete for resources — this analysis informs allocation.
- [Opportunity Assessment Template](OPPORTUNITY_ASSESSMENT_TEMPLATE.md): Deep-dive analysis on each option feeds into this comparison.
- [Decision Memo Template](DECISION_MEMO_TEMPLATE.md): For communicating the final recommendation.
