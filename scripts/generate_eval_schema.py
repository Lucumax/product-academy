#!/usr/bin/env python3
"""
Reproducibly generate the condition->output-label randomization schema.

Round one runs three conditions (A=model alone, B=strong prompt, C=Product Academy skill).
Condition D (competitor method) is UNAVAILABLE in round one (see CONDITION_D_AVAILABILITY.md),
so the schema maps three conditions to three output labels (Output A/B/C) per scenario.

Run:  python scripts/generate_eval_schema.py > skills/evals/external/randomization-schema.json
"""

import json
import random

SEED = 20260802
CONDITIONS = ["A", "B", "C"]
SCENARIOS = ["X%02d" % i for i in range(1, 17)]


def main():
    random.seed(SEED)
    schema = {
        "schema_version": "1.0",
        "conditions": {
            "A": "model alone",
            "B": "strong one-off prompt",
            "C": "product academy skill",
            "D": "unavailable in round one (competitor method) - no output label assigned",
        },
        "seeded": True,
        "seed": SEED,
        "generator": "scripts/generate_eval_schema.py",
        "note": (
            "Output label -> condition. Outputs are the rows (Output A..C) shown to "
            "reviewers; the mapping is randomized per scenario and NOT shown until scoring "
            "is complete. Condition D is not assigned an output label in round one. "
            "Regenerate with the generator script to reproduce exactly."
        ),
        "per_scenario": {},
    }
    for s in SCENARIOS:
        perm = CONDITIONS[:]
        random.shuffle(perm)
        schema["per_scenario"][s] = {f"Output {l}": c for l, c in zip("ABC", perm)}

    print(json.dumps(schema, indent=2))
    # Also emit a CSV mapping for the analysis team (reviewers must never see it).
    lines = ["scenario,Output A,Output B,Output C"]
    for s in SCENARIOS:
        m = schema["per_scenario"][s]
        lines.append(f"{s},{m['Output A']},{m['Output B']},{m['Output C']}")
    print("\n# CSV mapping for the analysis team (do not show reviewers):")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
