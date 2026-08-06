# Governance Lifecycle, Issue-Scoring Engine and Obligation Register

**Model 1** — a reference architecture for connecting governance to operations.

Préface

Ce dépôt est actuellement publié en langue anglaise.
Son ambition est cependant internationale.
Les futures évolutions pourront comprendre progressivement une documentation en français, avant une ouverture à d'autres langues.

Les critères d'évaluation (rubric anchors) sont provisoires. L'observation la plus utile que vous puissiez adresser est la suivante : évaluez vous-même l'un des cinq exemples au regard du tableau des critères, et indiquez où votre jugement aurait différé. Un désaccord motivé vaut mieux qu'un accord.

---

A register of asset inspections. Every record carries the correct inspection
date. Nothing is missing, nothing contradicts, and an auditor asking *are the
records complete* would leave satisfied.

The metadata shows that all of them were created in a single batch, eighteen
months after the inspections, by one author.

Is anything wrong? And if so, which of the things you would normally measure has
actually failed? Not completeness — the records are complete. Not the timeline —
the dates are correct and the sequence is clear. That is the difficulty: this
issue fails on an axis most assessment tools do not have, and it scores *worse*
the clearer its chronology becomes.

This repository is one answer. A governance lifecycle with an explicit
pre-execution checkpoint, an engine that scores observations across five
independent dimensions and derives a priority tier from them, and a register that
decomposes legal duties into the lifecycle stages that must carry them. Worked
examples and conformance checkers are included, so the mechanism can be run
rather than only read.

## Start here

Three ways in, depending on what you came for.

**To see it work — about a minute.** Read
[`examples/B-records-created-after-the-fact.input.json`](examples/B-records-created-after-the-fact.input.json)
and its expected output. That is the case above. Then run
`python3 scripts/check_examples.py`, which re-derives every tier from the
published rules.

**To see it decline to find something.** Read
[`examples/D-authorised-absence.expected.json`](examples/D-authorised-absence.expected.json).
Records are missing; a retention schedule authorises their destruction; the
engine returns Tier 0, no issue. An instrument that cannot return *nothing* is
not a diagnostic instrument, and this is the case that proves it can.

**To see the law layer.** Read
[`register/eu-ai-act-50-2.json`](register/eu-ai-act-50-2.json). One provision of
the EU AI Act, decomposed into what must be true before an action proceeds, what
discharges the duty, what evidences it, and who confirms it. Note its history:
the entry was written while the amending regulation was still a political
agreement, and had to be corrected when it became law.

## What would be most useful from you

Not a pull request. One thing, and it takes about ten minutes:

**Score one of the five examples yourself against the anchor table in
[`docs/example-suite.md`](docs/example-suite.md), and tell me where you would
have judged differently.** The anchors are the softest part of this framework —
they are judgement calls written as a table, and consistency between independent
scorers cannot be tested by one person. A single "I would have called that
Moderate, not High, and here is why" is worth more than any amount of agreement.

Open an issue on this repository, or write to the address on the profile.

---

## The three layers

| Layer | What it holds | Document |
|---|---|---|
| **Lifecycle** | Thirteen stages, an admissibility gate, standards mapping | [`docs/lifecycle.md`](docs/lifecycle.md) |
| **Obligation register** | Legal duties, decomposed into the stages that carry them | [`docs/obligation-register.md`](docs/obligation-register.md) |
| **Scoring engine** | Observations in, tier and next action out | [`docs/example-suite.md`](docs/example-suite.md) |

The lifecycle is generic and stays that way. Jurisdiction lives in the register;
judgement lives in the engine. Each can change without disturbing the others.

```
schema/      Input, output and obligation contracts (JSON Schema)
examples/    Five worked scenarios, input and expected output
register/    Five obligation entries
scripts/     Conformance checkers for both
docs/        The three layers explained
```

## The scoring engine

An observation enters as structured input — the issue, the evidence and the
method by which it was found, the chronology, and what the assessment feeds
into. It leaves scored on five dimensions, with a derived priority tier and a
next action.

| Dimension | Question it answers |
|---|---|
| Evidence Strength | How directly, and how well corroborated? |
| Chronology Clarity | Is the sequence established? |
| Governance Relevance | Does it bear on transparency, assurance, accountability? |
| Operational Impact | What does it do to auditability and assurance posture? |
| Actionability | Is there an owner, a lever and a forum? |

Tiers are **derived** from the scores, not assigned:

- **Tier 0 — no issue.** An authorising instrument accounts for the observation.
- **Tier 1 — priority.** Governance Relevance high *and* Actionability moderate or above.
- **Tier 2 — contextual / supporting.** Relevant and evidenced, but no immediate lever.
- **Tier 3 — monitor.** Evidence or chronology too thin to act on; revisit on trigger.

### The design choice that matters

Actionability is scored **independently**, and strong evidence alone never
reaches Tier 1. An issue that cannot be acted on is not a priority, however well
documented. This is deliberate: it is what stops a triage engine from ranking
grievance above remedy. It also lets the engine return a finding most tools
cannot express — *fully documented, entirely inert* (Example C).

Equally deliberate: the engine can return **no finding at all**. Example D is an
absence of records that a retention schedule authorises, and it scores Tier 0. A
tool that always finds something is not a diagnostic instrument.

## The obligation register

Specific laws do not belong inside a lifecycle — naming them would date the
model to one jurisdiction and one moment. They sit in a register instead, where
each provision decomposes into the stages that must carry it:

| Column | Lifecycle stage |
|---|---|
| Gate criteria | Admissibility Gate — what must be true before the action proceeds |
| Controls | Controls — what discharges the duty |
| Evidence types | Evidence — what shows the control operated |
| Assurance activities | Assurance — who independently confirms it |

This gives the engine something to score beyond discrete observations:
**coverage**. An obligation with a gate criterion but no evidence type is a
finding of the same shape as Example C — documented and inert.

Five entries are included, chosen because each behaves differently. EU AI Act
Article 50(1), 50(2) and 50(4) — one article, three entries, because
sub-provisions bind different parties. Hazardous chemicals storage — a
**standing** duty, conditional on a threshold ordinary trading can cross, with
gate criteria resting on instruments that **expire**. Post-quantum cryptographic
migration — the **anticipatory** case, where the duty crystallises in the future
but the harm begins now.

Entries can declare dependencies on one another, which is where the
framework-of-frameworks claim stops being presentational: Article 50(2) marking
that rests on digital signatures inherits the shelf life of the signing
algorithm, so it is gated by the cryptographic migration entry — a fact neither
entry shows alone.

No statutory or standards text is reproduced anywhere in this repository.
Entries paraphrase and point to source.

## Running the checks

```bash
python3 scripts/check_examples.py     # schema conformance + tier derivation
python3 scripts/check_register.py     # structure + coverage findings
```

No dependencies. The first re-derives each tier from the published rules: if a
tier cannot be reproduced, either the rules or the example is wrong, which is
what a worked example is for. The second reports where an obligation is recorded
but not carried, evidenced or assured — and currently reports three findings,
because two entries honestly declare an unknown.

## Status, and what is provisional

**v0.1.0.** The lifecycle, the tier rules and the schema contracts are stable.

**The rubric anchors are provisional.** The Low / Moderate / High definitions in
[`docs/example-suite.md`](docs/example-suite.md) are judgement calls written as a
table, and they have not been tested for consistency between independent
scorers — which cannot be done alone. They may change before v1.0 — see *What would be most useful from you*, above.

Adding examples? Vary the **failure mode**, not the labels. Two scenarios with
different names but the same underlying shape exercise the same branch of the
rubric twice. The five here fail on five different dimensions: conflict,
retrofit, inertia, authorised absence, unverifiability. Published examples are
fictional and stay that way.

## Licence

| Component | Licence |
|---|---|
| Code — schema, scripts | Apache License 2.0 (`LICENSE`) |
| Documentation — framework, rubric, examples, register | CC BY 4.0 (`LICENSE-DOCS.md`) |

Both require attribution downstream. See `NOTICE`.
