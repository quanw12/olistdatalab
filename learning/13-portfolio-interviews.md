# 13 · Portfolio and interviews

**Time:** week 16, then ongoing

## Make the repo yours
1. Run everything on the **real** dataset. Fill the table in `docs/data-contract.md` with your numbers.
2. Replace README "Status" rows with what you actually ran; add screenshots (Airflow, Metabase,
   dbt lineage, MLflow) under `docs/img/`.
3. Keep `docs/ai-log.md` honest: what AI suggested, what was wrong, how you caught it.
4. Rename the GitHub repo to something descriptive (e.g. `olist-data-platform`) and pin it on your profile.

## CV bullets (edit to your real numbers; never claim what you did not run)
- Built an end-to-end batch pipeline on ~100k real e-commerce orders (Python, DuckDB, dbt,
  Airflow): contract checks at ingestion, idempotent loads, 50+ dbt tests including a
  cent-level revenue reconciliation.
- Modelled a star schema (order and item facts, customer/seller/product/date dimensions) and an
  incremental daily revenue mart; served to Metabase via PostgreSQL.
- Streamed order lifecycle events through Kafka with an at-least-once, idempotent consumer and a
  dead-letter table.
- Trained a late-delivery classifier with leakage-safe, time-based features (scikit-learn,
  MLflow); labelled Portuguese reviews with local and hosted LLMs, validated against customer scores.
- Infrastructure as code for a GCS + BigQuery deployment (Terraform); CI with GitHub Actions.

## Explain in 2 minutes (practise out loud, in English)
- The architecture, from CSV to dashboard.
- One bug you found in the data and how you proved it (grain / time zone / revenue gap).
- One failure scenario and how the pipeline recovers (see `docs/runbook.md`).
- One decision you would change with more time.

## Common interview questions mapped to this repo
| Question | Answer from |
|---|---|
| Tell me about a pipeline you built | README architecture + data-contract findings |
| How do you ensure data quality? | `quality.py`, dbt tests, reconciliation test |
| Batch vs streaming? | Modules 06 and 09 |
| How do you handle failures / reruns? | `docs/runbook.md`, idempotency in ingest and consumer |
| SQL live coding | Module 02 queries |
| How do you use AI tools? | `docs/ai-log.md`, module 12 evaluation |

## Done when
- [ ] Real-data numbers and screenshots in the repo
- [ ] CV updated with bullets you can defend line by line
- [ ] Mock interview done (with a friend or recorded) for each question above
