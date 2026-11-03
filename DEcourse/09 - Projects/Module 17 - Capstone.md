# 17 · Capstone: end-to-end acceptance

> **Theory notes:** [[Olist Product Brief]] · [[Failure Drills]] · [[Observability and Recovery]] · **Route:** [[Roadmap]] · **Labs:** [[Labs Guide]]

**Weeks:** integrated from module 09 onwards; consolidated in weeks 29–31 · **Prerequisites:** core through G4 plus one chosen branch. You do not need every elective module.

## Goal

Prove that the pipeline answers a business question, that the data is correct, and that someone else can operate it. Do not wait until the end of the course to run real data: this module is an acceptance checklist that you fill in step by step as the course progresses.

## Milestones

| When | Required output | Evidence |
|---|---|---|
| Module 04 | Profile the real Olist data (or the sample until the download works) | Rows/nulls/keys/date range and 5 observations, each backed by a query |
| End of 09 | Real Olist batch, live FX, `dbt build` and reconciliation | Input hash, versions, real counts in `docs/data-contract.md` |
| End of 11 | One dashboard, Postgres, a schedule and a backfill over the correct interval | Logs, per-day proof SQL, screenshot |
| End of 19 | 30-day-old update, delete, changed order date, SCD2 | Incremental compared with a full rebuild key by key |
| End of 20 | Stale-data alert and recovery from raw on a copy | Incident report, recovery time, counts/money reconciled |
| End of 21 | Reader/writer roles, clean environment, rollback | Positive and negative permission tests, release manifest |
| End of 14 | One BigQuery mart, IaC, permissions/cost | Plan, dry run, bytes cap, resource cleanup |
| Elective branch | One main extension from the list below | Measurements and failure proof |
| End of 22 | A new project with no reference solution, plus a changed requirement | Brief, ADR, review, demo, rubric score |

Keep a log in `docs/capstone-log.md` in your code repo: date/timezone, code/input/config version, command, expected result, actual result, problem and fix. Create entries only when you actually run something; never fill in estimated results.

## Choose one main extension

- **Spark:** RFM that matches the SQL version, plus a benchmark with skew/partitions/shuffle/file count. Small Olist data proves functionality, not scale.
- **Kafka:** a broker end to end, 10k events, crash/replay, out-of-order events and a DLQ; reconcile by event_id, not just row counts.
- **ML scoring:** feature known_at, time split, baseline, tracked experiment, batch scoring of open orders.
- **LLM labelling:** keyword baseline + a model on the same held-out gold set; schema pass/unparsed rate, macro-F1, latency/cost, cache invalidation on input/model changes.

Other branches, RAG, text-to-SQL and extra clouds/BI tools are extensions; they do not block graduating from the core.

## Mandatory core failure drills

1. Renamed column / duplicate key: block the publish, keep the last good version, record the version.
2. Snapshot A→B→A: the result is A; a missing or stale Parquet output after the DB commit is repaired by a retry.
3. API fails on a middle page: retry/replay produces no gaps and no duplicates, and half a batch is never published.
4. Update after 30 days, delete, changed date and an emptied partition: the result matches a rebuild.
5. Job exits 0 but a partition is missing: the freshness check must alert.
6. Lose a copy of the warehouse: restore from raw, measure the time and reconcile.
7. Republish a mart: the reader can still read it and still cannot write or read raw.

If you chose Kafka or LLM, add that branch's drills too. Use a separate environment and drill folder; never break your only copy of the data. Update the runbook after each measured result. Details for every drill are in [[Failure Drills]].

## Done when

- [ ] G1–G5 have evidence you produced yourself; reference code never stands in for your results.
- [ ] The core and the chosen branch are recorded with their true status; anything not run is marked as such.
- [ ] Another person reproduces the batch from the README and reviews the independent project.
- [ ] The demo explains the need, the metric, a failure/recovery and one trade-off.
