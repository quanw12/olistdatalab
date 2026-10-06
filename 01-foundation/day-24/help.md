# Day 24 — Warehouses, query plans, and a small cloud lab


1. Use pgAdmin on your local lab DB for EXPLAIN. A Seq Scan is unsurprising for this tiny table. Compare estimates with actual SELECT execution using EXPLAIN ANALYZE only after understanding the query.
2. Cloud upload uses the independent base CSV, so later database corrections cannot change its expectations. Check all seven column types and header handling before comparing aggregates.
3. In BigQuery Explorer choose Create dataset under your project, then Create table under the dataset; source Upload, file weather_base.csv, format CSV. Use an explicit schema rather than trusting autodetection blindly. UI wording can change; the local-loading documentation is linked in the lesson.
4. Use the console's generated fully qualified table reference in your SQL. A PostgreSQL schema/table name is not a BigQuery project/dataset/table reference.
5. Convert observed_at to the named local date for reporting. Group by city or date, not the entire timestamp. NULL remains unknown; do not fill missing temperatures with0.
6. Record estimated and actual processed bytes even if the dataset is tiny; the goal is learning where cost evidence appears, not demonstrating a meaningful performance gain.
7. If no sandbox is available, stop the cloud setup and finish the same fixed-data aggregates locally from the CSV. Mark the proposed GoogleSQL as unexecuted.

## GoogleSQL date syntax

Run this constant expression in BigQuery:

~~~sql
SELECT DATE(TIMESTAMP '2026-09-17 18:30:00+00', 'Asia/Ho_Chi_Minh') AS local_date;
~~~

Expected local_date is2026-09-18. For an aggregate, select city and COUNT(*), use the console's fully qualified table reference after FROM, then GROUP BY city. BigQuery encloses project.dataset.table in backtick characters; PostgreSQL uses different identifier quoting.
