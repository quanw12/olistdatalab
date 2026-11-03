---
tags: [decourse, sql, incremental]
module: 09
---

# CTE, Dedup và Incremental SQL

## Khi dùng

CTE đặt tên cho từng bước logic; không tự bảo đảm materialize hay nhanh hơn. Dedup chọn version đúng theo key; incremental giảm phần dữ liệu xử lý, cần semantics cho update/delete và lịch sử.

## Latest version — DuckDB chạy độc lập

```sql
-- runnable
-- expect: [["o1", 120]]
WITH events(order_id, version, amount, is_deleted) AS (
    VALUES ('o1',1,100,false), ('o1',2,120,false),
           ('o2',1,50,false), ('o2',2,50,true)
), ranked AS (
    SELECT *, row_number() OVER (PARTITION BY order_id ORDER BY version DESC) AS rn
    FROM events
)
SELECT order_id, amount FROM ranked
WHERE rn = 1 AND NOT is_deleted ORDER BY order_id;
-- Expected: chỉ ('o1',120).
```

Phải chọn latest **trước khi** lọc delete. Nếu lọc tombstone trước ranking, o2 sống lại từ version cũ. Tie version cần event id/sequence và quy tắc xử lý conflict.

## Pattern watermark cần tích hợp

```sql
-- Pattern: :lower và :upper do caller bind, không ghép input tùy ý vào SQL.
SELECT * FROM source_orders
WHERE updated_at >= :lower AND updated_at < :upper;
```

Postgres/driver có placeholder khác; đây là pattern logic. Interval nửa mở giúp batch liền nhau không overlap biên. Lookback có overlap vẫn cần dedup/upsert; timestamp bằng nhau cần tie-breaker. Hard delete cần nguồn thông báo hoặc snapshot diff.

## Kiểm chứng incremental

```sql
-- Pattern: tạo hai bảng cùng schema trước, query phải trả 0 dòng ở cả hai chiều.
SELECT * FROM incremental_result EXCEPT ALL SELECT * FROM full_result;
SELECT * FROM full_result EXCEPT ALL SELECT * FROM incremental_result;
```

Chỉ so tổng tiền có thể bỏ sót chuyển tiền nhầm order. So sánh theo key/column và semantics NULL/decimal. Nếu order_date đổi, aggregate của ngày cũ và mới đều bị ảnh hưởng.

## Tự luyện và ôn

Replay events ba lần, thêm update của đơn cũ 30 ngày, delete, đổi ngày và cùng timestamp. Viết expected bằng tay trước. Khi nào full rebuild đơn giản và đáng tin hơn một incremental phức tạp?

Liên quan: [[Incremental CDC Backfill]], [[dbt Models Tests va Incremental]]. Nguồn: [DuckDB CTE](https://duckdb.org/docs/stable/sql/query_syntax/with.html), [dbt incremental](https://docs.getdbt.com/docs/build/incremental-models).
