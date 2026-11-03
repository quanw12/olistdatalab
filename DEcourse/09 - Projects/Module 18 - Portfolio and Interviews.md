# 18 · Portfolio and interviews

> **Theory notes:** [[Interviews and Portfolio]] · **Route:** [[Roadmap]] · **Labs:** [[Labs Guide]]. Videos are optional: use the diagnostic test to decide what to watch.

**Weeks:** 32, then ongoing · **Level:** Integration

## 1. Watch
| Video | Why |
|---|---|
| [SQL Data Analyst Portfolio Project — Data with Baraa](https://www.youtube.com/watch?v=2jGhQpbzHes) | How a project is presented, not only built |
| [How I Would Learn SQL FAST (2026 roadmap) — Data with Baraa](https://www.youtube.com/watch?v=kkKPD7khA54) | Keep SQL sharp for interviews |

## 2. Make the repo yours
1. README "Status" table: only what you ran, with screenshots in `docs/img/`.
2. `docs/data-contract.md` filled with your real numbers.
3. `docs/ai-log.md`: honest entries — what AI suggested, what was wrong, how you caught it.
4. Rename the repo (e.g. `olist-data-platform`), make it public, pin it on your GitHub profile.
5. A 3-minute demo video (screen recording): architecture → one finding → one failure and recovery.

## 3. CV bullets (edit to your real numbers; claim nothing you did not run)
- Built an end-to-end batch pipeline on ~100k real e-commerce orders (Python, DuckDB, dbt,
  Airflow): contract checks at ingestion, idempotent loads, 50+ dbt tests incl. cent-level
  revenue reconciliation.
- Modelled a star schema and an incremental daily revenue mart; served via PostgreSQL to a
  Metabase dashboard.
- Streamed order events through Kafka with an at-least-once, idempotent consumer and dead-letter handling.
- Processed customer segments with PySpark; deployed GCS + BigQuery with Terraform; CI with GitHub Actions.
- Trained a leakage-safe late-delivery model (scikit-learn, MLflow); labelled Portuguese reviews
  with local and hosted LLMs, validated against customer scores.

## 4. Two-minute answers (practise out loud in English)
- The architecture, from CSV to dashboard.
- One data problem you found and proved (grain / time zone / revenue gap).
- One failure and how the pipeline recovers.
- One decision you would change with more time.

## 5. Question bank → where your answer lives
| Question | Answer from |
|---|---|
| Tell me about a pipeline you built | README, capstone log |
| How do you ensure data quality? | module 06, dbt tests, reconciliation |
| Batch vs streaming? | modules 11, 13 |
| How do you handle failures and reruns? | runbook, idempotency |
| SQL live coding | module 03 + LeetCode practice |
| Spark: what is a shuffle? | module 12 |
| How do you use AI tools? | ai-log, module 16 evaluation |

Practice platforms: [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/),
[DataLemur](https://datalemur.com/questions), [StrataScratch](https://www.stratascratch.com/).

## Done when
- [ ] Public repo with real results, screenshots, demo video
- [ ] CV updated with bullets you can defend line by line
- [ ] Mock interview done for every question above

## Product-focused requirements

List only the core and branch that have real evidence on your CV. Do not copy all bullets if you ran only one branch or only sample data. G5 needs the independent project from module 22 and a review from another person; the mock interview covers SQL, trade-offs, an incident and how you check AI output. If evidence is missing, say so instead of switching the status to Done.
