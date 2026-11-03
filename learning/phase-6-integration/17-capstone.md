# 17 · Capstone: everything on real data

**Level:** Integration · **Weeks:** 30–31 · **Prerequisite:** all previous modules

## Goal
Run the whole platform on the real Olist dataset, end to end, the way a team would operate it,
and record the evidence. Until now, each module worked mostly in isolation; here they meet.

## 1. Watch
| Video | Why | Length |
|---|---|---|
| [How I'd Learn Data Engineering in 2026 — Data with Baraa](https://www.youtube.com/watch?v=1nVGaNbvuXg) | Re-watch: you can now judge each part from experience | 33 min |
| [Intro to Data Architecture (Part 1) — Data with Baraa](https://www.youtube.com/watch?v=fBOtbNqgc0s) | Architecture vocabulary for your write-up | 4 h (skim) |
| DataTalksClub Zoomcamp [project guidelines](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/projects/README.md) | How reviewers grade a DE project | read |

## 2. The integration path
Do each step, and keep a log in `docs/capstone-log.md` (date, command, result, problem, fix).

| Step | Integrates | Evidence to save |
|---|---|---|
| 1. Download the 9 Kaggle CSVs into `data/landing/olist/`, record the zip's SHA-256 | 02 | hash in the log |
| 2. `olist run` (live FX API) | 06, 07, 09 | row counts per table, quality warnings, dbt PASS count |
| 3. Fill the real-data table in `docs/data-contract.md` (fan-out size, revenue gap explained to the cent, VND gaps, late rate, ambiguous summer-time hours) | 03, 05 | the filled table |
| 4. Airflow runs the daily DAG in Docker, publishes to Postgres | 10, 11 | Airflow screenshot |
| 5. Metabase dashboard on Postgres | 10 | dashboard screenshot |
| 6. Spark RFM on the real gold Parquet; segments shown in the dashboard | 12 | segment table |
| 7. Kafka: replay 10k orders; consumer crash test | 13 | proof query |
| 8. Gold marts in BigQuery via Terraform + your publish command | 14 | plan + a BigQuery query |
| 9. Late-delivery model on real data in MLflow; risk table scored | 15 | metrics, MLflow screenshot |
| 10. LLM labels on 1,000 real reviews with the best provider; topics in the dashboard | 16 | evaluation table |
| 11. A fresh clone on another machine (or WSL) reproduces steps 1–2 from the README alone | all | your notes on what was missing |

## 3. Failure drills (do all, write the result in `docs/runbook.md` if it adds something)
- Rename a column in one CSV → what stops, what keeps working, how do you recover?
- Block the FX API (wrong URL) → retries, exit code, Airflow status, recovery.
- Delete the DuckDB file → rebuild everything from landing; how long?
- Duplicate 100 rows in `order_items` → which check catches it?
- Kill the Kafka consumer and Postgres in the middle of a run.

## 4. Improve one thing on your own
Pick one and design it yourself (decision record in `docs/decisions.md`):
- Data freshness SLA + alert, data lineage view, or a cost report for BigQuery.
- A slowly changing `dim_sellers` (SCD2) fed by simulated changes.
- An incremental `fct_orders` by `order_date` partitions instead of a full rebuild.

## Done when
- [ ] Steps 1–11 have evidence in the repo
- [ ] Failure drills done; runbook updated
- [ ] One improvement shipped with a decision record
