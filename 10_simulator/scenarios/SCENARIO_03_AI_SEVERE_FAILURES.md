# Scenario 03: AI Workflow — 98% Success, 2% Catastrophic Failure

| Field | Value |
|-------|-------|
| **scenario_id** | SIM-003 |
| **title** | AI Workflow — 98% Success, 2% Catastrophic Failure |
| **leadership_level** | Senior PM, Principal PM, Director |
| **primary_tension** | Performance vs. harm in edge cases |
| **key_capability** | Ethical trade-off reasoning |
| **estimated_time** | 45 minutes |
| **related_principles** | PRN-0014 (AI Product Decisions), PRN-0003 (Cost of Delay vs. Imperfection), PRN-0011 (Ethics in Product Leadership) |

## Situation

You are the **Product Lead for AI** at **CareConnect**, a digital health platform that provides virtual care coordination for chronic disease patients. The platform serves 2.3 million patients across 14 health systems. CareConnect's core workflow is care coordination: when a patient is discharged from a hospital, the platform coordinates follow-up appointments, medication reconciliation, specialist referrals, and home care instructions.

Six months ago, CareConnect launched **AutoTriage**, an AI-powered workflow that automatically prioritizes patient follow-up cases based on clinical risk. The system ingests discharge summaries, lab results, medication lists, and patient demographics, then classifies each case into one of four risk tiers:
- **Critical (Red):** Requires immediate clinician review (within 2 hours)
- **High (Orange):** Requires same-day review
- **Routine (Yellow):** Standard follow-up within 72 hours
- **Low (Green):** Automated management with patient self-service

The results have been strong:
- 30% faster time-to-review for Critical cases (from 4.2 hours to 2.9 hours average)
- 18% reduction in 30-day readmission rates across the platform
- Clinicians report 25% less burnout because the system filters out low-acuity noise
- 98% classification accuracy across all 500,000 cases processed so far
- Covered in Modern Healthcare and STAT News as an "AI success story in clinical operations"

### The Problem

Last week, your clinical safety team flagged two incidents that came through the adverse event reporting system:

**Case A:** A 72-year-old patient, Mrs. Chen, with congestive heart failure and COPD was classified as "Routine" by AutoTriage. Her discharge summary mentioned "mild pedal edema" (foot swelling) in one sentence buried in a 14-page document. In a patient with CHF, pedal edema is a potential indicator of fluid overload and impending heart failure decompensation. Because AutoTriage classified her as Routine, she was scheduled for a 72-hour follow-up call. At 48 hours, she was readmitted to the ER with acute heart failure. The classifying clinician (who escalated to Critical) caught it 24 hours too late because AutoTriage had down-ranked the case.

**Case B:** A 34-year-old patient, Mr. Torres, with Type 1 diabetes was classified as "Low" by AutoTriage. His discharge summary noted "blood glucose 280 mg/dL at discharge" (normal is 70-180). The system flagged this as "elevated but consistent with post-discharge status for T1D." However, the summary also mentioned — in a separate section added by a social worker, not a physician — that the patient "reports running out of insulin 4 days before admission and rationing remaining supply." This social determinant of health (SDOH) data was in a non-standard field that the AI model was not trained to weight appropriately. The patient was re-admitted 5 days later with diabetic ketoacidosis (DKA), a life-threatening condition.

Both patients are from vulnerable populations: Mrs. Chen is a non-English-speaking elderly patient on Medicare; Mr. Torres is an undocumented immigrant who relies on a safety-net hospital's charity care program.

The aggregate numbers are confusing. 98% accuracy sounds excellent. But the 2% failure rate means approximately 10,000 misclassified cases per year. And the cases being misclassified disproportionately involve:
- Patients with complex comorbidities (multiple chronic conditions)
- Patients whose clinical data is scattered across non-standard fields (social work notes, physical therapy notes, dietary consults)
- Patients from vulnerable populations whose clinical presentations are underrepresented in the training data
- Non-English-speaking patients whose discharge instructions may not be fully captured in structured fields

In other words: the system is failing exactly where human clinicians add the most value — and where the consequences of failure are most severe.

### The Human Baseline

Before AutoTriage, care coordinators manually reviewed every case. The human baseline error rate was approximately 7% — meaning humans missed or down-ranked about 7% of cases that should have been higher priority. But critically, human errors were randomly distributed across the patient population. They did not systematically fail on vulnerable patients. The AI system's 2% error rate is better overall but systematically biased — and 2% of cases that should be Critical being missed is a different kind of failure than 7% of cases being slightly delayed.

### The Decision

Your CEO, **Dr. Sarah Williams** (a physician by training), called an emergency meeting after the clinical safety report. She asked you three questions:

1. "Should we turn AutoTriage off until we understand and fix the failure pattern?"
2. "If we keep it running, what do we tell our health system customers about these failures?"
3. "What's your plan for making this safe, and how long will it take?"

The engineering team estimates that fixing the systematic failure pattern — retraining the model on better representative data, adding SDOH fields to the model, and building a fairness evaluation framework — would take 4-6 months. During that time, the system would continue operating with the known failure pattern. Turning it off means reverting to human-only triage, which would:
- Increase time-to-review for Critical cases by approximately 45% (back to 4.2 hours average)
- Add approximately 40 hours/week of manual review work across the care coordination team
- Lose the 18% reduction in readmissions
- Potentially damage CareConnect's reputation as an AI innovator

## Characters

**Dr. Sarah Williams (CEO).** Physician-entrepreneur. Started CareConnect after her father was readmitted following a missed follow-up. Genuinely committed to patient outcomes. Has publicly championed "responsible AI in healthcare." Motivated by: patient safety, company mission, not becoming a cautionary tale about AI in healthcare.

**Dr. James Okonkwo (Chief Medical Officer).** Practicing hospitalist who works shifts every other weekend. The clinical safety report came from his team. He is concerned but not alarmist. His instinct is "we have a problem we need to fix, but we shouldn't throw away a system that is helping more patients than it's hurting." Motivated by: clinical evidence, patient outcomes, physician trust in the platform.

**Priya Mehta (VP Engineering).** Built the AutoTriage team. Proud of the 98% accuracy number. Worried that "turning it off" will demoralize her team and set an impossible precedent — no AI system is perfect, so does every failure pattern trigger a shutdown? Motivated by: engineering team morale, shipping velocity, avoiding a blame culture.

**Michael Chen (Head of Clinical Safety).** Reported the two cases. Has been warning for weeks that the model's performance metrics masked systematic bias. Feels vindicated but also anxious — he doesn't want to be seen as "the person who killed the AI project." Motivated by: patient safety, professional integrity, being taken seriously by leadership.

**Kira Johnson (VP of Customer Success).** Manages relationships with the 14 health system customers. Two of them have already heard about "issues with AutoTriage" through clinical networks and are asking questions. She needs a communication plan before the narrative spins out of control. Motivated by: customer retention, trust, not having to explain a scandal.

**Your AI/ML Team Lead (Dr. Amir Bashir).** PhD in machine learning with a focus on fairness in clinical AI. He has been advocating for representative training data and fairness testing for 8 months but was told to "ship first, improve later." He is frustrated but not vindictive. He has a concrete plan for fixing the model but estimates 4-6 months. Motivated by: scientific rigor, fairness, building AI that actually helps everyone.

## Constraints

- The system is live. Every day it runs, it processes approximately 1,400 new cases.
- Turning it off requires a rollback to the previous manual triage workflow, which has its own failure rate (7% human error, randomly distributed).
- The fix requires more representative training data, which means negotiating data-sharing agreements with health systems that serve vulnerable populations — a process that could add months.
- Regulatory: FDA and HHS have both signaled increased scrutiny of clinical AI. An adverse event that becomes public could trigger an investigation.
- Reputation: STAT News and other outlets are watching. A story about AI failing vulnerable patients writes itself.
- The engineering team is already at capacity. There is no "extra" team to work on the fix while the current system continues operating.

## Your Role

You are the Product Lead for AI at CareConnect. You own AutoTriage as a product. You report to the CEO (Dr. Williams). You are responsible for the product's outcomes, safety, and roadmap. You have the authority to recommend turning the system off, keeping it running with modifications, or any intermediate option. You do not have unilateral authority — the decision goes through Dr. Williams and likely the board.

## Response Format

### Part 1: Assumptions

List your assumptions with confidence labels. Key areas to address:
- The nature of the failure pattern: is it bias in the training data, a model architecture problem, or a workflow design problem?
- The pace of harm: how many patients per week are being misclassified in ways that could lead to adverse events?
- The regulatory and reputational risk timeline
- The feasibility of a "safe mode" that combines AI and human review
- What Dr. Williams actually needs from you (a decision or a decision framework?)

### Part 2: Decision

Describe your decision with:
- **What you will do.** Specific actions, timeline, resource allocation.
- **What you will NOT do.** Explicit trade-offs.
- **Communication plan.** What you say to the health system customers, to the media (if asked), to your own team, to the board.
- **Metrics for safety during remediation.** What metrics will you track to ensure the system is getting safer (not just more accurate) during the fix period?

### Part 3: Pre-Mortem

Assume your decision was implemented. 12 months later, it failed. Write a specific pre-mortem. At least 3 distinct failure paths must include: a failure related to the model fix, a failure related to organizational incentives, and a failure related to external stakeholders (regulators, media, customers).

---

## Scoring Rubric (Scenario-Specific)

### Ethical Trade-Off Reasoning

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Binary thinking ("shut it down" or "the numbers are good, keep running"). No recognition that 98% overall accuracy with systematic bias is a different ethical problem than 98% accuracy with random error. |
| 3 | Recognizes that distribution matters more than aggregate accuracy. Identifies the tension between "helping more patients overall" and "systematically harming a specific vulnerable group." |
| 4 | Engages with the utilitarian vs. deontological tension explicitly: "A system that helps 100 patients but predictably harms 2 is morally different from a system that helps 98 patients and unpredictably misses 2." Proposes a framework for deciding when aggregate benefit justifies systematic harm. |
| 5 | Reframes the question from "should we turn it off?" to "what conditions must be met for this system to be ethically defensible?" Defines those conditions — representative data, fairness metrics, clinician-in-the-loop for vulnerable populations, transparency to patients — and makes the fix plan conditional on meeting them. |

### Evidence and Metrics

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Relies on the 98% accuracy number without interrogating what it hides. No fairness metrics proposed. |
| 3 | Proposes fairness metrics (false negative rate by demographic group, error rate by comorbidity count, detection rate for SDOH-related cases). |
| 4 | Defines safety metrics that are leading indicators (not just after-the-fact adverse event reports). Proposes monitoring systems that detect failure patterns before they cause harm, not after. |
| 5 | Designs a multi-layered safety system: real-time model monitoring for fairness degradation, clinical override tracking (how often do clinicians override the AI and why?), patient outcome tracking by demographic segment, and an independent clinical safety review board with external members. |

### Stakeholder and Incentive Analysis

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Assumes all stakeholders are aligned on "patient safety." Misses the career incentives (Priya's team morale, Michael's credibility, Kira's customer relationships). |
| 3 | Distinguishes between each stakeholder's stated goal (patient safety) and their latent concerns (career risk, team morale, professional reputation). |
| 4 | Identifies the coalition dynamics: Priya and James may ally to "keep the system running with fixes" while Michael and Amir may ally for "significant changes or shutdown." Kira is the swing vote — she cares about customer trust, which cuts both ways (trust is damaged by both failure and arbitrary shutdown). |
| 5 | Proposes specific interventions to align incentives: position the fix as a platform investment that makes CareConnect the leader in responsible AI (Priya's team gets to build state-of-the-art fairness infrastructure, not just fix bugs); give Michael a visible leadership role in the remediation (his credibility concern is addressed); give Kira a communication framework that positions transparency as a competitive advantage. |

### Pre-Mortem Quality

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Generic AI failure modes ("the model was biased," "regulators got involved"). |
| 3 | Specific, causal failure mechanisms: "The model retraining used data from academic medical centers, which over-represented insured populations, making the SDOH detection WORSE for the vulnerable populations it was supposed to help." |
| 4 | Includes organizational failure modes: "Dr. Williams lost patience with the 6-month fix timeline and pushed the team to ship the 'improved' model at 4 months, before fairness testing was complete. The model looked better on aggregate metrics but still failed on the same vulnerable populations because the training data problem wasn't actually solved." |
| 5 | Includes industry/systemic failure modes: "A competitor launched a competing AI triage system that reported 99% accuracy (with no fairness reporting), creating market pressure to downplay the failure rate. Sales started using the 98% number again. The press got wind of the original incidents plus the new ones and ran a story: 'CareConnect knew its AI was biased for 18 months and kept it running.' HHS opened an investigation." |

---

## Facilitator Notes

**Common traps:**
1. Treating this as a purely technical problem ("retrain the model, problem solved"). The bias is in the data, the workflow design, and the organizational incentives — not just the model weights.
2. Failing to recognize that the current system is actively harming patients every day it continues operating. A 6-month fix timeline means 6 more months of systematic harm to vulnerable patients.
3. Assuming "transparency" (telling customers about the failures) is always the right move without considering what customers will actually do with that information — some may demand immediate shutdown, which could harm more patients than the status quo.
4. Proposing "we'll keep the AI but add human review for all cases" without doing the math: that's the manual workflow plus the AI workflow, with the cost of both.

**Discussion prompts:**
- Is it ever acceptable to run a system that you know systematically harms a specific group of people, even if it helps more people overall? Under what conditions?
- If you were Mrs. Chen's family member, what would you want CareConnect to do?
- How would your answer change if the failure rate was 0.2% instead of 2%? What about 5%?
- What does "fairness" mean in this context? Equal accuracy across groups? Equal false negative rates? Something else?
- If the board asks you "can we get sued for this?" — what do you say?

**Related Academy Content:**
- [PRN-0014](../../01_core_doctrine/PRINCIPLES.md): AI product management principles
- [PRN-0011](../../01_core_doctrine/PRINCIPLES.md): Ethics in product leadership
- [05_ai_product_management/](../../05_ai_product_management/): AI-specific frameworks
