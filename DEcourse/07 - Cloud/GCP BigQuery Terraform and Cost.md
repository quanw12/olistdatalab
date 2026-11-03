---
tags: [decourse, cloud, gcp]
module: 14
---

# GCP, BigQuery, Terraform and Cost

> [!info] Learning goals
> After this note you can: explain the core cloud building blocks (object storage, warehouse, identity, IaC) in a vendor-neutral way; load Parquet into BigQuery; design partitioned and clustered tables; control query cost with dry runs, bytes caps and partition filters; grant least-privilege access with IAM; write and apply Terraform safely; and clean up resources and verify the bill.

## 1. Cloud building blocks

Learn the concepts once; service names change between providers.

| Layer | GCP | AWS / Azure equivalent | Concept |
|---|---|---|---|
| Object storage | Cloud Storage (GCS) | S3 / Blob Storage | buckets of objects; versioning; lifecycle rules |
| Warehouse | BigQuery | Redshift, Athena / Synapse; Snowflake everywhere | datasets/tables, separated storage and compute |
| Identity | IAM, service accounts | IAM roles / Entra ID | principals, roles, scopes |
| IaC | Terraform | same | declare infrastructure in code: plan → apply |
| Orchestration | Cloud Composer (Airflow) | MWAA / Data Factory | managed scheduler |

Pick one cloud for the first round; understand the concepts before collecting service names.

## 2. BigQuery fundamentals

- **Serverless**: no cluster to size; you pay for **storage** and for **bytes processed** by queries (on-demand pricing) or reserved slots.
- Organisation: project → dataset (has a location, e.g. `asia-southeast1`) → table.
- Columnar storage: selecting fewer columns processes fewer bytes. `SELECT *` on a wide table is expensive.
- Data and processing location must match: loading from a bucket in another region fails or costs egress.

### Partitioning and clustering

```sql
-- BigQuery DDL pattern
CREATE TABLE `my-project.olist_marts.fct_orders`
PARTITION BY order_date                    -- daily partitions on a DATE column
CLUSTER BY customer_state, seller_id       -- sorts data inside partitions
OPTIONS (require_partition_filter = TRUE)  -- reject queries without a partition filter
AS SELECT * FROM `my-project.olist_staging.orders_enriched`;
```

- **Partitioning** splits the table by date (or integer range); a filter on the partition column prunes partitions and reduces billed bytes.
- **Clustering** sorts data within partitions by up to four columns; filters on those columns skip blocks. Benefit appears on larger tables.
- `require_partition_filter` is a guard rail against accidental full scans.

### Loading Parquet

```bash
bq load --source_format=PARQUET olist_marts.fct_orders gs://my-bucket/gold/fct_orders/*.parquet
```

Parquet keeps types, so no schema guessing is needed. Check row counts and money totals after loading, exactly as locally.

## 3. Cost control

```python
# Integration pattern: replace project/dataset/table with your lab resources.
from google.cloud import bigquery
client = bigquery.Client()
sql = '''SELECT order_date, SUM(payment_total) AS payments
FROM `my-project.olist_marts.fct_orders`
WHERE order_date >= DATE '2018-01-01' AND order_date < DATE '2018-02-01'
GROUP BY order_date'''
dry = client.query(sql, job_config=bigquery.QueryJobConfig(dry_run=True, use_query_cache=False))
print(dry.total_bytes_processed)
# Run for real only after reading the estimate and choosing a suitable cap.
config = bigquery.QueryJobConfig(maximum_bytes_billed=100_000_000)
# rows = client.query(sql, job_config=config).result()
```

- **Dry run**: estimates bytes processed without running or billing.
- **`maximum_bytes_billed`**: the query fails instead of running if it would exceed the cap. The example threshold is not guaranteed to fit a real table.
- **`LIMIT` does not reduce bytes scanned** on regular tables — the full columns are read before limiting. Use partition filters and fewer columns.
- **Budget alerts notify; they do not stop spending.** Combine quotas, bytes caps, partition filters and resource checks.
- Preview data with the table preview (free) instead of `SELECT * … LIMIT 10`.

Rough mental math: cost ∝ bytes in the columns you reference × partitions you touch.

## 4. IAM: least privilege

- Use a **service account** per pipeline (loader, transformer), not your personal account.
- Grant **predefined roles at the narrowest scope**: `roles/bigquery.dataViewer` on one dataset for readers; `roles/bigquery.dataEditor` on the target dataset plus `roles/bigquery.jobUser` on the project for writers; `roles/storage.objectViewer` on one bucket.
- Avoid basic roles (`Owner`, `Editor`) — they grant far more than needed.
- Prefer workload identity / short-lived credentials over downloaded JSON keys; if you must use a key, keep it out of Git and rotate it.
- Verify: as the reader, a query works and an INSERT or a query on another dataset fails ([[Security and Governance]]).

## 5. Terraform

Terraform declares infrastructure as code. You describe the desired state; Terraform computes and applies the difference.

```hcl
# Pattern: needs the google provider and a project_id variable in your lab module.
variable "project_id" { type = string }

resource "google_storage_bucket" "lake" {
  project                     = var.project_id
  name                        = "${var.project_id}-olist-lake"
  location                    = "ASIA-SOUTHEAST1"
  uniform_bucket_level_access = true
  lifecycle_rule {
    condition { age = 30 }
    action    { type = "Delete" }
  }
}

resource "google_bigquery_dataset" "marts" {
  project    = var.project_id
  dataset_id = "olist_marts"
  location   = "asia-southeast1"
}

resource "google_bigquery_dataset_iam_member" "reader" {
  project    = var.project_id
  dataset_id = google_bigquery_dataset.marts.dataset_id
  role       = "roles/bigquery.dataViewer"
  member     = "serviceAccount:bi-reader@${var.project_id}.iam.gserviceaccount.com"
}
```

Workflow:

```bash
terraform init      # download providers, configure the backend
terraform fmt && terraform validate
terraform plan -out tfplan   # show exactly what will change — read it!
terraform apply tfplan       # create real (billable) resources
terraform destroy            # remove lab resources you manage — read the plan first
```

- **State** maps your code to real resources and can contain sensitive values. Never commit state or credentials; teams use a **remote backend** (e.g. a GCS bucket) with **locking**.
- Changes made by hand in the console cause **drift**; `plan` reveals it.
- Only destroy lab resources you manage; afterwards check that nothing is left and remember billing data can update with a delay — `destroy` does not instantly bring the bill to zero.

## 6. Minimum cloud exercise

One bucket and dataset created with IaC, one mart loaded from Parquet, reader and writer roles, a query with a partition filter, a dry run and a bytes cap. Porting all of dbt, a Snowflake trial and a second cloud are extensions.

## 7. Common mistakes

| Mistake | Effect | Fix |
|---|---|---|
| `SELECT *` / `LIMIT` to "save cost" | Full scan billed | Fewer columns, partition filters |
| Treating budget alerts as caps | Surprise bills | Quotas + `maximum_bytes_billed` |
| Owner/Editor for pipelines | Over-privilege | Predefined roles at dataset scope |
| JSON keys in Git | Credential leak | Workload identity, secret manager, rotation |
| Local state on one laptop | Lost or conflicting state | Remote backend with locking |
| Bucket and dataset in different locations | Load errors/egress | Same location |

## 8. Exercises

1. Create the bucket, dataset and IAM binding with Terraform; paste the plan into your evidence log.
2. Load `fct_orders` Parquet; compare the dry-run bytes of `SELECT *` vs two columns with a one-month filter.
3. Set `require_partition_filter` and show the error for an unfiltered query.
4. As the reader service account, prove that SELECT works and INSERT fails. Then destroy everything and verify no resources remain.

## 9. Review questions

> [!question]- What is the difference between partitioning and clustering?
> Partitioning splits a table into segments by a date/integer column so whole partitions can be skipped; clustering sorts data within partitions by chosen columns so blocks can be skipped.

> [!question]- Why does the location of buckets and datasets matter?
> BigQuery loads and queries require compatible locations; mismatches fail or incur cross-region transfer costs.

> [!question]- How would you check that a reader does not accidentally have Owner rights?
> Inspect IAM policy bindings at project and dataset level (including inherited ones and groups), and run negative tests as that principal (write and admin actions must fail).

> [!question]- Does `LIMIT 10` reduce BigQuery cost?
> Not for regular tables: billing is based on the columns and partitions scanned, not on the rows returned.

Related: [[Security and Governance]], [[Performance and Storage]], [[Module 14 - Cloud and Terraform]]. Sources: [BigQuery cost best practices](https://docs.cloud.google.com/bigquery/docs/best-practices-costs), [BigQuery partitioned tables](https://cloud.google.com/bigquery/docs/partitioned-tables), [Terraform GCP tutorial](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started).
