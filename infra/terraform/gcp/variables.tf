variable "project_id" {
  description = "GCP project id"
  type        = string
}

variable "region" {
  description = "Region for the bucket and dataset"
  type        = string
  default     = "asia-southeast1"
}

output "lake_bucket" {
  value = google_storage_bucket.lake.url
}

output "bigquery_dataset" {
  value = google_bigquery_dataset.marts.dataset_id
}

output "pipeline_service_account" {
  value = google_service_account.pipeline.email
}
