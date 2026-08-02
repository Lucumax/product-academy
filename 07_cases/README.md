# 07 — Cases

## Purpose

Cases are the bridge between doctrine and practice. Principles tell you what to believe; frameworks tell you how to think; cases tell you what actually happened, under what conditions, and why. The case catalog is designed to develop pattern recognition for product leadership decisions — not to provide recipes, but to expose the texture of real decisions: the information gaps, the pressure, the rejected alternatives, and the uncertain causality.

## Case Selection Criteria

Cases are selected and structured against four criteria:

1. **Decision richness.** The case must involve a genuine product leadership decision with alternatives that reasonable people could disagree about.
2. **Evidence quality.** We must be honest about what we know and what we are reconstructing. Cases are labelled with causal confidence and source provenance.
3. **Transferability analysis.** Every case includes what does NOT transfer — the conditions, industry factors, or context that limit generalization.
4. **Leadership level specificity.** Cases are tagged with the decision level so that a Senior PM does not waste time studying CPO-level decisions (and vice versa).

## Case Types

| Type | Description |
|------|-------------|
| `success` | Decision led to a clearly positive outcome |
| `failure` | Decision led to a clearly negative outcome |
| `reversal` | Organization reversed a prior decision (pivot, strategy change) |
| `sunset` | Decision to discontinue a product or feature |
| `platform_migration` | Decision to migrate between platforms or architectures |
| `ambiguous` | Outcome is contested or genuinely unclear |
| `regulated_decision` | Decision made under regulatory constraints |

## Causal Confidence Labels

| Label | Meaning |
|-------|---------|
| `high` | Strong evidence that the decision caused the outcome; multiple contemporaneous sources; counterfactual analysis available |
| `medium` | Reasonable evidence linking decision to outcome; some sources; plausible counterfactual |
| `low` | Limited evidence; outcome could plausibly be attributed to external factors |
| `correlation_only` | Decision and outcome are temporally associated; no causal evidence |
| `retrospective_narrative` | Outcome is known and the story has been reconstructed backward; high risk of narrative bias |

## Source Policy for Cases

Cases follow the same source policy as all Academy content (see `SOURCE_POLICY.md`). We do not fabricate case details. When we reconstruct a narrative from secondary sources, we label it. When we are uncertain about what information was available at the time, we say so. When the decision-maker has told their own story (with the incentives that implies), we note that incentive.

## How to Use Cases

1. **Read the situation first.** Before looking at the decision, ask: what would I have done?
2. **Identify what was missing.** The most important field in a case is `information_missing` — what the decision-maker did NOT know. 
3. **Assess causality honestly.** The `causal_confidence` field is your guard against retrospective bias.
4. **Check non-transferability.** Before applying a lesson, verify that your situation matches the conditions where it transferred.
5. **Discuss with others.** Cases contain `discussion_questions` designed for group deliberation.

## Maintenance

- Cases should be reviewed annually for accuracy
- New cases should be added when new primary sources become available
- Case outcomes should be updated if subsequent events change the assessment
- The catalog should maintain the required distribution of case types
