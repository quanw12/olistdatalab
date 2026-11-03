---
tags: [decourse, performance, storage]
module: 12
---

# Performance và Storage

## Khi dùng

Tối ưu sau khi đo bottleneck và giữ semantics. Olist vừa một laptop; Spark là bài học distributed processing, không phải điều kiện để dataset nhỏ chạy nhanh.

| Ý tưởng | Lợi ích | Bẫy |
|---|---|---|
| Projection | Đọc ít cột | SELECT * tăng I/O |
| Partition pruning | Bỏ partition không cần | Filter không dùng partition key |
| Columnar Parquet | Scan/encode/nén theo cột | Nhiều file nhỏ gây overhead |
| Index Postgres | Tìm/selective lookup | Tốn write/storage, không luôn được dùng |
| Broadcast dimension | Tránh shuffle bảng lớn | Dimension quá lớn làm hết RAM |

## Filter/projection — DuckDB chạy độc lập

```sql
-- runnable
-- expect: [["o1", 100]]
WITH orders(id, day, amount) AS (
    VALUES ('o1',DATE '2026-01-01',100), ('o2',DATE '2026-02-01',200)
)
SELECT id, amount FROM orders
WHERE day >= DATE '2026-01-01' AND day < DATE '2026-02-01';
-- Expected: chỉ ('o1',100). Đọc query plan trên Parquet thật để xác minh pruning.
```

## Benchmark có ích

Ghi input size/rows, machine, threads/memory, engine/version, query, plan, wall time và bytes read. Warm-up và lặp vài lần để tránh kết luận từ một run nhiễu. Kiểm tra output giống nhau trước so tốc độ; sampling/approximate aggregate có trade-off accuracy.

## Tự luyện và ôn

CSV vs Parquet trên cùng dữ liệu, chỉ đọc 3 cột. Với Spark nếu chọn nhánh: sinh phân bố key lệch, quan sát skew/shuffle và file count. Không chỉ nhân đôi cùng ID rồi gọi đó là dataset hợp lệ lớn hơn.

Khi nào scale-up đơn giản hơn distributed? Partition cardinality quá cao tạo small files như thế nào? Compression file nhỏ hơn có luôn query nhanh hơn không?

Liên quan: [[Transactions Index va EXPLAIN]], [[Spark Partitions Shuffle va Skew]], [[GCP BigQuery Terraform va Cost]]. Nguồn: [DuckDB Parquet](https://duckdb.org/docs/stable/data/parquet/overview.html), [Spark tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html).
