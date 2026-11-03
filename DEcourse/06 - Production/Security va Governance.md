---
tags: [decourse, security, governance]
module: 21
---

# Security và Governance

## Khi dùng

Quyền truy cập và ý nghĩa dữ liệu phải được thiết kế cùng pipeline. Least privilege: mỗi principal có đúng quyền cần; data contract cần owner và chính sách thay đổi, không chỉ schema YAML.

## Ma trận thực hành

| Principal | Raw | Mart | DDL | Secret |
|---|---|---|---|---|
| Ingest writer | Ghi nguồn cần thiết | Không cần | Phạm vi được cấp | Credential source |
| Transform writer | Đọc | Ghi | Schema transform | Credential warehouse |
| BI reader | Không | Đọc được phép | Không | Read-only credential |

## SQL PostgreSQL — pattern lab

```sql
-- Thay tên role theo tài khoản lab đã tạo. Chạy bằng admin có quyền.
GRANT USAGE ON SCHEMA marts TO analyst_reader;
GRANT SELECT ON ALL TABLES IN SCHEMA marts TO analyst_reader;
REVOKE ALL ON SCHEMA bronze FROM analyst_reader;
```

REVOKE một role không loại quyền nhận từ role khác/PUBLIC. Kiểm tra bằng login thật; “đã chạy GRANT” không phải bằng chứng quyền đúng. Sau publish tạo lại bảng kiểm tra lại grant, default privilege và ownership.

## PII và secrets

Email, địa chỉ, review tự do có thể chứa dữ liệu riêng. Dùng PII giả trong lab; mask/loại khỏi mart và logs nếu không cần. Hash không tự biến mọi PII thành dữ liệu ẩn danh; vẫn có khả năng liên kết hoặc dò từ điển.

Credential qua env/secret store phù hợp môi trường; `.env` bỏ khỏi git. Không log DSN chứa password, không commit state Terraform có dữ liệu nhạy cảm. Không gửi raw cho hosted AI chỉ vì API chạy được.

## Data governance tối thiểu

Tên dataset, owner, nguồn, grain, định nghĩa metric, schema version, retention, freshness và quy trình thay đổi. Lineage hỗ trợ biết downstream nào bị ảnh hưởng; không thay data quality test.

## Tự luyện và ôn

Reader SELECT mart thành công, INSERT và đọc raw thất bại. Thêm PII giả và kiểm tra nó không tới dashboard/log. Schema đổi tên cột: ai quyết định, báo ai, chuyển consumer thế nào?

Liên quan: [[Docker PostgreSQL va Serving]], [[LLM Cache Evaluation va Guardrails]]. Nguồn: [Postgres privileges](https://www.postgresql.org/docs/current/ddl-priv.html), [GCP service accounts](https://cloud.google.com/iam/docs/best-practices-service-accounts).
