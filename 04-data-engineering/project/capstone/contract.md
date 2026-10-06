# Integrated retail capstone contract

## Business question and source assumptions

Produce current active order count and exact integer-cent amount by customer and occurred day, with an explicit timezone policy. This is current truth over event date, not an as-of historical accounting system.

Source batches b1/b2 contain versioned upserts/deletes. DE04 defines fields. Per-id version is authoritative; equal-version conflicting content fails the batch. Preserve tombstones and immutable raw evidence. updated_at is source change availability; extraction cursor pair ordering follows DE09's unique-pair assumption. All labs run one writer. Empty/invalid data follows a stated quarantine and missing-data policy.

## Required implementation

Use your own Python library/CLI under this folder; starter code is intentionally absent. Suggested modules: contracts.py, state.py, db.py, export.py, cli.py, orchestration.py. Keep functions small and importable. Design naming is a suggestion, not a required abstraction.

- Native PostgreSQL stores raw/staged evidence, authoritative current state, batch ledger and progress. Use parameterized SQL; data/progress commit together.
- Batch identity plus content hash distinguishes an identical replay from reuse with changed bytes.
- Export is separately recoverable. Database commit followed by export failure leaves explicit publication pending; regenerate from committed state.
- Produce full source history as a typed/documented export for warehouse latest-state transformations, or declare/test an equivalent source adapter. Do not mix fixture seed data with actual exports and claim integration.
- Reuse the dbt model graph against your exported source; the supplied seed is for standalone lessons. Document how the capstone source enters dbt. Reconciliation compares active authoritative PostgreSQL state to warehouse facts/mart.
- Prefect wraps stages with fixed batch/interval parameters, bounded retry ownership and failed-quality publication blocking.
- CLI returns nonzero for failed runs; structured events include run/stage/counts and sanitized errors.
- Delivery includes offline unit/contract tests, separately configured native integration tests, dependency versions, Docker packaging after its lesson, and an optional deliberate CI activation. No credentials embedded in images/code.

## Fixture acceptance

- [ ] b1: 2 active orders, 2500 cents.
- [ ] b2 correction/delete/late arrival: 2 active orders, 2000 cents.
- [ ] State has A v2, B v2 tombstone, C v1.
- [ ] Identical replay preserves totals/state.
- [ ] Stale b1 cannot resurrect B or replace A v2.
- [ ] Conflicting equal revision fails visibly with unchanged committed state.
- [ ] Injected pre-commit failure changes neither state nor progress.
- [ ] Post-commit export failure is recoverable without double-applying source changes.
- [ ] Backfill and full rebuild reconcile.
- [ ] Cursor timestamp tie visits every source row under the stated source guarantee.
- [ ] dbt tests detect a deliberate semantic defect.
- [ ] Mart count/amount matches committed active source state.
- [ ] Failed load/quality gate prevents downstream publication.
- [ ] Fresh terminal setup and five-minute demo work.
- [ ] Environment and actual runtime evidence are recorded.

## Delivery files

README.md: problem, grain, architecture, setup/versions, credentials mechanism, run/tests, expected outputs and limitations.
runbook.md: four incidents, diagnosis/repair and durable boundary.
evidence.md: commands/results/run identities, changed-input proof and runtime limits.
demo.md: source changes -> state/mart -> replay -> failure -> recovery -> trade-offs.
tests/: offline deterministic cases, live database tests explicitly marked.
Dockerfile/Compose/workflow: only after corresponding Linux lessons; scoped learning resources and no active publishing by default.

Save runtime artifacts in output/ or your native lab area. Use synthetic data. Keep original fixture files intact. Do not delete or overwrite other course databases.

## Known limits to explain

One writer; source version/order assumptions; no distributed exactly-once claim; PostgreSQL/files/warehouse do not share one transaction; fixture load volume is not a throughput benchmark. Optional cloud/Airflow/Spark do not belong in the main stack unless selected for a real requirement.

## Commit — Windows PowerShell

~~~powershell
Set-Location "C:\DE Courses"
git status
git add -- 04-data-engineering/project/capstone 04-data-engineering/project/dbt
git diff --cached --stat
git diff --cached
git commit -m "feat(portfolio): complete reliable retail pipeline"
git push -u origin HEAD
~~~

