# Changelog

All notable changes to this project are recorded here.
Format follows Keep a Changelog; versioning follows Semantic Versioning.

## [0.1.0] — unreleased

### Added
- `docs/lifecycle.md`: the lifecycle architecture, standards mapping and an
  account of how the three layers meet.
- Governance lifecycle with the admissibility gate sited between decision
  support and execution, and feedback paths from assurance and audit to
  governance, controls and risk management.
- Framework-of-frameworks mapping: each lifecycle stage anchored to the
  external standards it draws on.
- Issue-scoring engine: five scored dimensions, derived priority tier,
  next action.
- JSON Schema for the input and output contracts.
- Worked example suite: five fictional scenarios spanning five failure modes
  and four outcome tiers, including an authorised-absence control case.
- Dependency-free conformance checker that re-derives every tier from the
  published rules.
- Obligation register: a jurisdiction-specific layer decomposing each legal
  provision into gate criteria, controls, evidence types and assurance
  activities, with its own schema and coverage checker.
- Worked register entries for EU AI Act Article 50(1), 50(2) and 50(4).
- Register support for standing duties (`duty_character`, `reentry_triggers`),
  conditional applicability (`applicability`) and expiring instruments behind
  gate criteria (`validity`), with UNMONITORED, LAPSED and UNREFRESHED coverage
  findings.
- Worked register entry for storage of hazardous chemicals above manifest
  quantities, exercising all three.
- Register support for anticipatory obligations (`latent_exposure`) and for
  advisory-status instruments, with UNANTICIPATED and OVERTAKEN findings.
- Worked register entry for post-quantum cryptographic migration and
  harvest-now-decrypt-later exposure, including hardware key custody, hardware
  refresh planning and algorithm-agility procurement as controls.
- Cross-entry dependencies (`depends_on`) with an UNRESOLVED coverage finding,
  and a worked dependency from EU AI Act Article 50(2) marking to the
  cryptographic migration entry.

### Changed
- Article 50 entries cite Regulation (EU) 2024/1689 as amended by Regulation
  (EU) 2026/1744 (Digital Omnibus on AI, in force 27 July 2026). The 50(2)
  transitional period to 2 December 2026 is recorded as enacted rather than
  agreed.
- Added `contingent_on` for duties agreed but not yet law, with a CONTINGENT
  coverage finding.
- Standards mapping now records legal status, and distinguishes voluntary
  standards from harmonised standards under the EU AI Act. As at August 2026 no
  CEN-CENELEC AI Act standard has been published or cited in the Official
  Journal, so none yet confers presumption of conformity.
- Article 50(1) entry: added linguistic accessibility controls — disclosure in
  the languages of the affected audience, and review of translations for
  meaning — with a record of the languages assessed and the basis for that set.
- Noted the distinction between control type and control timing (preventive,
  detective, corrective), and the cross-instrument boundary between the AI Act
  and the GDPR for agentic systems. Both flagged for v0.2.0.  
- Noted that entries record what a provision requires but not how it has been
  interpreted, and that pending cases are a better signal of interpretive
  instability than a review date. An `interpreted_by` field is planned for
  v0.2.0.
- Noted national implementations in the spaces the AI Act leaves to Member
  States (Italy, Legge 132/2025; Spain, Proyecto de Ley Orgánica, pending), and
  that the register records who owes a duty but not who supervises it. A
  `supervised_by` field is planned for v0.2.0.
- Noted what authority a published text carries: the presumption attaching to
  official publication, the distinction between errata corrige and avviso di
  rettifica, and consolidated texts as sources on which the public may
  innocently rely.
- Noted that certification schemes are assurance activities rather than duties,
  using the EU Cloud Services scheme (ENISA candidate scheme, 22 December 2020)
  as the harder case: voluntary in form, capable of binding through NIS2 and
  procurement, with its sovereignty criteria unsettled and no final scheme
  published. Also noted that a control's guarantee has a boundary, which an entry
  should record.
- Placed distributed ledgers as an integrity and custody control on the Evidence
  stage, with the boundary stated: a ledger secures a record's integrity and its
  custody, but not the accuracy of the record at the point of writing.
- Corrected the Article 50(2) entry: the transitional period to 2 December 2026
  sits in Article 111(4) of Regulation (EU) 2024/1689, added by Regulation (EU)
  2026/1744, not in Article 50 itself. Verified against the adopted text.
- Recorded Article 4a of Regulation (EU) 2024/1689, inserted by Regulation (EU)
  2026/1744: a permission to process special categories of personal data for bias
  detection and correction, expressly in addition to data protection law, with six
  cumulative conditions each of which is a control, an evidence type, or both.
- Recorded the Article 5 prohibitions added by Regulation (EU) 2026/1744,
  applying from 2 December 2026, as the worked example of a duty not to do
  something: liability attaches to the absence of adequate safeguards against
  reasonably foreseeable misuse, so compliance is evidenced by the safeguards
  rather than by absence.
- Verified the Italian provisions against the text of Legge 23 settembre 2025, n.
  132: Article 1(2) subordinates the law to Regulation (EU) 2024/1689 in
  interpretation; Article 13 restricts use before requiring disclosure; Article 25
  narrows copyright to works of human intellect while preserving protection for
  works created with AI assistance, and adds a text and data mining provision;
  Article 24 delegates literacy and training to professional orders, with fair
  compensation scaled to responsibility.
- Collected the eight limitations the schema does not express, previously
  recorded separately, into a single section.
- Verified the Spanish provisions against the Proyecto de Ley Orgánica as
  published in the BOCG: the delegado de inteligencia artificial in the state
  public sector; market surveillance allocated by provision and by use rather
  than by sector, with AESIA competent by default until the Consejo de Ministros
  designates otherwise; and a national sanction attached to a procedural step in
  the Regulation, which the schema has no field to record.
- Recorded the Australian Protective Security Policy Framework as an instance of
  an instrument voluntary in form and binding in effect: Release 2026 binds
  non-corporate Commonwealth entities by ministerial direction under the PGPA
  Act, represents better practice for others, and elevates voluntary standards
  by listing them within a mandatory framework.
- Refined the Italian material: Article 1(2) characterised as an express
  conformity clause rather than a subordination, since primacy already governs
  where the Regulation applies; and Article 3(5) added, by which the law produces
  no new obligations relative to the Regulation for AI systems and general-purpose
  AI models.
  
  ### Notes
- The rubric anchors are published as provisional and may change before v1.0.
  The tier rules and schema contracts are stable.
