#!/usr/bin/env python3
"""Coverage check for the Model 1 obligation register.

An obligation register that merely lists obligations is a bibliography. This
script checks that each entry is actually connected to the lifecycle, and
reports the connections that are missing.

Coverage findings, in the same idiom as the issue-scoring engine:

  UNCARRIED   nothing in the entry carries the duty at all — the obligation
              is recorded and inert, the register-level equivalent of
              Example C in the issue suite
  UNEVIDENCED controls exist but no record demonstrates they operated;
              conformance could not be shown if asked
  UNASSURED   evidence exists but nothing independently confirms it
  RECONSTRUCTED  the only evidence is generated on demand, i.e. assembled
              after the question is asked rather than as the control ran
  STALE       the review date has passed, or a transitional entry has no
              review date at all
  UNMONITORED an obligation binds above a threshold, but no control watches
              whether the threshold has been crossed — scope can be entered
              by ordinary trading, with nobody aware
  LAPSED      a gate criterion rests on an instrument that has expired, or
              on one with no control watching its expiry. The quietest
              failure available: it was true, nobody changed anything, and
              it stopped being true
  UNREFRESHED a standing duty with no re-entry triggers. The gate model
              assumes an action to authorise; a standing duty has none, so
              without triggers the gate is never re-entered and conformance
              is asserted from the last check indefinitely
  UNANTICIPATED  a latent exposure is recorded but no date is derived for when
              mitigation must start — the obligation remains a future
              problem on paper while accruing in fact
  OVERTAKEN   the confidentiality horizon plus the migration duration exceeds
              the capability horizon, so material protected today is already
              exposed on the entry's own assumptions; or the derived
              mitigation start date has passed
  UNRESOLVED  a declared dependency points at an entry that is not in the
              register. Two obligations can each look adequately carried
              while the combination is impossible; an unresolved dependency
              means nobody has checked whether this is such a pair
  CONTINGENT  the entry's dates depend on something that has not yet
              happened — publication, commencement, an implementing act —
              or the condition's expected date has passed while it is still
              recorded as unresolved. Agreed is not enacted

None of these is automatically a defect. Each is a finding to be dispositioned.

No third-party dependencies. Run from the repository root:

    python3 scripts/check_register.py
"""

import datetime
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "schema" / "obligation-entry.schema.json"
REGISTER = ROOT / "register"

TODAY = datetime.date.today()


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def check_structure(entry, schema, label, errors):
    props = schema.get("properties", {})
    for key in schema.get("required", []):
        if key not in entry:
            errors.append(f"{label}: missing required field '{key}'")
    if schema.get("additionalProperties") is False:
        for key in entry:
            if key not in props:
                errors.append(f"{label}: unexpected field '{key}'")
    for key, value in entry.items():
        spec = props.get(key, {})
        allowed = spec.get("enum")
        if allowed and value not in allowed:
            errors.append(f"{label}: '{key}' = {value!r} not permitted")

    d = entry.get("decomposition", {})
    for gc in d.get("gate_criteria", []):
        if gc.get("failure_outcome") not in ("NO-GO", "CONDITIONAL GO"):
            errors.append(f"{label}: gate criterion has an invalid failure outcome")
    for ev in d.get("evidence_types", []):
        if ev.get("generated_at") not in ("design", "execution", "periodic", "on-demand"):
            errors.append(f"{label}: evidence type has an invalid generated_at")


def coverage(entry, known_ids=frozenset()):
    d = entry.get("decomposition", {})
    gates = d.get("gate_criteria", [])
    controls = d.get("controls", [])
    evidence = d.get("evidence_types", [])
    assurance = d.get("assurance_activities", [])

    findings = []

    if not gates and not controls:
        findings.append(("UNCARRIED", "no gate criterion and no control carries this duty"))
    if controls and not evidence:
        findings.append(("UNEVIDENCED", "controls defined but no record demonstrates they operated"))
    if evidence and not assurance:
        findings.append(("UNASSURED", "evidence defined but nothing independently confirms it"))
    if evidence and all(e.get("generated_at") == "on-demand" for e in evidence):
        findings.append(("RECONSTRUCTED", "every evidence type is generated on demand"))

    # Standing duties must be able to return to the gate.
    if entry.get("duty_character") == "standing" and not entry.get("reentry_triggers"):
        findings.append(("UNREFRESHED", "standing duty with no re-entry triggers defined"))

    # Conditional scope must be watched.
    applicability = entry.get("applicability")
    if applicability:
        if not applicability.get("monitoring_control"):
            findings.append(("UNMONITORED",
                             "applicability is conditional but no control watches the threshold"))
        if applicability.get("currently_in_scope") == "unknown":
            findings.append(("UNMONITORED",
                             "scope status is 'unknown' — determine it or record why it cannot be"))

    # Expiring instruments behind gate criteria.
    for gc in gates:
        v = gc.get("validity")
        if not v:
            continue
        expires = v.get("expires")
        if expires:
            try:
                if datetime.date.fromisoformat(expires) < TODAY:
                    findings.append(("LAPSED",
                                     f"gate criterion rests on a {v.get('basis')} that expired {expires}"))
            except ValueError:
                findings.append(("LAPSED", f"invalid expiry date {expires!r}"))
        if not v.get("monitored_by"):
            findings.append(("LAPSED",
                             f"gate criterion rests on a {v.get('basis')} with nothing watching its expiry"))

    # Anticipatory obligations: harm accruing ahead of the compliance date.
    latent = entry.get("latent_exposure")
    if latent:
        start_by = latent.get("mitigation_must_start_by")
        if not start_by:
            findings.append(("UNANTICIPATED",
                             "latent exposure recorded but no mitigation start date derived"))
        else:
            try:
                if datetime.date.fromisoformat(start_by) < TODAY:
                    findings.append(("OVERTAKEN",
                                     f"mitigation should have started by {start_by}"))
            except ValueError:
                findings.append(("UNANTICIPATED", f"invalid start date {start_by!r}"))

        x = latent.get("confidentiality_horizon_years")
        y = latent.get("migration_duration_years")
        z = latent.get("capability_horizon_years")
        if None not in (x, y, z) and (x + y) > z:
            findings.append(("OVERTAKEN",
                             f"confidentiality horizon ({x}y) + migration ({y}y) exceeds "
                             f"capability horizon ({z}y): material protected today is "
                             f"already exposed on these assumptions"))

    # Cross-entry dependencies must resolve.
    for dep in entry.get("depends_on", []):
        target = dep.get("entry_id")
        if target not in known_ids:
            findings.append(("UNRESOLVED",
                             f"depends on '{target}', which is not in the register"))

    # Agreed is not enacted.
    cont = entry.get("contingent_on")
    if cont and not cont.get("resolved"):
        expected = cont.get("expected_by")
        if expected:
            try:
                if datetime.date.fromisoformat(expected) < TODAY:
                    findings.append(("CONTINGENT",
                                     f"still unresolved past {expected}: {cont.get('condition')}"))
                else:
                    findings.append(("CONTINGENT",
                                     f"dates do not bind until: {cont.get('condition')}"))
            except ValueError:
                findings.append(("CONTINGENT", f"invalid expected date {expected!r}"))
        else:
            findings.append(("CONTINGENT",
                             f"unresolved, no expected date: {cont.get('condition')}"))

    review = entry.get("review_date")
    if review:
        try:
            if datetime.date.fromisoformat(review) < TODAY:
                findings.append(("STALE", f"review date {review} has passed"))
        except ValueError:
            findings.append(("STALE", f"review date {review!r} is not a valid date"))
    elif entry.get("status") in ("transitional", "pending", "proposed"):
        findings.append(("STALE", f"status is '{entry.get('status')}' with no review date set"))

    return findings


def main():
    schema = load(SCHEMA)
    entries = sorted(REGISTER.glob("*.json"))
    if not entries:
        print("no register entries found", file=sys.stderr)
        return 1

    loaded = [(path, load(path)) for path in entries]
    known_ids = {e.get("id") for _, e in loaded}

    errors = []
    total_findings = 0

    for path, entry in loaded:
        label = entry.get("id", path.stem)
        check_structure(entry, schema, label, errors)

        d = entry.get("decomposition", {})
        counts = (
            f"gate {len(d.get('gate_criteria', [])):>2}  "
            f"ctrl {len(d.get('controls', [])):>2}  "
            f"evid {len(d.get('evidence_types', [])):>2}  "
            f"asur {len(d.get('assurance_activities', [])):>2}"
        )
        findings = coverage(entry, known_ids)
        total_findings += len(findings)

        provision = entry.get("provision", "")
        if len(provision) > 34:
            provision = provision[:31] + "..."
        marker = "  ok " if not findings else "  !! "
        print(f"{marker}{label[:28]:28s} {provision:34s} {counts}")
        for dep in entry.get("depends_on", []):
            print(f"       depends on {dep.get('entry_id')} ({dep.get('nature')})")
        for kind, detail in findings:
            print(f"       {kind}: {detail}")

    print()
    if errors:
        print(f"{len(errors)} structural problem(s):")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"{len(entries)} entries structurally valid; "
          f"{total_findings} coverage finding(s) to disposition.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
