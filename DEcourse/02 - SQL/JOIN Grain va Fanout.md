---
tags: [decourse, sql, modeling]
module: 03
---

# JOIN, Grain và Fan-out

> [!info] Trước khi JOIN
> Viết một dòng nghĩa là gì và khóa nào duy nhất ở mỗi bảng. JOIN thành công về syntax có thể vẫn nhân tiền.

## Ví dụ sai — DuckDB chạy độc lập

```sql
-- runnable
-- expect: [[4, 200]]
WITH orders(id) AS (VALUES ('o1')),
items(order_id, item_id) AS (VALUES ('o1', 1), ('o1', 2)),
payments(order_id, amount) AS (VALUES ('o1', 60), ('o1', 40))
SELECT count(*) AS joined_rows, sum(p.amount) AS wrong_total
FROM orders o
JOIN items i ON o.id = i.order_id
JOIN payments p ON o.id = p.order_id;
-- Expected: 4 dòng, tổng sai = 200; payment thật chỉ 100.
```

Hai quan hệ 1-n tạo tích số dòng theo từng parent. DISTINCT sau khi aggregate không chữa được; SUM(DISTINCT amount) cũng sai khi hai payment hợp lệ cùng giá trị.

## Cách đúng: pre-aggregate theo grain đích

```sql
-- runnable
-- expect: [["o1", 2, 100], ["o2", null, null]]
WITH orders(id) AS (VALUES ('o1'), ('o2')),
items(order_id, item_id) AS (VALUES ('o1', 1), ('o1', 2)),
payments(order_id, amount) AS (VALUES ('o1', 60), ('o1', 40)),
item_summary AS (
    SELECT order_id, count(*) AS item_count FROM items GROUP BY order_id
),
payment_summary AS (
    SELECT order_id, sum(amount) AS payment_total FROM payments GROUP BY order_id
)
SELECT o.id, i.item_count, p.payment_total
FROM orders o
LEFT JOIN item_summary i ON o.id = i.order_id
LEFT JOIN payment_summary p ON o.id = p.order_id
ORDER BY o.id;
-- Expected: ('o1',2,100), ('o2',NULL,NULL).
```

## Chọn JOIN

INNER bỏ parent không match; LEFT giữ parent. Đặt `WHERE right.status='x'` sau LEFT có thể loại các dòng không match; nếu muốn giữ parent, cân nhắc điều kiện trong ON hoặc chính sách NULL rõ.

## Ứng dụng và kiểm chứng

Olist: orders, order_items và order_payments có grain khác nhau. Test row count fact bằng orders, unique order_id và tổng payment bằng nguồn. Geolocation có nhiều điểm cùng zip: chọn chính sách aggregate trước khi nối dimension, không tùy tiện chọn một dòng.

## Tự luyện và ôn

Thêm hai payment cùng 50; chứng minh SUM(DISTINCT) sai. Thêm orphan payment và viết anti-join tìm nó. Vì sao đối soát tổng tiền vẫn chưa chứng minh mọi order đều được gán đúng tiền?

Liên quan: [[Data Modeling va SCD2]], [[Aggregation va Window Functions]], [[Testing Logging va CI]]. Nguồn: [Postgres joins](https://www.postgresql.org/docs/current/queries-table-expressions.html).
