# Runbook

What to do when something fails. Every command exits with code 1 on failure and logs to
`logs/<command>.log`; run history is in `audit.pipeline_runs`.

```sql
-- in DuckDB: duckdb data/warehouse/olist.duckdb
SELECT * FROM audit.pipeline_runs ORDER BY started_at DESC LIMIT 10;
SELECT * FROM audit.quality_results WHERE failed_rows > 0 ORDER BY checked_at DESC;
SELECT * FROM audit.ingest_manifest ORDER BY loaded_at DESC;
```

| Symptom | Likely cause | Action |
|---|---|---|
| `ContractError: missing columns` | Source renamed/dropped a column | Compare header with the contract. Update the contract **and** the staging model together, never only one |
| `ContractError: primary_key_unique` | Duplicate rows in the new file | Find them: `SELECT key, count(*) ... HAVING count(*) > 1` on `bronze.<table>__candidate` (re-run with a breakpoint) or the CSV. Bronze still holds the last good version |
| `ContractError: accepted_values` | New status / payment type | Decide what it means, add it to the contract and to staging tests |
| `FxError ... retryable=True` | API down or rate limited | Airflow retries twice with backoff. If it persists, `olist fx --offline` is **not** a fix for production data — wait or replay the saved raw file |
| `dbt build` test failure | Data broke an assumption | Read the failing test in `dbt/target/run_results.json`; `dbt test --select <model> --store-failures` keeps the bad rows |
| `assert_money_reconciles` fails | A join fanned out or lost rows | Check grain of the last changed model; count rows before/after each join |
| `IO Error: Could not set lock` | Another process holds DuckDB | Close notebooks/dashboards writing to the file; the DAG allows one active run |
| Stream consumer crashed | Any | Restart it. Uncommitted messages are re-delivered and deduplicated by `event_id` |
| Events in `live.dead_letter` | Producer bug or schema change | Inspect `reason`, fix the producer, replay from the topic |

## Backfill and replay

- Reload everything from landing: `olist run --force --full-refresh`.
- Rebuild one model and its children: `cd dbt && dbt build --select fct_orders+`.
- Replay the stream from the start: use a new consumer `group.id` (offsets start at earliest).
