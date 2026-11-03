---
tags: [decourse, sql, analytics]
module: 03
---

# Aggregation và Window Functions

> [!info] Nội dung
> GROUP BY, COUNT/SUM/AVG, OVER/PARTITION/ORDER/frame, running total, moving average, ranking, LAG, dedup và retention.

## Aggregate làm gộp dòng

```sql
-- runnable
-- expect: [["A", 2, 30, 15.0], ["B", 1, 30, 30.0]]
WITH sales(seller, day, amount) AS (
    VALUES ('A', DATE '2026-01-01', 10), ('A', DATE '2026-01-02', 20),
           ('B', DATE '2026-01-01', 30)
)
SELECT seller, count(*) AS n, sum(amount) AS revenue, avg(amount) AS average
FROM sales GROUP BY seller HAVING sum(amount) >= 30 ORDER BY seller;
-- Expected: A,2,30,15.0; B,1,30,30.0.
```

COUNT(col) không đếm NULL; MIN/MAX trên text không phải thứ tự trạng thái nghiệp vụ. WHERE lọc trước aggregate, HAVING lọc nhóm sau aggregate.

## Window giữ từng dòng

```sql
-- runnable
-- expect: [["2026-01-01", 10, 10, 10.0, null], ["2026-01-02", 20, 30, 15.0, 10], ["2026-01-03", 30, 60, 25.0, 20]]
WITH daily(day, revenue) AS (
    VALUES (DATE '2026-01-01', 10), (DATE '2026-01-02', 20),
           (DATE '2026-01-03', 30)
)
SELECT day, revenue,
       sum(revenue) OVER (ORDER BY day ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running,
       avg(revenue) OVER (ORDER BY day ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS moving_2_rows,
       lag(revenue) OVER (ORDER BY day) AS previous
FROM daily ORDER BY day;
-- Expected running: 10,30,60; moving: 10,15,25; previous: NULL,10,20.
```

`PARTITION BY seller` tính riêng mỗi seller; khác GROUP BY vì không giảm số dòng. Hai dòng cùng ORDER BY key cần tie-breaker nếu thứ tự ảnh hưởng kết quả.

## ROWS và RANGE

ROWS đếm số dòng; RANGE dùng miền giá trị và có thể bao gồm các peer cùng key. Moving average 7 dòng chỉ là 7 ngày nếu đã có đúng một dòng mỗi ngày, kể cả ngày không có giao dịch. Tạo date spine trước khi gọi nó là “7-day average”. LAST_VALUE với frame mặc định thường không phải giá trị cuối partition; khai báo frame tới UNBOUNDED FOLLOWING khi đó là yêu cầu.

## Ranking và top N

```sql
-- runnable
-- expect: [["A", 1, 1, 1], ["B", 2, 1, 1], ["C", 3, 3, 2]]
WITH scores(seller, revenue) AS (VALUES ('A',100), ('B',100), ('C',50))
SELECT seller,
       row_number() OVER (ORDER BY revenue DESC, seller) AS row_n,
       rank() OVER (ORDER BY revenue DESC) AS rank_n,
       dense_rank() OVER (ORDER BY revenue DESC) AS dense_n
FROM scores ORDER BY seller;
-- Expected: A 1,1,1; B 2,1,1; C 3,3,2.
```

Top 10 dòng khác top 10 mức doanh thu; xác định có giữ ties không. Dedup dùng ROW_NUMBER theo business key và version; xem [[CTE Dedup va Incremental SQL]].

## Month-over-month và retention — pattern cần bảng

```sql
-- Pattern: monthly đã có đúng một dòng mỗi tháng, kể cả tháng 0 doanh thu.
WITH compared AS (
    SELECT month, revenue, lag(revenue) OVER (ORDER BY month) AS previous
    FROM monthly
)
SELECT month, (revenue - previous) / NULLIF(previous, 0) AS growth
FROM compared;
```

Retention cần người dùng duy nhất theo cohort và kỳ hoạt động. COUNT(order_id) là số đơn, không phải số người quay lại; mẫu số cohort phải cố định và phân biệt kỳ chưa quan sát đủ.

## Ứng dụng và tự luyện

Olist: doanh thu theo tháng, seller rank trong state, khách mua lại theo customer_unique_id. Tự thêm ngày thiếu và seller đồng hạng; dự đoán kết quả ROWS/RANGE và rank trước khi chạy.

Ôn: OVER khác GROUP BY thế nào? LAG của tháng trước khác “dòng trước” khi thiếu tháng ra sao? Khi nào window function gây sort/shuffle lớn?

Nguồn: [DuckDB window functions](https://duckdb.org/docs/stable/sql/functions/window_functions.html), [Postgres window tutorial](https://www.postgresql.org/docs/current/tutorial-window.html).
