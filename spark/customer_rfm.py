"""PySpark batch job: RFM customer segments from the gold order fact.

Reads data/lake/gold/fct_orders.parquet (written by `olist run`) and writes
data/lake/gold/customer_rfm/ as Parquet partitioned by segment.

Run locally (needs Java 8/11/17):
    pip install -e ".[spark]"
    python spark/customer_rfm.py --lake data/lake

The same code runs on a cluster (Databricks, Dataproc, EMR) with spark-submit; only the paths
change (s3://, gs://, abfss://).

RFM = Recency (days since last order), Frequency (orders), Monetary (total paid).
Each is scored 1-5 by quintile with ntile() over a window, then mapped to a segment.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from pyspark.sql import SparkSession, Window
from pyspark.sql import functions as F


def build_rfm(orders):
    delivered = orders.where(F.col("order_status") == "delivered").where(
        F.col("payment_total").isNotNull()
    )
    snapshot = delivered.agg(F.max("order_date").alias("d")).first()["d"]
    per_customer = delivered.groupBy("customer_unique_id").agg(
        F.datediff(F.lit(snapshot), F.max("order_date")).alias("recency_days"),
        F.countDistinct("order_id").alias("frequency"),
        F.round(F.sum("payment_total"), 2).alias("monetary"),
    )
    # Lower recency is better, so it is ordered descending to give recent buyers a 5.
    scored = (
        per_customer
        .withColumn("r_score", F.ntile(5).over(Window.orderBy(F.desc("recency_days"))))
        .withColumn("f_score", F.ntile(5).over(Window.orderBy("frequency")))
        .withColumn("m_score", F.ntile(5).over(Window.orderBy("monetary")))
    )
    return scored.withColumn(
        "segment",
        F.when((F.col("r_score") >= 4) & (F.col("m_score") >= 4), "champions")
        .when((F.col("r_score") >= 3) & (F.col("f_score") >= 3), "loyal")
        .when(F.col("r_score") >= 4, "new_or_recent")
        .when((F.col("r_score") <= 2) & (F.col("m_score") >= 4), "big_spenders_at_risk")
        .when(F.col("r_score") <= 2, "hibernating")
        .otherwise("needs_attention"),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lake", default="data/lake")
    args = parser.parse_args()
    lake = Path(args.lake).resolve()

    spark = (SparkSession.builder.appName("olist-customer-rfm")
             .master("local[*]")
             .config("spark.sql.shuffle.partitions", "8")
             .getOrCreate())
    orders = spark.read.parquet(str(lake / "gold" / "fct_orders.parquet"))
    rfm = build_rfm(orders)
    out = lake / "gold" / "customer_rfm"
    rfm.write.mode("overwrite").partitionBy("segment").parquet(str(out))
    rfm.groupBy("segment").count().orderBy(F.desc("count")).show()
    spark.stop()


if __name__ == "__main__":
    main()
