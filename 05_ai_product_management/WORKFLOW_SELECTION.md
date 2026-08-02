# Workflow Selection: Identifying AI-Appropriate Use Cases

**Status:** v0.1.0
**Depends on:** Product Archetypes (Module 04), Core Doctrine (Module 01)

---

## TL;DR

Before you ask "which model should we use?" or "how should we prompt this?" ask "should AI be doing this at all?" Most AI product failures trace back to poor workflow selection — choosing a use case that AI can't reliably perform, one where the error cost exceeds the automation value, or one where a deterministic solution would be cheaper and more reliable.

This file provides a structured methodology for answering: **Is this workflow appropriate for AI?**

---

## Part 1: Workflow-Centric vs Model-Centric Thinking

### The Model-Centric Trap

The most common AI product mistake is model-centric thinking:

> "GPT-5 can do X. Let's build a product that does X."

This approach produces:
- **Solutions looking for problems** — Features that use impressive AI capabilities but don't solve a real user need
- **Fragile demos that never ship** — The model does X in a controlled demo but fails on real-world inputs
- **Benchmark-chasing products** — Products optimized for leaderboard scores rather than user outcomes
- **Perpetual model-swapping** — Endless cycles of "the next model will fix it" without addressing system-level issues

### Workflow-Centric Thinking

Workflow-centric thinking starts from the opposite direction:

> "Here is a workflow that humans do. What would it mean to automate or augment parts of it? Which parts are appropriate for AI? Which are not?"

This approach has the advantage of:
- **Grounding in observable reality** — The workflow exists today. You can study it, measure its current performance, and understand its failure modes.
- **Defining success in workflow terms** — Success means the workflow completes with acceptable quality, cost, and time — not that the model achieved a high benchmark score.
- **Identifying intervention points precisely** — You don't need to AI-ify the entire workflow. You can identify specific subtasks where AI adds value and leave the rest to humans or deterministic systems.
- **Surfacing the unit economics** — When you understand the human workflow, you can compare the cost and quality of human execution to AI execution on a per-task basis.

### The Workflow Decomposition Methodology

For any candidate workflow, answer these questions in order:

#### Step 1: Describe the workflow without mentioning AI

```
Who: [user role]
What: [the task they're trying to accomplish]
Input: [what information they start with]
Output: [what they produce]
Constraint: [time, quality, regulatory, resource constraints]
Current performance: [how well it works today, measured]
```

**Example — Medical coding:**

*Who:* Medical coders in a hospital billing department
*What:* Review clinical documentation and assign ICD-10, CPT, and HCPCS codes for insurance reimbursement
*Input:* Physician notes, lab results, procedure documentation (unstructured or semi-structured)
*Output:* Coded encounter with procedure codes, diagnosis codes, and modifiers
*Constraint:* Must comply with payer-specific coding guidelines. Error rate target <3%. Turnaround <24 hours for inpatient, <48 hours for outpatient.
*Current performance:* 96.8% accuracy, $4.25 per encounter (fully loaded), 18-hour average turnaround

Notice that AI is not mentioned. The workflow exists independently of AI. Your job is to understand it deeply before introducing AI.

#### Step 2: Decompose the workflow into subtasks

Not all parts of a workflow benefit equally from AI. Decompose into:

| Subtask | Type | Input | Output | Difficulty for Humans | Current Error Rate | Frequency of Exception Cases |
|---------|------|-------|--------|----------------------|--------------------|------------------------------|
| Extract diagnoses from notes | Information extraction | Free text | Structured diagnosis list | Low | 1.2% | 15% |
| Map diagnoses to ICD-10 codes | Classification/retrieval | Diagnosis list | ICD-10 code list | Medium | 2.8% | 25% |
| Apply payer-specific rules | Rule application | Codes + payer | Modified code list | High | 4.1% | 40% |
| Verify code bundling rules | Rule checking | Code list | Validated code list | Low | 0.5% | 5% |
| Add modifiers for special circumstances | Judgment | Clinical context | Modifier list | High | 6.2% | 30% |

#### Step 3: Classify each subtask by AI suitability

For each subtask, score it on three dimensions (1-5 scale):

**Determinism:** How clear is the correct answer?
- 5 = There is exactly one correct answer given the input (e.g., mathematical calculation)
- 4 = There is a clear rule set that determines correctness (e.g., tax calculation)
- 3 = There are guidelines but interpretation is required (e.g., content moderation against a policy)
- 2 = Correctness depends heavily on context and judgment (e.g., prioritizing features)
- 1 = Correctness is inherently subjective or creative (e.g., brand voice, strategic vision)

**Error Tolerance:** What is the consequence of being wrong?
- 5 = Errors are inconsequential or trivially correctable (e.g., autocomplete suggestions)
- 4 = Errors create minor rework or annoyance (e.g., wrong categorization in a search facet)
- 3 = Errors create moderate cost or delay (e.g., routing a support ticket to the wrong team)
- 2 = Errors create significant financial, legal, or safety consequences (e.g., missed medical diagnosis)
- 1 = Errors are catastrophic (e.g., autonomous vehicle collision, financial fraud approval)

**Automation Value:** How much value does automation create?
- 5 = Huge volume, repetitive, expensive human labor (e.g., document processing at scale)
- 4 = High volume, moderate human cost, quality improvement opportunity
- 3 = Moderate volume, some cost savings, quality improvement possible
- 2 = Low volume or low human cost, marginal improvement
- 1 = Rare task, specialized skill, automation adds negligible value

#### Step 4: Plot on the AI Suitability Matrix

Combine the three scores. The sweet spot for AI is:

```
High Determinism  +  High Error Tolerance  +  High Automation Value
     (4-5)                (4-5)                      (4-5)
```

The danger zones are:

```
Low Determinism   +  Low Error Tolerance   +  High Automation Value
     (1-2)               (1-2)                       (4-5)
```

This is the combination where automation is tempting (high volume, expensive humans) but AI is likely to produce consequential errors because the task requires judgment and the cost of being wrong is high.

---

## Part 2: Value Assessment vs Technical Novelty Assessment

### The Innovation Error

A common failure pattern among product leaders with technical backgrounds:

> "This is a novel application of AI. The paper just came out. We could be first to market."

The error is conflating technical novelty with product value. They are uncorrelated. Many technically novel AI applications create zero product value. Many mundane AI applications (using decade-old techniques) create enormous product value.

### The Value-First Framework

Before assessing technical feasibility, assess product value using a framework that doesn't mention AI:

#### Problem Value Score (PVS)

Rate each of these on 1-5:

| Dimension | 1 (Low) | 3 (Moderate) | 5 (High) |
|-----------|---------|--------------|----------|
| **Frequency** | Happens once per quarter per user | Happens weekly per user | Happens multiple times per day per user |
| **Pain** | Minor annoyance with workaround | Moderate friction, costs 15-30 min | Mission-critical, blocks work, costs hours |
| **Willingness to pay** | Wouldn't pay for a solution | Would accept as part of existing subscription | Would pay separately for a solution |
| **Market size** | <1,000 potential users | 10,000–100,000 potential users | >1,000,000 potential users |
| **Strategic alignment** | Peripheral to company strategy | Supports current strategy | Core to current strategy |

**PVS = (Frequency + Pain + WTP + Market + Strategic) / 5**

- PVS ≥ 4.0: Strong product case. Proceed to technical assessment.
- PVS 3.0–3.9: Questionable. Only proceed with strong evidence that PVS is understated or that this is a wedge into a higher-PVS opportunity.
- PVS < 3.0: Do not build. The problem doesn't matter enough.

#### Technical Novelty Assessment (TNA)

Only after passing the PVS gate, assess technical feasibility:

| Dimension | 1 (Hard) | 3 (Moderate) | 5 (Easy) |
|-----------|----------|--------------|----------|
| **Existing solutions** | No known approach works | Published approaches exist but not productionized | Commodity capability, multiple providers offer it |
| **Data availability** | No labeled data exists, hard to generate | Some data exists, moderate labeling effort | Rich labeled data exists or can be auto-generated |
| **Determinism** (from above) | Subjective/creative task | Guidelines exist but interpretation needed | Clear correct answer |
| **Error tolerance** (from above) | Errors are catastrophic | Errors create moderate cost | Errors are trivial |

**TNA = (Solutions + Data + Determinism + Error Tolerance) / 4**

- TNA ≥ 4.0: Strong technical case. AI is a good fit for this workflow.
- TNA 3.0–3.9: Moderate difficulty. Proceed with expectation of significant engineering investment in evaluation, guardrails, and human-in-the-loop.
- TNA < 3.0: High risk. Do not proceed unless (a) the PVS is exceptionally high (>4.5) AND (b) you have a credible path to improving TNA through data acquisition, system design, or staged deployment.

### The PVS-TNA Matrix

| | TNA High (4-5) | TNA Medium (3-3.9) | TNA Low (1-2.9) |
|---|---|---|---|
| **PVS High (4-5)** | BUILD NOW — Strong product and technical case | INVESTIGATE — Build evaluation harness, validate with real data | HIGH-RISK BET — Only with exceptional PVS and credible research path |
| **PVS Medium (3-3.9)** | OPPORTUNISTIC — Build if engineering cost is low | MONITOR — Wait for technical maturity or PVS increase | DO NOT BUILD |
| **PVS Low (1-2.9)** | DO NOT BUILD — Solution looking for a problem | DO NOT BUILD | DO NOT BUILD |

---

## Part 3: When NOT to Use AI

### The Anti-Pattern Catalog

Knowing when to say no is more important than knowing when to say yes. Here are the situations where AI is the wrong answer:

#### 1. Deterministic solution exists and works well

If you can solve the problem with a database lookup, a rules engine, a deterministic algorithm, or a well-structured API call, do that. AI introduces probabilistic failure where none is necessary.

**Example:** "Let's use AI to calculate sales tax."
**Correction:** Sales tax is deterministic (given location, product category, and transaction type). A tax calculation API is faster, cheaper, and has zero error rate. Using AI here adds cost, latency, and error for zero benefit.

#### 2. Error cost exceeds automation value

If getting the answer wrong creates more cost than the automation saves, AI is inappropriate unless you have a human-in-the-loop review step — which may eliminate the cost savings.

**Example:** "Let's use AI to approve mortgage applications."
**Correction:** The cost of a single bad mortgage decision (hundreds of thousands of dollars) far exceeds the cost of human underwriting (hundreds of dollars per application). AI might flag obvious approvals or denials for triage, but should not make the final decision unless error rates approach human levels AND you have acceptable recourse mechanisms.

#### 3. Training data doesn't exist and can't be generated

AI models learn from examples. If you don't have examples of the task being done correctly (and incorrectly), you cannot build a reliable AI system for that task. This is different from "we have a few examples." You need sufficient volume and diversity to cover the input distribution.

**Example:** "Let's use AI to detect novel types of fraud we've never seen before."
**Correction:** By definition, novel fraud has no examples. AI can detect variations of known fraud patterns, but cannot reliably detect genuinely novel patterns. This requires rules-based anomaly detection or human investigation.

#### 4. The task requires causal reasoning, not pattern matching

AI models are pattern matchers, not causal reasoners. They excel at "given X, Y typically follows" but fail at "if we change X, what happens to Y?" — the counterfactual reasoning that defines causal understanding.

**Example:** "Let's use AI to decide our product strategy."
**Correction:** Strategy requires causal reasoning about counterfactuals: "If we enter this market, how will competitors respond? If we lower price, how does that change unit economics?" AI can provide inputs (market analysis, competitive intelligence summaries) but cannot make the causal inference.

#### 5. The cost structure destroys unit economics

AI inference costs money. For high-volume, low-value-per-transaction workflows, AI inference costs can exceed the value created. This is especially true for LLM-based systems where each token costs money.

**Example:** "Let's use an LLM to classify every user click as 'engaged' or 'not engaged.'"
**Correction:** A trained classifier (small model) costs fractions of a penny per inference. An LLM might cost $0.01–$0.10 per inference. On 100M clicks/day, the difference is $1,000/day vs $10,000,000/day.

#### 6. Latency requirements are below AI inference time

If the workflow requires sub-100ms responses and your AI system takes 500ms+, AI is inappropriate — or requires a hybrid architecture (caching, pre-computation, speculative execution).

**Example:** "Let's use AI to generate personalized content on every page load."
**Correction:** Page load budgets are typically 1-2 seconds total. If AI inference adds 500ms per component, you can't use it inline. Solutions: pre-generate content, cache common patterns, use AI for async content that loads progressively.

#### 7. You can't measure success

If you cannot define what "good" looks like in measurable terms, you cannot evaluate an AI system, which means you cannot improve it, which means you should not ship it.

**Example:** "Let's use AI to make the product 'more delightful.'"
**Correction:** "Delightful" is not measurable. Define the specific behaviors that correlate with delight (e.g., reduced time to first value, increased feature discovery, reduced support tickets) and measure those.

#### 8. Regulatory environment prohibits it

Some jurisdictions and industries have explicit or de facto prohibitions on automated decision-making for certain use cases. Check before building, not after.

**Example:** GDPR Article 22 restricts automated individual decision-making with legal or similarly significant effects. EU AI Act classifies certain use cases as unacceptable risk (banned) or high risk (requires conformity assessment).

---

## Part 4: Product Value vs Model Performance Distinction

### The Benchmark Illusion

Model providers publish benchmarks: MMLU, HumanEval, GSM8K, HELM, etc. These measure model capabilities in controlled, artificial settings. They correlate weakly — and sometimes not at all — with product performance on real user workflows.

Key limitations of model benchmarks:

1. **Contaminated training data** — Many benchmark questions are memorized during training. High benchmark scores reflect memorization, not reasoning.
2. **Uniform difficulty** — Benchmarks have calibrated difficulty. Real-world inputs have a long tail of edge cases the benchmarks don't cover.
3. **No user context** — Benchmarks test the model in isolation. Products have context (user history, preferences, domain knowledge) that benchmarks ignore.
4. **No cost dimension** — Benchmarks don't measure cost, latency, or throughput. A model with 5% higher benchmark accuracy but 10x cost may be worse for your product.
5. **No failure correlation** — Benchmarks don't tell you what kinds of failures the model makes and whether those failures matter for your use case.

### The Product Performance Model

Instead of model benchmarks, define product performance in terms of your specific workflow:

| Dimension | Definition | Example Metric |
|-----------|-----------|----------------|
| **Task success rate** | What % of user tasks are completed successfully without human intervention? | 92% of customer support inquiries resolved without escalation |
| **Error severity distribution** | When errors occur, how severe are they? | <0.1% severe errors (wrong answer with financial consequence) |
| **Time to resolution** | How long does it take to complete the workflow end-to-end? | 95th percentile: <2 minutes (down from 45 minutes) |
| **User trust** | Do users trust the system enough to use it? | >80% acceptance rate (users accept AI output without modification) |
| **Exception handling** | How well does the system handle edge cases? | >95% of edge cases detected and escalated to humans |
| **Cost per task** | What does it cost to complete one workflow instance? | $0.15/task (down from $4.25/task for human-only) |
| **Outcome quality** | Does the output achieve the business objective? | 97% first-pass approval rate for coded medical claims (same as human) |

### Measuring Product Performance Before Model Selection

The sequence should be:

1. **Define the workflow** (this file, Part 1)
2. **Define product performance metrics** (this section)
3. **Build an evaluation harness** that measures these metrics (EVALUATION_CONTRACTS.md)
4. **Test existing models** against your evaluation harness
5. **Identify failure patterns** (FAILURE_MODES.md)
6. **Design system mitigations** (MODEL_VS_SYSTEM.md, AGENT_ARCHITECTURE.md)
7. **Iterate on the system** until product performance meets thresholds
8. **Only then select a production model** based on real product performance, not benchmark scores

The error most teams make is jumping from step 1 directly to step 8: "This looks like a good use case, let's use the best model." They skip evaluation, skip failure analysis, skip system design — and wonder why their product doesn't work.

---

## Part 5: The Selection Decision Memo

When you've completed the analysis above, document your workflow selection decision in a brief memo. This memo is your quality gate — if you can't complete it convincingly, you're not ready to build.

### Memo Template

```
# AI Workflow Selection: [Workflow Name]

## 1. Workflow Description (without AI)
[Step 1 output from Part 1]

## 2. Subtask Decomposition
[Step 2 output from Part 1]

## 3. AI Suitability Assessment
[Step 3-4 output from Part 1, with PVS and TNA scores]

## 4. Anti-Pattern Check
[Confirm none of the 8 anti-patterns apply, or explain mitigation]

## 5. Product Performance Metrics
[Part 4 metrics with target thresholds]

## 6. Non-AI Alternative
What is the best non-AI solution to this problem? Why is AI better?

## 7. Key Risks and Mitigations
[Top 3 risks and how you'll mitigate them]

## 8. Decision
[BUILD / INVESTIGATE / MONITOR / DO NOT BUILD]

## 9. Sign-off
Product Lead: ___________ Date: ___________
Engineering Lead: ___________ Date: ___________
Data Science Lead: ___________ Date: ___________
```

---

## Practical Application

Take a product or feature you're currently considering for AI augmentation. Work through the following:

1. Write the workflow description without mentioning AI.
2. Decompose it into subtasks.
3. Score each subtask on the AI suitability dimensions.
4. Calculate the PVS and TNA.
5. Check against the anti-pattern catalog.
6. Write the selection decision memo.

If you cannot convincingly complete all six steps, you have more analysis to do before building.

---

## Discussion Prompts

1. What AI features has your organization built that would have failed the PVS/TNA assessment? What happened to those features?

2. What non-AI solutions exist for problems where your team has proposed AI? Why is AI better?

3. What workflows in your product have high determinism, high error tolerance, and high automation value — but you haven't considered AI for them because they're "boring"?

4. What model benchmarks does your team cite when making AI product decisions? Have you measured correlation between those benchmarks and real product performance? If not, why not?

5. Describe a situation where you said "no" to an AI feature. What was your reasoning? In retrospect, was the decision correct?
