# AI PM Playbook

**A focused playbook for product leaders making AI product decisions.**

**Status:** v0.1.0  
**Prerequisites:** Core doctrine (Track 01); AI archetype (Archetype 5); `handbook/PRODUCT_LEADERSHIP_BIBLE.md` for doctrine context

---

## 1. The AI PM Mandate

**[E]** Every product leader will make AI-related product decisions within the next 3 years. Not "might" — will. The question is not "should we use AI?" but "where should we use AI, how do we evaluate it, and how do we govern it?"

**[P]** AI product management is not a specialization for a few PMs with ML backgrounds. It's becoming a core competency for all PMs. The AI PM's job is not to build models — it's to make product decisions about where, when, and how to use AI capabilities to solve user problems.

**[R]** If you are a PM and you don't understand AI product management, your career is at risk — not because AI will replace PMs, but because PMs who CAN make AI product decisions will be chosen over PMs who can't.

---

## 2. When to Use AI (and When Not To)

### 2.1 The Workflow-First Methodology

**[E]** The most common AI product mistake is model-centric thinking: "Model X can do Y. Let's build a product that does Y." This produces solutions looking for problems, fragile demos that never ship, and benchmark-chasing products.

**[P]** The Academy's counter-methodology: workflow-centric thinking. Start from the human workflow. Decompose it. Identify which subtasks are appropriate for AI. Leave the rest to humans or deterministic systems.

**[R]** Before any AI product decision, work through the Workflow Selection methodology (`05_ai_product_management/WORKFLOW_SELECTION.md`):

**Step 1: Describe the workflow without mentioning AI**
```
Who: [user role]
What: [task they're trying to accomplish]
Input: [what information they start with]
Output: [what they produce]
Constraint: [time, quality, regulatory, resource constraints]
Current performance: [how well it works today, measured quantitatively]
```

**Step 2: Decompose into subtasks**

| Subtask | Type | Input | Output | Human Difficulty | Current Error Rate | Exception Frequency |
|---------|------|-------|--------|-----------------|--------------------|---------------------|

**Step 3: Score each subtask on AI suitability (1-5)**

- **Determinism:** How clear is the correct answer? (5 = exactly one correct answer; 1 = inherently subjective)
- **Error Tolerance:** What is the consequence of being wrong? (5 = inconsequential; 1 = catastrophic)
- **Automation Value:** How much value does automation create? (5 = huge volume, expensive human labor; 1 = rare, specialized task)

**Step 4: Plot on the AI Suitability Matrix**
- Sweet spot: High Determinism (4-5) + High Error Tolerance (4-5) + High Automation Value (4-5)
- Danger zone: Low Determinism (1-2) + Low Error Tolerance (1-2) + High Automation Value (4-5) — tempting but dangerous

### 2.2 The Anti-Pattern Catalog: When NOT to Use AI

**[R]** Before proposing AI for any workflow, check against these eight anti-patterns. If any apply, AI is the wrong solution.

**Anti-Pattern 1: Deterministic solution exists and works well.**
If a rules engine, database lookup, or deterministic algorithm solves the problem, use it. AI introduces probabilistic failure where none is necessary.
*Example: "Use AI to calculate sales tax." → Correction: Tax is deterministic. Use a tax API.*

**Anti-Pattern 2: Error cost exceeds automation value.**
If getting the answer wrong costs more than the automation saves, AI is inappropriate — unless you have human-in-the-loop review that doesn't eliminate the savings.
*Example: "Use AI to approve mortgage applications." → Correction: The cost of one bad mortgage exceeds the cost of human underwriting. Use AI for triage, not decision.*

**Anti-Pattern 3: Training data doesn't exist and can't be generated.**
AI models learn from examples. Without sufficient volume and diversity of examples, you cannot build a reliable AI system.
*Example: "Use AI to detect novel types of fraud we've never seen." → Correction: By definition, novel fraud has no examples. Use rules-based anomaly detection.*

**Anti-Pattern 4: The task requires causal reasoning, not pattern matching.**
AI models are pattern matchers, not causal reasoners. They fail at counterfactual reasoning: "if we change X, what happens to Y?"
*Example: "Use AI to decide our product strategy." → Correction: Strategy requires causal reasoning about counterfactuals. AI can provide inputs, not decisions.*

**Anti-Pattern 5: Cost structure destroys unit economics.**
AI inference costs money. For high-volume, low-value-per-transaction workflows, AI costs can exceed value.
*Example: "Use an LLM to classify every user click." → Correction: A trained classifier costs fractions of a penny per inference. An LLM might cost $0.01-0.10.*

**Anti-Pattern 6: Latency requirements are below AI inference time.**
If the workflow requires sub-100ms responses and your AI takes 500ms+, AI is inappropriate for inline use.
*Example: "Use AI to generate personalized content on every page load." → Correction: Pre-generate or use async loading.*

**Anti-Pattern 7: You can't measure success.**
If you can't define what "good" looks like in measurable terms, you can't evaluate an AI system, which means you can't improve it, which means you shouldn't ship it.
*Example: "Use AI to make the product more delightful." → Correction: "Delightful" isn't measurable. Define specific, measurable behaviors.*

**Anti-Pattern 8: Regulatory environment prohibits it.**
Some jurisdictions prohibit automated decision-making for certain use cases. Check BEFORE building.
*Example: GDPR Article 22 restricts automated individual decision-making with legal or similarly significant effects. EU AI Act classifies certain uses as banned or high-risk.*

### 2.3 The Value-First Framework

**[R]** Before assessing technical feasibility, assess product value:

**Problem Value Score (PVS)** = (Frequency + Pain + WTP + Market + Strategic) / 5

Score each 1-5:
- **Frequency:** How often does the problem occur? (1 = quarterly, 5 = multiple times daily)
- **Pain:** How painful is it? (1 = minor annoyance, 5 = mission-critical, blocks work)
- **Willingness to pay:** Would users pay? (1 = wouldn't pay, 5 = would pay separately)
- **Market size:** How many potential users? (1 = <1,000, 5 = >1,000,000)
- **Strategic alignment:** How core to strategy? (1 = peripheral, 5 = core)

**PVS ≥ 4.0:** Strong product case. Proceed to technical assessment.
**PVS 3.0-3.9:** Questionable. Only proceed with strong evidence.
**PVS < 3.0:** Do not build. The problem doesn't matter enough.

**Technical Novelty Assessment (TNA)** = (Solutions + Data + Determinism + Error Tolerance) / 4

**TNA ≥ 4.0:** Strong technical case. AI is a good fit.
**TNA 3.0-3.9:** Moderate difficulty. Expect significant engineering investment.
**TNA < 3.0:** High risk. Only proceed with exceptional PVS (>4.5) and credible research path.

**The PVS-TNA Matrix:**

| | TNA High (4-5) | TNA Medium (3-3.9) | TNA Low (1-2.9) |
|---|---|---|---|
| **PVS High (4-5)** | BUILD NOW | INVESTIGATE | HIGH-RISK BET |
| **PVS Medium (3-3.9)** | OPPORTUNISTIC | MONITOR | DO NOT BUILD |
| **PVS Low (1-2.9)** | DO NOT BUILD | DO NOT BUILD | DO NOT BUILD |

---

## 3. Evaluation Contracts

### 3.1 Why Evaluation Is the Hardest Problem

**[E]** AI evaluation is harder than software testing because:
1. **There is no single correct answer.** For many AI tasks, "correct" is multi-dimensional and contested.
2. **Benchmarks lie.** Model benchmarks (MMLU, HumanEval) correlate weakly with product performance. They test memorized knowledge, not real-world generalization.
3. **Distribution shift is invisible.** The model that works on your test data may fail on real user inputs.
4. **Failure modes are unpredictable.** Unlike deterministic bugs, AI failures are probabilistic and often surprising.

**[P]** The evaluation contract is the Academy's solution to this problem. It defines what "good enough" means for YOUR specific workflow with YOUR specific users. Not a generic benchmark. A contract.

### 3.2 The Evaluation Contract Template

**[R]** From `05_ai_product_management/EVALUATION_CONTRACTS.md`. For every AI feature or product:

| Field | Definition |
|-------|-----------|
| **Workflow** | What user task is the AI performing? |
| **Input specification** | What does the AI receive? (Format, source, constraints) |
| **Output specification** | What must the AI produce? (Format, content, constraints) |
| **Task success criteria** | What does "correct" mean? (Multiple dimensions if needed) |
| **Error severity classification** | Severity 1 (catastrophic) through 5 (trivial) — what counts for each? |
| **Acceptance thresholds** | Maximum acceptable error rate for each severity level |
| **Test dataset** | How was it constructed? Is it representative? Is it held out? |
| **Human baseline** | What is the current human performance on this task? |
| **Evaluation method** | Automatic? Human review? Hybrid? How often? |
| **Edge case strategy** | How are edge cases identified and handled? |
| **Model update protocol** | What happens when the underlying model changes? Re-evaluation required? |
| **Monitoring** | What metrics are monitored in production? What triggers investigation? |

### 3.4 Second Example: AI-Generated Marketing Copy Evaluation Contract

**[R]** A second filled example for a different use case:

**Workflow:** Generating social media marketing copy for small business owners.

**Input specification:** Business type, product/service description (50-200 words), target audience (demographic + psychographic), tone preference (professional, casual, witty, urgent), platform (Instagram, LinkedIn, Twitter, Facebook), character/word limits.

**Output specification:** 3-5 variations of social media post copy, each with: headline, body text, call-to-action, hashtag suggestions. Must comply with platform-specific character limits. Must not contain false claims, competitor disparagement, or copyrighted material.

**Task success criteria:**
- Primary: Copy is factually accurate (no hallucinated product features or claims)
- Secondary: Copy is on-brand for the specified tone (human-rated)
- Tertiary: Copy is engaging (measured by engagement rate when posted)
- Quaternary: Copy is distinct across variations (not just word-swapped versions)

**Error severity classification:**
- Severity 1: False claims about the product (legal risk) — 0% tolerance
- Severity 2: Competitor disparagement or copyrighted material — 0% tolerance  
- Severity 3: Completely off-tone or off-platform (witty copy for a funeral home) — max 2%
- Severity 4: Generic, unengaging copy that doesn't differentiate — max 20%
- Severity 5: Minor formatting issues, suboptimal hashtag choices — no threshold

**Acceptance thresholds:**
- Severity 1-2: 0%
- Severity 3: <2%
- Severity 4: <20%
- 80% of outputs rated "would post with minor edits or no edits" by human reviewer

**Test dataset:** 200 business/product combinations across 10 industries, 3 tone preferences each, covering all 4 platforms. Not used in prompt engineering.

**Human baseline:** Professional copywriter produces copy that is 95% "would post" quality at $50-150 per set. AI should match or exceed "would post" rate while being 10x+ cheaper.

**Evaluation method:** Weekly spot check of 50 outputs by marketing professional. Monthly blind comparison: AI copy vs human copywriter copy, rated by small business owners. Continuous monitoring: engagement rate of AI-generated posts vs human-written posts.

**Edge case strategy:** Businesses in regulated industries (finance, healthcare, legal) flagged for compliance review regardless of AI confidence. Copy containing superlatives ("best," "guaranteed," "#1") flagged. Copy about sensitive topics (health claims, financial promises, legal advice) escalated to human.

**Model update protocol:** After any model update, run full test dataset. If Severity 1-3 thresholds breached, block update. If Severity 4 increases by >5 percentage points, investigate before promoting.

**Monitoring:** Dashboard tracking: copy approval rate (human reviewer passed), time saved vs human copywriting, engagement rate comparison (AI vs human), Severity 1-3 incidents per 1000 outputs, token cost per approved output.

---

### 3.5 Common Evaluation Failures (And How to Avoid Them)

**[P]** The five most common evaluation failures in AI product management:

**Failure 1: Testing on your prompt development data.**
You develop prompts using a set of example inputs. Then you "evaluate" on those same examples. Of course performance looks good — you optimized for those inputs. *Fix: Hold out a separate test dataset before prompt development begins. Never evaluate on data used in prompt engineering.*

**Failure 2: Testing only happy-path inputs.**
Your test dataset contains only common, straightforward inputs. Real users produce edge cases — long inputs, misspelled inputs, inputs in unexpected formats, inputs that combine multiple requests. *Fix: Include edge cases in your test dataset. Reserve 20% of your test set for edge cases, long-tail inputs, and adversarial examples.*

**Failure 3: Updating evaluation criteria to match model behavior.**
The model consistently fails on a criterion. Instead of fixing the model, you relax the criterion. "Well, maybe it doesn't need to be THAT accurate." *Fix: Criteria should be based on user needs and business requirements, not model capability. If the model can't meet the criterion, the model isn't good enough — don't move the goalposts.*

**Failure 4: Automated-only evaluation without human spot-checks.**
You rely entirely on automated metrics (BLEU, ROUGE, accuracy against test set). Automated metrics can be gamed and miss real-world failure modes. *Fix: Supplement automated evaluation with regular human review. The human review sample should include the inputs where the model had lowest confidence AND a random sample.*

**Failure 5: Never updating the test dataset.**
Your test dataset was built 6 months ago. User behavior, input patterns, and use cases have evolved. The test set no longer represents real usage. *Fix: Refresh the test dataset quarterly. Sample recent production inputs to ensure coverage of current usage patterns.*

**[R]** A filled example:

**Workflow:** Routing customer support inquiries to the correct department.

**Input specification:** Free-text customer inquiry (1-500 words), customer account tier, product category (if known), language.

**Output specification:** Department tag (Billing, Technical, Account, Feature Request, Complaint) + confidence score (0-100) + routing explanation (1-2 sentences).

**Task success criteria:**
- Primary: Correct department identified (ground truth: where the ticket was actually resolved)
- Secondary: Routing explanation is accurate and helpful to the receiving agent
- Tertiary: No PII leakage in explanation

**Error severity classification:**
- Severity 1 (catastrophic): PII leaked to wrong department or external party — 0% tolerance
- Severity 2 (severe): Ticket routed to completely wrong department causing >24h delay — max 0.5%
- Severity 3 (moderate): Ticket routed to adjacent but suboptimal department — max 5%
- Severity 4 (minor): Routing correct but explanation unclear or unhelpful — max 15%
- Severity 5 (trivial): Minor formatting issues in output — no threshold

**Acceptance thresholds:**
- Severity 1: 0%
- Severity 2: <0.5%
- Severity 3: <5%
- Severity 4: <15%
- Overall routing accuracy: >92% (matching or exceeding current human routing accuracy of 91%)

**Test dataset:** 2,000 tickets randomly sampled from the past 6 months, stratified by department, customer tier, and language. Held out — not used in prompt engineering or model selection.

**Human baseline:** Human agents route with 91% accuracy, 98% Severity 1-2 avoidance.

**Evaluation method:** Monthly evaluation on the test dataset. Weekly spot-check of 100 production tickets by senior support lead. Continuous monitoring of reroute rate (tickets that were routed and then re-routed by the receiving agent).

**Edge case strategy:** Tickets with confidence score <70 are flagged for human review before routing. Tickets from enterprise customers (top tier) are always human-reviewed. Tickets containing words from the legal/escalation watchlist are flagged.

**Model update protocol:** When the underlying model is updated, run full evaluation on test dataset before promoting to production. If any acceptance threshold is breached, the update is blocked.

**Monitoring:** Real-time dashboard tracking: routing accuracy (sampled), reroute rate, confidence score distribution, Severity 1-2 incident count, average time-to-resolution (did routing AI reduce resolution time?).

---

## 4. Failure Mode Checklist

### 4.1 The 15 AI Failure Modes

**[E]** From `05_ai_product_management/FAILURE_MODES.md`. Before shipping any AI feature, assess each failure mode:

| # | Failure Mode | Description | Detection Method |
|---|-------------|-------------|-----------------|
| 1 | **Hallucination** | Model confidently produces incorrect output | Spot-check outputs against ground truth; user reports |
| 2 | **Brittleness** | Small input changes produce large output changes | Adversarial testing; input perturbation tests |
| 3 | **Distribution shift** | Performance degrades on real-world vs test data | Production monitoring vs test dataset performance |
| 4 | **Mode collapse** | Output variety decreases over time or across users | Track output diversity metrics |
| 5 | **Bias amplification** | Model amplifies biases in training data | Bias audits; subgroup performance analysis |
| 6 | **Overreliance** | Users trust AI too much, stop exercising judgment | Acceptance rate monitoring; user feedback surveys |
| 7 | **Cost overrun** | Inference costs exceed budget or project revenue | Token/cost monitoring per request and aggregate |
| 8 | **Prompt fragility** | Carefully crafted prompts break on model update | Regression tests on held-out dataset after every model update |
| 9 | **Latency degradation** | Response time increases under load or after update | P50/P95/P99 latency monitoring |
| 10 | **Context window overflow** | Model loses context in long conversations or documents | Track input length vs model context limit |
| 11 | **Output toxicity** | Model generates harmful, offensive, or inappropriate content | Content safety filters; toxicity classifiers |
| 12 | **Data leakage** | Model memorizes and reproduces training data | Membership inference testing; PII detection in outputs |
| 13 | **Reward hacking** | Model optimizes for evaluation metric at expense of real quality | Human evaluation alongside automated metrics |
| 14 | **Feedback loop degradation** | Model trained on its own outputs degrades over time | Output quality trend monitoring; periodic human evaluation |
| 15 | **Competitive model catch-up** | Competitor offers better model making your AI feature obsolete | Competitive monitoring; model-swappable architecture |

### 4.2 Failure Mode Assessment Template

**[R]** For each AI feature, complete:

| Failure Mode | Probability (1-10) | Severity (1-10) | Detectability (1-10) | RPN (P×S×D) | Mitigation |
|-------------|-------------------|-----------------|---------------------|-------------|------------|
| Hallucination | | | | | |
| Brittleness | | | | | |
| (etc.) | | | | | |

**RPN (Risk Priority Number) = Probability × Severity × Detectability**

- RPN > 200: Must have documented mitigation and reversal trigger
- Severity > 7: Must have mitigation regardless of probability

**[R]** The failure mode assessment is not optional. It's the minimum viable safety analysis for any AI feature. If you can't complete it, you don't understand the risks well enough to ship.

---

## 5. Build vs Buy vs Provider Framework

### 5.1 The AI-Specific Build-Buy Decision

**[D]** The build-vs-buy decision for AI is different from traditional software (CON-0010). The options:

**Build (train or fine-tune your own model):**
- When: Differentiation depends on model behavior; you have unique, valuable training data; off-the-shelf models don't meet quality requirements
- Cost: High upfront (training, infrastructure, ML team) + ongoing (retraining, evaluation, maintenance)
- Risk: Model quality may not surpass off-the-shelf; training is unpredictable; maintaining model quality requires ongoing investment

**Buy (use a model API — OpenAI, Anthropic, Google, etc.):**
- When: The model is not the differentiator (the product experience, data, or workflow is); quality requirements are met by off-the-shelf models; you want to move fast
- Cost: Variable (per-token or per-request pricing) + integration engineering
- Risk: Provider dependency (pricing changes, deprecation, terms of service changes); all competitors have access to the same models

**Provider (use an AI-powered product that includes AI):**
- When: The AI capability is not differentiating and a product already exists; you're buying a product, not model access
- Cost: SaaS pricing (per-seat, per-usage)
- Risk: Limited customization; vendor lock-in; feature roadmap controlled by vendor

### 5.2 The Decision Framework

**[R]** Score each dimension 1-5 toward Build or Buy/Provider:

| Dimension | Favors Build | Favors Buy/Provider |
|-----------|-------------|---------------------|
| **Differentiation** | This AI capability IS the product | This AI capability supports the product |
| **Data advantage** | We have unique training data competitors don't | Standard data; no data advantage |
| **Quality requirements** | Off-the-shelf models can't meet our quality bar | Off-the-shelf models are sufficient |
| **Speed to market** | Build timeline is acceptable | Need it faster than we can build |
| **Build competence** | We have ML engineering capability | No ML team; building would be a distraction |
| **Vendor risk** | Single dominant provider; high switching cost | Competitive provider market; alternatives exist |
| **Optionality** | Owning creates valuable future options | Unlikely to become more differentiating |

**[R] Default to Buy** unless differentiation, data advantage, and quality requirements all favor Build. Most organizations overestimate how differentiating their AI use case is.

**[R] Re-evaluate the decision every 6 months.** The AI provider landscape changes rapidly. A capability that was best "bought" six months ago may be best "built" today — or may have become a commodity available from multiple providers.

---

## 6. Governance Proportional to Consequence

### 6.1 The Tiered Governance Framework

**[E]** Not all AI uses carry the same risk. The EU AI Act's risk-tiered approach provides a useful framework. The Academy extends it for product management:

**[R] Tier 1 — High-Consequence Domains**
*Healthcare diagnosis, financial advice, hiring decisions, safety-critical systems, legal judgments, access to essential services.*

**Governance requirements:**
- Human-in-the-loop required for final decisions
- Evaluation contract mandatory, externally reviewed
- Failure mode assessment mandatory, externally reviewed
- Bias audit mandatory, by subgroup
- Explainability: users must understand how decisions are made
- Appeal mechanism: users must be able to challenge decisions
- Monitoring: real-time, with automated alerts for threshold breaches
- Model update protocol: full re-evaluation before any model change
- External audit: annual or semi-annual

**Examples:** AI for medical diagnosis, AI for loan approval, AI for resume screening, AI for parole recommendation.

**[R] Tier 2 — Medium-Consequence Domains**
*Customer-facing recommendations, content generation, code generation, internal analytics, customer support.*

**Governance requirements:**
- Human review for edge cases and low-confidence outputs
- Evaluation contract mandatory, internally reviewed
- Failure mode assessment for relevant failure modes
- Bias awareness: bias audit before launch, periodic thereafter
- Monitoring: automated for known failure modes, periodic human spot-checks
- User feedback mechanism: easy way to report problems
- Model update protocol: regression testing on held-out dataset

**Examples:** AI for content recommendations, AI for code completion, AI for support ticket routing, AI for content summarization.

**[R] Tier 3 — Low-Consequence Domains**
*Internal tools, classification for non-critical use, summarization of non-sensitive content, formatting/normalization.*

**Governance requirements:**
- Automated evaluation sufficient
- Failure mode awareness: team knows what to watch for
- Basic monitoring: cost, latency, error rate
- Periodic review: does the AI still add value? Should it be replaced?

**Examples:** AI for internal document search, AI for formatting data, AI for meeting note summarization within a team.

### 6.2 Governance Failure Modes

**[P]** The two most common governance failures:

1. **Over-governing low-consequence uses.** Applying Tier 1 governance to Tier 3 uses. Slows everything down. Teams route around governance. Creates cynicism about AI governance.
2. **Under-governing high-consequence uses.** Applying Tier 3 governance to Tier 1 uses. Creates unacceptable risk. When something goes wrong, the regulatory and reputational damage is catastrophic.

**[R]** Governance should be proportional to consequence. Not all AI is high-risk. Not all AI is low-risk. Classify each use case and apply the appropriate tier.

---

## 7. Adoption and Trust Building

### 7.1 The AI Trust Problem

**[E]** Users don't trust AI by default. They trust it when:
1. It demonstrates competence consistently
2. Its failures are predictable and non-catastrophic
3. They understand how to use it effectively
4. They have control over when and how it's used
5. They can override or correct it when it's wrong

**[P]** AI products that ignore trust building fail even when the underlying model is excellent. Users try it once, are impressed, encounter a failure, and never return. The product fails — not because the AI wasn't good enough, but because the trust architecture wasn't designed.

### 7.2 The Trust Architecture

**[R]** Six design principles for AI trust:

**1. Calibrated confidence.** Show users how confident the AI is in its output. Don't show "92% confident" — show "High confidence / Medium confidence / Low confidence." Users need to know when to trust and when to verify.

**2. Graceful failure.** When the AI is uncertain or wrong, the failure should be non-catastrophic and recoverable. "I'm not confident about this — would you like me to try a different approach or connect you with a human?" Not: silently wrong answer delivered with full confidence.

**3. Explainability.** Users should understand WHY the AI produced this output. Not a technical explanation — a user-facing explanation. "I recommended this article because you've read similar topics and it's highly rated by readers like you."

**4. User control.** Users should control when AI is used and how. Opt-in, not forced. Configurable, not one-size-fits-all. "Use AI suggestions" toggle rather than always-on AI.

**5. Feedback loop.** Users should be able to tell the AI when it's wrong — and see that feedback improve the system. "Was this helpful? Yes / No" with a path to provide detail.

**6. Progressive trust.** Start with low-stakes AI features. As users build trust, introduce higher-stakes features. Don't lead with the AI feature that has the highest consequence of failure.

### 7.3 Adoption Through Workflow Integration

**[R]** AI features are adopted when they fit into existing workflows, not when they require learning new workflows. The design principle:

- **Bad:** "Here's an AI chatbot. Ask it anything."
- **Good:** "When you're writing a support response, the AI suggests a draft based on similar past tickets. You can accept, edit, or ignore."

The AI should meet users where they already are, not demand they come to where the AI is.

---

## 8. AI PM Anti-Patterns

### 8.1 The 10 Anti-Patterns

**[P]** Observed patterns of AI product management failure:

**Anti-Pattern 1: The Model-Hopper**
"I'll just switch to [newest model] and it'll fix everything." Every new model release triggers a model switch without evaluation. The product never stabilizes because the PM treats model selection as the primary product activity. *Fix: Product performance depends on system design, not model selection (see MODEL_VS_SYSTEM.md). Evaluate models against your specific workflow before switching.*

**Anti-Pattern 2: The Prompt Alchemist**
Spending weeks crafting the perfect prompt. Treating prompt engineering as the primary product development activity. Prompts are fragile, hard to evaluate, and not a moat. *Fix: Invest in system design, evaluation infrastructure, and user experience — not prompt optimization. A great prompt with no evaluation framework is worthless.*

**Anti-Pattern 3: The Demo-Driven PM**
Shipping AI features that work beautifully in demos but fail on real-world inputs. The demo used curated inputs. Real users don't provide curated inputs. *Fix: Evaluate on representative, held-out data. If it only works on the inputs you tested during development, it doesn't work.*

**Anti-Pattern 4: The Benchmark-Chaser**
Optimizing for model benchmarks (MMLU, HumanEval) rather than product outcomes. Citing benchmark scores as evidence of product quality. *Fix: Define product performance metrics for your specific workflow. Benchmark scores are directional at best.*

**Anti-Pattern 5: The Safety Procrastinator**
"We'll add safety guardrails after we ship." By then, trust is damaged, regulatory attention has been attracted, and the product has a reputation for unreliability. *Fix: Safety and evaluation are prerequisites for launch, not post-launch optimizations.*

**Anti-Pattern 6: The AI-for-Everything PM**
Proposing AI for every problem. "Can we use AI for this?" asked reflexively without first asking "Should we?" or "Is there a simpler solution?" *Fix: For every AI proposal, ask: "What is the best NON-AI solution to this problem? Why is AI better?" If you can't answer convincingly, don't use AI.*

**Anti-Pattern 7: The Cost-Ignorant PM**
Building AI features without understanding or tracking inference costs. Discovering after launch that each user interaction costs $0.50 on a product that generates $0.10 in revenue. *Fix: Model unit economics before building. Track costs per interaction from day one. If the economics don't work, either reduce costs or increase value — don't ignore it.*

**Anti-Pattern 8: The Black-Box Shipper**
Shipping AI features with no evaluation, no monitoring, no feedback mechanism. Users are the evaluators — and they discover problems the hard way. *Fix: Evaluation contract before launch. Monitoring from day one. User feedback mechanism built into the product.*

**Anti-Pattern 9: The Model-Agnostic Dreamer**
"We'll design the system to be model-agnostic so we can swap models easily." Building an abstraction layer for a capability that doesn't exist yet, for model-swapping flexibility that may never be needed. Over-engineered and under-shipped. *Fix: Start with one model. When you need to support a second model, refactor for model-agnosticism. Don't build it before you need it.*

**Anti-Pattern 10: The Singularity Strategist**
"We don't need to solve this today because models will be much better in 6 months." Deferring product decisions to a hypothetical future where AI capabilities have advanced. *Fix: Build for today's capabilities. If models improve, your product improves. If they don't, you still have a product.*

### 8.2 The Anti-Pattern Self-Check

**[R]** Before any AI product decision, ask: "Am I falling into any of these anti-patterns?" Read the list. Be honest. If the answer is yes, pause and re-examine your approach.

---

## 9. The AI PM's Toolkit

### 9.1 Essential Academy Modules

**[R]** These Academy modules are the AI PM's foundational toolkit:

1. **WORKFLOW_SELECTION.md** — For every AI use case: Is this workflow appropriate for AI? Read this first. Always.
2. **EVALUATION_CONTRACTS.md** — For every AI feature: How do we know if it's good enough? Define the contract before building.
3. **FAILURE_MODES.md** — For every AI launch: What could go wrong? Complete the checklist before shipping.
4. **MODEL_VS_SYSTEM.md** — For every AI architecture decision: Are we over-investing in model selection and under-investing in system design?
5. **GOVERNANCE.md** — For every AI product: What governance is proportional to consequence?
6. **AGENT_ARCHITECTURE.md** — For agentic AI products: How do we design for reliability, observability, and control?
7. **ADOPTION.md** — For every AI launch: How will users adopt and trust this?
8. **TOOLS.md** — Practical tools and templates for AI product management

### 9.2 The AI Decision Sequence

**[R]** The sequence for any AI product decision:

```
1. Workflow Selection     → Should AI be doing this at all?
2. PVS/TNA Assessment     → Is this problem worth solving with AI?
3. Anti-Pattern Check     → Are we falling into any anti-patterns?
4. Evaluation Contract    → How will we know if it works?
5. Failure Mode Assessment → What could go wrong?
6. Build vs Buy Decision  → Build, buy model API, or use AI-powered product?
7. Governance Tier        → What governance is appropriate?
8. Trust Architecture     → How will users trust and adopt this?
9. Build (with monitoring and feedback loop)
10. Iterate (based on evaluation, not model benchmarks)
```

**[R]** Skipping steps in this sequence is the most common cause of AI product failure. The most commonly skipped steps: 3 (Anti-Pattern Check), 4 (Evaluation Contract), and 5 (Failure Mode Assessment). These are the steps that separate AI products that work from AI demos that impress.

---

## 10. The AI PM's Learning Path

### 10.1 What to Study (in Order)

**[R]**

**Phase 1: Foundation (Week 1-2)**
1. Read `05_ai_product_management/README.md` — Module overview
2. Read `05_ai_product_management/WORKFLOW_SELECTION.md` — The methodology
3. Read `handbook/PRODUCT_LEADERSHIP_BIBLE.md` Part 6 — AI Product Leadership summary
4. Complete the Workflow Selection exercise for a real product you work on

**Phase 2: Evaluation (Week 3-4)**
5. Read `05_ai_product_management/EVALUATION_CONTRACTS.md`
6. Write an evaluation contract for a real AI feature (or proposed feature)
7. Read `05_ai_product_management/FAILURE_MODES.md`
8. Complete the failure mode assessment for the same feature

**Phase 3: System Design (Week 5-6)**
9. Read `05_ai_product_management/MODEL_VS_SYSTEM.md`
10. Read `05_ai_product_management/AGENT_ARCHITECTURE.md` (if building agentic products)
11. Read `05_ai_product_management/GOVERNANCE.md`
12. Classify your AI features by governance tier

**Phase 4: Go-to-Market (Week 7-8)**
13. Read `05_ai_product_management/ADOPTION.md`
14. Read `05_ai_product_management/TOOLS.md`
15. Design the trust architecture for your AI feature
16. Complete the Build vs Buy framework for any AI build decisions in your pipeline

### 10.2 Ongoing Practice

**[R]**

**Weekly:**
- Read one AI product launch announcement. Analyze: did they do workflow selection? What's their evaluation approach? What failure modes are they exposed to?
- Talk to one user of an AI product you use. Ask: "What do you trust about it? What don't you trust? What would make you use it more?"

**Monthly:**
- Review the AI features in your product. Are they meeting their evaluation contracts? Are failure modes emerging? Are costs within budget?
- Model landscape update: What new models are available? Do they change any build-vs-buy decisions? Should you re-evaluate?

**Quarterly:**
- Full evaluation contract review: Are thresholds still appropriate? Has the test dataset become stale?
- Governance tier review: Has any AI feature moved up or down in consequence?
- AI strategy review: What AI capabilities do we need vs buy vs partner? What's changed?

---

## 11. Quick Reference: When AI Goes Wrong

**[R]** When an AI feature is failing, use this diagnostic:

| Symptom | Most Likely Cause | First Action |
|---------|------------------|--------------|
| Users try once, don't return | Trust not built; first failure was catastrophic | Improve failure mode design; add calibrated confidence |
| Users don't try at all | No adoption architecture; AI doesn't fit workflow | Redesign for workflow integration; add progressive disclosure |
| High error rate in production | Distribution shift; test data not representative | Update test dataset; add production monitoring |
| Costs exceeding budget | Inference cost model wrong; usage higher than expected | Implement cost controls; consider smaller/cheaper model |
| Model behaving differently after update | Prompt fragility; no regression testing | Implement model update protocol; add regression tests |
| Users over-trusting and not verifying | Overreliance; AI always presented with high confidence | Show calibrated confidence; add friction for high-stakes outputs |
| Competitor launching better AI | Model commoditized; system design is the differentiator | Invest in product experience, not model chasing |
| AI feature works but nobody cares | Problem not worth solving (PVS < 3.0) | Reassess problem value; consider killing the feature |

---

## 12. The AI PM's Weekly Practice

**[R]** AI product management requires deliberate practice. Weekly habits:

**Monday: Model landscape update.** Check for new model releases, pricing changes, capability announcements. Maintain a running document of what each model can and cannot do for your specific use cases.

**Tuesday: Evaluation review.** Spot-check 10 AI outputs from production. Are they meeting quality thresholds? Any new failure patterns? Update the failure log.

**Wednesday: User trust pulse.** Review user feedback on AI features. Acceptance rate trending up or down? Override rate? Trust-related complaints? Talk to one user about their experience with an AI feature.

**Thursday: Cost review.** Check inference costs against budget. Any surprises? Are per-interaction costs stable? Is usage growing faster than expected?

**Friday: Anti-pattern check.** Review your AI features against the 10 anti-patterns. Are you slipping into any of them? What needs to change next week?

---

## 13. The AI PM's Career Development

**[R]** AI product management is the fastest-growing specialization in product management. To develop your AI PM capability:

1. **Build something with AI.** Not a product spec — a working prototype. Use an LLM API. Experience the gap between "the model can do this in a demo" and "the model works reliably in a product."
2. **Evaluate, don't just build.** The hardest AI PM skill is evaluation. Practice: for any AI feature you use, write an evaluation contract. What would "good" look like? How would you measure it?
3. **Study failures, not successes.** AI product failure postmortems teach more than success stories. Read about AI products that failed. Diagnose why using the frameworks in this playbook.
4. **Understand the economics.** Track token costs for real AI products you use. Model the unit economics. Most PMs ignore AI costs until they're a problem.
5. **Develop governance judgment.** For any AI product you encounter, classify it by governance tier. What governance SHOULD it have? Does it have it?

---

## 12. AI PM Scenarios

### Scenario 1: "Should We Add AI to This Feature?"

**Situation:** Your team maintains a document editing product. The VP of Product read about AI summarization and wants to add a "Summarize Document" button. You're not sure this is the right use of AI.

**AI PM response:**

1. **Workflow Selection first.** Describe the user's current summarization workflow: "A team lead reads a 20-page report and manually creates a 1-page executive summary." Decompose: (a) Reading and understanding the document, (b) Identifying key findings, (c) Synthesizing into a coherent summary, (d) Formatting for executives. Score each subtask.

2. **Anti-pattern check.** Is summarization novel? No — it's a commodity AI capability. Is there a deterministic solution? Sort of — templates exist, but they don't handle variable content well. What's the error tolerance? Medium — a bad summary wastes executive time but doesn't cause catastrophe. What's the cost? Moderate — LLM summarization costs $0.01-0.05 per page depending on length.

3. **Evaluation contract.** What does "good summary" mean? (a) All key findings present, (b) No hallucinated content, (c) Appropriate reading level, (d) Correct length. Define each with measurable criteria. Build a test set of 50 documents with human-written executive summaries as ground truth.

4. **Trust architecture.** Show the AI summary alongside key source highlights. Let users click any sentence to see where in the document it came from. Add an "edit summary" mode so users can correct AI mistakes. Track acceptance rate (users use AI summary vs write their own).

5. **Recommendation.** Build, but with evaluation contract, trust architecture, and measured rollout. Not "ship the summarization API and see what happens."

### Scenario 2: "Our AI Feature Is Producing Bad Outputs"

**Situation:** Three months after launch, users are reporting that the AI feature sometimes produces nonsensical outputs. The engineering team says "we need a better model." You're not sure that's the problem.

**AI PM response:**

1. **Don't switch models — investigate.** Model switching without diagnosis treats the symptom, not the cause. Investigate: (a) When did the failures start? (Model update? Data distribution shift? New user segment?) (b) What patterns exist in the failures? (Specific input types? Specific times? Specific users?) (c) Is the evaluation infrastructure catching these failures? If not, evaluation needs improvement before model switching.

2. **Check for distribution shift.** Are the failing inputs different from your test dataset? If users are now asking questions your test set didn't cover, your evaluation is stale. Update the test dataset.

3. **Check for prompt fragility.** Was the model updated by the provider? Did model behavior change in ways your prompts didn't anticipate? Run your evaluation contract against the new model version. If performance degraded, you have a prompt or evaluation problem, not necessarily a model problem.

4. **If the model IS the problem.** Only after eliminating distribution shift and prompt fragility, consider model switching. But switch with data: "Our evaluation shows the current model has X% error rate on our test set. Alternative model Y shows Z% error rate. The improvement justifies the switching cost."

### Scenario 3: "Competitor Launched AI Feature We Don't Have"

**Situation:** A competitor launched an AI feature that's getting press attention. Your executive team wants to know "why don't we have this?" Your team could build it in 6-8 weeks.

**AI PM response:**

1. **PVS first.** Does this feature solve a real problem for YOUR users (not the competitor's)? Run the Problem Value Score. If PVS < 3.0, recommend not building — "our users don't have this problem."

2. **Workflow Selection.** Is this an appropriate AI use case? Many competitor AI features fail the anti-pattern check. They're demos, not products.

3. **If it IS a real use case for your users.** Don't copy the competitor. Understand the underlying user need and design your solution independently. The competitor's approach may be wrong despite the press attention.

4. **If it's strategically necessary to respond.** Build the minimum viable version. Evaluate. Iterate. Don't match the competitor feature-for-feature. Solve the user problem in the simplest way possible, which may not involve AI (anti-pattern 1: deterministic solution exists).

---

## 13. AI PM Decision Framework Quick Reference

**[R]** Print this. Put it on your wall. Use it for every AI product decision.

```
For every proposed AI feature or product:

1. WORKFLOW SELECTION         — Describe the workflow without mentioning AI
   □ Who, what, input, output, constraints, current performance
   □ Decompose into subtasks
   □ Score each subtask: Determinism, Error Tolerance, Automation Value

2. PROBLEM VALUE SCORE (PVS)  — Is this problem worth solving?
   □ Frequency (1-5) + Pain (1-5) + WTP (1-5) + Market (1-5) + Strategic (1-5)
   □ Average must be ≥ 4.0 to proceed

3. ANTI-PATTERN CHECK          — Why NOT use AI?
   □ □ □ □ □ □ □ □ (check all 8)

4. TECHNICAL NOVELTY (TNA)    — Can AI do this well enough?
   □ Solutions + Data + Determinism + Error Tolerance
   □ Average must be ≥ 3.0 to proceed (≥ 4.0 to proceed without concern)

5. PVS-TNA MATRIX             — Combined assessment
   □ High PVS + High TNA = BUILD NOW
   □ High PVS + Medium TNA = INVESTIGATE
   □ Medium PVS + High TNA = OPPORTUNISTIC
   □ Everything else = DO NOT BUILD or MONITOR

6. EVALUATION CONTRACT         — How do we know it works?
   □ Task success criteria, error severity, acceptance thresholds
   □ Test dataset (representative, held out)
   □ Human baseline, evaluation method, edge case strategy

7. FAILURE MODE ASSESSMENT     — What could go wrong?
   □ All 15 failure modes: P × S × D = RPN
   □ Mitigation for RPN > 200 or Severity > 7

8. BUILD vs BUY vs PROVIDER    — How do we get this capability?
   □ Differentiation, data advantage, quality, speed, competence, vendor risk, optionality

9. GOVERNANCE TIER             — What oversight is appropriate?
   □ Tier 1 (high consequence), Tier 2 (medium), Tier 3 (low)

10. TRUST ARCHITECTURE         — How will users trust this?
    □ Calibrated confidence, graceful failure, explainability
    □ User control, feedback loop, progressive trust

11. LAUNCH                     — Ship with monitoring and feedback
12. ITERATE                    — Based on evaluation, not benchmarks
```

---

## 14. Case Studies in AI Product Failure

### Case Study A: The Chatbot That Hallucinated Prices

**What happened:** An e-commerce company added an AI chatbot to answer customer questions. The chatbot was prompted with product information but was not given price data directly. When customers asked about prices, the chatbot hallucinated prices that were 30-50% below actual prices. Customers demanded the hallucinated prices. The company had to honor them or face chargeback claims.

**Academy diagnosis:** 
- No evaluation contract (Step 6 skipped) — hallucinations weren't tested for
- Failure mode assessment missed hallucination on untrained data (Step 7 skipped) — severity was high (financial)
- Trust architecture failed — the chatbot presented prices with full confidence, no disclaimer
- **Primary failure:** Anti-pattern 2 (error cost exceeded automation value) — the cost of hallucinated prices exceeded the savings from chatbot automation

### Case Study B: The AI Writing Assistant That Nobody Used

**What happened:** A SaaS company added an AI writing assistant to their platform. Impressive demo. Launched with fanfare. 90% of users tried it once. 5% used it regularly after week one. The product team blamed "adoption" and proposed adding more features.

**Academy diagnosis:**
- PVS was never calculated (Step 2 skipped) — was improving writing actually a pain point for this user base?
- Anti-pattern 6 (AI-for-everything) — the team added AI because it was exciting, not because users needed it
- No discovery — users were never asked whether writing assistance was a problem they had
- **Primary failure:** Anti-pattern 3 (demo-driven PM) — the feature worked beautifully in controlled settings but solved a problem users didn't actually have

### Case Study C: The Model Update That Broke Everything

**What happened:** A company used an LLM API for document classification. The model provider released a new version that was "better on benchmarks." The team switched models without testing. Classification accuracy dropped from 94% to 78% on their specific use case. Thousands of documents were misclassified before the issue was detected.

**Academy diagnosis:**
- No evaluation contract with model update protocol (Step 6 incomplete) — model switching wasn't gated by evaluation
- Anti-pattern 1 (model-hopper) — switched models based on benchmarks, not product performance
- Detectability was low — no production monitoring comparing output distribution to known-good baseline
- **Primary failure:** Anti-pattern 4 (benchmark-chaser) — benchmark scores correlated weakly with product performance on this specific classification task

---

## 15. The AI PM's Ethical Decision Framework

**[E]** AI products raise ethical questions that deterministic software doesn't. The PM must navigate these proactively, not reactively.

### 15.1 The Three Ethical Gates for AI Products

**[R]** Before shipping any AI feature, pass it through three gates:

**Gate 1: Harm Prevention**
- Could this AI feature cause harm to users? (Physical, financial, psychological, reputational, discriminatory)
- If yes: Can the harm be prevented through system design? If not, the feature should not be built.
- Examples: AI for medical diagnosis (potential physical harm) requires clinical validation. AI for resume screening (potential discriminatory harm) requires bias auditing.

**Gate 2: User Agency**
- Do users understand when AI is being used? (Transparency)
- Can users opt out of AI and use a non-AI alternative? (Choice)
- Can users correct AI mistakes or appeal AI decisions? (Recourse)
- If any answer is "no": Can the feature still be justified? Some workflows (spam filtering) don't require transparency; most do.

**Gate 3: Societal Impact**
- Does this feature create systemic risks? (Labor displacement, information quality degradation, concentration of power)
- Who benefits and who might be harmed beyond the immediate user?
- This gate doesn't require a perfect answer — but it requires asking the question and documenting the answer.

### 15.2 Red Lines: When AI Should Not Be Used

**[R]** The Academy identifies situations where AI should NOT be used regardless of technical capability or commercial opportunity:

1. **Autonomous lethal decisions** — AI should not make life-or-death decisions without meaningful human oversight
2. **Decisions where the decision-maker must be accountable** — legal judgments, parole decisions, child custody — accountability requires a human who can explain and defend the decision
3. **Manipulation at scale** — AI optimized to exploit cognitive vulnerabilities for commercial gain (addictive design for children, financial products targeting vulnerable populations)
4. **Decisions where the error is invisible and irreversible** — AI making decisions that users cannot detect are wrong and cannot reverse once made
5. **AI that presents as human without disclosure** — impersonation erodes trust in all communication

**[R]** These red lines represent the Academy's ethical position. They are not laws (though some align with emerging regulation). They are product leadership decisions — you choose whether to cross them. The Academy recommends you don't.

---

## 16. AI Product Leadership: Summary of Core Principles

**[R]** If you remember nothing else from this playbook, remember these ten principles:

1. **Workflow-first, never model-first.** Start from the human workflow. Decompose it. Only then decide which parts AI should touch.
2. **Evaluation is the product.** If you can't measure whether the AI is good, you can't ship AI. The evaluation contract is your minimum viable product artifact.
3. **System design > model selection.** Prompts are fragile. System architecture is durable. Invest in the system, not the prompt.
4. **Governance proportional to consequence.** Not all AI is high-risk. Not all AI is low-risk. Classify and govern accordingly.
5. **Trust is architected, not assumed.** Users don't trust AI by default. Design for calibrated confidence, graceful failure, explainability, and user control.
6. **Cost is a product variable.** AI inference costs money. Model unit economics before building. Track costs from day one.
7. **Benchmarks lie.** Model benchmarks correlate weakly with product performance. Evaluate on your specific workflow with your specific users.
8. **Anti-patterns are predictable.** The 10 anti-patterns in Section 8 are a checklist. Use them before every AI product decision.
9. **The non-AI alternative is the baseline.** For every AI proposal, define the best non-AI solution. AI must be measurably better or cheaper — preferably both.
10. **AI PM is not a specialization.** It's becoming a core PM competency. Every PM will make AI product decisions. The question is whether you'll make them well.

---

*This playbook is a companion to `05_ai_product_management/` and `handbook/PRODUCT_LEADERSHIP_BIBLE.md`. The modules provide detailed methodology; the Bible provides doctrinal context; this playbook provides the decision framework, practical scenarios, and ethical guidance. Use all three.*
