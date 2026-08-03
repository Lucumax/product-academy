# Condition D — Competitor Method: Availability

Status: **MARKED UNAVAILABLE for the first round.**

## Why

Condition D requires a fair, comparable competing skill or framework for each scenario. Two
candidate packs were identified in the positioning decision:

| Pack | License (GitHub API, 2026-08-02) | Verdict |
|---|---|---|
| `deanpeters/Product-Manager-Skills` | `NOASSERTION` (no license declared) | **Unusable.** No license = no permission to reproduce or adapt into an eval fixture. |
| `RefoundAI/lenny-skills` | MIT | MIT permits use, but building a fair condition requires either importing their skill text into this repo (a scope/legal decision) or an external harness, and their 86-skill coverage is not a 1:1 scenario map. |

## Decision

Rather than construct a strawman (a weak imitation we could trivially beat) or copy
non-permitted material, the first round runs conditions **A, B, C only**, and condition D is
recorded as `UNAVAILABLE` per scenario in the results. This is the honest outcome the
instructions permit:

> "If a fair competitor condition cannot be created, mark it unavailable rather than
> constructing a strawman."

## What would unblock D

- A clear license (or explicit permission) for a competitor pack, AND
- A decision by Walter that importing/adapting it for evaluation is in scope, OR
- A reviewer who brings their own preferred competing method and runs it themselves under the
  same scenario + blinding rules (BYO-method). That last option is the lowest-friction path
  and is recommended for round one.

If a reviewer runs a BYO competitor method, they record which method they used in the form's
"Anything else worth flagging" field, and the output is labeled per the randomization schema
so scoring stays blind.
