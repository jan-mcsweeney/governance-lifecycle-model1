#!/usr/bin/env python3
"""Conformance check for the Model 1 example suite.

Two things are checked, and the second is the point:

  1. Every example input and expected output conforms to its schema
     (required fields present, enum values legal, no stray keys).
  2. Every expected tier can be re-derived from the five scores by the
     published tier rules. If a tier in the suite cannot be reproduced
     from the rules, either the rules or the example is wrong — and that
     is exactly the defect a worked example is supposed to expose.

No third-party dependencies. Run from the repository root:

    python3 scripts/check_examples.py
"""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "schema"
EXAMPLES = ROOT / "examples"

# Ordinal scale. Compound values resolve DOWN to their lower anchor for
# tier derivation: a straddling score never promotes an issue on its own.
SCALE = {
    "Low": 1,
    "Low–Moderate": 1,
    "Moderate": 2,
    "Moderate–High": 2,
    "High": 3,
}

DIMENSIONS = [
    "evidence_strength",
    "chronology_clarity",
    "governance_relevance",
    "operational_impact",
    "actionability",
]

TIER_0 = "Tier 0 — no issue"
TIER_1 = "Tier 1 — priority"
TIER_2 = "Tier 2 — contextual / supporting"
TIER_3 = "Tier 3 — monitor"


def derive_tier(scores, authorising_instrument=None):
    """Reference implementation of the published tier rules.

    Order matters: the authorised-absence test runs first, so a properly
    accounted-for observation can never be escalated by strong scores.
    """
    if authorising_instrument:
        return TIER_0

    rank = {d: SCALE[scores[d]] for d in DIMENSIONS}

    # Tier 3 — the evidentiary floor. Too thin to act on, so hold and revisit.
    if rank["evidence_strength"] < 2 or rank["chronology_clarity"] < 2:
        if rank["governance_relevance"] < 3:
            return TIER_3

    # Tier 1 — relevance high AND a lever exists. Evidence alone never suffices.
    if rank["governance_relevance"] == 3 and rank["actionability"] >= 2:
        return TIER_1

    # Tier 2 — relevant and evidenced, but nothing to pull.
    if rank["governance_relevance"] >= 2:
        return TIER_2

    return TIER_3


def load_schema(name):
    return json.loads((SCHEMA / name).read_text(encoding="utf-8"))


def check_object(obj, schema, label, errors):
    """Minimal structural check: required keys, unknown keys, enum membership."""
    props = schema.get("properties", {})
    defs = schema.get("$defs", {})

    for key in schema.get("required", []):
        if key not in obj:
            errors.append(f"{label}: missing required field '{key}'")

    if schema.get("additionalProperties") is False:
        for key in obj:
            if key not in props:
                errors.append(f"{label}: unexpected field '{key}'")

    for key, value in obj.items():
        spec = props.get(key)
        if spec is None:
            continue
        ref = spec.get("$ref")
        if ref and ref.startswith("#/$defs/"):
            spec = defs[ref.split("/")[-1]]
        allowed = spec.get("enum")
        if allowed and value not in allowed:
            errors.append(f"{label}: '{key}' = {value!r} is not a permitted value")
        minlen = spec.get("minLength")
        if minlen and isinstance(value, str) and len(value) < minlen:
            errors.append(f"{label}: '{key}' shorter than {minlen} characters")


def main():
    in_schema = load_schema("issue-input.schema.json")
    out_schema = load_schema("assessment-output.schema.json")

    inputs = sorted(EXAMPLES.glob("*.input.json"))
    if not inputs:
        print("no examples found", file=sys.stderr)
        return 1

    errors = []
    for path in inputs:
        stem = path.name[: -len(".input.json")]
        expected_path = EXAMPLES / f"{stem}.expected.json"
        if not expected_path.exists():
            errors.append(f"{stem}: no matching .expected.json")
            continue

        issue = json.loads(path.read_text(encoding="utf-8"))
        expected = json.loads(expected_path.read_text(encoding="utf-8"))

        check_object(issue, in_schema, f"{stem} (input)", errors)
        check_object(expected, out_schema, f"{stem} (expected)", errors)

        if any(d not in expected for d in DIMENSIONS):
            continue

        derived = derive_tier(expected, issue.get("authorising_instrument"))
        if derived != expected.get("priority_tier"):
            errors.append(
                f"{stem}: tier rules derive {derived!r} but the suite records "
                f"{expected.get('priority_tier')!r}"
            )
        else:
            print(f"  ok  {stem:38s} → {derived}")

    print()
    if errors:
        print(f"{len(errors)} problem(s):")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"{len(inputs)} examples conform; all tiers re-derived from the rules.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
