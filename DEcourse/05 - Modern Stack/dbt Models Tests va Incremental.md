---
tags: [decourse, dbt, transformation]
module: 09
---

# dbt: Models, Tests và Incremental

## Khi dùng

dbt tổ chức SQL thành dependency graph với tests/docs. `source()` trỏ nguồn, `ref()` khai báo phụ thuộc và tên relation theo môi trường. Nó không tự biết metric nghiệp vụ đúng hay dữ liệu nguồn đầy đủ.

## Syntax — pattern trong project dbt

```sql
-- Pattern: models/staging/stg_payments.sql; cần source bronze.order_payments.
select order_id, payment_value::decimal(12,2) as amount
from {{ source('bronze', 'order_payments') }}
```

```sql
-- Pattern: singular test trả về dòng vi phạm, 0 dòng là pass.
select order_id, count(*) as n
from {{ ref('fct_orders') }}
group by order_id having count(*) <> 1
```

| Materialization | Chọn khi | Chi phí |
|---|---|---|
| view | Logic nhẹ, muốn đọc mới | Tính lại lúc query |
| table | Đọc nhiều, rebuild vừa sức | Storage/rebuild |
| incremental | Input lớn, xác định changes đúng | Watermark/delete/backfill phức tạp |
| ephemeral | CTE dùng trong downstream | SQL compile có thể lớn |

## Lệnh — từ thư mục dbt, cùng venv

```bash
dbt debug --profiles-dir .
dbt build --profiles-dir .
dbt build --profiles-dir . --select fct_orders+
dbt test --profiles-dir . --select fct_orders --store-failures
dbt docs generate --profiles-dir .
```

Repo có `olist transform` điều phối build và export. Nếu gọi dbt trực tiếp, kiểm tra DUCKDB_PATH để không chạy nhầm warehouse.

## Incremental đúng hơn “chạy hai lần không đổi”

`is_incremental()` và unique_key không tự bắt update cũ. Daily mart nhìn lại 3 ngày theo order_date bỏ sót order cũ sửa hôm nay; delete hết dữ liệu một ngày có thể để aggregate cũ nếu strategy chỉ xóa key còn xuất hiện trong batch mới.

Học module 19: theo dõi affected keys/partitions, rebuild đúng phạm vi, full-refresh làm đối chứng. Không sửa historical data bằng tăng lookback tùy ý mà chưa hiểu nguồn.

## Ứng dụng và tự luyện

Module 09 chạy Olist thật sớm: counts nguồn/fact, cent reconciliation, key tests, docs lineage. Đổi một order cũ hơn 30 ngày rồi so daily mart incremental và full-refresh. Snapshot thử SCD2 với nguồn changes mô phỏng.

Ôn: ref() cho gì ngoài tên bảng? Test unique có chứng minh grain đúng không? Phân biệt snapshot dimension và incremental fact.

Liên quan: [[Data Modeling va SCD2]], [[CTE Dedup va Incremental SQL]], [[Incremental CDC Backfill]]. Nguồn: [dbt models](https://docs.getdbt.com/docs/build/models), [incremental](https://docs.getdbt.com/docs/build/incremental-models).
