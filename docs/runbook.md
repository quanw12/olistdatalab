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
| Bronze Parquet missing/stale after DB commit | Export interrupted | Re-run ingest: current DB loads are skipped but bronze outputs are re-exported; compare Parquet keys/counts with DB |
| A previously seen snapshot is restored | Source reverted A→B→A | Ingest compares against current published lineage and reloads A; inspect current `_file_sha256`, not only historical manifest |
| Historical daily revenue stale | Update/delete outside bounded order_date lookback | Rebuild with `olist transform --full-refresh`, reconcile against source; implement affected-partition handling before claiming general incremental support |
| LLM label stale after text/model change | Cache identity changed | Re-run ai-label for the provider; input/model versions get separate entries. ai-eval excludes obsolete text; review-score agreement remains only a weak quality signal |
| Events in `live.dead_letter` | Producer bug or schema change | Inspect `reason`, fix the producer, replay from the topic |

## Backfill and replay

- Reload everything from landing: `olist run --force --full-refresh`.
- Rebuild one model and its children: `cd dbt && dbt build --select fct_orders+`.
- Replay the stream from the start: use a new consumer `group.id` (offsets start at earliest).

The reference Airflow DAG schedules the same snapshot CLI. Backfilling DAG dates alone does not
reconstruct historical source snapshots: use fixed input versions and an interval-aware lab job
(module 11/19). Keep sample/real/drill data and DuckDB paths separate before destructive drills.
