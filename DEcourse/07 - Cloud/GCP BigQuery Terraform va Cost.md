---
tags: [decourse, cloud, gcp]
module: 14
---

# GCP, BigQuery, Terraform và Cost

## Khi dùng

Cloud cho storage/compute dùng chung, IAM và dịch vụ quản lý; Terraform khai báo hạ tầng tái lập. Chọn một cloud cho vòng đầu, hiểu khái niệm trước khi học thêm tên dịch vụ.

| Lớp | GCP | Khái niệm chuyển sang cloud khác |
|---|---|---|
| Object storage | GCS | Bucket/object, version, lifecycle |
| Warehouse | BigQuery | Dataset/table, partition/cluster, compute billing |
| Identity | IAM/service account | Principal, role, scope |
| IaC | Terraform | Plan/state/provider/remote backend |

## Pattern BigQuery cost control — cần SDK và quyền

```python
# Pattern tích hợp: project/dataset/table phải thay bằng tài nguyên lab của bạn.
from google.cloud import bigquery
client = bigquery.Client()
sql = '''SELECT order_date, SUM(payment_total) AS payments
FROM `my-project.olist_marts.fct_orders`
WHERE order_date >= DATE '2018-01-01' AND order_date < DATE '2018-02-01'
GROUP BY order_date'''
dry = client.query(sql, job_config=bigquery.QueryJobConfig(dry_run=True, use_query_cache=False))
print(dry.total_bytes_processed)
# Chỉ chạy thật sau khi đọc estimate và chọn ngưỡng phù hợp.
config = bigquery.QueryJobConfig(maximum_bytes_billed=100_000_000)
# rows = client.query(sql, job_config=config).result()
```

Ngưỡng ví dụ không bảo đảm đủ cho bảng thật. LIMIT chỉ giới hạn kết quả, không bảo đảm giảm bytes scan. Budget alert là thông báo, không tự tắt mọi chi tiêu; kết hợp quota/bytes cap, partition filter và kiểm tra tài nguyên.

## Terraform — pattern HCL

```hcl
# Pattern, cần provider và biến project_id trong module lab.
resource "google_bigquery_dataset" "marts" {
  project    = var.project_id
  dataset_id = "olist_marts"
  location   = "asia-southeast1"
}
```

`terraform init` tải provider; `plan` hiển thị thay đổi; `apply` tạo tài nguyên thật. State có thể chứa dữ liệu nhạy cảm; không commit state/credential. Khi làm nhóm cần remote backend và locking. Chỉ destroy tài nguyên lab do mình quản lý, xem plan trước và kiểm tra resource còn lại; hóa đơn có thể cập nhật trễ.

## Bài tối thiểu

Một bucket/dataset bằng IaC, một mart load từ Parquet, reader/writer role, query có partition filter, dry run và bytes cap. Port toàn bộ dbt, Snowflake trial và cloud thứ hai là mở rộng.

Ôn: partitioning khác clustering? Vì sao location của bucket/dataset ảnh hưởng load? Làm sao biết reader không vô tình có quyền Owner?

Liên quan: [[Security va Governance]], [[Performance va Storage]]. Nguồn: [BigQuery cost](https://docs.cloud.google.com/bigquery/docs/best-practices-costs), [Terraform GCP](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started).
