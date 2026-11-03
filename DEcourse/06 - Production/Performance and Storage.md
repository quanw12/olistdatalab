---
tags: [decourse, performance, storage]
module: 21
---

# Performance and Storage

> [!info] Learning goals
> After this note you can: find the real bottleneck before optimising; apply projection, predicate pushdown and partition pruning; choose a partitioning scheme and avoid the small-files problem; understand compression and encodings in columnar formats; decide between scaling up and scaling out; and run a benchmark that others can trust.

## 1. Measure first

Optimising without measuring usually speeds up the wrong thing. Steps:

1. Define the target (dashboard query < 2 s, nightly run < 30 min).
2. Measure where time goes: query plans ([[Transactions Indexes and EXPLAIN]]), step durations in logs, Spark UI.
3. Change **one** thing; measure again on the same data; keep the semantics identical.

Most data pipelines are bound by **I/O** (reading/writing bytes) or **data movement** (shuffles, network), not by CPU. So the biggest wins come from reading less data.

Olist fits on a laptop. Spark is taught as distributed processing, not because the small dataset needs it.

## 2. Read less data

| Technique | Benefit | Trap |
|---|---|---|
| Projection (select only needed columns) | Columnar formats read only those columns | `SELECT *` multiplies I/O |
| Predicate pushdown | Filters evaluated at the scan; row groups skipped via min/max stats | Functions on columns can block pushdown |
| Partition pruning | Whole partitions (folders) skipped | Filters not on the partition key prune nothing |
| Columnar Parquet | Compression and encoding per column | Many tiny files add overhead |
| Postgres index | Selective lookups | Write and storage cost; not always used |
| Broadcast small dimension | Avoids shuffling the big table | A "small" dimension that is large exhausts memory |

```sql
-- runnable
-- expect: [["o1", 100]]
WITH orders(id, day, amount) AS (
    VALUES ('o1',DATE '2026-01-01',100), ('o2',DATE '2026-02-01',200)
)
SELECT id, amount FROM orders
WHERE day >= DATE '2026-01-01' AND day < DATE '2026-02-01';
-- Expected: only ('o1',100). Read the query plan on real Parquet to confirm pruning.
```

Write filters so the engine can use them: `WHERE day >= DATE '2026-01-01' AND day < DATE '2026-02-01'` can prune; `WHERE strftime(day, '%Y-%m') = '2026-01'` may not.

## 3. Partitioning

Partitioning splits a dataset by a column into separate folders/segments:

```text
fct_orders/order_month=2018-01/part-0.parquet
fct_orders/order_month=2018-02/part-0.parquet
```

Choosing the key:

- Use the column most queries filter on (usually a date).
- Aim for partitions of a healthy size: roughly 100 MB – 1 GB of Parquet per partition in distributed systems. Too many partitions (e.g., partition by `customer_id`) creates **millions of tiny files**: listing and opening files then dominates the runtime and metadata overhead explodes.
- Daily partitions for small data often produce small files; monthly may be better. Compact small files periodically.
- **Clustering/sorting** within partitions (BigQuery clustering, Z-ordering, sorted Parquet) improves min/max skipping for a second column.

Partitioning also enables idempotent **partition overwrite** for incremental loads and backfills ([[Incremental CDC and Backfill]]).

## 4. Compression and encoding

Parquet compresses each column chunk (Snappy: fast; ZSTD: smaller; GZIP: small but slow) and encodes values (dictionary encoding for repeated strings, run-length encoding for runs of equal values). Low-cardinality, sorted columns compress extremely well. Smaller files usually mean less I/O, but heavier codecs cost CPU — a smaller file is not always a faster query.

```python
# runnable
import pandas as pd
from pathlib import Path
from tempfile import TemporaryDirectory

df = pd.DataFrame({"state": ["SP"] * 50_000 + ["RJ"] * 50_000, "amount": range(100_000)})
with TemporaryDirectory() as directory:
    csv_path, pq_path = Path(directory) / "a.csv", Path(directory) / "a.parquet"
    df.to_csv(csv_path, index=False)
    df.to_parquet(pq_path, index=False)
    assert pq_path.stat().st_size < csv_path.stat().st_size       # columnar + compressed
    print(f"csv {csv_path.stat().st_size:,} bytes vs parquet {pq_path.stat().st_size:,} bytes")
    assert pd.read_parquet(pq_path, columns=["state"]).shape == (100_000, 1)
```

## 5. Scale up or scale out?

- **Scale up** (bigger machine, DuckDB/Polars on 32 cores and 128 GB RAM) is simpler, cheaper to operate and handles hundreds of GB.
- **Scale out** (Spark, BigQuery, distributed clusters) is needed when data or concurrency exceed one machine, but adds shuffles, skew, cluster management and cost ([[Spark Partitions Shuffle and Skew]]).

Choose the simplest option that meets the target with headroom.

## 6. Trustworthy benchmarks

Record: input size and row count, machine (CPU, RAM, disk), threads/memory limits, engine and version, the exact query, the plan, wall time, and bytes read. Warm up and repeat several runs; report median and spread. **Check outputs are identical before comparing speed** — a faster query with different NULL handling or rounding is not faster, it is wrong. Sampling and approximate aggregates trade accuracy for speed; state it.

For Spark experiments, generate data with a realistic key distribution. Duplicating the same IDs many times does not create a valid larger dataset — it creates artificial skew and broken keys.

## 7. Applying it to Olist

Compare CSV vs Parquet on the same data, reading only 3 columns; partition `fct_orders` by month and confirm pruning in the plan; record a benchmark with the template above.

## 8. Common mistakes

| Mistake | Effect | Fix |
|---|---|---|
| Optimising without a profile | Wasted effort | Measure, then change one thing |
| `SELECT *` on wide tables | Excess I/O | Select needed columns |
| Partitioning by high-cardinality keys | Small-files explosion | Date/month partitions, compaction |
| Functions on filter columns | No pruning | Rewrite as range predicates |
| Comparing engines with different semantics | Misleading results | Verify identical outputs first |
| Jumping to a cluster | Complexity and cost | Scale up first |

## 9. Exercises

1. CSV vs Parquet on 1M rows: compare size and time to read 3 columns.
2. Partition a table by day and by month; compare file counts and query time for a one-month filter.
3. Write the same filter two ways (range vs function on the column) and compare the plans.
4. When is scaling up simpler than going distributed? Give numbers for your machine.

## 10. Review questions

> [!question]- How does high partition cardinality create small files?
> Each partition gets at least one file; with thousands or millions of partition values, data is spread into many tiny files, and file listing/opening overhead dominates.

> [!question]- Is a more compressed file always faster to query?
> No. Heavier codecs cost CPU to decompress; the best trade-off depends on I/O vs CPU limits.

> [!question]- Why check outputs before comparing speed?
> Different semantics (NULL handling, rounding, filters) can make one query faster only because it computes something else.

Related: [[Transactions Indexes and EXPLAIN]], [[Spark Partitions Shuffle and Skew]], [[GCP BigQuery Terraform and Cost]], [[Files CSV JSON and Parquet]]. Sources: [DuckDB Parquet](https://duckdb.org/docs/stable/data/parquet/overview.html), [Spark SQL performance tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html), [Parquet file format](https://parquet.apache.org/docs/file-format/).
