# External Comparative Evaluation

Status: **PACKAGE PREPARED. NO RESULTS YET. NO REVIEWERS RECRUITED.** Do not claim any
external validation until forms are returned and scored.

This is the external, blinded, comparative evaluation package. It exists so independent PMs
can fairly compare four ways of answering a product decision — and so we can learn whether the
Product Academy skill pack actually improves output, or whether a strong one-off prompt is
just as good.

The prior internal evaluation (`../EVALUATION_REPORT.md`) is authoring-agent self-scored and
explicitly says so. This package replaces nothing; it is the independent, blinded layer the
internal report lists as an open gap.

## Four conditions

| Condition | What the model receives | Where |
|---|---|---|
| A. Model alone | The scenario + one line | `baseline-prompts/A-model-alone.md` |
| B. Strong one-off prompt | The scenario + a general senior-PM prompt (no Academy material) | `baseline-prompts/B-strong-prompt.md` |
| C. Product Academy skill | The scenario + the relevant `SKILL.md` + `references/` + shared contract | in-repo `skills/<skill>/` |
| D. Competitor method | A relevant competing public skill/framework, where licensing and access permit | — |

**Condition D is optional and honest.** If a fair competitor condition cannot be built for a
scenario (licensing, access, or a strawman risk), mark D unavailable for that scenario. Do not
build a weak competitor just to win. **Round one runs conditions A, B, C only; D is marked
UNAVAILABLE** — see `CONDITION_D_AVAILABILITY.md`. The randomization schema and reviewer form
therefore expose three output labels (Output A/B/C) in round one, so the protocol is
executable as documented with no empty slots.

## Scenario set

16 scenarios in `scenarios/` (X01–X16) covering: bespoke enterprise feature pressure, weak
activation / strong retention, AI demo without an evaluation contract, interview enthusiasm
vs usage behavior, irreversible launch with weak reliability evidence, Sales/Product/Eng
deadlock, marketplace without liquidity, vanity-metric PMF claims, a proxy-metric experiment
with possible harm, a reversible UI change, conflicting qualitative/quantitative evidence,
executive roadmap pressure, a sunset decision, build-vs-buy, an early-stage founder with
sparse evidence, and an irreversible pricing restructure.

The scenarios are rewrites of the internal fixtures where overlap exists; any that leaked the
expected answer were rewritten so the answer is not implied by the question.

All company names, products, and people in the scenarios are fictional.

## How to run a round

1. For each scenario, generate the round-one outputs (one per active condition: A, B, C) using
   the same model and the same temperature. Do not tell the model which condition it is in;
   conditions differ only in the materials it receives. Condition D has no output in round one.
2. Anonymize: label outputs only Output A / Output B / Output C.
3. Use `randomization-schema.json` to assign which condition each output label represents.
   This mapping is kept secret until all scoring is complete. Do not put condition names in
   the files reviewers see. **Reviewers must never be shown `randomization-schema.json`** —
   it exists in-repo so the mapping is precommitted and auditable, but it is for the analysis
   team only until unblinding.
4. Recruit reviewers using `RECRUITMENT_MESSAGE.md` (do not send until Walter approves).
5. Send reviewers: the scenarios they are assigned, the three outputs, `reviewer-rubric.md`,
   and `reviewer-form.md`.
6. Collect forms. After scoring completes, unblind using `randomization-schema.json`.
7. Analyze with `ANALYSIS_PLAN.md` (precommitted — do not change the statistics after seeing
   data) and fill `RESULTS_TEMPLATE.md`.

## Blinding caveat (stated honestly)

Outputs from condition A (one-line instruction) will typically be shorter than outputs from
condition C (full skill contract), so a careful reviewer can guess which is which by length
and format. The blinding is per-condition-identity (reviewers never see condition *names*),
not a perfect stylistic match. Treat reviewer scores as informative despite this known
signal; do not claim the study was double-blinded.

## Files

- `README.md` — this file
- `scenarios/` — 16 fictional scenario files (X01–X16)
- `baseline-prompts/` — the A (model alone) and B (strong prompt) conditions
- `reviewer-rubric.md` — the 10-dimension scoring rubric + preference questions
- `reviewer-form.md` — per-scenario scoring form
- `randomization-schema.json` — seeded condition→output-label mapping (secret until unblind)
- `RESULTS_TEMPLATE.md` — the report shell to complete after results
- `RECRUITMENT_MESSAGE.md` — outreach template (unsent)
- `ANALYSIS_PLAN.md` — precommitted statistics and reversal conditions
- `CONDITION_D_AVAILABILITY.md` — why competitor condition is unavailable for round one

## Ground rules

- No fabricated reviewers, results, or significance claims.
- No claim of superiority until a blind round shows it.
- Reviewer scoring is the only legitimate source of "independent evaluation" claims.
- The blinding is condition-identity blinding: reviewers never see condition names, and the
  scenario/condition pairing is randomized per scenario. Output length/format differences
  may hint at condition identity (see the blinding caveat above); this is a stated limitation,
  not a guarantee of double-blinding.
