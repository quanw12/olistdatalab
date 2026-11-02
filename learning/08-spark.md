# 08 · Spark and big data

**Time:** weeks 10–11 · **Stack:** PySpark, Spark SQL, partitioning, Delta Lake; Hadoop/HDFS/Hive concepts; Databricks

## Why
When data no longer fits on one machine, Spark is the default engine (Databricks, EMR, Dataproc).
Even if your first job uses a warehouse, interviews ask how Spark executes work.

## Learn
- Driver/executors, partitions, lazy evaluation, transformations vs actions
- Narrow vs wide transformations, shuffle, `explain()`, skew, broadcast joins
- File layout: partitioned Parquet, small-files problem, Delta Lake (ACID on Parquet, time travel)
- History: HDFS + MapReduce + Hive metastore → why object storage + Spark + table formats replaced them
- [Spark SQL guide](https://spark.apache.org/docs/latest/sql-programming-guide.html), Databricks Community/Free Edition

## Setup
PySpark needs Java 17 (`java -version`). On Windows, writing files needs Hadoop `winutils`; the
easiest path is to run Spark inside WSL2 or Docker (`docker run -it -v ${PWD}:/work apache/spark-py`).
`pip install -e ".[spark]"`, then `python spark/customer_rfm.py --lake data/lake`.

## Read in this repo
- `spark/customer_rfm.py` — group by, window `ntile`, partitioned write.

## Build
1. Run the RFM job on the real data. Print `rfm.explain(True)`; find the shuffle (Exchange) and explain it.
2. Write the same RFM in dbt/DuckDB SQL. **Check:** identical segment counts.
3. Spark job #2: seller × category monthly revenue from `fct_order_items`, written partitioned by
   `year_month`. Compare file count with and without `repartition`/`coalesce`.
4. Join a small dimension with `broadcast()`; compare the plan.
5. Write the RFM output as a **Delta** table (`delta-spark`), overwrite once, then query the
   previous version with time travel.
6. Run the notebook version on Databricks Free Edition (upload the gold Parquet).

## Break it
- Set `spark.sql.shuffle.partitions=1` vs `200` on the real data; time both and explain.
- Create skew: give 50% of rows the same key, watch one task take all the time in the Spark UI (http://localhost:4040).

## Interview questions
- What triggers a shuffle? How do you reduce one?
- `repartition` vs `coalesce`?
- Why are many small files bad?
- When would you not use Spark?

## Done when
- [ ] RFM on real data, plan explained, SQL version matches
- [ ] Partitioned job + Delta time travel done, notes on file counts
