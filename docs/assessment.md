# Independent gates and readiness rubric

Use documentation for syntax. For an assessment, avoid generated implementation/SQL solutions. Explain a key function aloud and reproduce a small change independently. A supplied fixture pass is not a passing gate on its own.

## Gate A — Python independence, 90–120 minutes

From a blank file, read a new CSV with ID, quantity, unit-price cents and aware timestamp. Validate values, quarantine errors with reasons, state duplicate policy, produce an exact customer total and offer CLI input/output arguments. Add tests for empty/malformed/boundary input. Run from a different cwd. Explain return versus print, mutability, exception boundaries and time normalization.

Pass: core task works with changed input, meaningful tests fail on a deliberate wrong behavior and code is explainable. Missing packaging polish can be noted; inability to structure functions calls for Python review.

## Gate B — SQL correctness, 45–60 minutes

In a new native PostgreSQL test schema use:
- customers: c1, c2, c3; c3 has no orders.
- orders: o1/c1/1000 at Sep 1 09:00 UTC; o2/c1/1500 at Sep 1 10:00; o3/c2/800 at Sep 2 09:00.
- payments: two rows for o1, 400 and 600; one for o2, 1500; no payment for o3.

Tasks: all customers including zero-order counts; correct total order revenue without payment join multiplication; paid amount by order; latest order per customer with a deterministic tie-break; month and local-day amounts with a half-open interval; unpaid orders using EXISTS logic; quality query for orphan payment order IDs; running customer revenue with an explicit window frame.

After the attempt, expected totals: c1 two/2500, c2 one/800, c3 zero/0; all-order revenue 3300, payments 2500. A raw one-to-many payment join repeats o1's full amount and yields 3500 for c1, which is wrong. Change a timestamp tie and one orphan row to test your queries.

Pass: reconciled results with preserved zero groups, correct NULL/count/filter handling and explanations. Use your chosen SQL course for unresolved syntax; this is a diagnostic, not an extra SQL curriculum.

## Gate C — Model and native database, 2–3 hours

State fact grain and natural/surrogate keys. Show event-time dimension boundary behavior, parameterized inserts and actual rollback with injected failure. Explain equal-version conflicts, single-writer assumption and what is committed. Live PostgreSQL evidence is required; a fake connection is insufficient.

## Gate D — Reliable pipeline

Prove b1 -> b2 -> replay leaves 2000 cents; tombstone blocks resurrection; cursor ties do not skip records; backfill matches rebuild; fixed-clock checks catch defects. Demonstrate database rollback and post-commit publication recovery separately. Explain which late-data guarantee the source supports.

## Gate E — Reproducible delivery

Follow the capstone README from a fresh terminal/environment. Show dbt model/tests, one manual Prefect run, Docker/CI evidence where claimed, scoped configuration and a useful recovery runbook. A concept-only optional cloud/Spark/Airflow lab is labeled as such. The project passes checks before publishing.

## Gate F — Transfer and communication

Complete DE26's unfamiliar parcel task and SQL diagnostic within an honest timebox. First write a small task contract and plan using DE02's method. Read an unfamiliar entry point, reproduce a defect, preserve a failing regression test and verify a small repair using DE03's method. Deliver a handoff with actual checks and remaining limits. Give a 90-second English introduction and answer follow-ups on grain, replay, late data, transactions, joins and recovery without reading a script.


## Gate G — Source discovery and verified recovery

On a changed source, complete DE27's profile and explain grain, candidate keys,
defects and unanswered owner guarantees before selecting a cleaning policy.
Hand off a catalog, column lineage and consumer contract, omitting unnecessary
sensitive fields.

Complete DE28 on two new owned databases: inspect the archive, restore to an empty
target, compare complete item/deletion/ledger state and prove constraints. Add a
different baseline item so hard-coded totals cannot pass. Record restore-plus-
verification time and post-dump changes that were not recovered. Explain logical
backup, access-policy and PITR limits. These checks can span separate sessions.

Pass: facts and business decisions are separated, changed-source checks work, and
a native restore produces verified usable data. An archive alone or mock is insufficient.

## Score each gate

| Score | Meaning | Action |
|---|---|---|
| 0 | Cannot begin independently | Return to targeted guided practice |
| 1 | Works only with a full solution or happy path | Practise changed inputs, explain code and failure cases |
| 2 | Independent core works, meaningful tests/evidence, limitations clear | Sufficient evidence to discuss relevant internship work |
| 3 | Handles new variations, diagnoses errors and explains trade-offs well | Stronger evidence; pursue role-specific extension |

Aim for at least 2 on A–G, especially Python/SQL/modeling and reliability. This is a course rubric, not an employer standard or a hiring guarantee. If one supporting delivery skill is weaker, apply to roles matching what you can demonstrate and state the gap; keep practising.

## Role-fit check

For 3–5 fresh postings, record date, location, student-year eligibility, work schedule, required/preferred skill and your evidence. Some inspected descriptions ask for final-year students, so your upcoming third year may not fit every listing. Technical readiness and eligibility are separate.

## Repair rule

Name the failed behavior, choose at most two focused lessons, practise on a new fixture, then retry the gate. Do not restart all courses or install five new tools. Preserve failed/repaired evidence so improvement is visible.
