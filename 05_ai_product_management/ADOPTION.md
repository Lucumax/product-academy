# AI Product Adoption: Trust, Organizational Change, and Measuring Success

**Status:** v0.1.0
**Depends on:** All previous module files

---

## TL;DR

Building an AI product is hard. Getting users to adopt it is harder. Getting them to keep using it after the novelty wears off is hardest. AI products face adoption barriers that traditional software doesn't: trust deficits, accuracy anxiety, automation bias, workflow disruption, and organizational resistance. This file provides frameworks for building user trust, designing effective disclosure, managing the prototype-to-production discontinuity, driving organizational change, and measuring AI product success in ways that matter.

---

## Part 1: The AI Adoption Problem

### Why AI Adoption Is Different

Traditional software adoption is primarily about utility: "Does this solve my problem?" AI adoption is about utility PLUS trust: "Does this solve my problem, AND can I trust it to do so reliably?"

This trust dimension changes everything:

| Traditional Software | AI Software |
|---------------------|-------------|
| Users expect bugs | Users fear AI "going rogue" |
| Errors are visible (500 error, crash) | Errors are invisible (plausible wrong answers) |
| Users learn the tool's boundaries through use | AI's boundaries are fuzzy and inconsistent |
| "It works" is binary | "It works" is probabilistic |
| Trust is earned once and maintained with reliability | Trust must be earned continuously because failure is inevitable |
| Adoption curve follows utility discovery | Adoption curve follows trust building, which is slower and more fragile |

### The AI Trust Deficit

Research consistently shows a trust deficit for AI products:

- Users trust AI less than humans even when AI performs better on objective metrics ("algorithm aversion")
- A single visible AI error destroys trust more than multiple invisible AI successes ("negativity dominance")
- Users over-trust AI in some contexts (automation bias) and under-trust it in others — often in ways that are suboptimal for their own outcomes
- Trust is asymmetric: it takes many correct outputs to build trust and one bad output to destroy it

**Implication for product leaders:** AI product adoption is a trust-building campaign, not a feature launch. Plan for it accordingly.

---

## Part 2: Building User Trust

### The Trust-Building Framework

Trust in AI products is built on four pillars:

```
    ┌──────────────────────────────────────┐
    │              USER TRUST              │
    ├──────────────────────────────────────┤
    │                                      │
    │  RELIABILITY    TRANSPARENCY         │
    │  "It works      "I understand        │
    │   consistently"  what it's doing"    │
    │                                      │
    │  CONTROL        RECOURSE             │
    │  "I can guide   "I can fix it        │
    │   and override"  when it's wrong"    │
    │                                      │
    └──────────────────────────────────────┘
```

#### Pillar 1: Reliability

Trust requires the system to work consistently — not perfectly, but predictably.

**Tactics:**

1. **Start narrow, expand gradually.** Launch with a narrow, well-defined use case where the AI is highly reliable. Expand scope as quality improves. Users who experience initial reliability are more forgiving of occasional failures in expanded scope.

2. **Never ship a feature at "50% accuracy" hoping to improve later.** The first experience defines user expectations. If users' first 10 interactions contain 5 errors, they will never trust the system — even if you later improve it to 95%.

3. **Graceful degradation over silent failure.** When the system is uncertain, it should say "I'm not confident enough to answer this. Let me connect you with a specialist" rather than producing a plausible wrong answer. The user trusts a system that knows its limits more than one that confidently fabricates.

4. **Consistency over brilliance.** A system that produces "B+" quality consistently builds more trust than a system that sometimes produces "A+" and sometimes produces "F." Erratic quality is more damaging than mediocre quality.

5. **Demonstrate improvement, not just claim it.** "This feature improved by 12% this quarter because we updated our training data. Here are three examples of things it used to get wrong and now gets right."

#### Pillar 2: Transparency

Users need to understand what the AI is doing, why, and what its limitations are.

**Tactics:**

1. **Show your work.** When the AI provides an answer, show the evidence, sources, or reasoning behind it. "This recommendation is based on your purchase history (showing 3 similar purchases) and what similar customers bought (aggregate data from 10,000+ customers)."

2. **Be honest about limitations.** Every AI disclosure should include what the system CANNOT do. "I can help with product questions, returns, and order status. I can't help with billing disputes or account security — those go to our specialist team."

3. **Communicate confidence, calibrated.** "Based on the information available: [answer]. Confidence: High (similar cases handled correctly 97% of the time)." But ONLY if your confidence is well-calibrated. Miscallibrated confidence destroys trust.

4. **Explain errors when they happen.** "I made a mistake in my previous response. The correct information is [correction]. I've logged this error so our team can prevent similar mistakes in the future."

5. **Version transparency.** "I'm running on model version 2.3, last updated June 15, 2026." Users should know when the system changed, because its behavior may have changed.

#### Pillar 3: Control

Users must feel they are in control of the AI, not the other way around.

**Tactics:**

1. **AI is a suggestion, not a command.** Design the UX so users feel they're accepting or rejecting AI suggestions, not being dictated to. "Here's a suggestion: [AI output]. Use as is / Edit / Dismiss."

2. **Granular control.** Don't make AI an all-or-nothing toggle. Let users enable AI for specific tasks: "Use AI for grammar suggestions: ON. Use AI for tone suggestions: OFF. Use AI for content generation: ON."

3. **Adjustable AI behavior.** Let users tune the AI's behavior: "Prefer shorter responses" or "Be more thorough." This gives users agency over the interaction style.

4. **Easy-to-find human escalation.** The "talk to a human" option should be visible and always available, not buried in a menu after the AI has frustrated the user for 10 minutes.

5. **AI that asks permission, not forgiveness.** Before taking consequential actions, the AI should confirm: "I'm about to cancel your subscription. This will take effect immediately. Proceed?"

#### Pillar 4: Recourse

When the AI gets it wrong, users need a clear path to correct the error and feel heard.

**Tactics:**

1. **One-click feedback.** "Was this helpful? Yes / No." If No: "What went wrong?" with specific options and a free-text field. This closes the loop AND captures training data.

2. **Visible action on feedback.** "Based on your feedback, we've updated our system. Here's what changed." Users who see their feedback result in improvement become more invested in the product.

3. **Easy correction.** If the AI produces wrong output, the user should be able to correct it inline. "Click to edit" — then the corrected version becomes training data.

4. **Error acknowledgment, not deflection.** "I understand that my previous response was incorrect. Here's what I should have said: [correction]." Don't make excuses. Don't blame the user's input. Acknowledge the error and correct it.

5. **Compensation where appropriate.** If an AI error cost the user money, time, or opportunity, compensate them. A $5 credit for a wrong product recommendation that the user acted on buys more loyalty than a perfect apology.

---

## Part 3: Disclosure and Transparency

### The Disclosure Ladder

Not all users need or want the same level of disclosure. Provide a ladder:

```
Level 1: "AI-POWERED" badge (optional)
  - Subtle indicator that AI is involved
  - For: Low-risk features, established products, AI-native users

Level 2: Inline disclosure
  - "This response was generated by AI. Learn more."
  - For: Informational AI features, content generation

Level 3: Expanded disclosure
  - "AI generated this based on [sources]. It may contain errors. Verify before relying on it. [Report error] [See sources]"
  - For: Moderate-risk features, decisions users rely on

Level 4: Active disclosure with acknowledgment
  - "This information was generated by AI and has not been reviewed by a human. By using this information, you acknowledge that it may contain errors. [I understand] [Show me the sources]"
  - For: High-risk features, regulated use cases, first-time users

Level 5: Mandatory human review disclosure
  - "This information was generated by AI and reviewed by [qualified human reviewer name/ID]. Reviewer notes: [notes]. [See AI's original output] [See reviewer's changes] [Report issue]"
  - For: High-stakes decisions, regulated industries
```

### Disclosure Anti-Patterns

**Anti-pattern 1: The Hidden AI**
"Our users don't need to know it's AI. If it works, it works."
**Problem:** Users who discover they were interacting with AI without knowing feel deceived. Trust is destroyed. Also, regulatory requirements increasingly mandate disclosure.
**Fix:** Disclose. Always. The question is HOW, not IF.

**Anti-pattern 2: The Liability Disclaimer**
"This AI-generated content may contain errors, inaccuracies, or omissions. The company assumes no liability for any damages arising from its use."
**Problem:** This tells users "we built something we don't stand behind." If it's not reliable enough to take responsibility for, why should users trust it?
**Fix:** Either build something reliable enough to stand behind, or limit its scope to what you can stand behind.

**Anti-pattern 3: The "Human-Like" Deception**
Giving the AI a human name, avatar, and conversational style designed to make users forget they're talking to AI.
**Problem:** Deceptive design. Users form false expectations about the system's capabilities. When the AI inevitably fails, the trust breach is magnified because the user thought they were dealing with something more capable.
**Fix:** Be clear it's AI. You can be friendly without being deceptive.

**Anti-pattern 4: The "Always Improving" Deflection**
When users report errors: "Our AI is always learning and improving!"
**Problem:** This is a non-response. It tells the user nothing about whether their specific error will be fixed, when, or what they should do now.
**Fix:** "Thank you for reporting this. Here's what happened: [explanation]. Here's what we're doing about it: [specific action and timeline]. Here's what you should do now: [guidance]."

---

## Part 4: Feedback Loops and Continuous Improvement

### The AI Product Feedback Architecture

AI products require more feedback loops than traditional software because:
- You need to know when the AI is wrong (not just when it crashes)
- You need to know when user needs shift (distribution shift)
- You need to improve the model continuously (not just at release boundaries)

| Feedback Loop | What It Captures | Collection Method | Cadence | Action |
|--------------|-----------------|-------------------|---------|--------|
| **Explicit user feedback** | User satisfaction with specific outputs | "Was this helpful?" prompts, ratings, reports | Continuous | Immediate correction; training data for model improvement |
| **Implicit behavioral feedback** | How users actually interact with AI outputs | Acceptance rate, override rate, edit rate, abandonment rate, time-to-next-action | Continuous | UX improvements; confidence threshold adjustment |
| **Human review sampling** | Quality assessment by domain experts | Random sampling of outputs for expert review | Daily/Weekly | Quality monitoring; training data; model retraining triggers |
| **Golden example testing** | Regression detection on known cases | Automated testing of evaluation set | Continuous (CI) | Block deployment; investigate regression |
| **Business outcome correlation** | Is AI actually improving business outcomes? | Correlating AI metrics with business KPIs | Monthly | Strategic decisions: invest more, pivot, or deprecate |
| **User research** | Qualitative understanding of trust, workflow, unmet needs | Interviews, observation, diary studies | Quarterly | Product roadmap; UX redesign; new feature opportunities |
| **Competitive benchmarking** | How does our AI compare to alternatives? | Comparative evaluation on shared tasks | Quarterly | Feature prioritization; positioning; build vs buy decisions |

### The Feedback Flywheel

```
   User uses AI ──▶ AI provides output ──▶ User accepts/edits/rejects
                                                   │
                                                   ▼
   AI improves ◀── Model updated ◀── Feedback aggregated
```

The faster and tighter this flywheel spins, the faster the product improves. PMs should optimize for flywheel speed:

- Reduce the time between error occurrence and user feedback (make feedback easy)
- Reduce the time between feedback and model update (automate where possible)
- Reduce the time between model update and user experiencing the improvement (continuous deployment)

### When NOT to Automate the Feedback Loop

Some feedback should NOT automatically update the model:

1. **Feedback from adversarial users:** Users trying to poison or bias the model.
2. **Feedback during distribution shift:** If input distribution has shifted, feedback from the new distribution may not be representative.
3. **Feedback that contradicts safety policies:** If users "correct" the AI to produce policy-violating content.
4. **Feedback with identity or privacy implications:** Single-user feedback that could personalize the model in ways that affect other users.

In these cases, feedback should go to a human review queue before being incorporated into model updates.

---

## Part 5: The Prototype-to-Production Discontinuity

### Why AI Prototypes Don't Scale

The most dangerous moment in an AI product's lifecycle is the transition from prototype to production. This is where most AI products die. The reasons:

#### The Demo Effect

An AI prototype handles 5 carefully chosen examples beautifully. The team is excited: "It works!" They start building the production system.

In production, the system handles 10,000 diverse inputs per day. The edge cases that the prototype never encountered are now the majority of failures. The team is surprised: "It worked in testing!"

**Prevention:** Test on representative data, not cherry-picked examples. The evaluation set should match the production distribution in volume, diversity, and edge case frequency.

#### The Cost Surprise

The prototype costs $0.02 per query. "At scale, that'll be fine."

At scale (100,000 queries/day), the cost is $2,000/day — $730,000/year. The unit economics collapse. The prototype used cheap models or small context windows that can't handle real user inputs.

**Prevention:** Model costs at projected volume BEFORE building the production system. Include worst-case scenarios: longer conversations, more context, more retries.

#### The Latency Surprise

The prototype responds in 500ms. "Great, that's fast enough."

In production, with concurrent users, context assembly time, retrieval latency, tool call latency, and model inference latency stacking up, real-world p95 latency is 8 seconds. Users abandon.

**Prevention:** Load test with realistic concurrency. Measure end-to-end latency including all system components, not just model inference.

#### The Maintenance Surprise

The prototype was built last month. Since then:
- The model provider updated their API (prompts broke)
- New user segments started using the product (distribution shift)
- A competitor launched a similar feature (expectations changed)
- Three edge cases were discovered that require fundamental architecture changes

The team is now spending 70% of their time maintaining the AI system, not improving it.

**Prevention:** Budget for ongoing AI maintenance (20-40% of engineering capacity, not 5%). Plan for model migrations, prompt updates, evaluation set expansion, and monitoring improvements as ongoing work, not one-time setup.

### The Production Readiness Checklist

Before moving from prototype to production:

```
[ ] Evaluation contract completed and signed off
[ ] Evaluation set of 500+ representative examples (not just 20 golden examples)
[ ] Adversarial testing completed and results reviewed
[ ] Load testing at 2x projected peak volume with acceptable latency
[ ] Cost modeling at projected volume across multiple scenarios
[ ] Monitoring dashboards built and tested
[ ] Alert thresholds configured and tested with simulated failures
[ ] Rollback procedure documented and tested (ideally, performed a live rollback drill)
[ ] Human review workflow operational and staffed
[ ] Incident response plan documented and team trained
[ ] User disclosure and transparency UX implemented
[ ] Provider fallback implemented (if using external API)
[ ] Feedback collection mechanisms implemented and tested
[ ] Bias audit completed and results within thresholds
[ ] Privacy review completed (PII handling, data retention, DPAs signed)
[ ] Regulatory compliance verified (for applicable tiers)
[ ] Launch communication plan prepared (internal + external)
[ ] Success metrics defined and baseline measured
```

---

## Part 6: Organizational Change for AI Products

### The AI Product Organization Problem

AI products require different organizational structures than traditional software. The traditional boundaries (engineering builds, product manages, design creates the UX) break down because:

- **The model IS the product behavior.** "Engineering" decisions about model selection, prompt design, and evaluation methodology ARE product decisions. The PM can't delegate these entirely.
- **Design must account for probabilistic behavior.** Traditional UX assumes deterministic responses. AI UX must handle uncertainty, errors, and variable quality — this requires new design patterns.
- **Quality assurance is continuous, not point-in-time.** Traditional QA tests once before release. AI QA requires ongoing monitoring, evaluation, and human review — this is an operational function, not a pre-release function.
- **Data is a product asset, not an input.** The quality, diversity, and freshness of training, evaluation, and retrieval data directly determines product quality. Data management is a product function, not just an infrastructure function.

### Organizational Models

| Model | Structure | Best For | Risks |
|-------|----------|----------|-------|
| **Embedded AI** | AI capabilities built into existing product teams. No separate AI team. | AI as a feature (not the product). Products where AI enhances existing workflows. | AI expertise diluted. AI treated as feature, not capability shift. |
| **Central AI Platform** | Central AI/ML team builds platforms, tools, and models that product teams consume. | Organizations building AI into multiple products. Standardization benefits. | Platform team disconnected from user needs. Product teams can't customize AI behavior. |
| **AI SWAT Team** | Small dedicated AI team works across products, embedding temporarily to launch AI features, then handing off. | Early-stage AI adoption. Proof-of-concept acceleration. | Handoff failures. Product teams can't maintain what the SWAT team built. |
| **AI-First Product Team** | Product team built from the ground up around an AI product. PM, engineers, designers, data scientists, and domain experts all focused on one AI product. | AI as the core product. New AI-native products. | Expensive. Requires AI talent density. |
| **Federated AI** | Central AI team provides infrastructure, governance, and best practices. Product teams own AI implementation. Joint accountability. | Mature organizations with AI across multiple products. | Coordination overhead. Inconsistent quality across teams. |

### The AI PM's Organizational Role

The AI PM must bridge gaps that don't exist in traditional product management:

| Traditional PM | AI PM |
|---------------|-------|
| Writes PRDs and user stories | Writes evaluation contracts and failure taxonomies |
| Defines feature scope with engineering | Defines AI behavior boundaries with ML engineers and domain experts |
| Reviews designs for UX quality | Reviews designs for trust building, transparency, and error handling |
| Launches features and moves on | Launches features and monitors continuously |
| Measures adoption and engagement | Measures trust, accuracy, and business outcome correlation |
| Manages feature backlog | Manages evaluation backlog (golden examples, adversarial tests, monitoring improvements) |
| Coordinates with engineering, design, marketing | Coordinates with engineering, design, marketing, legal, compliance, data science, domain experts, and sometimes regulators |

### Building AI Literacy in Your Organization

The PM can't do it alone. The organization needs AI literacy at every level:

| Role | AI Literacy Required |
|------|---------------------|
| **Executive** | AI strategy, ROI models, risk governance, regulatory landscape |
| **PM** | Full AI PM curriculum (this module) |
| **Engineering** | AI system architecture, evaluation methodology, prompt engineering, monitoring |
| **Design** | AI UX patterns (trust, transparency, error handling, progressive disclosure) |
| **Marketing** | AI product positioning (features vs trust), competitive landscape, user education |
| **Sales** | AI product capabilities and limitations, handling AI-related objections, demo integrity |
| **Support** | AI triage, identifying AI vs non-AI issues, feeding feedback to product |
| **Legal/Compliance** | AI regulatory frameworks, AI-specific liability, data rights in AI context |
| **HR** | AI in hiring tools compliance, employee AI usage policies |

---

## Part 7: Measuring AI Product Success

### The AI Product Metrics Framework

Traditional product metrics (DAU, retention, revenue) are necessary but insufficient for AI products. Add AI-specific metrics:

#### Quality Metrics

| Metric | Definition | How to Measure |
|--------|-----------|---------------|
| **Task Success Rate (TSR)** | % of user tasks completed successfully without human intervention | Human review sampling; user "task complete" signals |
| **Severity-Weighted Error Rate (SWER)** | Error rate weighted by failure severity (from evaluation contract) | Human review sampling with severity annotation |
| **Hallucination Rate** | % of outputs containing fabricated information | Citation verification; factual consistency check |
| **Golden Example Accuracy** | % of golden examples answered correctly | Automated testing against golden example set |
| **Human-AI Agreement Rate** | % of outputs where human reviewer agrees with AI | Human review sampling |
| **Critic Rejection Rate** | (if using critic) % of outputs rejected by critic model | Automated logging |

#### Trust Metrics

| Metric | Definition | How to Measure |
|--------|-----------|---------------|
| **Acceptance Rate** | % of AI outputs accepted by users without modification | Telemetry (tracking when users use/edit/dismiss AI output) |
| **Override Rate** | % of AI outputs modified or rejected by users | Telemetry |
| **Escalation Rate** | % of interactions where user requests human help | Telemetry |
| **Repeat Use Rate** | % of users who use the AI feature again after first try | Cohort analysis |
| **Trust Score** | User-reported trust in the AI feature | In-product survey: "How much do you trust this feature?" (1-5) |
| **NPS for AI Feature** | Specific NPS for the AI functionality | Survey: "How likely are you to recommend this AI feature?" |

#### Operational Metrics

| Metric | Definition | How to Measure |
|--------|-----------|---------------|
| **Cost Per Task** | Fully loaded cost per completed task | Inference cost + infrastructure + human review amortized |
| **Cost Efficiency Ratio** | Cost per task relative to human-only cost | AI cost / Human cost per same task |
| **Time to Resolution** | End-to-end time from user task initiation to completion | Telemetry |
| **Autonomy Rate** | % of tasks completed without any human involvement | Telemetry |
| **AI Uptime/Quality-Time** | % of time the AI system is operating above quality thresholds | Monitoring |

#### Business Metrics

| Metric | Definition | How to Measure |
|--------|-----------|---------------|
| **AI-Attributed Revenue** | Revenue attributable to AI features | A/B testing; user segmentation (AI users vs non-AI users) |
| **AI-Attributed Cost Savings** | Cost reduction from AI automation | Comparison to pre-AI cost baseline |
| **AI ROI** | (AI-attributed revenue + savings) / (AI development + operations cost) | Financial analysis |
| **AI-Driven Retention** | Retention improvement correlated with AI usage | Cohort analysis |
| **AI Competitive Win Rate** | % of competitive deals where AI capability was a deciding factor | Sales feedback |

### The Metric Hierarchy

Not all metrics are equally useful. Structure them:

```
Level 1: NORTH STAR — The one metric that defines AI product success
  Example: "Task success rate > 95% with per-task cost < 50% of human baseline"

Level 2: HEALTH METRICS (3-5 metrics that signal system health)
  Example: TSR, SWER, Acceptance Rate, Cost Per Task, p95 Latency

Level 3: DIAGNOSTIC METRICS (metrics for debugging when health metrics decline)
  Example: Hallucination rate by input category, override rate by user segment,
           cost by model, latency by component

Level 4: EXPLORATORY METRICS (metrics for future optimization)
  Example: User trust score correlation with retention, AI feature usage
           patterns by persona, feedback sentiment analysis
```

### The Success Measurement Cadence

| Cadence | Review | Participants | Focus |
|---------|--------|-------------|-------|
| **Daily** | AI Health Dashboard | On-call engineer | Are we within thresholds? Any anomalies? |
| **Weekly** | AI Quality Review | PM, Engineering Lead, Data Science | Quality trends, feedback review, evaluation set updates |
| **Monthly** | AI Product Review | PM, Engineering, Design, Data Science, Support, Marketing | Metric trends, user feedback themes, competitive landscape, roadmap adjustments |
| **Quarterly** | AI Business Review | PM, Executive Sponsor, Finance, Legal | ROI, strategic alignment, build vs buy decisions, regulatory updates, budget planning |
| **Annually** | AI Strategy Review | Leadership Team, Board | AI product strategy, major investments, organizational structure, long-term roadmap |

---

## Part 8: The AI Adoption Playbook

### Phase 1: Internal Validation (2-4 weeks before external launch)

1. **Dogfood the AI yourself.** Use it for real tasks. Keep a log of every error, frustration, and surprise.
2. **Internal beta with non-engineering teams.** Get feedback from people who didn't build it. Sales, support, marketing — they'll find different issues than engineering.
3. **Controlled pilot with 5-10 friendly customers.** Not your biggest fans, but customers who will give honest feedback. Set expectations that this is early and will improve.

### Phase 2: Limited Launch (2-8 weeks)

1. **Launch to a segment with high tolerance and low stakes.** Users who need the feature and will give constructive feedback.
2. **Heavy monitoring and rapid response.** Review every piece of feedback daily. Fix critical issues within 24 hours.
3. **Active community building.** Create a feedback channel (Slack, Discord, forum). Respond to every post. Show users their feedback matters.
4. **Weekly quality reports to the team.** "This week: 94.2% task success, 3 critical errors (all resolved), 47 pieces of user feedback (12 implemented, 18 in backlog, 17 not planned)."

### Phase 3: Scaled Launch (weeks 8+)

1. **Gradual rollout.** 10% → 25% → 50% → 100%. Monitor at each stage. Be willing to pause or roll back.
2. **Segmented by trust profile.** Launch faster to AI-tolerant segments; slower to AI-skeptical segments. Use learnings from tolerant segments to improve the product for skeptical segments.
3. **Proactive communication.** Don't wait for users to discover the AI feature. Email, in-app messaging, blog post, documentation. Explain what it does, what it doesn't do, and how to give feedback.
4. **Success story amplification.** When users have great experiences, capture and share them (with permission). User testimonials build trust more effectively than marketing claims.

### Phase 4: Sustained Growth (ongoing)

1. **Continuous quality improvement.** The product should be better this month than last month, measurably. Publish improvement reports.
2. **Expanding scope.** As quality improves on the narrow use case, expand to adjacent use cases. Users who trust the narrow version are more accepting of the expanded version.
3. **Community engagement.** Power users become evangelists. Engage them with early access to new features, feedback channels, and recognition.
4. **Competitive differentiation through quality.** When competitors race to ship more AI features, you win by shipping more RELIABLE AI features. Quality is the moat.

---

## Practical Application

1. Rate your AI product on the four trust pillars (Reliability, Transparency, Control, Recourse). Score each 1-5. Which is weakest? What's one concrete improvement you can make this month?

2. Audit your disclosure UX. Do you clearly tell users they're interacting with AI? Do you explain limitations? Is human escalation easy to find?

3. Map your feedback loops. How long does it take from a user reporting an error to that error being fixed for all users? Where is the bottleneck?

4. Calculate your prototype-to-production readiness. Using the checklist in Part 5, how many items can you check? What's missing?

5. Review your AI product metrics. Do you have a clear North Star? Health metrics? Diagnostic metrics? Is anyone actually looking at them regularly?

---

## Discussion Prompts

1. What's the biggest trust issue users have with your AI product? What evidence do you have for that (vs. what you assume)?

2. Has your team launched an AI feature that users didn't adopt as expected? What do you think happened? Was it a trust issue, a utility issue, or something else?

3. Does your organization have the right structure for AI product development? What's the biggest organizational barrier to AI product success?

4. How do you currently measure AI product success? Would your CEO agree that your metrics are the right ones?

5. When was the last time you personally used your AI product as a real user (not in a demo or test environment)? What did you learn?
