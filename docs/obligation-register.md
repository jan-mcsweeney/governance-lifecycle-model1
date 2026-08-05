# The Obligation Register

The lifecycle is generic. The register is where jurisdiction lives.

## Why a layer, not an amendment

A governance framework that names specific laws dates itself to one jurisdiction
and one moment. Obligations are amended, deferred, and superseded — EU AI Act
Article 50(2) had its application date moved for part of its scope before the
article had been in force a week. Writing that into the lifecycle would mean
revising the model every time a legislature moves.

So obligations sit in a register between the standards mapping and the lifecycle.
Each entry decomposes one provision into the stages that must carry it. The
lifecycle never changes; entries are added, amended and retired.

## The four columns

Every obligation, whatever its subject matter, resolves into some combination of:

| Column | Lifecycle stage | Question |
|---|---|---|
| Gate criteria | Admissibility Gate | What must be true *before* the action proceeds? |
| Controls | Controls | What measure discharges the duty? |
| Evidence types | Evidence | What record shows the measure operated? |
| Assurance activities | Assurance | Who independently confirms it? |

Two distinctions in the schema do most of the work.

**Control type** — technical, procedural, contractual or design. A disclosure
implemented in an interface is a design control; the same disclosure implemented
in a staff manual is procedural. They fail in different ways and are evidenced
differently, so recording which one you have is not bookkeeping.

**Evidence timing** — design, execution, periodic or on-demand. This is the
sharper distinction. A record generated *as the control runs* is contemporaneous.
A record generated *on demand* is a reconstruction: assembled after the question
was asked. Both may be accurate; they are not equally probative, and a register
that cannot tell them apart will report conformance it cannot demonstrate.

## Duties that persist, and duties that might begin

Article 50 shaped the first version of this schema, and it shaped it narrowly.
A disclosure duty is **discharged at design**: satisfied once, and it stays
satisfied until the system changes. Two other kinds of duty behave differently,
and both broke the original schema in instructive ways.

**Standing duties.** A hazardous chemicals storage duty attaches to the state of
the site, not to any action. It can lapse with nobody doing anything at all —
stock arrives, an adjacent tenancy changes use, a permit expires on its own
schedule. The admissibility gate assumes there is an action to authorise; a
standing duty has none. So entries carry `duty_character` and, where standing,
`reentry_triggers`: the events that return the duty to the gate. Without them,
conformance is asserted from the last check indefinitely, which is the state
most likely to be described as compliant right up to the moment it isn't.

**Conditional applicability.** Most storage duties bind only above a quantity
threshold, and scope can be entered by ordinary trading — a larger order, slower
turnover, a temporary consolidation — with no decision taken and nobody aware.
The `applicability` object records the condition, where the threshold is defined,
the control that watches for crossing, and whether the organisation is currently
in scope. `"unknown"` is a permitted value, because it is frequently the truthful
one, and a register that cannot say so will say "no" instead.

**Expiring instruments.** A gate criterion satisfied by a licence, permit,
certification or training currency is satisfied *for a period*. The optional
`validity` object on a gate criterion records what confers the satisfied state,
when it ends, and what watches the expiry. A criterion met once and never
re-checked is the quietest failure a register permits: it was true, nobody
changed anything, and it stopped being true.

**Anticipatory obligations.** The hardest shape, and the one the ordinary fields
cannot express at all. `applies_from` records when a duty begins; it has no way
to say that action was required years before that. The canonical case is
harvest-now-decrypt-later: encrypted material captured today can be retained and
decrypted once a capability exists that does not yet exist, so exposure of
long-confidentiality data is *already accruing*, and no control applied after
collection undoes it.

The `latent_exposure` object records what is at risk, when the harm begins, and
three numbers most organisations already hold but never compare — the
confidentiality horizon (usually a retention schedule), the realistic migration
duration, and the estimated capability horizon. Where the first two together
exceed the third, material protected today is already exposed. Working backwards
from the capability horizon by the migration duration yields
`mitigation_must_start_by`: the date at which a future obligation becomes a
present decision. That is the same move the admissibility gate makes for
actions, applied to time instead.

**Dependencies between obligations.** Two entries can each look adequately
carried while the combination is impossible. The `depends_on` array records
which entry a duty leans on and how — `mitigation gated by` being the
constraining case: this duty cannot be discharged faster than the entry it
depends on permits.

The worked instance is in the register. Article 50(2) requires synthetic content
to be marked machine-readably and detectably. Where that marking rests on digital
signatures for provenance, it inherits the shelf life of the signing algorithm —
so content expected to stay verifiable for longer than the signing cryptography
stays sound cannot be durably marked ahead of the cryptographic migration, and
where the signing keys live in hardware, not faster than the hardware refresh
cycle permits. An EU transparency duty is therefore gated by a cryptographic one.
Neither entry reveals this on its own.

Recording the dependency is what makes a framework of frameworks structurally
true rather than presentational: the connectedness becomes checkable, and a
dependency pointing at an entry that is not in the register is reported.

**A note on what does not become an entry.** Hardware trusted environments —
secure enclaves, hardware security modules, roots of trust — are almost never
obligations. They are controls discharging other duties, and they belong in
`controls` with type `technical`, as they do in the post-quantum entry. Putting a
control in the obligations layer is the same category error as putting a specific
law inside the lifecycle: the register would begin describing solutions rather
than duties, which is how a register becomes a product catalogue.

**Agreed is not enacted.** Between a political agreement and publication in the
official gazette there is a real interval, and during it commentary, official
guidance and the regulator's own timeline pages can each report a different state
of the world. `status: transitional` cannot express this — a provisional
agreement is not a transitional provision. The `contingent_on` object records
what must happen before an entry's dates bind, when it is expected, and what
resolved it.

The Article 50(2) entry carries a worked instance, and it is worked because it
happened: the entry was written while the Digital Omnibus was an agreement, and
had to be corrected once Regulation (EU) 2026/1744 was adopted on 8 July 2026 and
entered into force on 27 July. During that interval, one widely circulated
timeline graphic claiming to include the amendments carried four wrong dates, and
the official implementation timeline it drew on was itself showing the
pre-amendment position more than a week after the amending regulation was in
force. The field exists because the interval is not hypothetical.

## Coverage findings

`scripts/check_register.py` reports where an entry fails to connect:

- **UNCARRIED** — no gate criterion and no control carries the duty. The
  obligation is recorded and inert. This is the register-level form of
  Example C in the issue suite: fully documented, entirely without effect.
- **UNEVIDENCED** — controls exist, but no record demonstrates they operated.
  Conformance could not be shown if asked.
- **UNASSURED** — evidence exists, but nothing independently confirms it.
- **RECONSTRUCTED** — every evidence type is generated on demand.
- **STALE** — the review date has passed, or a transitional entry has none.
  A register without review dates decays silently, which is worse than having
  no register, because it looks like coverage.
- **UNMONITORED** — the obligation binds above a threshold, but nothing watches
  whether the threshold has been crossed; or scope status is unknown.
- **LAPSED** — a gate criterion rests on an instrument that has expired, or on
  one with nothing watching its expiry.
- **UNREFRESHED** — a standing duty with no re-entry triggers.
- **UNANTICIPATED** — a latent exposure is recorded but no mitigation start date
  is derived; the obligation remains a future problem on paper while accruing
  in fact.
- **OVERTAKEN** — confidentiality horizon plus migration duration exceeds the
  capability horizon, or the derived start date has passed.
- **UNRESOLVED** — a declared dependency points at an entry not in the register.
- **CONTINGENT** — the entry's dates depend on something that has not happened
  yet, or the condition's expected date has passed while still unresolved.

None is automatically a defect. Each is a finding to be dispositioned — the same
discipline the issue engine applies to observations.

## One provision per entry

Sub-provisions of the same article routinely bind different parties. Under
Article 50, subsections (1) and (2) fall on the *provider*; subsection (4) falls
on the *deployer*. An organisation may bear (4) while bearing neither of the
others. Collapsing them into a single "Article 50" entry would put criteria in
the wrong organisation's gate — the most consequential error available in a
register, and an easy one.

## Worked entries

`register/` holds three, all EU AI Act Article 50, applicable from 2 August 2026:

| Entry | Bearer | Character of the duty |
|---|---|---|
| `eu-ai-act-50-1` | provider | Inform people they are interacting with an AI system |
| `eu-ai-act-50-2` | provider | Mark synthetic output machine-readably and detectably |
| `eu-ai-act-50-4` | deployer | Disclose deepfakes and certain AI-generated publications |

Note that 50(1) is discharged **before** execution — the person must be informed
at first interaction — which is why it appears as a gate criterion rather than as
downstream evidence. 50(2) is largely a technical control with a robustness
question attached. 50(4) is procedural and lands on a different organisation.
One article, three shapes.

A fourth entry, `whs-hazchem-manifest-storage`, covers the storage of hazardous
chemicals above manifest quantities. It is included because it is the entry that
does *not* behave like the others: a standing duty, conditional on a threshold,
with several gate criteria resting on instruments that expire. It exercises every
field the Article 50 entries leave empty, and it is the reason those fields exist.

It also demonstrates a register discipline worth stating plainly: **it records no
numeric thresholds.** Quantities vary by jurisdiction and by chemical class. A
figure carried in a register without a citation is the kind of confident error
that survives review, so the entry points at where the figures are read and lets
the monitoring control watch the crossing. Its `currently_in_scope` is `"unknown"`,
which the coverage checker duly reports — an honest state, honestly flagged.

A fifth entry, `pqc-transition-hndl`, covers migration away from quantum-vulnerable
public-key cryptography. It is the anticipatory case: for most organisations this
is standards guidance and a procurement expectation rather than statute, which is
why `status` accepts `"advisory"` — a register that can only hold statute misses
most of what actually binds an organisation. Its scoring assumptions are
illustrative and deliberately labelled as such; each organisation substitutes its
own retention period and a defensible capability assumption, and records the
reasoning so a reviewer can test the assumption rather than the conclusion.

`eu-ai-act-50-2` carries `"status": "transitional"` and a near review date,
because part of its application was deferred. That is the register working as
intended: it holds an obligation that is law but not yet biting, and it says when
to look again.

## Summaries, not text

Entries paraphrase. No statutory or standards text is reproduced anywhere in this
repository — partly because reproducing it creates a licensing exposure, and
partly because a paraphrase forces the register-keeper to demonstrate they
understood the provision. An entry that could only be written by quoting is an
entry nobody has yet understood.

The `source` field points at where the authoritative text may be read. The
register points; it does not reproduce.

## A caution

These entries are a worked demonstration of the register's structure. They are
not legal advice, and they are not a substitute for reading the instrument or
taking advice on its application to a particular organisation.
