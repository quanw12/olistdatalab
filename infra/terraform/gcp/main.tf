# Cloud version of the lake + warehouse on Google Cloud (free-tier friendly):
#   GCS bucket       = the Parquet lake (bronze/, gold/)
#   BigQuery dataset = the warehouse the marts are loaded into
#   service account  = what the pipeline runs as, with only the roles it needs
#
#   cd infra/terraform/gcp
#   terraform init
#   terraform plan  -var-file=example.tfvars
#   terraform apply -var-file=example.tfvars
#   terraform destroy -var-file=example.tfvars   # when done, to avoid costs

terraform {
  required_version = ">= 1.6"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_storage_bucket" "lake" {
  name                        = "${var.project_id}-olist-lake"
  location                    = var.region
  uniform_bucket_level_access = true
  force_destroy               = true # a learning project: allow destroy with data inside

  lifecycle_rule {
    condition { age = 30 }
    action { type = "Delete" }
  }
}

resource "google_bigquery_dataset" "marts" {
  dataset_id                 = "olist_marts"
  location                   = var.region
  delete_contents_on_destroy = true
  # Tables expire after 60 days so a forgotten lab never keeps billing storage.
  default_table_expiration_ms = 60 * 24 * 60 * 60 * 1000
}

resource "google_service_account" "pipeline" {
  account_id   = "olist-pipeline"
  display_name = "Olist pipeline"
}

# Least privilege: write objects in this bucket only, edit tables in this dataset only.
resource "google_storage_bucket_iam_member" "pipeline_lake" {
  bucket = google_storage_bucket.lake.name
  role   = "roles/storage.objectAdmin"
  member = "serviceAccount:${google_service_account.pipeline.email}"
}

resource "google_bigquery_dataset_iam_member" "pipeline_marts" {
  dataset_id = google_bigquery_dataset.marts.dataset_id
  role       = "roles/bigquery.dataEditor"
  member     = "serviceAccount:${google_service_account.pipeline.email}"
}

resource "google_project_iam_member" "pipeline_jobs" {
  project = var.project_id
  role    = "roles/bigquery.jobUser"
  member  = "serviceAccount:${google_service_account.pipeline.email}"
}
