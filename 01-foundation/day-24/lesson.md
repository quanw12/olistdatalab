# Day 24 — Warehouses, query plans, and a small cloud lab


## Operational database versus analytical warehouse

A transactional database supports many small reads/writes with constraints and transactions. A warehouse is optimized for analytical scans and aggregation. These are workload tendencies, not a ban on analytics in PostgreSQL. Our small mart works well locally.

Object storage stores objects under keys, rather than giving you relational SQL tables by itself. A data lake keeps files such as JSON/Parquet; a warehouse exposes managed analytical tables. A lakehouse combines lake storage with table-management capabilities. These terms do not replace the need for keys, quality checks and ownership.

## Read a PostgreSQL plan first

~~~sql
EXPLAIN
SELECT city, AVG(temperature_c)
FROM staging.weather_observations
WHERE observed_at >= TIMESTAMPTZ '2026-09-18 00:00:00+00'
GROUP BY city;
~~~

EXPLAIN describes the planned operations. EXPLAIN (ANALYZE, BUFFERS) executes the query and adds runtime statistics; use it only for a query you intend to execute. Start with read-only SELECT.

An index is an additional structure that can speed selective lookup at storage/write cost. A sequential scan may be best for eight rows. Do not claim an index helped merely because you created it. Our key starts with city, so time-only filtering may benefit from a different index at real scale. Today's assignment is reading a plan, not manufacturing a benchmark.

## Partitioning and columnar scans

Partitioning divides a large table by a key such as date. Filtering a partition key can prune irrelevant partitions. Clustering organizes data within storage to help relevant filtering. Selecting fewer columns can reduce scanning in a columnar warehouse. LIMIT alone is not a reliable way to reduce bytes scanned.

GoogleSQL and PostgreSQL are different dialects. BigQuery uses DATE(timestamp_value, 'Asia/Ho_Chi_Minh') for a local date, rather than PostgreSQL's AT TIME ZONE expression. Fully qualified cloud tables include project, dataset and table identifiers.

## Optional BigQuery sandbox

Use only the sandbox for this exercise, without enabling billing. As checked on 2026-10-06, its documented allowance includes10GiB lifetime storage and1TiB query processing per month; tables expire after60 days and DML, streaming and Data Transfer Service are unavailable. Deleting data does not restore the lifetime storage allowance. Recheck [sandbox limits](https://docs.cloud.google.com/bigquery/docs/sandbox) before use.

In the console create a project/dataset, then a table from Upload using ../data/weather_base.csv. Skip its header row and specify seven fields in CSV order: city STRING, observed_at TIMESTAMP, requested_at TIMESTAMP, timezone_name STRING, temperature_c FLOAT64, humidity_pct INT64, source STRING. Use a single region consistently. Eight rows are enough.

Run only SELECT reports: total/min/max/mean; city aggregate; local-date aggregate. Inspect estimated bytes before execution and actual job statistics afterward. You do not need INSERT/MERGE for this sandbox lesson. If sandbox access is unavailable, complete the local plan/design work and label cloud SQL unexecuted.

## Where Spark fits — optional reading

Spark distributes computation across workers. A DataFrame describes structured data; transformations build a plan; actions trigger execution. Grouping/joining can require a shuffle that moves data between partitions. More workers do not automatically improve a tiny job. Eight weather rows do not justify installing Spark this month. Read [Spark SQL introduction](https://spark.apache.org/docs/latest/sql-getting-started.html) and explain when a single machine would become insufficient.

Read: [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html), [BigQuery local loading](https://docs.cloud.google.com/bigquery/docs/loading-data-local).
