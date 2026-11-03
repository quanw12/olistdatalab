---
tags: [decourse, spark, elective]
module: 12
---

# Spark: Partitions, Shuffle và Skew

## Khi dùng

Khi workload cần distributed compute hoặc stack doanh nghiệp dùng Spark. Với Olist nhỏ, DuckDB là baseline; đánh giá Spark qua semantics/plan và thí nghiệm scale, không hứa nó luôn nhanh hơn.

## Pattern PySpark — cần Java và pyspark tương thích

```python
# Pattern standalone sau khi cài Spark/Java; Windows nên dùng WSL cho lab này.
from pyspark.sql import SparkSession, functions as F
spark = SparkSession.builder.master('local[2]').appName('shuffle-lab').getOrCreate()
try:
    df = spark.createDataFrame([('SP',100),('SP',50),('RJ',20)], ['state','amount'])
    result = df.groupBy('state').agg(F.sum('amount').alias('total'))
    result.explain(True)
    assert {r['state']: r['total'] for r in result.collect()} == {'SP':150,'RJ':20}
finally:
    spark.stop()
```

Transformations lazy; actions trigger execution. GroupBy/join/sort có thể tạo Exchange/shuffle. Stage chậm không chỉ do tổng volume; một key hot có thể làm task lệch mạnh.

| Khái niệm | Dùng để | Cần đo |
|---|---|---|
| repartition | Phân phối lại, tăng/giảm partitions | Shuffle và file count |
| coalesce | Thường giảm partitions tránh full shuffle | Mất song song hoặc imbalance |
| broadcast join | Gửi dimension nhỏ tới workers | Memory và size thật |
| AQE | Điều chỉnh plan lúc chạy | Plan cuối, không chỉ config |
| Delta/Iceberg | Table metadata, snapshot, evolution | Compatibility và semantics commit |

## Bài chọn nhánh

RFM cùng kết quả DuckDB; ngày tham chiếu cố định, tie handling rõ. Sinh 1M+ bản ghi có ID khác nhau và key skew có chủ đích theo RAM máy; giữ seed và semantics. So plan/task times trước/sau broadcast hoặc xử lý skew. Đếm file trước/sau partitioning; không partition theo order_id cardinality cao.

## Ôn

Vì sao collect toàn bảng có thể làm driver hết RAM? 100k orders có chứng minh distributed scale không? Làm sao benchmark không bị Python UDF thay native expression làm lệch kết luận?

Liên quan: [[Performance va Storage]], [[DataFrames pandas Polars]]. Nguồn: [Spark SQL](https://spark.apache.org/docs/latest/sql-programming-guide.html), [tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html).
