# Model vs System: Why the Model Is Not the Product

**Status:** v0.1.0
**Depends on:** WORKFLOW_SELECTION.md, EVALUATION_CONTRACTS.md

---

## TL;DR

In AI product management, the most persistent and damaging misconception is:

> "If the model is good enough, the product will work."

The model is one component in a system. The system includes data pipelines, context assembly, retrieval mechanisms, tool integrations, validation layers, human-in-the-loop workflows, caching, routing, output formatting, monitoring, and fallback logic. In most AI products, system design matters more than model selection for the first 80% of product quality. The model becomes the binding constraint only when the system is well-designed.

---

## Part 1: System Architecture Fundamentals

### The AI System Stack

Every AI product has the following layers, whether explicit or implicit. The PM's job is to make them explicit and ensure they're designed, not left as emergent properties.

```
┌──────────────────────────────────────┐
│         PRESENTATION LAYER           │
│  UI, API design, output formatting,  │
│  streaming, progressive rendering    │
├──────────────────────────────────────┤
│         ORCHESTRATION LAYER          │
│  Workflow routing, multi-step logic, │
│  tool calling, human handoff,        │
│  state management, retry logic       │
├──────────────────────────────────────┤
│         VALIDATION LAYER            │
│  Output validation, guard models,    │
│  format enforcement, PII detection,  │
│  business rule compliance            │
├──────────────────────────────────────┤
│         CONTEXT LAYER               │
│  Retrieval, context assembly,        │
│  prompt construction, data           │
│  formatting, citation management     │
├──────────────────────────────────────┤
│         DATA LAYER                  │
│  Knowledge bases, vector stores,     │
│  databases, APIs, document stores,   │
│  user profiles, session history      │
├──────────────────────────────────────┤
│         MODEL LAYER                 │
│  LLM, embedding model, classifier,   │
│  reranker, speech-to-text,           │
│  image generation, etc.              │
├──────────────────────────────────────┤
│         INFRASTRUCTURE LAYER        │
│  Compute, networking, caching,       │
│  CDN, logging, monitoring,           │
│  rate limiting, authentication       │
└──────────────────────────────────────┘
```

### The 80/20 Rule of AI System Quality

In most AI products in 2026, the quality distribution looks approximately like:

| Layer | Contribution to Overall Quality | Key PM Decisions |
|-------|-------------------------------|-----------------|
| Data & Context | 35% | What data do we have? How do we retrieve, format, and prioritize it? |
| Prompt Construction | 15% | What instructions, examples, and constraints do we provide? |
| Validation & Guardrails | 15% | How do we catch and handle bad outputs? |
| Orchestration | 10% | What's the workflow? When do we route to humans? |
| Model Selection | 15% | Which model family? What size? What provider? |
| Infrastructure | 5% | Latency, throughput, cost, reliability |
| Presentation | 5% | How do users interact with AI outputs? |

Notice: **Model selection is ~15% of the quality equation.** Yet most AI PM conversations start and end with "which model should we use?" This is a category error.

### What This Means for PM Decision-Making

1. **Invest in data and context before chasing model upgrades.** A well-retrieved, well-formatted context improves output quality more than switching from one frontier model to another for most use cases.

2. **Build validation before you build orchestration.** If you can't tell whether an output is good or bad, it doesn't matter how sophisticated your multi-step workflow is — you can't trust any step.

3. **Model selection is a cost/quality/latency trade-off, not a quality decision.** For most products, frontier models are overkill. A smaller, faster, cheaper model with good context and validation often outperforms an expensive frontier model with poor system design.

4. **The model layer is the most swappable.** Design your system so you can change models without rewriting everything. This is not just about avoiding vendor lock-in — it's about being able to route different tasks to different models based on complexity, cost, and latency requirements.

---

## Part 2: Data and Context Architecture

### The Context Quality Hierarchy

Not all context is equal. The quality of the context you provide to the model directly determines the quality of the output. The hierarchy:

```
Tier 1: PERFECT CONTEXT
- Exactly the information the model needs, organized exactly as the model needs it
- No irrelevant information, no noise, no contradictions
- Source: Curated knowledge base, structured database with high-quality schema

Tier 2: GOOD CONTEXT
- Relevant information present but may include some noise
- May require the model to identify which parts are relevant
- Source: Good retrieval pipeline, well-organized document store

Tier 3: ADEQUATE CONTEXT
- Most relevant information present but also significant noise
- Some relevant information may be missing
- Source: Basic retrieval pipeline, loosely organized documents

Tier 4: POOR CONTEXT
- Most information is irrelevant, key facts missing or buried
- Model must work hard to extract signal from noise
- Source: Naive retrieval, poorly organized data, keyword search

Tier 5: NO CONTEXT
- Model relies entirely on training data
- Produces confident-sounding hallucinations, generic responses, or outdated information
```

**Key PM insight:** Moving from Tier 5 to Tier 3 typically improves output quality more than switching from the 3rd-best model to the best model. Moving from Tier 3 to Tier 1 often makes a mid-tier model outperform a frontier model with Tier 3 context.

### Context Architecture Patterns

#### Pattern 1: Simple Retrieval-Augmented Generation (RAG)

```
User Query → Query Reformulation → Embedding Search → Top-K Retrieval → 
Context Assembly → Prompt Construction → Model Inference → Output
```

**When to use:** Document Q&A, knowledge base search, any use case where answers exist in a corpus.

**PM considerations:**
- Chunking strategy: How do you split documents? By paragraph? By semantic unit? Fixed size? This is one of the highest-leverage decisions in RAG quality.
- Retrieval count (K): More documents = more context but more noise and higher cost. Find the sweet spot.
- Reranking: A second-pass reranker can dramatically improve retrieval quality at modest additional cost.
- Freshness: When was the corpus last updated? If the answer changed yesterday but the index is a week old, the model will confidently give the outdated answer.

#### Pattern 2: Structured Data Integration

```
User Query → Query Decomposition → SQL/API Generation → Database Query → 
Result Formatting → Context Assembly → Prompt Construction → Model Inference → Output
```

**When to use:** Analytics Q&A, business intelligence, any use case where answers live in structured databases.

**PM considerations:**
- Text-to-SQL is not text-to-insight. The model can generate a query, but interpreting results, identifying anomalies, and deriving insights is a different (harder) task.
- Schema quality matters enormously. If your database has cryptic column names, the model will fail — not because of model limitations but because the schema is unreadable.
- Query validation: Generated queries should be validated (syntax check, read-only enforcement, row limit) before execution. Never let an LLM write and execute arbitrary SQL without guardrails.
- Cost: Each query requires 2+ model calls (query generation + result interpretation). Plan accordingly.

#### Pattern 3: Multi-Source Fusion

```
User Query → Source Routing → [Source A Retrieval, Source B Query, Source C API] →
Result Merging → Deduplication → Contradiction Detection → Context Assembly →
Prompt Construction → Model Inference → Output
```

**When to use:** Complex research tasks, competitive intelligence, any use case requiring information from multiple heterogeneous sources.

**PM considerations:**
- Contradiction handling: What happens when Source A and Source B disagree? Must the system surface the contradiction, pick a winner, or escalate to human?
- Source freshness: Different sources update at different cadences. Real-time API, daily database sync, weekly knowledge base refresh. The model may synthesize information from incompatible time windows.
- Cost explosion: Multiple retrievals × multiple model calls. Multi-source systems can easily cost 5-10x more per query than single-source systems.

#### Pattern 4: Agentic Retrieval

```
User Query → Planning → [Search, Filter, Read, Evaluate, Refine Query, Search Again] →
Iteration until sufficient → Context Assembly → Model Inference → Output
```

**When to use:** Research tasks requiring exploration, complex questions where the information need cannot be fully specified upfront.

**PM considerations:**
- Termination: When does the agent stop searching? Without clear stopping criteria, agents either give up too early (miss relevant information) or search forever (cost and latency explode).
- Search budget: Define maximum search steps, maximum tokens, maximum cost per query.
- Transparency: Show the user what the agent did. "I searched for X, found Y documents, read Z sections..." This builds trust and lets users identify when the agent missed something important.

### Context Quality Metrics

How do you know if your context pipeline is working? Measure:

| Metric | Definition | Target |
|--------|-----------|--------|
| **Recall@K** | % of queries where the correct answer exists in the top K retrieved documents | >95% |
| **Precision@K** | % of retrieved documents that are relevant | >80% |
| **Mean Reciprocal Rank (MRR)** | How highly ranked the first relevant document is | As close to 1.0 as possible |
| **Context utilization** | % of retrieved tokens that are actually used in the output | >50% (if less, you're wasting money) |
| **Hallucination rate** | % of statements in output not supported by retrieved context | As close to 0% as possible |

**PM action:** These metrics should be part of your evaluation contract's monitoring plan. If recall drops below threshold, your model will hallucinate regardless of which model you use.

---

## Part 3: Retrieval and Tool Use Patterns

### The Tool-Use Decision Framework

Not every AI product needs tool use. Adding tools increases complexity, cost, and failure modes. Use this framework to decide:

```
Can the model answer from its training data alone?
├── YES → No tools needed. Use a strong prompt with instructions.
└── NO → Does the answer depend on real-time data?
    ├── YES → Add retrieval or API tool for that data source.
    └── NO → Does the answer require computation the model can't do internally?
        ├── YES → Add calculator, code execution, or reasoning tool.
        └── NO → Does the answer require taking an action in external systems?
            ├── YES → Add action tool with appropriate permissions.
            └── NO → The model's training data should suffice. Re-examine your data/context strategy.
```

### Tool Design Principles

When designing tools for AI systems:

1. **Single responsibility:** Each tool does one thing well. Don't build a "do everything" tool — it's hard to prompt, hard to evaluate, and produces unpredictable behavior.

2. **Clear failure modes:** Every tool should return explicit error messages that the model can understand and act on. "Error 500" is useless. "Database query failed: connection timeout after 30s" gives the model something to work with.

3. **Idempotency:** If the model calls a tool twice (retry, looping, error), the second call should not cause problems. This is especially important for action tools (sending emails, creating records, charging payments).

4. **Cost and latency metadata:** The model doesn't know which tools are fast/cheap vs slow/expensive. Consider providing this in the tool description so the model can plan its tool use intelligently.

5. **Permission boundaries:** Tools should enforce permissions, not rely on the model to respect them. If a tool can delete production data, that capability should be restricted by infrastructure-level controls, not by prompt instructions.

### Retrieval Quality Anti-Patterns

**Anti-pattern 1: "Just dump everything in a vector database"**
Symptom: Low precision, high noise, model produces plausible-sounding answers built on irrelevant chunks.
Fix: Curate what goes into retrieval. Not all documents belong in the retrieval index. Some should be structured data, rule engines, or reference documents the model can query directly.

**Anti-pattern 2: "More context is always better"**
Symptom: High cost, slow responses, model "loses" information in long contexts (lost-in-the-middle problem).
Fix: Set a token budget for context. Prioritize the most relevant information. If context exceeds budget, summarize or compress before including.

**Anti-pattern 3: "Retrieval is a solved problem"**
Symptom: No evaluation of retrieval quality. Assumption that "semantic search" works out of the box.
Fix: Measure retrieval quality independently of output quality. Run retrieval evaluation on a labeled dataset. Track recall and precision over time.

**Anti-pattern 4: "One retrieval strategy for all queries"**
Symptom: Good performance on simple queries, terrible on complex ones (or vice versa).
Fix: Classify queries by complexity and route to appropriate retrieval strategies. Simple fact lookup → keyword search. Complex reasoning → multi-step retrieval. Comparison queries → parallel retrieval.

---

## Part 4: Build vs Buy vs Provider Strategy

### The Decision Framework

For any AI capability, you have three options:

| Strategy | What It Means | When to Choose |
|----------|--------------|----------------|
| **Provider** | Use a managed API (OpenAI, Anthropic, Google, etc.) | Standard model capabilities, fast time to market, low engineering investment, acceptable cost structure |
| **Buy** | Use a specialized AI product/SaaS that embeds AI | Vertical-specific workflows, regulated industries, don't want to build AI infrastructure, value is in integration not novel AI |
| **Build** | Train, fine-tune, or host models yourself | Proprietary data advantage, unique capability not available from providers, cost optimization for very high volume, data must never leave your infrastructure |

### Provider Strategy Considerations

Using a provider API (OpenAI, Anthropic, Google, Microsoft, etc.) is the default choice for most AI products in 2026. It's the fastest path to market and requires the least AI-specific engineering.

**Advantages:**
- Always using the latest model (providers update APIs automatically)
- No infrastructure to manage
- Pay-per-use pricing matches early-stage uncertainty
- Built-in safety and content moderation (varies by provider)

**Risks:**
- **Price changes:** Providers can (and do) change pricing. Your unit economics can shift without notice.
- **Model changes:** Providers update models. Your prompts may break. Your failure modes may change. Your costs may change.
- **Availability:** Provider outages are your outages. You cannot fix them.
- **Data terms:** Your data goes to the provider. For some use cases (healthcare, defense, finance), this is a non-starter.
- **Deprecation:** Providers deprecate old models. You must migrate, or your system breaks.

**PM mitigation strategies:**
1. Abstract model access behind your own API layer. Don't call provider APIs directly from application code.
2. Maintain a fallback provider. If Provider A is down, route to Provider B (even if quality is slightly lower).
3. Monitor provider status pages and have a communication plan for provider outages.
4. Understand the data processing terms. What does the provider do with your data? Do they train on it? What are the retention policies?
5. Budget for model migration. Assume you'll need to migrate models every 12-18 months.

### Buy Strategy Considerations

Buying a specialized AI product (e.g., Intercom's AI agent for customer support, GitHub Copilot for code, Notion AI for writing) can be the right choice when AI is ancillary to your core product.

**Advantages:**
- Zero AI infrastructure to build
- Productized AI with dedicated teams improving it
- Typically cheaper than building for non-core AI features
- May include compliance certifications you'd need to obtain independently

**Risks:**
- **Integration lock-in:** Your product couples to their API and UI patterns.
- **Limited customization:** You can't fine-tune or modify the AI behavior beyond their configuration options.
- **Pricing leverage:** Once integrated, they can raise prices.
- **Roadmap divergence:** Their product direction may diverge from your needs.
- **Data concentration:** Your users' data accumulates in another vendor's system.

**PM mitigation strategies:**
1. Evaluate the exit cost before integrating. Can you migrate to another provider or bring it in-house if needed?
2. Understand the data model. Can you export your data? In what format? How long does it take?
3. Negotiate data processing terms. Your AI vendor is a data processor; ensure the DPA covers your compliance requirements.
4. Build an abstraction layer even for bought AI. Your product should not be so tightly coupled that changing AI vendors requires a rewrite.

### Build Strategy Considerations

Building your own AI capability (training, fine-tuning, hosting) is the most expensive and slowest option. It should be chosen only when the other options are clearly insufficient.

**Valid reasons to build:**
- Proprietary data that creates a durable advantage if used for training/fine-tuning
- Volume so high that provider API costs exceed infrastructure costs by >2x
- Data that cannot leave your infrastructure (regulatory, contractual, security)
- Capability that no provider offers (novel model architecture, specialized domain fine-tuning)
- Latency requirements below what provider APIs can guarantee

**Invalid reasons to build:**
- "We want to own the technology" (provider APIs are cheaper and better for most use cases)
- "Our engineers are excited about it" (engineer excitement ≠ product value)
- "The provider margin seems high" (your infrastructure team's fully-loaded cost is almost certainly higher)
- "We might need it someday" (build when the need is demonstrated, not when it's hypothetical)

**Cost comparison framework:**

```
ANNUAL PROVIDER COST:
  = Annual inference volume × Cost per inference (provider API)

ANNUAL BUILD COST (3-year amortized):
  = (Engineering cost to build & maintain + Infrastructure cost + 
     GPU/compute cost + Ongoing fine-tuning cost + 
     Monitoring & ops cost) / 3

+ OPPORTUNITY COST:
  = Value of what your team would have built instead during the build time

+ RISK PREMIUM:
  = Probability of build failure × Cost of failure
    (Build failure includes: model doesn't meet quality bar, takes 2x longer,
     key engineers leave, technology becomes obsolete before completion)
```

**Decision rule:** If `Annual Provider Cost < (Annual Build Cost + Opportunity Cost + Risk Premium)`, use a provider. This will be true for the vast majority of products.

---

## Part 5: Model Portability and Vendor Lock-In

### The Portability Spectrum

AI vendor lock-in is real. It exists on a spectrum:

| Lock-In Level | Characteristics | Mitigation Strategy |
|--------------|----------------|-------------------|
| **Low** | Any model, any provider, standard API call | None needed. You're already portable. |
| **Medium** | Provider-specific API format, prompt engineering optimized for one model family | Abstract API layer, prompt versioning, multi-provider testing in CI |
| **High** | Fine-tuned on provider's API, custom model architecture from one provider, RAG pipeline optimized for one model's context window | Maintain fine-tuning data, document fine-tuning recipe, plan migration path |
| **Very High** | Custom model trained from scratch by one provider, proprietary architecture, no export path | This is a strategic bet. Ensure the value justifies the lock-in. |

### Portability Best Practices

1. **API abstraction layer:** Your application code should never call `openai.ChatCompletion.create()` directly. It should call `YourAIService.generate()` which routes to the appropriate provider. This is a one-week engineering investment that saves months of migration work.

2. **Prompt versioning and testing:** Every prompt should be versioned and tested across your supported providers. When Provider A updates their model, your CI system should flag any prompts that produce different (worse) outputs.

3. **Avoid provider-specific features unless they're 10x better:** Features like function calling, structured outputs, and vision capabilities are available from multiple providers. Features unique to one provider create lock-in. Use them only when the value is overwhelming.

4. **Multi-provider evaluation:** Run your evaluation set against multiple providers regularly. Know the quality/cost/latency trade-off for each provider on YOUR data, not on their published benchmarks.

5. **Negotiate data portability:** In enterprise contracts, negotiate for the right to export fine-tuning data, evaluation data, and usage data in a usable format.

---

## Part 6: Inference Economics

### Understanding the Cost Drivers

AI inference costs are driven by:

| Cost Driver | What It Means | PM Lever |
|------------|--------------|----------|
| **Model size** | Larger models cost more per token | Route simple tasks to smaller models |
| **Context length** | Longer context = more tokens processed = higher cost | Be aggressive about context pruning |
| **Output length** | Model generates tokens auto-regressively; longer outputs = more cost | Set output token limits; don't let models ramble |
| **Request volume** | More requests = more cost | Implement caching, rate limiting, user quotas |
| **Peak concurrency** | More simultaneous requests may require more provisioned throughput | Smooth demand with async processing, queues |
| **Provider margin** | Different providers have different markups over compute cost | Compare providers; negotiate enterprise pricing |

### The Cost-Per-Quality Curve

For any given task, there's a cost-per-quality curve:

```
Quality
  ^
  │                                    ┌─────────────
  │                              ┌─────┘  (diminishing returns)
  │                        ┌─────┘
  │                  ┌─────┘         ← "Sweet spot" region
  │            ┌─────┘
  │      ┌─────┘
  │ ┌────┘
  └────┴──────────────────────────────────────────→ Cost
```

Key insights:
- The first dollar of AI inference produces the most quality improvement.
- There's a "sweet spot" where cost is reasonable and quality is good.
- Beyond the sweet spot, each additional dollar produces less quality improvement.
- The PM's job is to find the sweet spot for their product and use case.

### Cost Optimization Toolkit

| Technique | What It Does | Quality Impact | Cost Impact |
|-----------|-------------|---------------|-------------|
| **Semantic caching** | If the same (or similar) query has been asked before, return the cached answer | None (if cache hit is correct) | Up to 50% reduction |
| **Model routing** | Send simple queries to cheap models, complex queries to expensive models | Minimal (if router is accurate) | 30-70% reduction |
| **Context pruning** | Only include relevant context; summarize or drop the rest | May improve quality by reducing noise | 20-50% reduction |
| **Output token limits** | Cap the number of tokens the model can generate | May truncate responses; set generous limits | 10-30% reduction |
| **Prompt compression** | Use shorter prompts; remove unnecessary instructions | May reduce instruction-following quality | 5-20% reduction |
| **Batching** | Group requests to use provider batch pricing | None (if latency not critical) | Up to 50% reduction |
| **Fine-tuning** | Fine-tune a smaller model on your task | May improve quality for narrow tasks | 80-95% reduction vs frontier model |
| **Self-hosting** | Run open-source models on your own infrastructure | Depends on model and team quality | May reduce, may increase |

### Latency, Throughput, and Cost Trade-Offs

The classic trade-off triangle:

```
                LATENCY
                  /\
                 /  \
                /    \
               /      \
              /  GOOD  \
             /   FAST   \
            /   CHEAP    \
           /______________\
    THROUGHPUT            COST
```

In AI systems, you can optimize for two of the three:

- **Low latency + high throughput:** Expensive. Needs lots of provisioned capacity, multiple replicas, or smaller/faster models.
- **Low latency + low cost:** Low throughput. Can't handle many concurrent requests. Good for internal tools, bad for consumer products.
- **High throughput + low cost:** High latency. Batching, queuing, async processing. Good for batch workloads, bad for interactive products.

**PM decision:** Which two matter most for YOUR product? A real-time customer support chatbot needs low latency + high throughput (users abandon slow chats). A document analysis pipeline needs high throughput + low cost (analysts submit documents and check back later). The evaluation contract should specify which trade-off governs.

---

## Part 7: The Model Selection Framework

### When Model Selection Matters

Model selection matters when your system is already good and you're trying to push the last 10-20% of quality. If your system is struggling with basics (context is missing, prompts are ambiguous, validation is absent), changing models will not fix it.

Model selection is a second-order concern. Fix first-order concerns (data, context, validation, orchestration) before optimizing model choice.

### The Selection Process

When you ARE at the model selection stage:

1. **Define evaluation criteria from your evaluation contract** — Not benchmarks, but your product-specific metrics: task success rate, severe error rate, cost per task, latency p95.

2. **Create a representative evaluation set** — 100-1000 real or realistic examples drawn from your target distribution. NOT the same as your golden examples (which should be a separate, smaller set).

3. **Evaluate multiple models on YOUR evaluation set** — Don't rely on published benchmarks. Run your evaluation.

4. **Analyze failure patterns, not just scores** — Two models might both score 92%, but Model A makes trivial errors and Model B makes catastrophic ones. The aggregate score doesn't tell you this.

5. **Factor in cost and latency** — A model with 94% accuracy at $0.10/query vs one with 92% accuracy at $0.01/query. The choice depends on your error cost. If each error costs $5 in human rework, the cheaper model saves $0.09/query but creates $0.10/query in additional rework — net negative.

6. **Consider the provider relationship** — Support SLAs, data processing terms, model stability commitments, deprecation policies. These "soft" factors can outweigh small quality differences.

### The Model Routing Architecture

Rather than picking ONE model, consider a router architecture:

```
User Query → Complexity Classifier → 
   ├── Simple → Cheap model (e.g., GPT-4o-mini, Claude Haiku)
   ├── Medium → Mid-tier model (e.g., GPT-4o, Claude Sonnet)
   └── Complex → Frontier model (e.g., GPT-4.5, Claude Opus)
```

This gives you the best of all worlds: low cost for simple queries, high quality for complex queries. The key is building an accurate complexity classifier (which can itself be a small, cheap model).

---

## Practical Application

For a product you're working on or considering:

1. Map your planned AI system onto the six-layer stack. What's defined at each layer? What's missing?
2. Characterize your context quality. What tier are you at? What would it take to move up one tier?
3. Apply the build-vs-buy-vs-provider framework. Which strategy is appropriate for your use case? What are the risks?
4. If using a provider, build a migration cost estimate. What would it cost (in engineering time and migration period) to switch providers?
5. Estimate your inference cost at projected volume. Does the unit economics work?

---

## Discussion Prompts

1. What percentage of your team's AI quality discussions focus on model selection vs data/context/validation? Is this the right balance?

2. Have you done a provider migration cost analysis? If your primary provider doubled prices, how quickly could you switch?

3. What's your context quality tier? What's the single highest-leverage improvement you could make to your context pipeline?

4. Has your team ever switched models and seen quality go DOWN despite higher benchmark scores on the new model? What did this teach you about the relationship between benchmarks and your product?

5. What's your inference cost as a percentage of the value created by the AI feature? Is it sustainable as the product scales?
