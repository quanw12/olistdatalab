# 12 · Apache Spark

> **Theory notes:** [[Spark Partitions Shuffle and Skew]] · [[Performance and Storage]] · **Route:** [[Roadmap]] · **Labs:** [[Labs Guide]]. Videos are optional: use the diagnostic test to decide what to watch.

**Weeks:** 26–28 · elective branch · **Prerequisites:** 04, 05, 10

## Goal
Process data that does not fit one machine: DataFrames in PySpark, partitions and shuffles,
reading query plans, partitioned output, Delta Lake; know where Hadoop/Hive fit historically.

## 1. Watch
| Video | What to watch | Length |
|---|---|---|
| [What is Spark? (Visual Explanation) — Data with Baraa](https://www.youtube.com/watch?v=nKRwjXRs4mY) | First | 12 min |
| [PySpark Tutorial: Full Course (Zero to Pro) — Ansh Lamba](https://www.youtube.com/watch?v=94w6hPk7nkM) | Main course | 5 h 54 |
| [Apache Spark Architecture — Explained — Databricks For Professionals](https://www.youtube.com/watch?v=iXVIPQEGZ9Y) | Driver, executors, stages, tasks | 1 h 15 |
| [Spark Basics: Partitions](https://www.youtube.com/watch?v=hvF7tY2-L3U) and [Shuffling — Palantir](https://www.youtube.com/watch?v=ffHboqNoW_A) | Short and precise | 11 min |
| [Shuffle Partition Spark Optimization — Afaque Ahmad](https://www.youtube.com/watch?v=q1LtBU_ca20) | Week 22 | 19 min |
| [Delta Lake — The Ultimate Guide — Ansh Lamba](https://www.youtube.com/watch?v=HQvAl0Bwpu8) | First hour | 3 h 16 |
| [Databricks Live Bootcamp Day 2: Data Engineering — Data with Baraa](https://www.youtube.com/watch?v=ldBLOasG23w) | Optional: Spark on Databricks | 4 h 10 |

## 2. Read
- [Spark SQL & DataFrames guide](https://spark.apache.org/docs/latest/sql-programming-guide.html) · [PySpark API](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/index.html)
- [Spark performance tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html)
- [Delta Lake quickstart](https://docs.delta.io/latest/quick-start.html)
- Concepts only: [HDFS architecture](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html), [Hive](https://hive.apache.org/) — what object storage + Spark + table formats replaced

## 3. Syntax sheet
```python
from pyspark.sql import SparkSession, Window, functions as F

spark = SparkSession.builder.appName("x").master("local[*]").getOrCreate()
df = spark.read.parquet("data/lake/gold/fct_orders.parquet")    # lazy
df.printSchema()

out = (df.where(F.col("order_status") == "delivered")
         .groupBy("customer_state")
         .agg(F.count("*").alias("orders"), F.avg("delivery_days").alias("avg_days")))
out.show(5)                                  # action: now it runs
out.explain(True)                            # look for "Exchange" = shuffle

w = Window.partitionBy("customer_state").orderBy(F.desc("payment_total"))
ranked = df.withColumn("rank", F.row_number().over(w))

small = spark.read.parquet("dim.parquet")
joined = df.join(F.broadcast(small), "seller_id")   # no shuffle of the big side

out.write.mode("overwrite").partitionBy("customer_state").parquet("out/")
spark.sql("SELECT count(*) FROM parquet.`out/`").show()
```

## 4. Setup (do this first)
PySpark 3.5 needs Java 8/11/17. On Windows, writing files needs Hadoop `winutils`; simplest is
to run Spark **inside WSL2**: `sudo apt install openjdk-17-jdk`, then
`pip install -e ".[spark]"` in a Linux venv. Spark UI: http://localhost:4040 while a job runs.

## 5. Apply to the project
1. Practice on `fct_orders.parquet` (after `olist run`): the syntax-sheet queries, then read
   `explain()` and find each shuffle.
2. Write **your own** RFM job in `labs/12-spark/my_rfm.py` before reading `spark/customer_rfm.py`:
   per `customer_unique_id`: days since last order, number of orders, total paid; score each
   1–5 with `F.ntile(5)` over a window; map scores to 4–6 segment names you define.
3. Same RFM in DuckDB SQL. **Check:** identical counts per segment.
4. Partitioned write by `customer_state`: count output files with and without
   `repartition("customer_state")`. Explain the small-files problem.
5. Broadcast vs normal join of `fct_order_items` with `dim_products`: compare plans and times.
6. Write RFM as a Delta table (`pip install delta-spark`), overwrite it, read the previous
   version with time travel (`versionAsOf`).

## 6. Self-check
- Transformation vs action? Why is Spark lazy?
- What triggers a shuffle and why is it expensive?
- `repartition` vs `coalesce`?
- When is Spark the wrong tool? (Hint: the whole Olist dataset fits in DuckDB.)

## Done when
- [ ] Your RFM matches the SQL version; plans explained in notes
- [ ] Partitioning + Delta time travel demonstrated

## Product-focused requirements

Small Olist data does not prove distributed scale. If you choose Spark as your main extension: generate data with valid IDs and a fixed seed sized to your RAM, create skew, read the plan/UI and measure shuffle, task imbalance and file count; compare semantics with DuckDB before benchmarking. Java/Spark/Delta need compatible versions that you record. This branch is not required for the core.
