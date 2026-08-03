# Channel 3 — One PM Community

Status: **TYPE DEFINED — NO COMMUNITY CHOSEN, NOTHING POSTED.** Do not post unless Walter
approves the exact community and message.

## Community type

One product-management community. Fits:

- A community where working PMs discuss product decisions and methods (senior-PM-heavy
  forum, Slack/Discord, or newsletter comments section).
- A community that tolerates a genuine question-and-method discussion, not pure promotion.
- A community where the audience uses or is curious about AI agents in product work (the
  install is only relevant if the audience already works with agents, or is open to it).

Do NOT choose a community where the post would be off-topic promotion (e.g. a pure
AI-infrastructure community, or a career-advice-only community).

## What makes the post non-spammy

1. It leads with a question, not a product: "When interviews say users want a feature but
   usage data disagrees, which evidence should win?"
2. It offers the skill's method as *one proposed answer*, not the answer.
3. It explicitly asks for criticism and failure modes, including from people who disagree.
4. It does not ask for stars, installs, or shares.
5. The product link is at the end as context, after the discussion value.
6. It discloses the author's role (maintainer of the skill pack) up front.

## Post draft

> When interviews say users want a feature but usage data disagrees, which evidence should win?
>
> A concrete case (fictional): a fitness app interviewed 25 active users about a "habit
> streaks" feature. 22 positive. Usage: 6% of DAU touches it. Sessions flat.
>
> Interviews say invest. Usage says almost nobody uses it.
>
> The usual failure is picking a side — "listen to your users" vs "trust the data" — and
> arguing forever. The better framing is that they're different evidence types: stated intent
> (what people think they want) vs behavior (what they do). For a claim about *why people come
> back*, behavior carries more weight, and the loudest interview voices are usually the most
> engaged cohort already using the product.
>
> So the honest answer isn't "invest" and isn't "ignore" — it's "we can't tell yet," plus the
> cheapest test that discriminates: compare retention for streak-users vs non-streak-users.
> If streaks cause retention, the cohort split shows it. If they merely accompany the
> already-engaged, it shows that too.
>
> That's one method (I maintain a small open-source skill pack that formalizes this — link at
> the end, happy to discuss rather than promote).
>
> What I want from you:
> - When should stated enthusiasm win over behavior?
> - What confounders is the cohort split missing?
> - What would you do differently with these 25 interviews and a 6% usage number?
>
> Context: [link to demo 1]. Install (if you want to try): `npx skills add
> Lucumax/product-academy`. No star-ask — I want the failure modes.
