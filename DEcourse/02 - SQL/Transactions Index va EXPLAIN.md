---
tags: [decourse, sql, database]
module: 10
---

# Transactions, Index và EXPLAIN

## Khi dùng

Transaction gộp các thay đổi DB thành một đơn vị; index hỗ trợ một số access pattern; EXPLAIN giúp biết engine thực sự đọc/join/sort gì. Không áp nguyên kết luận của Postgres sang DuckDB/BigQuery.

## Transaction — DuckDB chạy độc lập

```sql
-- runnable
-- expect: [[1, 100], [2, 0]]
CREATE TABLE account(id INTEGER PRIMARY KEY, balance INTEGER);
INSERT INTO account VALUES (1,100), (2,0);
BEGIN TRANSACTION;
UPDATE account SET balance = balance - 10 WHERE id = 1;
UPDATE account SET balance = balance + 10 WHERE id = 2;
ROLLBACK;
SELECT * FROM account ORDER BY id;
-- Expected: (1,100), (2,0): không có nửa giao dịch.
```

ACID không tự làm DB và Parquet chung transaction. Caller vẫn cần rollback khi lỗi; transaction dài có thể giữ lock và ảnh hưởng người đọc/ghi khác tùy engine/isolation.

## PostgreSQL upsert — pattern cần database

```sql
-- PostgreSQL; tạo bảng trong schema lab trước khi thực hành.
CREATE TABLE lab_orders(order_id text PRIMARY KEY, version bigint, amount numeric(12,2));
INSERT INTO lab_orders VALUES ('o1',2,120)
ON CONFLICT (order_id) DO UPDATE
SET version = EXCLUDED.version, amount = EXCLUDED.amount
WHERE EXCLUDED.version > lab_orders.version;
```

Gửi version 1 sau version 2; amount phải giữ 120. Version bằng nhau nhưng nội dung khác cần quy tắc conflict; không coi ON CONFLICT là lời giải mọi đồng thời.

## Query plan — PostgreSQL

```sql
-- Pattern; ANALYZE thực thi query. Dùng SELECT và fixture lab.
EXPLAIN (ANALYZE, BUFFERS)
SELECT order_id, amount FROM lab_orders WHERE order_id = 'o1';
```

So estimated/actual rows, scan, join, sort, buffers. Table nhỏ có sequential scan dù có index là bình thường. Index tăng storage và chi phí write; benchmark cùng dữ liệu, warm/cold cache và truy vấn.

## Lab hai session

Session A BEGIN rồi UPDATE một key chưa commit; session B update cùng key và quan sát chờ. Commit A, quan sát B; thử deadlock trên hai key ngược thứ tự ở lab. Tìm blocking PID bằng pg_stat_activity, không kill process dùng chung tùy tiện.

## Ôn

Atomic khác isolation thế nào? Reader có thể thấy hai bảng mart thuộc hai lần publish khác nhau không? Vì sao DROP/CREATE có thể mất index và grant?

Liên quan: [[Docker PostgreSQL va Serving]], [[Delivery va Reproducibility]]. Nguồn: [Postgres isolation](https://www.postgresql.org/docs/current/transaction-iso.html), [EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html).
