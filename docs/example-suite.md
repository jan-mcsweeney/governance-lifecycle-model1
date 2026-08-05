# Model 1 — Issue-Scoring Engine: Reference Example Suite

Replacement for Part 3. Five fictional scenarios spanning distinct governance failure
modes and distinct outcome tiers. No organisation, framework, jurisdiction or matter
in this suite is real.

---

## 1. Input schema

```json
{
  "issue":         "string  — the observation, stated neutrally",
  "evidence":      "string  — what was found, and how",
  "chronology":    "string  — the sequence, with periods identified",
  "intended_use":  "string  — what the assessment feeds into",
  "authorising_instrument": "string|null — instrument that authorises the
                             state observed, e.g. a retention schedule.
                             Present and verified ⇒ Tier 0."
}
```

`evidence` should record the *method of discovery* as well as the finding. An absence
established by internal audit sampling and an absence established by a records request
are not the same evidentiary object, and the engine should not score them alike.

## 2. Scoring dimensions and anchors

> **Provisional.** These anchors are judgement calls written as a table. They
> have not been tested for consistency between independent scorers, which cannot
> be done by one person. They may change before v1.0, and disagreement about
> where a boundary falls is the most useful feedback this project can receive.

Each dimension returns Low / Moderate / High. Compound values (Moderate–High)
are permitted where the rubric genuinely straddles.

| Dimension | Low | Moderate | High |
|---|---|---|---|
| **Evidence Strength** | Inference from secondary material | Direct but partial or single-source | Direct, corroborated, method documented |
| **Chronology Clarity** | Periods unclear or contested | Sequence known, some gaps | Dated sequence established end to end |
| **Governance Relevance** | Peripheral to accountability | Bears on one control objective | Goes to transparency, assurance or accountability directly |
| **Operational Impact** | No effect on assurance posture | Affects confidence in one domain | Affects auditability or assurance maturity broadly |
| **Actionability** | No owner, no lever, no forum | Reviewable, remedy unclear | Clear owner, clear next step, defined forum |

## 3. Tier rules

- **Tier 0 — No issue.** The observation is accounted for by an authorised process.
- **Tier 1 — Priority.** Governance Relevance High *and* Actionability Moderate or above.
- **Tier 2 — Contextual / supporting.** Relevant and evidenced, but no immediate lever.
- **Tier 3 — Monitor.** Evidence or chronology too thin to act on; revisit on trigger.

Note the asymmetry: strong evidence alone never produces Tier 1. An issue that cannot
be acted on is not a priority, however well documented. This is deliberate — it keeps
the engine from ranking grievance above remedy.

---

## Example A — Records in conflict

**Domain:** municipal waste collection contract

```json
{
  "issue": "Contractor service logs and council fleet telemetry record different
            collection dates for the same 14 rounds in the Autumn period.",
  "evidence": "Both record sets held and compared; discrepancy confirmed on
               sampling of 14 of 60 rounds.",
  "chronology": "Autumn collection period; discrepancy identified at
                 quarterly reconciliation.",
  "intended_use": "contract assurance review"
}
```

```json
{
  "evidence_strength":   "High",
  "chronology_clarity":  "Low",
  "governance_relevance":"High",
  "operational_impact":  "High",
  "actionability":       "High",
  "priority_tier":       "Tier 1 — priority",
  "next_action":         "Reconcile both record sets against payment records;
                          refer to contract manager."
}
```

*Demonstrates:* evidence and chronology are independent axes. Having the records does
not mean having the sequence.

---

## Example B — Records created after the fact

**Domain:** commercial building refurbishment, defect inspection records

```json
{
  "issue": "Defect inspection records for the prior refurbishment stage carry
            correct inspection dates but were all created in a single batch
            eighteen months later, by one author.",
  "evidence": "Register metadata: creation timestamps, author field, batch ID.",
  "chronology": "Inspection cycle Year 1; record creation Year 2, second half;
                 identified at Year 3 audit.",
  "intended_use": "assurance review / audit finding"
}
```

```json
{
  "evidence_strength":   "High",
  "chronology_clarity":  "High",
  "governance_relevance":"High",
  "operational_impact":  "High",
  "actionability":       "Moderate",
  "priority_tier":       "Tier 1 — priority",
  "next_action":         "Confirm whether a documented reconstruction process
                          authorised the batch entry; if not, raise as an
                          evidence-integrity finding."
}
```

*Demonstrates:* clarity of chronology can be the adverse finding rather than the
mitigating one. The engine must not treat a clean timeline as reassurance.

---

## Example C — Documented and inert

**Domain:** professional association standards committee

```json
{
  "issue": "An approved policy on automated analysis tools is complete and
            correctly minuted, but no accountable owner was recorded and no
            review has occurred across three scheduled cycles.",
  "evidence": "Policy register, committee minutes, review calendar — all complete
               and consistent.",
  "chronology": "Adoption Year 1; scheduled reviews Years 2, 3, 4 — none held.",
  "intended_use": "governance maturity assessment"
}
```

```json
{
  "evidence_strength":   "High",
  "chronology_clarity":  "High",
  "governance_relevance":"High",
  "operational_impact":  "Moderate",
  "actionability":       "Low",
  "priority_tier":       "Tier 2 — contextual / supporting",
  "next_action":         "Carry to maturity assessment; propose owner assignment
                          at next committee cycle."
}
```

*Demonstrates:* the finding most triage tools cannot express — fully documented,
entirely inert. Note it does **not** reach Tier 1, because there is no lever.

---

## Example D — Authorised absence *(control case)*

**Domain:** regional museum collection condition-report register

```json
{
  "issue": "No condition reports are held for the earliest three years of
            operation.",
  "evidence": "Internal audit sampling; retention schedule and signed disposal
               certificate located.",
  "chronology": "Operating years 1–3; disposal authorised and executed year 10.",
  "intended_use": "records governance review"
}
```

```json
{
  "evidence_strength":   "Moderate",
  "chronology_clarity":  "High",
  "governance_relevance":"Low",
  "operational_impact":  "Low",
  "actionability":       "Low",
  "priority_tier":       "Tier 0 — no issue",
  "next_action":         "Close. Absence accounted for by authorised disposal;
                          record the disposal certificate reference."
}
```

*Demonstrates:* the engine distinguishes a gap from a breach. This is the example
that establishes the tool is diagnostic rather than accusatory, and it is the one
to keep first in any demonstration.

---

## Example E — Unverifiable assertion

**Domain:** freight and logistics operator, driver fatigue training

```json
{
  "issue": "Annual fatigue-management training completion is reported at 100 per cent, but the
            only supporting record is a summary spreadsheet with no underlying
            attendance or assessment data.",
  "evidence": "Summary spreadsheet held; underlying source data not located
               and no system of record identified.",
  "chronology": "Reporting period Year 1; summary compiled at period end;
                 source system unidentified.",
  "intended_use": "assurance review"
}
```

```json
{
  "evidence_strength":   "Low–Moderate",
  "chronology_clarity":  "Moderate",
  "governance_relevance":"Moderate",
  "operational_impact":  "Moderate",
  "actionability":       "Moderate",
  "priority_tier":       "Tier 3 — monitor",
  "next_action":         "Request identification of the system of record;
                          re-score on response."
}
```

*Demonstrates:* the engine can hold an issue open without escalating it. Absence of
verification is not proof of failure.

---

## Why five and not one

A triage engine demonstrated on a single scenario reads as a case with a user
interface attached. Demonstrated across five scenarios that score differently and
land in four different tiers, it reads as a method. The control case (D) does more
for credibility than the other four combined: it is the only one that shows the
engine returning *no finding*.

Design constraint for any future examples: vary the **failure mode**, not just the
labels. Two scenarios with different names but the same underlying shape —
claim made publicly, implementation records absent, gap inferred — are one example
wearing two coats, and a reader will see it.
