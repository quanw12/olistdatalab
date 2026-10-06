# Spark schemas, plans and distributed-processing decisions

## Understand it

Spark distributes computation across partitions. DataFrame transformations build a plan; actions execute it. Joins/grouping may shuffle data, creating network/disk work. Built-in expressions are usually preferable to Python row UDFs. Local mode teaches APIs but does not prove distributed scale. Tiny course fixtures do not need Spark.

## Syntax and trace

~~~python
from pyspark.sql import SparkSession, functions as F
spark = SparkSession.builder.master("local[2]").appName("toy").getOrCreate()
frame = spark.createDataFrame([("c1", 10), ("c1", 20)], "customer_id string, amount_cents long")
report = frame.groupBy("customer_id").agg(F.sum("amount_cents").alias("total_cents"))
report.explain()
report.show()
spark.stop()
~~~

The grouped total is 30. explain displays a plan; show triggers execution. collect would pull all output into driver memory.

## Engineering connection

Select distributed tools from workload/role requirements rather than fixture size.

[Reference](https://spark.apache.org/docs/latest/api/python/getting_started/install.html). Original explanation and exercises; source/version boundaries are in [sources.md](../../sources.md).

