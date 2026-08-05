# The Governance Lifecycle

The architecture the scoring engine and the obligation register sit inside.

A closed loop, not a pipeline: assurance and review feed back into governance, so
the framework is a living cycle rather than a sequence with an end. One
checkpoint interrupts it — the admissibility gate, sited at the point where
written governance becomes an operational decision.

---

## Stage sequence

**1. Governance**
The standing frame: policy, principles, roles, and the applicable framework set.

**2. Impact Assessment**
Identify what the decision or system affects — rights, data, safety, operations.

**3. Risk Assessment**
Evaluate likelihood and consequence against defined criteria.

**4. Deliberation**
Reasoned consideration of options against governance criteria.

**5. Decision Support**
A cross-cutting capability rather than a sequential step: evidence, precedent and
analysis serving the whole cycle, and informing the gate.

### ◆ Admissibility Gate

The pre-execution checkpoint. Before an action proceeds:

- Is it authorised?
- Is the context complete?
- Are required conditions met?
- Is exposure within accepted boundaries?
- Has anything material changed?

Output: **GO** / **CONDITIONAL GO** / **NO-GO**.

Deliberation and Decision Support *inform* the gate; the gate *authorises*
movement into operation. That placement is the load-bearing choice in the model,
and the reason is worth stating: it is what makes the lifecycle auditable rather
than merely descriptive. A framework without a gate can describe how a decision
ought to be reached but cannot identify the moment at which it was taken, and so
cannot say what was known when.

**6. Execution / Operational Movement**
The action proceeds — only past a GO or CONDITIONAL GO.

**7. Risk Management**
Ongoing treatment of risks carried into operation.

**8. Controls**
The measures applied.

**9. Evidence**
Records generated that demonstrate the controls operated.

**10. Assurance**
Independent confirmation that controls and objectives are met.

**11. Audit / Review**
Systematic examination against criteria.

**12. Lessons Identified**
What the cycle revealed — gaps, near-misses, improvements.

**13. Continuous Improvement**
Changes fed back. The loop returns to Governance.

---

## Feedback, not a single return path

Assurance (10) and Audit/Review (11) feed back not only to Governance (1) but
directly to Controls (8) and Risk Management (7). Those minor return paths are
what distinguish a living governance system from a waterfall drawn in a circle:
an assurance finding that can only be actioned by revising policy is an assurance
finding that will not be actioned.

---

## Framework of frameworks

Each stage is anchored to the external standards it draws on. The connectedness
between stages and standards — rather than any single stage — is the
contribution.

| Lifecycle stage | Anchoring standards | Legal status |
|---|---|---|
| Impact Assessment | AI impact assessment and DPIA methodologies; ISO/IEC 42005 | Voluntary |
| Risk Assessment / Management | ISO 31000; ISO/IEC 23894; NIST AI RMF | Voluntary |
| Admissibility Gate | Decision-gate and change-advisory logic; organisation-defined criteria | Voluntary |
| Controls | ISO/IEC 27002; Essential Eight; NIST SP 800-53 | Voluntary; Essential Eight mandatory for some Australian Commonwealth entities |
| Assurance | ISO/IEC 42006; IRAP-type assessment; SOC 2-style attestation | Voluntary |
| Audit / Review | ISO 19011; internal audit standards | Voluntary |
| Whole-of-cycle management | ISO/IEC 42001; ISO/IEC 23053 | Voluntary |

### Voluntary standards and harmonised standards are not the same thing

Every standard above is voluntary: conforming to it is evidence of good practice,
not evidence of compliance with any law. That distinction matters under the EU AI
Act, where a separate category exists.

A **harmonised standard** is developed by a European standardisation organisation
under a Commission request, and once published *and* cited in the Official
Journal it confers a rebuttable presumption of conformity with the corresponding
legal requirements. CEN-CENELEC JTC 21 is developing such standards for the AI
Act, targeting Chapter III Section 2 — Articles 9 to 15 for high-risk systems —
and Article 17 on quality management systems.

None is yet available for that purpose. As at August 2026, seven projects are in
train: two in drafting, four at working or committee draft, one at enquiry, one
at formal vote. **None has been published, and none has been cited in the
Official Journal.** Publication and citation are separate steps, and citation is
at the Commission's discretion.

So there is presently no standard that delivers presumption of conformity with
the AI Act. Draft standards indicate the direction of regulatory expectation and
are useful for that; they do not discharge a legal obligation, and a mapping that
did not say so would mislead.

This is the same distinction the obligation register draws with `contingent_on`:
a thing that is not yet what it will become should be recorded as such rather
than anticipated. A future revision of this table will need a third status —
*cited in the OJEU* — and the entries that reach it will change category, not
merely progress.

Status information above is drawn from the independent CEN-CENELEC mapping
maintained by Adam Leon Smith at https://ai-act-standards.com/ (CC BY 4.0),
which is not an official publication of the European institutions or the
European standardisation organisations. Verify current stages at source.

Designations and scope are cited. No standard's text, clauses or control wording
is reproduced anywhere in this repository, and the project carries no affiliation
with, or endorsement by, any standards body. Confirm the current designation and
status of any standard before relying on it.

---

## How the three layers meet

The lifecycle is generic and stays that way. Two layers sit on it:

- The **[obligation register](obligation-register.md)** carries the
  jurisdiction-specific content. Each provision decomposes into gate criteria
  (the gate), controls (stage 8), evidence types (stage 9) and assurance
  activities (stage 10). Obligations are added, amended and retired without the
  lifecycle changing.
- The **[issue-scoring engine](example-suite.md)** handles what the cycle throws
  up. Observations arising anywhere — most often at stages 9 through 11 — are
  scored through one rubric with one output contract, and returned as a tier and
  a next action that re-enter at stage 12.

The gate is where the two meet. An obligation's gate criteria are evaluated
before execution; an issue's actionability is judged by whether a forum exists to
act. Both are asking the same question from different directions: *is there a
point at which someone can decide?*
