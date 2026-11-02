# 03 · Ingestion and data quality

**Time:** weeks 3–4 · **Stack:** pandas, NumPy, Polars, Parquet, DuckDB, data contracts

## Why
Most production incidents start at ingestion: a renamed column, duplicate rows, a new status
value. A pipeline that stops loudly and keeps yesterday's good data is worth more than a fast one.

## Learn
- Medallion layers (bronze / silver / gold) and why bronze keeps raw text
- Idempotency: running twice = running once
- Parquet vs CSV: columnar storage, types, compression — [Parquet overview](https://parquet.apache.org/docs/overview/)
- pandas → [Polars](https://docs.pola.rs/user-guide/getting-started/): lazy frames, expressions, why it is faster
- NumPy basics: vectorised operations vs Python loops

## Read in this repo
- `src/olist_platform/contracts/olist.yml` — the contract.
- `src/olist_platform/ingest.py` — hash → schema check → candidate table → checks → atomic swap.
- `src/olist_platform/quality.py` — every check is one counting SQL query.
- `tests/test_ingest.py` — the failure cases, each as a test.

## Build
1. Ingest the optional `geolocation` file from the real dataset. Add a staging model that
   dedupes it to one row per zip prefix (median lat/lng). **Check:** unique test on zip prefix.
2. Add a new check type `min_value` (e.g. `price >= 0`) to the contract and `quality.py`, with a test.
3. Add a `freshness` check: fail if the newest `order_purchase_timestamp` is older than N days
   (configurable; off for the static Olist snapshot).
4. Re-implement `int_order_payments_by_order` in **Polars** and in **pandas** in a notebook
   (`notebooks/`, Jupyter). Time both on the real file; compare to DuckDB. **Check:** same totals.
5. Write a quarantine: instead of failing the whole table on a bad row, write bad rows to
   `bronze.<table>_rejects` with a reason, publish the rest. When is this better, when worse?
   Write the answer in `docs/decisions.md`.

## Break it
- Duplicate one line in the orders CSV and run `olist ingest`. Confirm bronze still holds the old run.
- Save the CSV from Excel (changes date format and adds a BOM). What fails and is the message clear?

## Interview questions
- How do you make a load idempotent? What if the source sends corrections?
- Where do you put data quality checks, and what happens when one fails?
- Why is Parquet better than CSV for analytics?

## Done when
- [ ] Geolocation, `min_value`, freshness merged with tests
- [ ] Polars vs pandas vs DuckDB timing table in your notes
- [ ] You can whiteboard the ingest flow
