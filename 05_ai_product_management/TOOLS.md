# AI PM Tools and Templates

**Status:** v0.1.0
**Depends on:** All previous module files

---

## Overview

This file contains actual, usable templates and filled examples that you can adapt for your AI products. Every template here has been designed to be copied, filled out, and used in real product decisions. The filled examples show what "good" looks like — specific, quantified, and honest about limitations.

---

## Tool 1: AI Use Case Assessment Template

### Blank Template

```markdown
# AI Use Case Assessment: [Feature/Use Case Name]

## 1. Workflow Description (without AI)
Who: _________________________________
What: _________________________________
Input: _________________________________
Output: _________________________________
Constraints: _________________________________
Current performance: _________________________________

## 2. Subtask Decomposition

| Subtask | Type | Input | Output | Human Difficulty (1-5) | Current Error Rate | Exception Frequency |
|---------|------|-------|--------|------------------------|--------------------|---------------------|
|         |      |       |        |                        |                    |                     |
|         |      |       |        |                        |                    |                     |
|         |      |       |        |                        |                    |                     |

## 3. AI Suitability Scoring

| Subtask | Determinism (1-5) | Error Tolerance (1-5) | Automation Value (1-5) | Overall |
|---------|-------------------|----------------------|------------------------|---------|
|         |                   |                      |                        |         |
|         |                   |                      |                        |         |

## 4. Problem Value Score (PVS)

| Dimension | Score (1-5) | Evidence |
|-----------|-------------|----------|
| Frequency |             |          |
| Pain      |             |          |
| Willingness to pay |   |          |
| Market size |           |          |
| Strategic alignment |  |          |
| **PVS (Average)** |      |          |

## 5. Technical Novelty Assessment (TNA)

| Dimension | Score (1-5) | Evidence |
|-----------|-------------|----------|
| Existing solutions |        |          |
| Data availability |          |          |
| Determinism |               |          |
| Error tolerance |            |          |
| **TNA (Average)** |           |          |

## 6. PVS-TNA Matrix Placement

PVS: ____  TNA: ____  → Quadrant: _________________

## 7. Anti-Pattern Check

[ ] Deterministic solution exists that works better
[ ] Error cost exceeds automation value
[ ] Training data doesn't exist and can't be generated
[ ] Task requires causal reasoning, not pattern matching
[ ] Cost structure destroys unit economics
[ ] Latency requirements below AI inference time
[ ] Can't measure success
[ ] Regulatory environment prohibits it

## 8. Non-AI Alternative
What is the best non-AI solution? _________________________________
Why is AI better? _________________________________

## 9. Decision

[ ] BUILD — Strong product and technical case
[ ] INVESTIGATE — Build evaluation harness, validate with real data
[ ] MONITOR — Wait for technical maturity or problem value increase
[ ] DO NOT BUILD

## 10. Sign-Off

Product Lead: ___________ Date: ___________
Engineering Lead: ___________ Date: ___________
```

### Filled Example: Automated Medical Billing Code Review

```markdown
# AI Use Case Assessment: Automated Medical Billing Code Review

## 1. Workflow Description (without AI)
Who: Medical coders in ambulatory surgery centers (ASCs)
What: Review CPT and ICD-10 codes on surgical claims for accuracy before submission to payers
Input: Operative report (free text), surgeon's notes, anesthesia record, implant logs, patient demographics
Output: Verified/Corrected claim with accurate CPT codes, ICD-10 codes, modifiers, and units
Constraints: Must comply with CMS NCCI edits, payer-specific policies, and ASC fee schedules. Error tolerance: coding errors cause claim denials costing avg $118/denial in rework + delayed reimbursement avg $2,400/claim. Turnaround target: <4 hours.
Current performance: 94.3% first-pass approval rate. Average claim value: $12,400. Average rework cost per denied claim: $118 + $2,400 delay cost + $340 re-coding cost = ~$2,858/denial.

## 2. Subtask Decomposition

| Subtask | Type | Input | Output | Human Difficulty | Current Error Rate | Exception Frequency |
|---------|------|-------|--------|-----------------|--------------------|---------------------|
| Extract procedures from operative report | Information extraction | Free-text surgical narrative | Structured procedure list with laterality, approach, technique | 1 | 0.8% | 5% |
| Map procedures to CPT codes | Classification | Procedure list | CPT codes with modifiers | 3 | 3.2% | 20% |
| Map diagnoses to ICD-10 codes | Classification | Diagnosis descriptions | ICD-10 codes with specificity | 3 | 2.8% | 18% |
| Apply NCCI bundling edits | Rule checking | CPT codes | Flagged conflicts with edit rationale | 2 | 1.5% | 12% |
| Apply payer-specific policies | Rule application | Codes + payer | Modified codes per payer rules | 4 | 5.1% | 30% |
| Verify medical necessity linkages | Judgment | Diagnosis codes + procedure codes | Verified necessity linkages | 4 | 4.2% | 25% |
| Calculate units and apply modifiers | Rule application + Judgment | Procedure list + documentation | Final modifier and unit assignments | 3 | 2.0% | 15% |

## 3. AI Suitability Scoring

| Subtask | Determinism | Error Tolerance | Automation Value | Overall |
|---------|------------|----------------|-----------------|---------|
| Extract procedures | 4 | 4 (errors caught downstream) | 5 (high volume, repetitive) | 4.3 |
| Map to CPT codes | 3 | 3 | 5 | 3.7 |
| Map to ICD-10 codes | 3 | 3 | 5 | 3.7 |
| Apply NCCI edits | 5 (deterministic rules) | 3 | 4 | 4.0 |
| Apply payer policies | 2 (many exceptions) | 2 (denial costly) | 5 | 3.0 |
| Verify medical necessity | 2 | 2 | 4 | 2.7 |
| Calculate units/modifiers | 3 | 3 | 4 | 3.3 |

KEY INSIGHT: The extraction, CPT/ICD-10 mapping, and NCCI edits are strong AI candidates. Payer-specific policies and medical necessity verification are HIGH RISK for AI — likely better as human-only tasks with AI providing supporting evidence.

## 4. Problem Value Score (PVS)

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Frequency | 5 | Each ASC processes 50-150 surgical claims/day. Coder reviews 30-40/day at full productivity. |
| Pain | 4 | Coding denials cost $2,858 each. 5.7% denial rate. 3-4 denials/day per coder team = $8,500-11,400/day in rework cost. |
| Willingness to pay | 5 | ASCs pay $35-65/claim for outsourced coding. Internal coders cost $28-42/claim fully loaded. Resolution: AI at $5-10/claim would be dramatically cheaper. |
| Market size | 4 | ~6,200 ASCs in the US. Estimated 50M surgical claims/year across ASCs. TAM: $250M-500M at $5-10/claim. |
| Strategic alignment | 4 | Company's existing RCM platform already processes 8M claims/year. AI coding is a natural extension of the platform. |
| **PVS** | **4.4** | Strong product case. |

## 5. Technical Novelty Assessment (TNA)

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Existing solutions | 4 | Multiple AI-assisted coding products exist (3M, Optum, CodaMetrix). Commodity NLP for entity extraction. Specialized models for CPT/ICD-10 mapping. |
| Data availability | 4 | Access to 2M historical coded claims with operative reports. CPT and ICD-10 codebooks are public. Payer policies available (some proprietary, need licenses). |
| Determinism | 3 | CPT/ICD-10 mapping has clear correct answers for standard cases. Edge cases, payers with conflicting policies, and multi-procedure cases have ambiguity. |
| Error tolerance | 3 | Errors cost $2,858/denial. Acceptable error rate target: <3% (below current human 5.7% denial rate). AI must perform at or above human level on error rate. |
| **TNA** | **3.5** | Moderate difficulty. Good data availability but error tolerance is tight. |

## 6. PVS-TNA Matrix Placement

PVS: 4.4  TNA: 3.5  ->  Quadrant: PVS HIGH / TNA MEDIUM -> **INVESTIGATE**

## 7. Anti-Pattern Check

[x] Deterministic solution exists — Partially. NCCI edits are deterministic. CPT/ICD-10 mapping has deterministic answers but the input (operative reports) is unstructured — NLP extraction justified. AI is augmenting the deterministic rules, not replacing them.
[x] Error cost exceeds automation value — Checked. Current denial cost: $2,858. Target AI cost: $7/claim. At 3% error rate, expected error cost per claim: 0.03 x $2,858 = $85.74. Total AI cost per claim: $7 + $85.74 = $92.74 vs human cost $35 + (0.057 x $2,858) = $197.89. AI is NET POSITIVE even with errors — but only if error rate stays at 3% or below.
[ ] Training data doesn't exist — Has 2M+ coded claims.
[ ] Task requires causal reasoning — CPT/ICD-10 mapping is pattern matching with rule overlay.
[ ] Cost structure destroys economics — At $7/claim for AI vs $35/claim for human, economics are favorable.
[ ] Latency below AI threshold — Target <60 seconds per claim. AI latency adequate.
[ ] Can't measure success — Success = First-pass approval rate. Measurable via payer adjudication data.
[ ] Regulatory prohibited — Medical coding is not prohibited by current regulations. AI coding is assistive (coder reviews), not autonomous (fully automated).

## 8. Non-AI Alternative
Best non-AI solution: Continue human coding with better training, better payer policy databases, and automated NCCI edit checking (rules engine, not AI). This would improve human accuracy from 94.3% to ~96%.
Why AI is better: Humans still miss 4% of claims at their best. At 8M claims/year, that's 320,000 denials/year costing ~$914M in rework across the customer base. AI at 97%+ first-pass rate would eliminate ~2/3 of those denials.

## 9. Decision

[X] INVESTIGATE — Build evaluation harness with 500 coded claims across 20 ASCs and 50 procedure types. Measure AI coding accuracy vs human baseline. If AI achieves <3% error rate with human review of high-risk claims only, proceed to BUILD.

## 10. Sign-Off

Product Lead: J. Chen Date: 2026-07-28
Engineering Lead: A. Patel Date: 2026-07-28
Clinical Domain Expert: Dr. S. Morrison Date: 2026-07-29
```

---

## Tool 2: Evaluation Contract Template (Filled Example)

This is a partial fill of the full evaluation contract template from EVALUATION_CONTRACTS.md, showing how the most critical sections look when completed.

### Section 4: Failure Taxonomy (Filled Example)

**Use Case:** AI-Assisted Medical Billing Code Review

```
FAILURE TAXONOMY:

SEVERITY SCALE:
1 (Trivial) — Minor formatting issue. No impact on claim outcome. Autocorrected.
2 (Minor) — Modifier missing or incorrect but doesn't affect reimbursement amount. Flagged, coder can fix in <30 seconds.
3 (Moderate) — Wrong CPT code. Would cause denial if submitted. Coder rework: 2-5 minutes. Denial cost if caught after submission: $118 + rework.
4 (Major) — Upcoding or unbundling that, if submitted, could trigger payer audit, compliance risk, or fraud investigation. Requires immediate correction and root cause analysis.
5 (Critical) — Patient harm: wrong code leads to wrong treatment authorization. OR: Systematic coding error affecting hundreds of claims before detection.

FAILURE TYPES (with this product's specific examples):

1. HALLUCINATION: AI invents procedures not documented in operative report.
   Example: Operative report describes carpal tunnel release. AI adds code for "neuroplasty" which was not performed.
   Severity: 4 (upcoding — compliance risk)
   Detection: Cross-reference AI output against extracted procedures. Any CPT code without a corresponding extracted procedure = flagged for review.
   Mitigation: Only generate codes for procedures explicitly found in extraction step. Second-pass verification that all codes have evidence in the source document.

2. OMISSION: AI fails to code a documented procedure.
   Example: Operative report describes carpal tunnel release AND trigger finger release. AI only codes the carpal tunnel release.
   Severity: 3 (lost revenue but no compliance risk)
   Detection: Procedure count mismatch between extraction (2 procedures found) and coding output (1 code group).
   Mitigation: Always produce output with procedure count summary. If extraction count != coding count, flag.

3. CONFIDENCE MISCALIBRATION: AI expresses high confidence on wrong code.
   Example: AI codes "29827" (rotator cuff repair, arthroscopic) for a procedure described as "mini-open rotator cuff repair." AI is confident. Correct code is "23412" (open repair). Difference matters for reimbursement AND compliance.
   Severity: 4 (wrong surgical approach = compliance risk if pattern emerges)
   Detection: Human coder review of all shoulder cases during pilot phase. Measure calibration: for cases where AI says "high confidence, what is actual accuracy?"
   Mitigation: Never show confidence to coder. Instead, when confidence is below threshold, flag for mandatory human review and show differential diagnosis: "This appears to be [CODE A] but could be [CODE B] depending on surgical approach. Please verify from operative report."

4. REASONING ERROR: AI selects correct code family but wrong specificity.
   Example: CPT 27447 (total knee arthroplasty) vs 27446 (partial knee arthroplasty). Operative report uses ambiguous language. AI picks 27447. Surgeon actually performed partial (27446). 
   Severity: 3 (wrong payment but direction of error could go either way; not systematic)
   Detection: Highlight ambiguous language in the report. Flag for review when key distinguishing terms ("total" vs "partial"/"unicompartmental") are absent or ambiguous.
   Mitigation: When key distinguishing terms are absent, flag and ask coder to verify rather than guessing.

5. BIAS/FAIRNESS: No identified direct bias risk for this use case (coding is based on clinical documentation, not patient demographics). However, INDIRECT BIAS RISK: if operative reports from certain patient populations are systematically less detailed (due to provider communication patterns), AI may perform worse on those populations. This is a data quality issue, not a model bias issue, but must be monitored.
   Severity: 3 (potential)
   Detection: Subgroup analysis of AI coding accuracy by patient demographics, provider type, facility type.
   Mitigation: If performance disparities found, improve training data for underrepresented groups rather than adjusting model behavior.

[... additional failure types omitted for brevity; all 12 types from the full taxonomy would be filled out]
```

### Section 11: Launch Threshold (Filled Example)

```
LAUNCH THRESHOLD:

The AI coding assistant may launch to the initial 5-practice pilot when:

MANDATORY GATES:

1. TASK SUCCESS RATE: AI-suggested codes are accepted by coder without modification for >= 90% of codes across 500+ test claims. (Note: "Accepted without modification" is the user-facing proxy for accuracy, since ground truth for every claim is established by expert consensus, not individual coder judgment.)

2. SEVERE ERROR RATE: <= 0.5% severity-4 errors (upcoding/unbundling with compliance risk). <= 0% severity-5 errors.

3. GOLDEN EXAMPLE ACCURACY: 100% on the 25 highest-value golden examples (most common procedures, highest reimbursement, highest compliance risk).

4. ADVERSARIAL RSILIENCE: >= 90% of adversarial examples handled correctly. Adversarial examples include: operative reports with contradictory information, reports with deliberately ambiguous language, edge-case combinations of procedures.

5. LATENCY: p95 <= 45 seconds end-to-end (document upload to code suggestions displayed).

6. COST: Per-claim cost <= $7.00 at 200 claims/day pilot volume.

7. BIAS AUDIT: No statistically significant accuracy difference across patient demographic subgroups at p < 0.05 level with sufficient sample size.

8. PRIVACY: All PHI scrubbed before sending to external AI provider. DPA signed. Zero-retention policy confirmed.

9. HUMAN CODERS TRAINED: Pilot coder team trained on AI review workflow. Calibration testing completed showing >90% detection rate for deliberately inserted errors.

10. ROLLBACK DRILL COMPLETED: Simulated rollback scenario. System reverted to human-only coding within 15 minutes. No claim processing interruption.

RECOMMENDED (met, but not mandatory):

11. PARALLEL RUN: System has run in shadow mode (AI produces codes, coder codes independently, results compared) for 2,000+ claims showing AI-human agreement of 93.1% with 0.3% severity-4 errors. 

12. CODER SATISFACTION: 4/5 pilot coders rate the system as "ready for my daily workflow" or better.
```

### Section 12: Rollback Threshold (Filled Example)

```
ROLLBACK THRESHOLD:

Automatic triggers:

1. SEVERE ERROR BURST: >3 severity-4 errors in any 24-hour period, OR any single severity-5 error.

2. CODER ACCEPTANCE DROP: Coder acceptance rate (using AI codes without modification) drops below 85% for 3 consecutive business days. This suggests either AI quality degradation OR coders losing trust.

3. COST SPIKE: Daily AI inference cost exceeds $10/claim for 3+ consecutive days.

4. LATENCY BREACH: p95 latency exceeds 90 seconds for 4+ consecutive hours.

5. PHI LEAK: Any confirmed instance of PHI appearing in AI provider logs or outputs.

6. PROVIDER OUTAGE: Primary AI provider unavailable for >30 minutes with fallback provider also unavailable or producing quality below 80% coder acceptance.

7. AUDIT FLAG: Payer or regulatory body inquiry into AI-assisted coding.

Rollback procedure:
- Decision: Product Lead + Engineering Lead + Compliance Officer, any one of whom can initiate rollback
- Speed: Within 1 hour of trigger confirmation
- Fallback: System reverts to human-only coding workflow. Coders see only their existing tools. AI panel hidden.
- Communication: In-app banner: "AI coding assistance is temporarily unavailable while we address a quality concern. Your coding workflow is unchanged." + email to pilot practice admins within 2 hours.
- Recovery criteria: Root cause identified, fix deployed, fix validated on 200+ test claims with <0.5% severity-4 error rate, pilot coders re-trained, Product Lead sign-off.
```

---

## Tool 3: Model Selection Framework

### Blank Template

```markdown
# Model Selection Decision: [Use Case]

## 1. Evaluation Criteria (from Evaluation Contract)

| Criterion | Target | Weight (1-5) |
|-----------|--------|-------------|
| Task success rate | >= ___% | |
| Severe error rate | <= ___% | |
| p95 latency | <= ___ms | |
| Cost per task | <= $___ | |
| Provider reliability | >= ___% uptime | |
| Data processing terms | [requirements] | |
| Model stability commitment | [requirements] | |

## 2. Candidate Models

| Model | Provider | Task Success | Severe Error | p95 Latency | Cost/Task | Provider SLA | Data Terms | Stability |
|-------|----------|-------------|-------------|------------|-----------|-------------|-----------|----------|
|       |          |             |             |            |           |             |           |          |
|       |          |             |             |            |           |             |           |          |
|       |          |             |             |            |           |             |           |          |

## 3. Failure Pattern Analysis

For each candidate, what types of failures dominate? Are they acceptable failure types?

| Model | Top Failure Mode | Frequency | Acceptable? |
|-------|-----------------|-----------|-------------|
|       |                 |           |             |
|       |                 |           |             |

## 4. Cost-Benefit Analysis

| Model | Annual Cost* | Expected Error Cost | Total | Quality Benefit |
|-------|-------------|-------------------|-------|----------------|
|       |             |                   |       |                |

*At projected annual volume

## 5. Provider Relationship Assessment

| Model/Provider | Data processing terms acceptable? | Migration difficulty (1-5) | Stability commitment | Overall risk |
|---------------|----------------------------------|---------------------------|---------------------|-------------|
|               |                                  |                           |                     |             |
|               |                                  |                           |                     |             |

## 6. Decision

Selected model: _________________
Fallback model: _________________
Router architecture? [Y/N] If yes, describe: _________________
Migration plan: _________________
Review date: _________________

## 7. Sign-off

Product Lead: ___________
Engineering Lead: ___________
Data Science Lead: ___________
```

---

## Tool 4: AI Product Decision Memo Template

Use this when proposing a significant AI product investment to leadership.

```markdown
# AI Product Decision Memo: [Proposal Name]

## EXECUTIVE SUMMARY (1 paragraph)
[What we're proposing, why, expected impact, and requested decision.]

## 1. PROBLEM STATEMENT
- What is the user/customer problem?
- What is the business problem?
- What happens if we don't solve it?
- What is the evidence that this problem matters? (Data, not anecdotes)

## 2. PROPOSED SOLUTION
- What will we build? (Describe in user terms, not AI terms)
- How does AI specifically address the problem?
- Why AI instead of non-AI alternatives?
- What is the user experience?

## 3. EVIDENCE OF FEASIBILITY
- What prototypes, experiments, or external evidence demonstrates this is possible?
- What are the key technical risks?
- What evaluation have we already done?

## 4. MARKET ASSESSMENT
- Total addressable market
- Competitive landscape (what exists today, what's announced)
- Why now? (Why not 2 years ago? Why not wait 2 years?)

## 5. BUSINESS CASE

### Investment Required
| Category | Year 1 | Year 2 | Year 3 |
|----------|--------|--------|--------|
| Engineering (FTE) | | | |
| AI/ML (FTE) | | | |
| AI inference costs | | | |
| Infrastructure | | | |
| Design | | | |
| Other | | | |
| **Total** | | | |

### Expected Returns
| Metric | Year 1 | Year 2 | Year 3 |
|--------|--------|--------|--------|
| Revenue (new) | | | |
| Revenue (retained) | | | |
| Cost savings | | | |
| Other value | | | |
| **Total value** | | | |

### ROI: [X]x return over 3 years. Payback period: [Y] months.

## 6. RISK ASSESSMENT

| Risk | Likelihood (1-5) | Impact (1-5) | Mitigation |
|------|-----------------|-------------|------------|
| Technical (can't achieve required quality) | | | |
| Adoption (users won't use it) | | | |
| Competitive (someone else ships first/better) | | | |
| Regulatory (compliance changes or blocks) | | | |
| Economic (cost structure doesn't scale) | | | |

## 7. GOVERNANCE (from GOVERNANCE.md)
- Risk tier: [1-5]
- Human oversight model: [in-the-loop / on-the-loop / in-command]
- Regulatory requirements: [list applicable regulations]
- Key governance requirements: [key ones from the tier]

## 8. SUCCESS METRICS (from ADOPTION.md)
- North Star: _________________
- Health metrics: _________________
- Launch threshold: _________________
- Rollback threshold: _________________

## 9. ALTERNATIVES CONSIDERED
- Alternative 1: [Do nothing / Status quo]
- Alternative 2: [Non-AI solution]
- Alternative 3: [Build vs buy alternative]
- Alternative 4: [Different scope or approach]
- Why the proposed approach is better: _________________

## 10. TIMELINE AND MILESTONES

| Milestone | Target Date | Success Criteria |
|-----------|------------|-----------------|
| Evaluation harness built | | |
| Initial results (go/no-go) | | |
| Prototype complete | | |
| Internal beta | | |
| Limited launch | | |
| Scaled launch | | |

## 11. ASK
- Decision requested: [Proceed / Fund further investigation / Reject]
- Resources requested: [Budget, headcount, access to data, cross-functional support]
- Constraints and dependencies: [What must be true for this to succeed]
- Decision needed by: [Date, and why that date]

## 12. APPENDICES
- A: Detailed technical assessment
- B: Competitive analysis
- C: Financial model
- D: User research summary
```

---

## Tool 5: AI Risk Register Template

Maintain this as a living document for each AI product. Update quarterly or after any incident.

```markdown
# AI Risk Register: [Product Name]

**Owner:** [Product Lead]
**Last Updated:** [Date]
**Next Review:** [Date]

## Summary

| Total risks identified | [N] |
|---|---|
| Critical (Red) | [N] |
| High (Orange) | [N] |
| Medium (Yellow) | [N] |
| Low (Green) | [N] |

## Risk Register

### RISK-001: [Risk Name]

| Field | Detail |
|-------|--------|
| **Category** | [Capability / Calibration / Deployment / Adversarial / Systemic / Fairness] |
| **Description** | [Detailed description of the risk — what could go wrong?] |
| **Trigger event** | [What would cause this risk to materialize?] |
| **Likelihood** | [1-Rare / 2-Unlikely / 3-Possible / 4-Likely / 5-Almost Certain] |
| **Impact** | [1-Negligible / 2-Minor / 3-Moderate / 4-Major / 5-Catastrophic] |
| **Risk score** | [Likelihood x Impact = 1-25] |
| **Detection** | [How would we know this risk has materialized?] |
| **Detection time** | [Minutes / Hours / Days / Weeks / Months] |
| **Mitigation** | [What are we doing to reduce likelihood or impact?] |
| **Contingency** | [If it materializes, what do we do?] |
| **Owner** | [Name/role accountable for this risk] |
| **Status** | [Monitored / Mitigated / Accepted / Resolved] |
| **Last reviewed** | [Date] |

### Filled Example: RISK-001 through RISK-005

### RISK-001: CPT Upcoding from Ambiguous Operative Reports

| Field | Detail |
|-------|--------|
| Category | Capability (Reasoning Error) |
| Description | AI misinterprets ambiguous surgical language in operative reports and selects a higher-paying CPT code (upcoding). While individually rare, systematic upcoding across thousands of claims triggers payer audits, repayment demands, and potential fraud investigations. |
| Trigger event | Surgeon uses non-standard terminology. Operative report missing key differentiating details (e.g., "cuff repair" without "partial" vs "complete"). AI defaults to higher-paying code. |
| Likelihood | 3 (Possible) — Ambiguous reports are 15-20% of all surgical cases in our dataset. |
| Impact | 5 (Catastrophic) — Payer audit could result in millions in repayments, exclusion from payer networks, and CMS investigation. Reputational damage to the product and the ASCs using it. |
| Risk score | 15 (HIGH) |
| Detection | (1) Flag when key differentiating terms absent from operative report. (2) Monitor for code distribution shifts — if AI starts coding significantly more high-paying variants of a procedure family vs historical distribution. (3) Monthly external audit of 500 randomly selected AI-coded claims by independent certified coders. |
| Detection time | Days to weeks (distribution monitoring); quarterly (external audit) |
| Mitigation | (1) AI flags ambiguous cases for mandatory human review — no auto-acceptance. (2) Confidence threshold: if AI confidence in code selection below 90%, escalate. (3) Training data enriched with ambiguous-case examples and correct resolutions. (4) Coder training on reviewing AI suggestions for ambiguous cases. |
| Contingency | If systematic upcoding detected: (1) Suspend AI coding for affected procedure families. (2) Retrospective review of all claims coded since last clean audit. (3) Voluntary disclosure to affected payers with corrected claims. (4) Root cause analysis and model retraining before reinstatement. |
| Owner | Dr. S. Morrison (Clinical Domain Lead) |
| Status | Mitigated — ambiguity detection in production since v1.2. First external audit results due Aug 15. |
| Last reviewed | 2026-07-30 |

### RISK-002: Coder Over-Reliance (Automation Bias)

| Field | Detail |
|-------|--------|
| Category | Systemic |
| Description | Coders become overly reliant on AI suggestions and stop critically evaluating them. Acceptance rate trends toward 100% regardless of AI accuracy. Errors slip through because coders assume "the AI checked it." |
| Trigger event | Coder fatigue, high volume pressure, normalization of AI in workflow, declining coder domain expertise over time. |
| Likelihood | 4 (Likely) — Automation bias is well-documented in high-volume review tasks. |
| Impact | 3 (Moderate) — Increased denial rate, but each error caught by payer (not by coder) costs money. |
| Risk score | 12 (MEDIUM-HIGH) |
| Detection | (1) Track individual coder acceptance rates. Alert if any coder >98% acceptance over rolling 30 days. (2) Plant deliberate errors in coding queue (2-3% of claims). Measure coder detection rate. If below 80% detection of planted errors, intervene. (3) Periodic independent coding test: coders code 10 claims without AI. Compare accuracy to their AI-assisted accuracy. |
| Detection time | Weekly (acceptance rate monitoring); monthly (planted error testing); quarterly (independent testing) |
| Mitigation | (1) Planted errors as ongoing calibration. (2) Require coders to annotate their review — one-click "accept" disabled; must click "confirmed from operative report section [X]." (3) Rotate coder assignments between AI-assisted and non-AI-assisted claims to maintain independent skills. (4) Quarterly coder training and recalibration. |
| Contingency | If coder over-reliance confirmed: (1) Increase planted error rate temporarily. (2) Mandatory retraining for affected coders. (3) If severe, temporarily increase human-only coding ratio to rebuild independent judgment. |
| Owner | M. Torres (Coding Operations Lead) |
| Status | Mitigated — Planted error program running since launch. Coder annotation requirement in development for v2.0. |
| Last reviewed | 2026-07-28 |

### RISK-003: Provider API Price Increase

| Field | Detail |
|-------|--------|
| Category | Deployment / Economic |
| Description | Primary AI provider increases API pricing (or changes pricing model so effective cost increases). Unit economics degrade. At $7/claim target, a 50% price increase pushes cost to $10.50/claim, reducing margin and potentially making AI more expensive than human coding in some scenarios. |
| Trigger event | Provider announces price change. OR: Provider deprecates current model, requiring migration to a more expensive model. |
| Likelihood | 3 (Possible) — AI API pricing has been volatile. Major providers have raised prices and changed pricing models. |
| Impact | 3 (Moderate) — Doesn't break the product but reduces margin and ROI. Could delay path to profitability. |
| Risk score | 9 (MEDIUM) |
| Detection | Provider pricing page monitoring. Alert on any price announcement. |
| Detection time | Immediate upon provider announcement (typically 30-90 days notice). |
| Mitigation | (1) Fallback provider with comparable quality tested quarterly. (2) Cost monitoring per claim with monthly trend analysis. (3) Model router architecture: route low-complexity claims to cheaper model, high-complexity to expensive model. (4) Budget for 20% annual price increase in financial model. (5) Long-term: explore self-hosted open-source model as hedge (currently quality is insufficient but monitoring). |
| Contingency | If price increase breaks unit economics: (1) Switch to fallback provider. (2) Aggressively expand model routing to cheaper models. (3) If neither restores economics, reduce AI scope to highest-ROI claim types; human coding for remainder. |
| Owner | A. Patel (Engineering Lead) |
| Status | Monitored — Fallback provider tested Q2 2026. Model router POC complete. |
| Last reviewed | 2026-07-15 |

### RISK-004: Distribution Shift from New Procedure Types

| Field | Detail |
|-------|--------|
| Category | Deployment (Distribution Shift) |
| Description | AI model trained primarily on orthopedic and GI procedures. Customer expands into cardiology and neurology procedures not well-represented in training data. AI accuracy drops significantly for new procedure types. |
| Trigger event | Customer acquisition in new specialty. Existing customer expands service lines. |
| Likelihood | 4 (Likely) — Product growth will naturally expand into new specialties. Current training data is 80% ortho/GI. |
| Impact | 3 (Moderate) — AI quality drops for new specialties but baseline (ortho/GI) unaffected. Customer satisfaction impacted for new specialties. |
| Risk score | 12 (MEDIUM-HIGH) |
| Detection | (1) Track AI accuracy by procedure category. (2) Alert when coder acceptance rate by procedure category drops below 85%. (3) New specialty onboarding triggers manual evaluation of 200+ claims before enabling AI for that specialty. |
| Detection time | Days (if monitoring by category active) or weeks (if discovered via customer complaint). |
| Mitigation | (1) New procedure type onboarding process: manual evaluation of 200+ claims before AI enabled. (2) Active training data expansion into new specialties as customers are acquired. (3) Auto-detection: when claim's procedure codes fall outside training data distribution, auto-flag for human review regardless of AI confidence. |
| Contingency | If accuracy drops below threshold for a specialty: (1) Disable AI for that specialty. (2) Communicate to affected customers with timeline for resolution. (3) Prioritize training data acquisition and model fine-tuning for that specialty. |
| Owner | J. Chen (Product Lead) |
| Status | Monitored — New specialty onboarding process documented. Cardiology evaluation in progress (expected completion Aug 30). |
| Last reviewed | 2026-07-28 |

### RISK-005: Payer Policy Change Creates Systemic Coding Errors

| Field | Detail |
|-------|--------|
| Category | Deployment (Environmental Change) |
| Description | A major payer changes their coding policy (e.g., changes bundling rules for a high-volume procedure family). The AI, trained on historical policies, continues applying old rules. This creates a SYSTEMATIC error — every claim to that payer with that procedure is coded wrong. Unlike individual errors, systematic errors affect thousands of claims before detection. |
| Trigger event | Payer announces policy change (typically quarterly updates). Lag between announcement and effective date. |
| Likelihood | 5 (Almost Certain) — Payer policies change regularly. Major payers update policies quarterly. |
| Impact | 4 (Major) — Systematic error across all affected claims. High denial volume, potential audit triggers, revenue impact. |
| Risk score | 20 (CRITICAL) |
| Detection | (1) Payer policy change monitoring: subscribe to all major payer policy bulletins. (2) When new policy detected, run existing evaluation claims through updated rules — identify divergence. (3) Denial rate spike by payer+procedure combination triggers investigation. |
| Detection time | Days (policy monitoring) to weeks (denial rate detection) |
| Mitigation | (1) Dedicated process for tracking payer policy changes (clinical team + engineering). (2) AI system can be updated with new policy rules within 5 business days of publication. (3) For high-risk payer+procedure combinations, coding is flagged for human review for 30 days after any policy change. (4) Payer policy version metadata attached to every AI-coded claim — enables retrospective identification of claims affected by policy changes. |
| Contingency | If systematic error from policy change detected: (1) Determine affected time window from policy metadata. (2) Identify all affected claims (already submitted and in queue). (3) Correct and resubmit affected claims proactively (before payer denies them). (4) If claims already denied, bulk appeal with explanation. |
| Owner | Dr. S. Morrison (Clinical Domain Lead) + A. Patel (Engineering Lead) |
| Status | Mitigated — Policy change monitoring process active. 5-day update SLA tested for 2 major payer updates. Payer policy metadata implemented in v1.3. |
| Last reviewed | 2026-07-30 |
```

---

## Tool 6: AI Feature Launch Checklist

```markdown
# AI Feature Launch Checklist: [Feature Name]

## Pre-Launch

### Product Readiness
[ ] Evaluation contract completed and signed off by Product, Engineering, Compliance
[ ] Evaluation set of 500+ representative examples
[ ] Golden examples accuracy at 100%
[ ] Adversarial examples tested, results documented, mitigations implemented
[ ] Launch thresholds defined and measured (all mandatory gates passed)
[ ] Rollback thresholds defined, trigger conditions documented, procedure tested
[ ] Rollback drill completed successfully
[ ] Human review workflow operational, tested, staffed
[ ] Escalation SLA defined and communicated to review team

### Technical Readiness
[ ] Load testing at 2x projected peak volume (latency within thresholds)
[ ] Cost modeling at projected volume (within budget)
[ ] Monitoring dashboards built and tested
[ ] Alerts configured and tested (simulated failures triggered correct alerts)
[ ] Provider fallback tested (if using external API)
[ ] Prompt version control in place
[ ] Model version pinned (if using provider API)
[ ] Audit logging operational (inputs, outputs, model versions, human overrides)
[ ] Feedback collection mechanisms implemented and tested
[ ] Semantic caching implemented where appropriate
[ ] PII scrubbing verified (if applicable)
[ ] Data processing agreements signed (if using external providers)

### UX/Design Readiness
[ ] AI disclosure implemented (appropriate level for use case tier)
[ ] AI limitations communicated to users
[ ] Human escalation path visible and accessible
[ ] Error handling UX designed and implemented (for AI failures)
[ ] Feedback mechanism designed and implemented (explicit + implicit)
[ ] Empty/loading/error states designed for all AI-dependent UI elements
[ ] Progressive disclosure of AI capabilities implemented

### Compliance and Legal
[ ] AI use case registered in AI Use Case Register
[ ] Risk tier classification completed and documented
[ ] Bias audit completed, results within thresholds, documented
[ ] Privacy review completed (PII handling, data retention, DPAs)
[ ] Regulatory compliance verified (EU AI Act, GDPR, industry regs as applicable)
[ ] Transparency documentation published (internal and external as appropriate)
[ ] Terms of service / AI policy updated
[ ] Incident response plan documented and team briefed

### Organizational Readiness
[ ] Support team trained on AI feature (what it does, what it doesn't, how to triage)
[ ] Sales team trained (capabilities, limitations, competitive positioning)
[ ] Marketing materials prepared (accurate, not overpromising)
[ ] Internal communication sent (what's launching, to whom, when, how to report issues)
[ ] Success metrics defined and baseline measured
[ ] Feedback triage process defined (who reviews feedback, how quickly, what actions)

### Launch Plan
[ ] Launch segmentation defined (which users, what % rollout)
[ ] Gradual rollout plan (10% -> 25% -> 50% -> 100%) with gates at each stage
[ ] Launch communication prepared (in-app, email, blog, docs)
[ ] Monitoring war room scheduled for launch day + 3 days
[ ] Rollback decision authority designated (who can pull the plug)
[ ] Post-launch retrospective scheduled (2 weeks post-launch)

## Launch Day
[ ] Monitoring dashboard active and staffed
[ ] Initial rollout to 10% of target users
[ ] First hour: check all metrics, review first 50+ AI interactions
[ ] First day: no critical alerts, task success rate within threshold
[ ] First week: expand to 25%, then 50%, then 100% per gates

## Post-Launch
[ ] Daily quality review for first week
[ ] Weekly quality review for first month
[ ] First user feedback report (1 week)
[ ] First comprehensive quality assessment (2 weeks)
[ ] Post-launch retrospective (2 weeks)
[ ] Ongoing monitoring per evaluation contract cadence
```

---

## Tool 7: AI Product Health Dashboard Specification

Provide this specification to your engineering team to build an AI health dashboard.

```markdown
# AI Product Health Dashboard Specification

## Real-Time Panel (refreshes every 1-5 minutes)

### Quality Metrics
- Task Success Rate (gauge): Current vs Target | Trend (1h, 24h)
- Severe Error Rate (gauge): Current vs Threshold | Trend (1h, 24h)
- Golden Example Accuracy (gauge): Current vs Target | List of failed examples

### Operational Metrics
- Request volume (line chart): Per minute, 1h window
- p50/p95/p99 latency (line chart): 1h window
- Error rate (line chart): 5xx errors, timeout errors, tool call failures
- Model provider status (status indicator): Primary, Fallback

### Cost Metrics
- Cost per minute (counter): Current vs Budget | Daily cumulative cost
- Cost per task (gauge): Current vs Target | Trend (1h, 24h)

### User Metrics
- Active users (counter): 5min, 1h windows
- Acceptance rate (gauge): Current vs Target | Trend (1h)
- Escalation rate (gauge): Current vs Threshold

## Trends Panel (refreshes hourly/daily)

### Quality Trends
- Task Success Rate by day (bar chart): 30-day view
- Severe Error Rate by day (bar chart): 30-day view
- Hallucination Rate by category (stacked bar): Weekly

### User Behavior Trends
- Acceptance Rate by user cohort (line chart): 30-day view
- Override Rate by user segment (line chart): 30-day view
- Feature Adoption (cumulative users): 30-day view

### Cost Trends
- Daily AI Cost (bar chart): 30-day view vs Budget
- Cost per Task by model (stacked bar): Weekly
- Cost Efficiency Ratio: AI cost / Human cost (line chart): 30-day view

### Distribution Health
- Input distribution drift score (gauge): Current vs Baseline
- Embedding distribution visualization (scatter plot): Current distribution vs baseline

## Alerts Panel (active alerts)

| Alert | Severity | Triggered | Duration | Owner | Action |
|-------|---------|-----------|----------|-------|--------|
|       |         |           |          |       |        |

## Drill-Down Capabilities

From any metric, ability to drill down into:
- Individual task traces (full agent trace for a specific invocation)
- User session replay (what did the user see/do?)
- Model input/output pairs with human review annotations
- Cost breakdown by component for a specific time window
```

---

## Practical Application

1. Fill out the AI Use Case Assessment template for a feature you're considering.
2. Take your most important AI product and fill out at least 5 rows of the Risk Register.
3. Complete the Launch Checklist for your next AI feature launch. How many items can you check? What's missing?
4. Review your current AI product dashboard against the specification. What's missing? Prioritize the top 3 gaps.

---

## Discussion Prompts

1. Which template would be most immediately useful for your team? Why don't you have something like it today?

2. Look at the filled examples. How does your AI product's rigor compare? Where are you stronger? Where are you weaker?

3. What's the most critical risk in your AI product that ISN'T in your current risk tracking? Why isn't it there?

4. How many of the Launch Checklist items can you check for your most recent AI feature launch? What's the biggest gap?

5. Would your CEO sign off on a decision memo in the format provided here? If not, what would they need that's missing?
