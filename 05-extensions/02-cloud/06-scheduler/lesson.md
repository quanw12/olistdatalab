# CL06 — Learn

## A trigger is not a business batch

Cloud Scheduler asks the Cloud Run API to execute a job. It may retry requests; a newly generated timestamp on every attempt can turn a retry into a new batch. The job must resolve a stable input/batch identity or acquire an explicit single-writer policy. A one-task job alone does not prevent overlapping executions.

## Syntax — Scheduler HTTP target shape

~~~json
{
  "httpMethod": "POST",
  "headers": {"Content-Type": "application/json"},
  "body": "e30=",
  "oauthToken": {"serviceAccountEmail": "scheduler@project-id.iam.gserviceaccount.com"}
}
~~~
body is base64 for {} in this REST representation. The googleapis.com Run endpoint uses OAuth; this is different from an OIDC token for a service URL. [Scheduling documentation](https://docs.cloud.google.com/run/docs/execute/jobs-on-schedule).

First run manually. For this small lab, trigger once and pause the schedule after collecting evidence; never enable unattended overlapping work until you have a durable concurrency/identity policy.

[Assignment](exercise.md) · [Hints](help.md)
