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

**Type is not timing.** The control type records how a control is implemented,
not when it acts. Those are different axes, and the second is currently absent
from the schema. A gate criterion requiring human intervention before a critical
action *prevents*; monitoring for unusual behaviour *detects*; an interruption
mechanism that halts a process already running *corrects*. All three may be
technical controls. Recorded only by type, a duty carried entirely by corrective
controls — everything recoverable, nothing prevented — reads the same as one
carried by preventive controls, which for irreversible actions is a material
difference. A `mode` field alongside `type` is planned for v0.2.0.

**A guarantee has a boundary, and the boundary is the point.** Recording that a
control exists says nothing about what it covers. The EU Cloud Services scheme
illustrates the difficulty twice over. Its published candidate version — ENISA,
22 December 2020, under Article 48(2) of the Cybersecurity Act — certifies
cybersecurity posture at defined assurance levels. Whether it also carries
sovereignty requirements, obliging data to be held in the EU and providers to be
established there, has been contested since; later drafts are reported to have
removed them, but those drafts were not officially published, and no final scheme
has issued. Six years after the candidate version, the position on what the
certification would guarantee is neither settled nor published.

If the sovereignty criteria are absent, a provider may hold the highest assurance
level and remain subject to foreign extraterritorial process over data held in
the EU: the certification would address security, not jurisdiction, and the two
are routinely conflated.

The pattern recurs. A trusted execution environment has a definitional literature
precisely because the term is used inconsistently and is poorly differentiated
from related concepts. A tamper-evident log secures the account without
establishing that the account was accurate when written. In each case the control
is real and the assumption about its reach is not. An entry that records the
control without recording where its guarantee stops has recorded the reassuring
half.

Distributed ledgers are the case where that assumption is most often made. A
ledger can establish that an entry has not been altered since it was written, and
that it was written by a holder of a particular key. It cannot establish that
what was written was true, that the key was held by the person it was issued to,
or that anything happened off the ledger at all. Where an obligation is evidenced
by a record, the ledger secures the record's integrity and the custody of it —
two of the three properties evidence needs. The third, accuracy at the point of
writing, is not a property any ledger confers, and no amount of cryptographic
assurance supplies it.

This places the mechanism in `controls`, with `type: technical`, as an integrity
and custody control on the Evidence stage. It does not place it in
`assurance_activities`: confirming that a record is unchanged is not confirming
that a control operated.

**One control is rarely enough.** Where a control is known to be weak, the
answer is not a stronger version of it but a second control of a different
kind. The Conseil d'État's charter on AI use in the French administrative
jurisdiction requires systematic human verification, then adds two further
requirements around it — that any AI-derived information be verifiable *by
another means*, and that responsibility for adopted content cannot be passed
back to the tool. The reason is stated: a person checking a proposal is subject
to anchoring bias in a way a person drafting is not. An entry recording human
review as its sole control has recorded a control whose known failure mode is
unaddressed. See [`docs/etude-de-cas-conseil-etat.md`](etude-de-cas-conseil-etat.md).

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

Obligations converging from several instruments are not hypothetical. On the
single question of whether an automated system may decide, the Conseil d'État's
charter stacks four: the AI Act at recital 61, GDPR Article 22, the French loi
informatique et libertés of 1978 at article 47, and the code de justice
administrative with the jurisdiction's own ethics charter. Different ranks,
different logics — two EU regulations, a French statute, a code — decomposed
into one operational requirement. This is the framework-of-frameworks claim
made by someone else, in another jurisdiction, without reference to this model.

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

**National law in the spaces the Regulation leaves.** Two Member States show
different answers to the same instrument, and both are cross-instrument
relationships of the kind this register exists to record.

Italy legislated. Legge 23 settembre 2025, n. 132 sets out principles on the
research, experimentation, development, adoption and application of AI systems
and models, and provides at Article 1(2) that its provisions are to be
interpreted and applied in conformity with Regulation (EU) 2024/1689. Not a
national law occupying ground the Regulation vacates, but one expressly
subordinated to it in interpretation.

Three provisions show what a Member State does with the space that leaves.

Article 13 restricts use before it requires disclosure. Paragraph 1 confines the
use of AI systems in the intellectual professions to instrumental and supporting
activities, with the intellectual work that is the object of the engagement
remaining predominant. Paragraph 2 then requires that information about the AI
systems used be communicated to the recipient of the intellectual service in
clear, simple and exhaustive language — grounded expressly in the fiduciary
relationship between professional and client rather than in transparency at
large. A gate criterion and a disclosure duty in two paragraphs.

Article 25 amends the copyright law of 1941 twice in a single provision. It
inserts the word *umano* after *opere dell'ingegno*, narrowing the subject matter
to works of human intellect; and then adds that protection extends to works
created with the aid of AI tools *purché costituenti risultato del lavoro
intellettuale dell'autore* — provided they constitute the result of the author's
intellectual work. One word restricts, the following clause preserves. A second
limb inserts Article 70-septies, permitting reproductions and extractions from
lawfully accessible works and databases for text and data mining through AI
models, including generative ones, in conformity with the existing exceptions and
subject to the Berne Convention.

Article 24 delegates. Points (e) and (f) provide for literacy and training paths
on the use of AI systems, and specifically for such paths to be provided by
professional orders and the most representative category associations for
professionals and operators in their sector — professional self-regulation as the
delivery mechanism rather than a state scheme. Point (f) closes with provision
for the possible recognition of an *equo compenso* modulated on the
responsibilities and risks connected with the use of AI systems: fair
compensation scaled to the responsibility the professional retains under
Article 13.

Spain has a bill. The Proyecto de Ley Orgánica para el buen uso y la gobernanza
de la inteligencia artificial was approved by the Consejo de Ministros on 26 May
2026 and published in the Boletín Oficial de las Cortes Generales, Serie A, núm.
97-1, on 12 June 2026. In this register's terms it is `status: pending`,
`contingent_on` publication in the BOE. Its fourth chapter requires the state
public sector to provide information about the AI systems used in the exercise of
its functions, to register those systems, and to designate a *delegado de
inteligencia artificial* responsible for coordinating correct application of the
AI regulatory framework — a named accountable role, of the kind the `bearer`
field could use.

**Who supervises is not who owes.** The Spanish architecture divides market
surveillance across AESIA, the Agencia Española de Protección de Datos, the Banco
de España, the Comisión Nacional del Mercado de Valores, the Dirección General de
Seguros y Fondos de Pensiones, the Consejo General del Poder Judicial and the
Junta Electoral Central.

The division is finer than sector. Article 5 designates AESIA as market
surveillance authority for prohibited practices under Article 5(1), points (a),
(b), (c) and (f) of Regulation (EU) 2024/1689 — not for the other points — and
for the Annex III biometrics category at point 1(c), but only where the systems
are not used in migration, asylum and border control management, or for law
enforcement and the administration of justice. The same Annex III entry therefore
falls to different authorities depending on the context of deployment. Allocation
is by provision and by use, not by domain.

The bill also answers a question the division creates. For cases not expressly
covered, and for new areas of supervision arising from delegated acts or
amendments to the Regulation, the Consejo de Ministros designates the authority
by agreement; **AESIA is competent by default until it does**. A residual
supervisor, and a mechanism for assigning new ones as the Regulation changes.

This register records `bearer` — who owes the duty. It records nothing about who
enforces it, and where enforcement is allocated by provision and by use, with a
residual authority behind it, that is a material omission. A `supervised_by`
field is planned for v0.2.0.

**And nothing records what breach costs.** Article 28 makes it a minor infraction
for a deployer to fail to request authorisation for post-remote biometric
identification under Article 26(10) of the Regulation — a national sanction
attached to a procedural step in an EU instrument. The register decomposes a duty
into what must be true before an action proceeds, what discharges it, what
evidences it and who confirms it. It says nothing about what follows if none of
that happens. Sanctions are a layer the schema does not have, and an obligation
whose breach carries a minor administrative penalty is a different governance
object from one carrying a fine of 7 per cent of worldwide turnover.

**A permission with its conditions on the face of it.** Article 4a of Regulation
(EU) 2024/1689, inserted by Regulation (EU) 2026/1744, permits providers of
high-risk AI systems to process special categories of personal data where
strictly necessary for bias detection and correction, and permits others to do so
where bias is likely to affect health and safety, negatively affect fundamental
rights, or lead to discrimination prohibited under Union law. Like Article 59 on
regulatory sandboxes, the permission is expressly *in addition to* the provisions
of Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680: an
AI Act permission that does not displace data protection law but sits on top of
it.

What distinguishes it is that the conditions are enumerated. Six of them,
cumulative: that the objective cannot be met by other data, including synthetic
or anonymised data; technical limitations on re-use with state-of-the-art
security and privacy-preserving measures including pseudonymisation; access
controls with documentation of access; no transmission, transfer or access by
other parties; deletion once the bias is corrected or the retention period ends,
whichever comes first; and a record in the processing activities register of why
the processing was strictly necessary and why the objective could not be achieved
by processing other data.

Each condition is a control, an evidence type, or both. The last is explicitly a
record. A register entry for this provision would decompose almost mechanically,
which is what a well-drafted permission looks like from the operational side —
and the contrast with provisions that state a duty and leave its discharge
unspecified is worth noticing.

The provision closes by stating that it creates no obligation to conduct bias
detection and correction at all.

**A prohibition, evidenced.** A register built around duties to do things handles
duties *not* to do them poorly, because compliance is evidenced by absence and an
absence is not a record. Article 5 of Regulation (EU) 2024/1689, as amended by
Regulation (EU) 2026/1744, shows how a well-drafted prohibition solves this.

Two practices are added from 2 December 2026: AI systems that generate or
manipulate realistic material depicting an identifiable natural person's intimate
parts or that person engaged in sexually explicit activities without their freely
given, specific, informed, unambiguous and explicit consent; and systems that
generate or manipulate material or performance within the meaning of Article 2,
points (c) and (e), of Directive 2011/93/EU, subject to a "without right" defence
under national law.

The operative content is in the qualifying paragraph. Placing on the market or
putting into service is prohibited only where such generation is the system's
intended purpose, **or** where its design, training, architecture, capabilities or
user-facing functionalities make that outcome reasonably foreseeable and
reproducible without significant technical modification, **and** the system lacks
reasonable and adequate technical safety measures and other safeguards to
reliably prevent it, taking into account reasonably foreseeable misuse, and to
correct observed or reported misuse. Use is prohibited only where the deployer
uses the system for that purpose.

So the prohibition is not evidenced by absence at all. It is evidenced by the
safeguards: what was assessed as reasonably foreseeable misuse, what measures
were implemented, whether they reliably prevent the outcome, and what was done
about misuse once observed or reported. Those are gate criteria, controls,
evidence types and assurance activities in the ordinary way.

The lesson generalises. Where a prohibition attaches liability to the absence of
adequate safeguards rather than to the occurrence of the prohibited act alone, it
becomes decomposable. Where it does not, the register has nothing to record but a
duty and a hope.

**An obligation with no defined discharge.** Article 4 of Regulation (EU)
2024/1689, as replaced by Regulation (EU) 2026/1744, requires providers and
deployers to take measures to support the development of AI literacy of their
staff and of other persons dealing with the operation and use of AI systems on
their behalf — taking into account technical knowledge, experience, education and
training, the context of use, and the persons on whom the systems are to be used.
It then states that the obligation *does not require providers or deployers to
guarantee any specific level of AI literacy of any individual*.

So the duty binds, and its discharge is expressly not measurable against any
standard. There is no threshold to meet, no state of affairs to bring about, and
the provision forecloses the obvious test. What remains is the taking of
measures, judged against the listed considerations.

Two things follow for an entry. The evidence is of *effort* rather than of
outcome: what was assessed, what was provided, to whom, and why it was
proportionate to the considerations the article lists. And the reach of the duty
extends beyond staff to other persons dealing with the operation and use of
systems on the organisation's behalf — contractors, which is a `bearer` question
in a provision that does not otherwise raise one.

The article also runs the other way. Paragraph 2 obliges the Commission and
Member States to support and facilitate those efforts, in particular for SMEs,
with the Commission to publish practical examples on the single information
platform. Paragraph 3 has the Board adopt recommendations taking European
competence frameworks into account. An obligation on organisations, with a
supporting obligation on institutions attached to it — a structure the register
has no way to record, since an entry has one bearer.

**A note on what does not become an entry.** Hardware trusted environments —
secure enclaves, hardware security modules, roots of trust — are almost never
obligations. They are controls discharging other duties, and they belong in
`controls` with type `technical`, as they do in the post-quantum entry. Putting a
control in the obligations layer is the same category error as putting a specific
law inside the lifecycle: the register would begin describing solutions rather
than duties, which is how a register becomes a product catalogue.

The same applies to certification schemes. The EU Cloud Services scheme, developed
by ENISA under the Cybersecurity Act, Regulation (EU) 2019/881, certifies
cybersecurity posture at three assurance levels. It is not a duty; nobody is in
breach for lacking certification. It is a means of demonstrating that controls
are in place, which belongs in `assurance_activities`.

This case is harder than the hardware one, and worth stating for that reason. The
scheme is formally voluntary, but NIS2 and the Data Act create pathways by which
authorities may require certified providers, and procurement may require it
independently. Member States may add national criteria — France through
SecNumCloud, Germany through BSI C5 — so the effective requirement varies within
a scheme designed to harmonise. Voluntary in form and binding in effect is a
condition this register's `status` vocabulary cannot express, and `advisory` does
not reach it.

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

**Two questions precede the gate.** The admissibility gate asks whether an
action may proceed. Two prior questions are not currently expressible: what role
the organisation occupies, which determines whose duty is engaged at all; and
whether the tool should be used for this task, which the Conseil d'État charter
frames as asking whether the same result could be reached by another means —
on grounds of efficiency, reliability and environmental cost together. Both sit
before the gate rather than in it. Planned for v0.2.0.

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

**What an entry does not record.** Each entry states what a provision requires
and points to where its text may be read. Neither tells you how the provision
has been *read* — by which authority, in which decision, with what effect. For
data protection in particular, most of the interpretive weight sits in
regulator decisions and guidance rather than in judgments, and a register that
points only at the text is pointing at the least contested part of the picture.

The scale is worth stating. The UCL Massively Crossreferenced Digital Laws
project, maintained by Michael Veale at UCL Laws, records the GDPR as cited by
over 20,000 documents, with thirty CJEU cases pending; the AI Act by over a
thousand. It also routes functionally equivalent provisions between instruments,
so that articles of the earlier Directive inherit the citations of the
Regulation that replaced them — a principled treatment of what happens to an
obligation's interpretive history when the instrument changes.

An `interpreted_by` field, distinct from `source`, is planned for v0.2.0.
Pending cases against a provision are also a better signal of interpretive
instability than a review date set by the register-keeper.

**What the published text is worth.** A register points at sources, so the status
of a published text is not incidental to it. Italian law is unusually explicit
here. Under article 8 of Testo Unico n. 1092/1985, publication in the Gazzetta
Ufficiale is presumed conform to the original and constitutes the legal text of
the act, until inaccuracy is proven by production of an authentic act. Errors are
corrected by one of two distinct instruments: an *errata corrige* for errors
arising in printing, and an *avviso di rettifica* for material errors in the
original or the copy sent for publication. Legge 132/2025 carries the second.

Consolidated and updated texts occupy a third position. They do not replace the
originals, but their official provenance makes them, in the Ministry of Justice's
formulation, *fonti di affidamento incolpevole da parte della collettività* —
sources on which the public may innocently rely. That names precisely the problem
this register met over the Digital Omnibus, when an official implementation
timeline still showed the pre-amendment position more than a week after the
amending regulation entered into force. An entry's `source` should point at the
instrument, and a register-keeper should know which of these three things they
are looking at.

## What the schema does not express

Eight limitations, each found by putting the model against an instrument becomes 
Nine limitations. They are listed together because the pattern is worth seeing: 
most concern what surrounds an obligation — who enforces it, how it
has been read, what a control actually covers, what breach costs — rather than
the obligation itself. That may be where the model's boundary genuinely lies.

None invalidates an existing entry. All are additive, and all are planned for
v0.2.0.

**1. When a control acts.** `type` records how a control is implemented —
technical, procedural, contractual, design. It does not record whether the
control prevents, detects or corrects. A duty carried entirely by corrective
controls reads the same as one carried by preventive controls, which for
irreversible actions is a material difference. A `mode` field would separate them.

**2. Role determination.** An entry records `bearer` as a conclusion. An
organisation applying the register must first determine what role it occupies —
provider, deployer, distributor, importer, or user of a third-party tool — and
that determination is itself a decision requiring evidence and an owner. It sits
before the gate, and has nowhere to sit in the schema.

**3. The necessity test.** The Conseil d'État charter asks, before use, whether
the same result could be reached by another means — on grounds of efficiency,
reliability and environmental cost together. That is a question about whether the
tool should be used at all, prior to whether the action may proceed. Also before
the gate, also unexpressed.

**4. How a provision has been read.** `source` points at where the text may be
found. Nothing records how the provision has been interpreted — by which
authority, in which decision, with what effect. For data protection in
particular, most interpretive weight sits in regulator decisions and guidance
rather than in judgments. An `interpreted_by` field would hold it.

**5. Who supervises.** `bearer` records who owes a duty. Where enforcement is
allocated by provision and by use across several authorities, with a residual
authority behind them, the register is silent on who would act. A `supervised_by`
field would record it.

**6. Voluntary in form, binding in effect.** `status` distinguishes in force,
transitional, pending, proposed, advisory and superseded. It cannot express a
scheme that binds nobody directly but is required through other instruments or
through procurement — nor one whose effective requirements vary by Member State
within a framework designed to harmonise.

**7. Where a guarantee stops.** An entry records that a control exists. It does
not record what the control covers and, more importantly, what it does not — a
certification addressing security but not jurisdiction, a validated module
covering one configuration and firmware version, a ledger securing a record's
integrity but not its accuracy. Recording the control without its boundary
records the reassuring half.

**8. What breach costs.** The register decomposes a duty into what must be true
before an action proceeds, what discharges it, what evidences it and who confirms
it. It says nothing about what follows if none of that happens. An obligation
whose breach carries a minor administrative penalty is a different governance
object from one carrying a fine of seven per cent of worldwide turnover.

**9. Obligations that pair.** An entry has one bearer. Article 4 of Regulation
(EU) 2024/1689 imposes a duty on providers and deployers and, in the same
article, a supporting duty on the Commission and Member States to facilitate
compliance with it. The two are connected — one exists to make the other
achievable — and the register can record them only as separate entries with no
relationship between them. `depends_on` records constraint, not support.

## A caution

These entries are a worked demonstration of the register's structure. They are
not legal advice, and they are not a substitute for reading the instrument or
taking advice on its application to a particular organisation.
