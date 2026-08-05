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

### Notes
- The rubric anchors are published as provisional and may change before v1.0.
  The tier rules and schema contracts are stable.
