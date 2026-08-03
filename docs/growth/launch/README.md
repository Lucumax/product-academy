# Launch Sequence — Bounded Four-Channel Plan

Status: **PREPARED — NOTHING POSTED, NO OUTREACH SENT.** Every post requires Walter's
approval of the exact text, community, and recipient list first. Every post leads with a
demonstration or a learning, never "please star my repo."

Live state this plan builds on (verified 2026-08-02, branch `skills-launch-validation-v1`):

- Live commit: `9c84756`; release `skills-v0.3.0`; 14 skills; site at `/skills/`.
- The discovery-contradiction demo is the launch centerpiece (Phase 4).
- Blinded external evaluation package exists but has no results yet (Phase 3). **Launch
  posts must not claim independent validation until reviewer forms are scored.**

## Launch sequence

| Step | Channel | Lead asset | Gate before posting |
|---|---|---|---|
| 1 | Channel 2 — Direct PM outreach (15–20 candidates) | The blinded eval ask (3 examples, ~40 min) | Walter approves the verified list + exact message |
| 2 | Channel 1 — LinkedIn | Primary post leads with Demo 1 (discovery contradiction) | Walter approves text + image |
| 3 | Channel 3 — One PM community | Question-first post (interviews vs usage) | Walter approves the exact community + message |
| 4 | Channel 4 — One AI-agent community | Experiment-design demo (precommitted interpretation, stop rules, rollback) | Walter approves the exact community + message |

Sequencing logic: outreach and community posts generate the *qualified* interest the funnel
needs; LinkedIn is the public anchor. Run outreach before/with LinkedIn so early reviewers
exist to sanity-check claims. Communities come after the GitHub storefront and demos are
confirmed live.

## Channel assets

- `channel-1-linkedin.md` — primary post, shorter alternate, technical follow-up,
  first-comment text, suggested image, four response templates.
- `channel-2-outreach.md` — selection criteria, list-building spec (15–20, verified names
  only), outreach template, four response templates.
- `channel-3-pm-community.md` — community-type selection rules, non-spam criteria, post draft.
- `channel-4-ai-agent-community.md` — post draft focused on skill design and agent
  reliability.

## Content rules (applies to all channels)

1. Lead with a problem or a demonstration. The discovery-contradiction and experiment-design
   demos are the two lead assets.
2. Explain the failure of generic AI output before showing the skill.
3. Provide the install command once per post, at the end.
4. Link to `/skills/` (after merge, the live site is the destination).
5. Invite critical use: "tell me where it fails" — never "please star."
6. Do not claim: independent validation (no reviewer results yet), adoption numbers, search
   rankings, benchmarks, or endorsements.
7. Do not fabricate traction, testimonials, users, or community interest.

## Explicit exclusions (first wave)

Do **not** launch to Product Hunt or Hacker News until all of:

- [ ] At least five external users have installed successfully.
- [ ] At least three external PM evaluations exist (scored, not just agreed).
- [ ] No critical installation failures remain.
- [ ] One public demonstration has received meaningful engagement.

Reason: PH/HN convert unproven, unmeasured claims into a one-day spike of stars that the
measurement plan explicitly warns against ("stars without installs = attractive positioning,
unproven value"). The four-channel launch above is designed to produce the evidence that
would justify PH/HN later — not to skip the evidence.

## Definition of the launch's success condition

Not "more stars." The launch succeeds when the funnel produces *informative* next-stage
signals:

- 3+ external PM evaluations returned (any verdict).
- 3+ installation attempts (success or failure — failures are data).
- 1+ issue or contribution, OR 1+ substantive critical discussion.
- The measurement snapshot after 14–30 days is reported against the baseline
  (`docs/growth/metrics/BASELINE_AFTER_V0.3.0.md`).
