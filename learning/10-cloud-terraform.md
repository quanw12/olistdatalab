# 10 · Cloud and infrastructure as code

**Time:** week 13 · **Stack:** Google Cloud (GCS, BigQuery, IAM), Terraform; Snowflake, Databricks, AWS/Azure mapping

## Why
Most DE jobs run in a cloud. Knowing one cloud well and being able to map it to others is enough
for an intern.

## Learn
- Object storage vs warehouse; separation of storage and compute
- IAM: service accounts, least privilege; never commit keys (`.env`, secret managers)
- BigQuery: partitioned and clustered tables, cost per bytes scanned, `--dry_run`
- Terraform: provider, resource, state, plan/apply/destroy — [Terraform GCP tutorial](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started)
- Mapping: GCS ≈ S3 ≈ ADLS; BigQuery ≈ Snowflake ≈ Redshift ≈ Synapse; Dataproc ≈ EMR ≈ Databricks

## Read in this repo
- `infra/terraform/gcp/main.tf` — bucket with lifecycle, dataset with expiration, least-privilege service account.

## Build
1. Create a GCP project with the free trial; set a **budget alert** first.
2. `terraform init/plan/apply` with your `project_id`. Screenshot the plan.
3. Add `olist publish-gcp`: upload `data/lake/gold/*.parquet` to the bucket
   (`google-cloud-storage`) and load into BigQuery (`google-cloud-bigquery`, `LoadJobConfig(source_format=PARQUET)`).
   Make `fct_orders` partitioned by `order_date` and clustered by `customer_state`.
4. Point dbt at BigQuery (`dbt-bigquery`, second profile target). Fix the SQL that is
   DuckDB-specific (`ASOF JOIN`, `arg_min`, `date_diff` argument order). Note each change.
5. Snowflake 30-day trial: load the same Parquet via a stage, run one mart. Compare the SQL.
6. `terraform destroy`. **Check:** nothing left billing.

## Break it
- Run a `SELECT *` on BigQuery with `--dry_run` vs selecting 3 columns with a partition filter; compare bytes.
- Remove the `bigquery.jobUser` role from the service account and run a load. Read the error.

## Interview questions
- How do you keep cloud costs under control on a data platform?
- What does Terraform state contain and why is it sensitive?
- Partitioning vs clustering in BigQuery?

## Done when
- [ ] Infra applied and destroyed by Terraform; budget alert set
- [ ] Marts loaded into BigQuery; dbt runs on BigQuery with notes on dialect changes
