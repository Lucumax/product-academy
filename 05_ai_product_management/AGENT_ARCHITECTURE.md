# Agent Architecture: AI Agent Product Design and Safety

**Status:** v0.1.0
**Depends on:** WORKFLOW_SELECTION.md, MODEL_VS_SYSTEM.md, FAILURE_MODES.md

---

## TL;DR

AI agents are systems that can plan, use tools, and take multi-step actions to achieve goals. They are the most powerful and most dangerous pattern in AI product design. Every agent capability you add increases the product's surface area for both value creation and catastrophic failure. The PM's job is to identify when agents add value (vs when simpler patterns suffice), bound agent authority, design multi-agent coordination where needed, embed human oversight at the right checkpoints, and ensure the system is observable and recoverable.

This is NOT an engineering architecture guide. It's a product architecture guide: what decisions a PM must make about agent systems, independent of how they're implemented.

---

## Part 1: When Agents Add Value (And When They Don't)

### The Agent Value Test

Before adding agent capabilities to your product, answer these five questions:

```
1. DOES THE TASK REQUIRE MULTIPLE STEPS?
   One-step tasks (Q&A, classification, summarization) don't need agents.
   Single model call + good prompt is sufficient.

2. DO THE STEPS DEPEND ON INTERMEDIATE RESULTS?
   If Step B's requirements are known before Step A executes,
   you can hardcode the workflow. Agents are for dynamic planning,
   not pre-defined pipelines.

3. IS THE ENVIRONMENT DYNAMIC?
   If the task operates on static information,
   a single smart prompt with all context may suffice.
   Agents shine when they need to discover information iteratively.

4. DOES THE TASK REQUIRE EXTERNAL ACTIONS?
   If the model can reason internally without tool use,
   an agent is overkill. Agents justify their complexity when
   they need to query APIs, search databases, or take actions.

5. DOES THE COST-BENEFIT OF AGENTIC FLEXIBILITY EXCEED
   THE COST-BENEFIT OF A DETERMINISTIC WORKFLOW?
   Agents are expensive (multiple model calls) and unreliable
   (error compounding). If a deterministic workflow handles
   90%+ of cases, add it for the remaining 10%, not for
   the 90%.
```

**Decision heuristic:**

| Circumstance | Recommended Approach |
|-------------|---------------------|
| Single-step, deterministic input/output | Simple prompt + model call. No agent. |
| Multi-step, but steps are always the same | Pre-defined workflow with fixed steps. Deterministic orchestration. No agent. |
| Multi-step, steps vary based on input, but structure is predictable | Template-based routing: classify intent + branch to appropriate fixed workflow. Lightweight agency. |
| Multi-step, steps vary based on intermediate discoveries | Full agent with planning + tool use. |
| Multi-step, open-ended exploration, unpredictable path | Full agent with planning + tool use + exploration budget + termination criteria. |

### The Agent Complexity Tax

Every layer of agent capability adds:

| Capability | Value Add | Complexity Add | Risk Add |
|-----------|----------|---------------|----------|
| Single model call with good prompt | Base capability | Baseline | Low |
| + Tool use (API calls, search, database queries) | Can access external information | Medium | Medium (tool errors, permission issues, cost) |
| + Planning (model decides what steps to take) | Can handle novel tasks without pre-defined workflow | High | High (bad plans, infinite loops, cost explosion) |
| + Memory (persistent state across invocations) | Can learn user preferences, maintain context across sessions | Medium | Medium (privacy, stale state, data corruption) |
| + Multi-agent coordination | Can handle tasks too complex for a single agent | Very High | Very High (coordination failures, cascading errors, cost multiplier) |
| + Autonomous action (agent takes actions without human approval) | Can operate at scale without human bottleneck | High | Very High (unauthorized actions, runaway agents, liability) |
| + Self-improvement (agent updates its own prompts, data, or models) | Can adapt to changing conditions | Extreme | Extreme (feedback loops, capability drift, unpredictable behavior) |

**PM principle:** Start with the simplest pattern that can deliver value. Add agent capabilities only when simpler patterns demonstrably fail. Most products never need to go beyond tool use + deterministic orchestration.

### The "Not Every Chatbot Needs to Be an Agent" Rule

In 2024-2026, there's a tendency to call everything an "agent." A customer support system that routes queries to pre-defined workflows is not an agent — it's a router with good NLU. Call things what they are. The word "agent" implies a specific architecture (planning + tool use + autonomous action) and a specific risk profile. Using it for simpler systems creates confusion and makes governance harder.

---

## Part 2: Permission Models and Safety Boundaries

### The Agent Authority Ladder

Define what your agent is authorized to do at each level:

```
Level 0: READ-ONLY OBSERVER
  - Can read/search information
  - Cannot modify anything
  - Cannot send messages to users (output is API response, not direct user communication)
  Examples: Internal search agent, data analysis agent, research assistant

Level 1: INFORMATIONAL RESPONDENT
  - All Level 0 capabilities
  - Can respond to users with informational content
  - Cannot take actions on behalf of users or the system
  - Cannot make promises about system capabilities
  Examples: Q&A chatbot, documentation assistant, knowledge base search

Level 2: ADVISORY RECOMMENDER
  - All Level 1 capabilities
  - Can make recommendations or suggestions to users
  - Recommendations are advisory only; user must take action
  - Cannot execute on its own recommendations
  Examples: Product recommendation engine, investment research assistant,
             code review suggestion tool

Level 3: DRAFT PRODUCER
  - All Level 2 capabilities
  - Can produce drafts that require human approval to take effect
  - Drafts are routed to a human review queue
  - Cannot publish, send, or execute drafts without approval
  Examples: Email draft generator (human must send), code generation with PR required,
             content creation with editor approval

Level 4: CONSTRAINED ACTOR
  - All Level 3 capabilities
  - Can take actions within tightly constrained boundaries
  - Boundaries: monetary limits, domain restrictions, time windows, rate limits
  - All actions logged, auditable, and reversible where possible
  Examples: Customer support agent that can issue refunds up to $50,
             scheduling agent that can book within calendar constraints,
             database agent that can update specific fields

Level 5: AUTONOMOUS ACTOR
  - Can take actions within broader boundaries
  - Human oversight is on-the-loop (monitoring, not approving each action)
  - Sophisticated safety mechanisms required
  - Full audit trail required
  Examples: Autonomous trading agent (within risk limits),
             autonomous infrastructure management agent,
             autonomous content moderation agent (for low-severity content)

Level 6: UNBOUNDED ACTOR (NOT RECOMMENDED for current technology)
  - Can take any action on behalf of users
  - Human oversight is post-hoc or absent
  - This level of agency is inappropriate for 2026 technology
  - If you think you need this, you're probably over-scoping your agent
```

### Selecting an Authority Level

Match the authority level to your governance risk tier (from GOVERNANCE.md):

| Governance Tier | Maximum Authority Level | Justification |
|----------------|------------------------|---------------|
| Tier 1 (Minimal) | Level 5 | Low stakes; autonomous action acceptable |
| Tier 2 (Low) | Level 3 | Moderate stakes; drafts require human approval |
| Tier 3 (Moderate) | Level 2 (Level 3 with strong approval workflow) | Advisory role; agent should not take consequential actions |
| Tier 4 (High) | Level 1 (Level 2 with human-in-the-loop for every recommendation) | High stakes; agent provides information and suggestions only |
| Tier 5 (Maximum) | Level 0 (Level 1 with extreme caution) | Maximum stakes; agent observes and reports only |

### Safety Boundaries Implementation

Safety boundaries must be enforced through multiple layers — never just the prompt:

| Layer | What It Does | Example |
|-------|-------------|---------|
| **Prompt-level instructions** | Instructions in the system prompt about what the agent should/shouldn't do | "Never approve refunds over $500." |
| **Tool-level restrictions** | Parameter validation in tool implementations | The refund tool validates amount is less than $500 before processing. |
| **Infrastructure-level permissions** | API scopes, database permissions, IAM roles | The agent's API key cannot call the refund endpoint for amounts over $500. |
| **Monitoring and alerting** | Real-time detection of boundary violations | If refund amount exceeds $500, alert and block. |
| **Human approval gates** | Required human approval for boundary-pushing actions | Any refund over $500 routed to human manager. |

**PM principle:** Assume the prompt-level boundary will be bypassed (via prompt injection, model error, or edge case). The infrastructure-level boundary must be the real boundary, not the last line of defense.

### The "Action Budget" Concept

Agents should have explicit action budgets that prevent runaway behavior:

| Budget Type | Description | Example |
|------------|-------------|---------|
| **Step budget** | Maximum number of sequential actions per task | Max 10 steps per user request |
| **Cost budget** | Maximum inference cost per task | Max $0.50 per user request |
| **Time budget** | Maximum wall-clock time per task | Max 60 seconds before timeout |
| **Action budget** | Maximum number of state-changing actions per task | Max 3 write operations per user request |
| **Retry budget** | Maximum number of retries for failed actions | Max 2 retries per action |
| **User budget** | Maximum agent actions per user per time period | Max 50 agent invocations per user per day |

Exceeding any budget should trigger graceful termination with user communication, not silent failure or infinite loop.

---

## Part 3: Multi-Agent Coordination

### When Multi-Agent Makes Sense

Multi-agent systems add massive complexity. They should only be considered when:

1. **Task requires diverse expertise:** No single agent/prompt can competently handle all aspects (e.g., a system that needs both legal analysis AND financial modeling).

2. **Parallel execution creates value:** The task can be decomposed into independent subtasks that produce value when executed concurrently.

3. **Separation of concerns reduces risk:** Different agents with different permission levels can isolate risky operations from routine ones.

4. **Independent evaluation improves quality:** A separate "critic" agent can evaluate output quality before it reaches the user.

**Anti-patterns that DO NOT justify multi-agent:**

- "It sounds cool" — No.
- "The demo was impressive" — So was the single-agent demo. Build the simpler thing first.
- "We might need it later" — Build the simpler thing first, then extend if needed.
- "The research papers show great results" — Research papers use idealized conditions and don't pay AWS bills.

### Multi-Agent Coordination Patterns

#### Pattern 1: Supervisor-Worker

```
           ┌─────────────┐
           │  SUPERVISOR │  (Plans, decomposes tasks, assigns to workers,
           └──────┬──────┘   aggregates results, makes final decisions)
                  │
        ┌─────────┼─────────┐
        │         │         │
   ┌────▼────┐ ┌──▼───┐ ┌───▼─────┐
   │ WORKER  │ │WORKER│ │ WORKER  │  (Specialized agents for specific subtasks)
   │   A     │ │  B   │ │   C     │
   └─────────┘ └──────┘ └─────────┘
```

**When to use:** Tasks that can be decomposed into distinct subtasks with different expertise requirements.

**PM considerations:**
- The supervisor is a single point of failure. If its plan is wrong, all workers produce wrong results.
- Supervisor quality depends on how well it understands worker capabilities.
- Cost = N+1 model calls (N workers + 1 supervisor), minimum. Often more with retries and replanning.

#### Pattern 2: Sequential Handoff

```
┌────────┐     ┌────────┐     ┌────────┐
│ AGENT  │────▶│ AGENT  │────▶│ AGENT  │
│   A    │     │   B    │     │   C    │
└────────┘     └────────┘     └────────┘
   Step 1         Step 2         Step 3
```

**When to use:** Tasks with a natural sequential workflow where each step has different requirements.

**PM considerations:**
- Error compounding: if Agent A is 95% accurate and Agent B is 95% accurate, the sequence is 90% accurate (0.95 x 0.95).
- With 5 agents at 95% each, overall accuracy drops to 77%. Multi-agent chains degrade quickly.
- Add verification steps between agents to catch and correct errors.

#### Pattern 3: Critic-Verifier

```
┌────────┐     ┌────────┐
│ AGENT  │────▶│ CRITIC │────▶ User (if approved)
│(worker)│     │(review)│
└────────┘     └────┬───┘
                    │ (if rejected)
                    ▼
               Back to AGENT for revision
```

**When to use:** High-stakes outputs where a second opinion significantly improves quality.

**PM considerations:**
- The critic must be a different model (or at minimum a different prompt/temperature) to provide value. A model agreeing with itself is not quality assurance.
- Critic rejection rate measures how often the worker produces unacceptable output. Track this over time.
- Cost is 2x single-agent cost for every task. Justify this with measured quality improvement.
- Critic can become a bottleneck if it rejects too many outputs (revision loops).

#### Pattern 4: Debate/Consensus

```
┌────────┐     ┌────────┐
│ AGENT  │     │ AGENT  │
│   A    │     │   B    │
└───┬────┘     └───┬────┘
    │              │
    └──────┬───────┘
           │
    ┌──────▼──────┐
    │  ARBITER    │──▶ Final output
    └─────────────┘
```

**When to use:** Tasks where there's no single "correct" answer and diverse perspectives produce better outcomes.

**PM considerations:**
- Agents must be primed with genuinely different perspectives; otherwise they'll converge on the same answer (false consensus).
- The arbiter needs to evaluate arguments, not just count votes. A 2-1 vote where the 1 is correct should lose to the better argument.
- Cost is 3x (or more) single-agent cost. Justify the diversity benefit.
- Most useful for creative, strategic, or analytical tasks; not useful for factual tasks with ground truth.

### The Multi-Agent Complexity Warning

Every multi-agent pattern increases:
- **Cost** (N agents vs 1, minimum)
- **Latency** (sequential patterns add latency; parallel patterns add coordination overhead)
- **Error surface** (N agents, each with their own failure modes, multiplied by interactions between them)
- **Debugging difficulty** (which agent made the error? who was wrong, and who correctly identified the wrong output?)
- **Observability requirements** (must trace decisions across multiple agents, not just one)

**Rule of thumb:** Before introducing a second agent, optimize the first agent's prompts, tools, context, and evaluation to its limit. Most multi-agent benefits can be achieved with better single-agent design at a fraction of the cost and risk.

---

## Part 4: Human-in-the-Loop Patterns

### Where to Insert Human Review

In an agent workflow, humans can be inserted at any of these points:

```
INPUT ──▶ [Pre-processing] ──▶ AGENT ──▶ [Post-processing] ──▶ OUTPUT
            │                    │               │
            │                    │               │
    [Human review of     [Human review of   [Human review of
     the plan before      intermediate        final output
     execution]           results/actions]    before delivery]
```

| Insertion Point | Best For | Trade-off |
|----------------|----------|-----------|
| **Pre-execution (plan review)** | Complex, high-stakes tasks where a bad plan wastes resources or causes harm | Requires domain expertise to evaluate plans; slows initial response |
| **Mid-execution (action approval)** | Actions with irreversible consequences or financial impact | Interrupts flow; requires fast human response time to avoid agent timeout |
| **Post-execution (output review)** | Tasks where cost of error is moderate and review is faster than doing the task | Bad outputs are produced (cost of wasted inference); errors may go undetected |
| **Exception-only (escalation)** | High-volume tasks where most are standard; only flag exceptions for review | Requires accurate exception detection; false negatives (unflagged errors) are dangerous |
| **Sampling (audit)** | On-going quality monitoring; not a safety mechanism | Doesn't protect individual users from bad outputs; detects systemic issues only |

### The Human-in-the-Loop Trade-Off Equation

```
VALUE OF AUTOMATION = (TASK VOLUME × VALUE PER TASK) - (AUTOMATION COST + ERROR COST)

WITH HUMAN REVIEW:
VALUE = (TASK VOLUME × VALUE PER TASK) - (AUTOMATION COST + ERROR COST + HUMAN REVIEW COST)

Where HUMAN REVIEW COST = REVIEW RATE × COST PER REVIEW × (1 - AUTOMATION RATE OF REVIEW TASK)
```

**If the human review cost exceeds the value of automation, you have two choices:**
1. Reduce review rate (only review high-risk cases, use sampling)
2. Accept that this is an augmented workflow (not an automated one) and price it accordingly

**Don't pretend it's automated when it's augmented.** The unit economics and user experience are fundamentally different.

### Designing the Human-Agent Interface

When humans and agents work together, design the interface explicitly:

| Design Element | What to Specify | Example |
|---------------|----------------|---------|
| **What the human sees** | What information does the human reviewer receive? | AI output, confidence score, key evidence used, alternatives considered, what the AI is uncertain about |
| **What the human can do** | What actions can the human take? | Approve, reject, edit, request revision, escalate, override with explanation |
| **What feedback goes back** | How does the human's action inform the agent? | Rejection reason logged; edited output used to improve future responses; override tracked as calibration data |
| **How long the human has** | SLA for human response | "Within 5 minutes" for real-time; "Within 4 hours" for async; "Before end of business day" for batch |
| **What happens if the human doesn't respond** | Timeout behavior | Auto-escalate, return to user with "pending review," auto-approve (dangerous — only for low-risk cases), auto-reject (safe default) |

---

## Part 5: Observability for Agent Systems

### What Observability Means for Agents

Traditional software observability (logs, metrics, traces) is necessary but insufficient for agent systems. Agent observability must answer:

1. **What did the agent decide to do and why?**
2. **What tools did it use, with what inputs and outputs?**
3. **What was the agent's reasoning for each step?**
4. **Where did the agent get stuck or go wrong?**
5. **What was the total cost (latency, tokens, tool calls) of this invocation?**

### The Agent Trace

Every agent invocation should produce a structured trace:

```
TRACE: agent_invocation_2026-08-01_14-32-17_UUID

SUMMARY:
- User intent: "Find the best flight from SFO to JFK on August 15"
- Result: "Delta Flight 1234, $349, departs 8:15am. Booked and confirmed."
- Outcome: SUCCESS
- Total steps: 7
- Total time: 12.3s
- Total cost: $0.047

STEPS:
1. PLAN      — "I need to: (1) search flights, (2) filter by preference, (3) present options, (4) book selected"
   Model: claude-sonnet-20250219 | Tokens: 847 | Cost: $0.003 | Time: 0.8s | Confidence: HIGH

2. TOOL_CALL — search_flights(origin=SFO, destination=JFK, date=2026-08-15)
   Input: {"origin": "SFO", "destination": "JFK", "date": "2026-08-15"}
   Output: {"flights": [...15 results...]}
   Success: true | Time: 1.2s | Provider: Amadeus API

3. REASON    — "I found 15 flights. I need to filter by the user's preferences: non-stop, morning departure, under $500."
   Model: claude-sonnet-20250219 | Tokens: 1204 | Cost: $0.004 | Time: 1.1s

4. TOOL_CALL — filter_flights(flights=[...], preferences={stops: 0, departure: "morning", max_price: 500})
   Input: [filtered results]
   Output: {"matching_flights": [...3 results...]}
   Success: true | Time: 0.3s

5. OUTPUT    — "Here are your options: 1) Delta 1234: $349, 8:15am-4:30pm, non-stop..."
   Model: claude-sonnet-20250219 | Tokens: 567 | Cost: $0.002 | Time: 0.7s | Presented to user

6. USER_CHOICE — User selected option 1 (Delta 1234)

7. TOOL_CALL — book_flight(flight_id=DL1234, passenger_id=P78901, payment_method=PM_***2345)
   Input: {"flight_id": "DL1234", "passenger_id": "P78901", "payment_method": "PM_***2345"}
   Output: {"booking_id": "BK98765", "status": "confirmed", "total": 349.00}
   Success: true | Time: 2.1s | Requires elevated permission: LEVEL_4 (booking)
   Authorization: Auto-approved (within booking budget of $500)

8. OUTPUT    — "Your flight is booked! Booking reference: BK98765..."
   Model: claude-sonnet-20250219 | Tokens: 234 | Cost: $0.001 | Time: 0.3s
```

### Observability Requirements by Authority Level

| Authority Level | Minimum Observability |
|----------------|----------------------|
| Level 0-1 | Log inputs and outputs; basic error logging |
| Level 2 | Full trace of reasoning steps; confidence tracking |
| Level 3 | Full trace + human review decisions logged + override tracking |
| Level 4 | Full trace + all tool call inputs/outputs + permission checks logged + cost tracking per step |
| Level 5 | Full trace + real-time monitoring dashboard + anomaly detection + cost anomaly alerts |
| Level 6 | Full trace + continuous human monitoring + automatic shutdown on anomaly detection |

### The Agent Health Dashboard

Every agent system in production should have a real-time dashboard showing:

| Metric | What It Measures | Alert Threshold |
|--------|-----------------|----------------|
| **Task success rate** | % of agent invocations that complete successfully | < 90% for 1 hour |
| **Human escalation rate** | % of invocations escalated to human | > 30% sustained (review workflow efficiency) |
| **Task abandonment rate** | % of invocations where user abandons before completion | > 20% increase week-over-week |
| **Average steps per task** | How many steps agents take to complete tasks | > 50% increase (may indicate struggling/looping) |
| **Tool failure rate** | % of tool calls that fail | > 5% |
| **Average cost per task** | Inference + tool costs per completed task | > 50% over budget |
| **p95 latency** | 95th percentile time to task completion | > 2x target |
| **Loop/cycle detection** | Instances where agent repeats the same action | Any sustained looping (more than 3 repetitions of the same action pattern) |
| **Permission elevation rate** | % of tasks requiring elevated permissions | Unexpected increase (may indicate scope creep or attack) |
| **Critic rejection rate** (if using critic pattern) | % of outputs rejected by critic | > 30% increase (may indicate worker model degradation) |

---

## Part 6: Rollback and Recovery

### Agent-Specific Recovery Challenges

Agents create recovery challenges that simpler AI patterns don't:

1. **Partial state changes:** An agent performs Steps A, B, and C, then fails at Step D. Steps A-C have changed system state. Rolling back means undoing A-C, not just D.

2. **External side effects:** The agent sent an email (Step A), created a database record (Step B), and tried to charge a credit card (Step C) before failing. Undoing Steps A-B is possible; the failed charge needs investigation.

3. **Distributed state:** In multi-agent systems, Agent 1's actions affect Agent 2's state. Rolling back Agent 1 requires understanding how Agent 2 used Agent 1's outputs.

4. **Non-reversible actions:** Some agent actions cannot be rolled back (sent emails, published content, external API calls to systems without undo).

### Recovery Architecture

#### Pattern 1: Compensating Transactions

For every agent action that changes state, define an explicit compensating action:

| Action | Compensating Action | Limitation |
|--------|-------------------|------------|
| Create database record | Delete record (or mark as void) | Other processes may have read the record |
| Send email | Send correction email | Original email was already read |
| Charge credit card | Issue refund | Processing fees may not be refundable |
| Publish content | Unpublish | Content may have been seen/cached/shared |
| Update user setting | Revert to previous value | User may have changed it independently |
| Send API call to third party | Call third party's undo endpoint | Third party may not support undo |

#### Pattern 2: Staged Execution

Don't let agents commit state changes until all preconditions are met:

```
Phase 1: PLAN        — Agent creates a plan. No state changes.
Phase 2: DRY RUN     — Agent simulates execution. Validates feasibility. No state changes.
Phase 3: PREPARE     — Agent prepares state changes (creates draft records, queues messages). Changes are "staged" not "committed."
Phase 4: VERIFY      — Agent or human verifies staged changes are correct.
Phase 5: COMMIT      — Staged changes are committed atomically.
Phase 6: VERIFY      — Post-commit verification that changes took effect correctly.
```

**When to use:** High-stakes actions where rolling back is impossible or expensive. Financial transactions, content publication, customer communications.

**When NOT to use:** Real-time interactions where users need immediate results and delayed commitment frustrates them.

#### Pattern 3: Checkpoint and Restore

Save agent state at key decision points so you can restore to the last known-good state:

```
Step 1: CHECKPOINT — Save agent state (plan, context, tool outputs so far)
Step 2: Action A — State change
Step 3: CHECKPOINT — Save state after Action A
Step 4: Action B — State change (FAILS)
Step 5: RESTORE to checkpoint at Step 3 — Undo Action B
Step 6: Try alternative Action B' — or escalate to human
```

**When to use:** Complex agent workflows with high decision-tree branching where some paths may lead to dead ends.

#### Pattern 4: Immutable Log + Event Sourcing

Instead of modifying state directly, agent actions produce events. State is derived from the event log:

```
Agent creates event: "FLIGHT_BOOKED(booking_id=BK98765, flight=DL1234, passenger=P78901, amount=$349)"
                       │
                       ▼
Event log: [..., FLIGHT_BOOKED(BK98765, ...)]
                       │
                       ▼
Current state derived from event log: Booking BK98765 exists, status = CONFIRMED

Agent needs to roll back: creates event: "BOOKING_CANCELED(booking_id=BK98765, reason=AGENT_ERROR)"
                       │
                       ▼
Event log: [..., FLIGHT_BOOKED(BK98765, ...), BOOKING_CANCELED(BK98765, ...)]
                       │
                       ▼
Current state derived from event log: Booking BK98765 exists, status = CANCELED
```

**Advantage:** Full audit trail. Any state can be reconstructed. Rollback is just another event.

**Disadvantage:** More complex to implement. Requires event sourcing infrastructure.

### Recovery Communication

When an agent system fails and requires recovery, users must be informed:

| Failure Type | User Communication | Timing |
|-------------|-------------------|--------|
| Agent unable to complete task | "I wasn't able to complete this. A team member will follow up within [timeframe]." | Immediately |
| Partial completion with compensating action | "I've started processing your request but hit an issue. I've undone the changes and saved your progress. Would you like me to try again or have a team member help?" | Immediately |
| Agent produced incorrect output that was delivered to user | "I wanted to let you know that a previous response about [topic] may have been incorrect. The correct information is: [correction]. I've updated our systems to prevent this in the future." | As soon as error is detected |
| Agent took an action that cannot be undone | "I took an action on your behalf [describe action]. If this wasn't what you wanted, here's how to correct it: [instructions]. I'm sorry for the inconvenience." | Immediately |

**Principle:** Honesty > saving face. Users forgive honest mistakes; they don't forgive coverups or silence.

---

## Part 7: The Agent Decision Template

When proposing an agent feature, complete this template:

```
# Agent Feature Proposal: [Feature Name]

## 1. Task Description
What task will the agent perform? Describe in user terms, not AI terms.

## 2. Agent Value Test
[ ] Multi-step task required?
[ ] Steps depend on intermediate results?
[ ] Environment is dynamic?
[ ] Requires external actions?
[ ] Agentic flexibility > deterministic workflow cost/benefit?

## 3. Why Not a Simpler Approach?
Why can't this be done with a single model call, a deterministic workflow, or a template-based router?

## 4. Authority Level
Proposed level (0-6): ___
Justification: ___

## 5. Safety Boundaries
- Step budget: ___
- Cost budget: ___
- Time budget: ___
- Action budget: ___
- Specific actions the agent CANNOT take: ___

## 6. Human Oversight
- Human insertion point: [pre-execution / mid-execution / post-execution / exception-only / sampling]
- Escalation triggers: ___
- Escalation SLA: ___

## 7. Observability
- Tracing level: [basic / full trace / full trace + real-time dashboard]
- Key metrics: ___

## 8. Recovery
- Compensating actions defined for: ___
- Recovery SLA: ___
- User communication plan: ___

## 9. Cost Estimate
- Expected cost per task: $___.___
- Expected daily volume: ___
- Expected daily cost: $___.___

## 10. Risk Assessment
- Top 3 failure modes (from FAILURE_MODES.md): ___
- Mitigation for each: ___
- Rollback trigger: ___

## 11. Decision
[ ] PROCEED — Agent architecture justified and risks acceptable
[ ] SIMPLIFY — Reduce to simpler pattern first
[ ] INVESTIGATE — Build evaluation harness before committing
[ ] REJECT — Risk/benefit not justified
```

---

## Practical Application

1. Identify a product workflow where an agent architecture is being considered. Run it through the Agent Value Test. Does it pass all five questions?

2. If you're using multi-agent coordination, justify each additional agent. What would happen if you collapsed the system to fewer agents?

3. Design the human-agent interface for your product. What does the human see? What can they do? What's the SLA? What's the timeout behavior?

4. Identify the top 3 agent actions in your product that cannot be easily rolled back. Define compensating actions for each.

5. Build a simple agent trace for your most important agent workflow. What would you learn from having this trace on every invocation?

---

## Discussion Prompts

1. Has your organization built an "agent" that could have been a simpler system? What drove the decision to use agent architecture?

2. At what authority level do your agents currently operate? Is this appropriate for your governance risk tier?

3. What's the longest chain of dependent AI calls in your system? What's the compound error rate at that chain length?

4. If your agent system produced a severely wrong output right now, how would you know? How long would it take? What would you do?

5. Do you have an agent trace that would let you reconstruct exactly what happened in the last 24 hours? If a user disputed an agent action, could you show them the full decision trail?
