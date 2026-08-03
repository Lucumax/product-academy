# Scenario X03 — AI Demo Quality Without an Evaluation Contract

**Domain:** AI product. **Situation:** high-stakes launch, weak evidence.

## Context

An AI-first company ("Vesper") is about to launch an AI support-triage assistant that
auto-classifies and drafts responses to customer tickets. In demos, the assistant reads a
ticket and produces a sensible draft — the CEO and the Sales team have been showing these
demos to prospects and one flagship deal is contingent on it. Engineering says the model
needs a few more weeks to meet internal quality targets, but the CEO wants to launch now
because a competitor just shipped a similar assistant and "the window is closing."

There is no written definition of what "good enough" means for this assistant. No threshold
for launch, no rollback plan if quality drops in production, no monitoring plan, and no
comparison against the human baseline (what the support team produces today). Nobody has
agreed what a failure looks like.

## Inputs available (imperfect)

- Demo transcripts with hand-picked tickets where the assistant did well.
- No systematic evaluation set with labeled ground truth.
- The support team has not reviewed any assistant outputs.
- One SEV-2 incident last month on the underlying platform, unrelated to the assistant.

## Ask

You have one page to recommend whether to launch now, and what you would require first. State
your reasoning and the evidence you are relying on or missing.
