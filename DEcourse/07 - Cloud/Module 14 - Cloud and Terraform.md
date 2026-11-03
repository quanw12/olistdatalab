# 14 · Cloud and Terraform

> **Theory notes:** [[GCP BigQuery Terraform and Cost]] · **Route:** [[Roadmap]] · **Labs:** [[Labs Guide]]. Videos are optional: use the diagnostic test to decide what to watch.

**Weeks:** 24–25 · **Prerequisites:** 09, 10, 21 (Spark not required)

## Goal
Deploy the lake and warehouse to a cloud with infrastructure as code, least-privilege access and
cost control; map the same design to Snowflake, Databricks, AWS and Azure.

## 1. Watch
| Video | What to watch | Length |
|---|---|---|
| [Terraform explained in 15 mins — TechWorld with Nana](https://www.youtube.com/watch?v=l5k1ai_GBDE) | First | 18 min |
| [Complete Terraform Course — DevOps Directive](https://www.youtube.com/watch?v=7xngnjfIlK4) | Main course (examples on AWS; same ideas on GCP) | 2 h 38 |
| [DataTalksClub Data Engineering Zoomcamp — module 1 (Terraform + GCP)](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform) | Videos linked in the module README | ~2 h |
| [Google BigQuery Tutorial — MeasureSchool](https://www.youtube.com/watch?v=MH5M2Crn6Ag) | All | 15 min |
| [Learn Snowflake — 1-hour crash course — Tom Bailey](https://www.youtube.com/watch?v=2t-ls6ekA8E) | Week 26 | 58 min |

## 2. Read
- [Terraform: get started with Google Cloud](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started)
- [BigQuery: partitioned tables](https://cloud.google.com/bigquery/docs/partitioned-tables) · [clustered tables](https://cloud.google.com/bigquery/docs/clustered-tables) · [loading Parquet](https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-parquet)
- [Google Cloud free program](https://cloud.google.com/free) · [budgets and alerts](https://cloud.google.com/billing/docs/how-to/budgets)
- [IAM: service accounts best practices](https://cloud.google.com/iam/docs/best-practices-service-accounts)

## 3. Syntax sheet
```hcl
terraform {
  required_providers { google = { source = "hashicorp/google", version = "~> 6.0" } }
}
provider "google" {
  project = var.project_id
  region  = var.region
}

variable "project_id" { type = string }

resource "google_storage_bucket" "lake" {
  name     = "${var.project_id}-lake"
  location = var.region
}
output "bucket" { value = google_storage_bucket.lake.url }
```
```bash
terraform init      # download providers
terraform fmt; terraform validate
terraform plan  -var-file=example.tfvars    # what would change
terraform apply -var-file=example.tfvars
terraform destroy -var-file=example.tfvars  # always, when the lab is over
```
```python
from google.cloud import bigquery
client = bigquery.Client()
job = client.load_table_from_uri("gs://bucket/gold/fct_orders.parquet", "proj.olist_marts.fct_orders",
        job_config=bigquery.LoadJobConfig(source_format="PARQUET", write_disposition="WRITE_TRUNCATE",
                                          time_partitioning=bigquery.TimePartitioning(field="order_date")))
job.result()
```

| Idea | GCP | AWS | Azure | Vendor |
|---|---|---|---|---|
| Object storage (lake) | GCS | S3 | ADLS Gen2 | — |
| Warehouse | BigQuery | Redshift | Synapse / Fabric | Snowflake |
| Managed Spark | Dataproc | EMR / Glue | Synapse Spark | Databricks |
| Orchestration | Cloud Composer | MWAA | Data Factory | Astronomer |

## 4. Practice
Free trial project → **budget alert first** → create a bucket and a BigQuery dataset by hand in
the console; delete them. Then do the same with Terraform.

## 5. Apply to the project
1. Read `infra/terraform/gcp/main.tf` line by line; explain each IAM role in your notes.
2. `terraform apply` with your project id. Screenshot the plan.
3. Add `olist publish-gcp` to the CLI: upload `data/lake/gold/*.parquet` to the bucket and load
   each into BigQuery (partition `fct_orders` by `order_date`, cluster by `customer_state`).
   Hint: `google-cloud-storage` + the load snippet above. Credentials: `gcloud auth application-default login`, never a key in git.
4. Optional extension: run dbt on BigQuery: add a `bigquery` target to a profile, install `dbt-bigquery`, fix the
   DuckDB-only SQL (`ASOF JOIN`, `arg_min`, `date_diff` argument order, `::` casts). List each change.
5. Cost: run one query with `SELECT *` and one with 3 columns + a partition filter; compare
   "bytes processed".
6. Optional extension: Snowflake trial (check current trial terms): load the same Parquet via a stage and run one mart. Compare dialects.
7. `terraform destroy`. **Check:** inventory has no unintended resources; billing can be delayed and past usage still costs money.

## 6. Self-check
- How do you keep cloud costs under control?
- What is in Terraform state and why is it sensitive?
- Partitioning vs clustering?

## Done when
- [ ] Infra created and destroyed with Terraform; budget alert set
- [ ] One mart in BigQuery, reader/writer tested, dry run and bytes cap demonstrated; full dbt migration is optional

## Product-focused requirements

Core cloud: one bucket/dataset created with IaC, one Parquet mart in BigQuery, reader/writer roles, dry run + `maximum_bytes_billed` + a partition filter. Porting all of dbt and a Snowflake trial are later extensions, not core requirements. A budget alert is not a hard cap; `LIMIT` does not guarantee a smaller scan. After cleanup check the remaining resources/state and late billing updates; do not assume `destroy` drops the bill to zero instantly.
