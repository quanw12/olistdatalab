---
tags: [decourse, sql, foundations]
module: 03
---

# SELECT, NULL và CASE

## Khi dùng

Lọc và phân loại dữ liệu mà không nhầm thiếu giá trị với 0. SQL dùng logic ba giá trị: TRUE, FALSE, UNKNOWN; WHERE chỉ giữ TRUE.

## Ví dụ DuckDB chạy độc lập

```sql
-- runnable
-- expect: [[3, 2, 100, 50.0]]
WITH payments(order_id, amount) AS (
    VALUES ('o1', 100), ('o2', NULL), ('o3', 0)
)
SELECT count(*) AS rows_total,
       count(amount) AS known_amounts,
       sum(amount) AS total,
       avg(amount) AS average_known
FROM payments;
-- Expected: (3, 2, 100, 50.0)
```

COUNT(*) đếm dòng; COUNT(column), SUM và AVG bỏ qua NULL. SUM trên tập rỗng hoặc toàn NULL trả NULL, không mặc định 0.

```sql
-- runnable
-- expect: [["o1", "paid"], ["o2", "missing"], ["o3", "zero"]]
WITH orders(id, amount) AS (VALUES ('o1', 10), ('o2', NULL), ('o3', 0))
SELECT id,
       CASE WHEN amount IS NULL THEN 'missing'
            WHEN amount = 0 THEN 'zero' ELSE 'paid' END AS state
FROM orders
ORDER BY id;
-- Expected: o1 paid; o2 missing; o3 zero.
```

## Syntax tra nhanh

| Nhu cầu | Syntax |
|---|---|
| Thiếu | `x IS NULL` |
| Blank thành NULL | `NULLIF(TRIM(x), '')` |
| Giá trị thay thế có chủ ý | `COALESCE(x, fallback)` |
| Chia tránh lỗi 0 | `numerator / NULLIF(denominator, 0)` |
| Lọc nhóm | `GROUP BY ... HAVING count(*) > 1` |
| Chuỗi thuộc tập | `status IN ('delivered', 'canceled')` |

## Bẫy và ứng dụng

`x = NULL` không phải kiểm tra missing. `NOT IN` có NULL trong tập con có thể làm mất tất cả kết quả mong muốn; cân nhắc NOT EXISTS với điều kiện join rõ. Olist không có payment khác payment bằng 0: giữ NULL và nêu số order thiếu payment trong báo cáo.

## Tự luyện và ôn

Thêm một order bị thiếu amount rồi dự đoán AVG nếu COALESCE về 0. Viết hai query chứng minh cách chọn làm metric thay đổi. Giải thích tại sao WHERE không dùng trực tiếp COUNT(*) mà HAVING dùng được.

Liên quan: [[JOIN Grain va Fanout]], [[BI Metrics va Data Product]]. Nguồn: [Postgres SELECT](https://www.postgresql.org/docs/current/sql-select.html), [DuckDB NULL](https://duckdb.org/docs/stable/sql/data_types/nulls.html).
