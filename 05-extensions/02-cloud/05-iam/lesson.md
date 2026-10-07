# CL05 — Learn

## Permissions follow actions

Read raw objects, create output objects and run/load warehouse work are different actions. Do not solve every permission error by granting Owner. Start with the failed action, resource and identity. A bucket-level object grant and a project-level query job grant address different boundaries.

## Syntax — inspect a role binding

~~~powershell
gcloud storage buckets get-iam-policy "gs://YOUR_OWNED_BUCKET"
gcloud projects get-iam-policy "YOUR_PROJECT_ID"
~~~
Use real owned names. Do not publish full IAM policies containing other identities. Python local credential files should be ignored; deployed runtime uses its attached service account. [Storage roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles), [BigQuery roles](https://docs.cloud.google.com/bigquery/docs/access-control).

The exercise's mapping is a narrow course policy. A local role list does not prove access: live tests must include an allowed action and a denied action under the intended runtime identity.

[Assignment](exercise.md) · [Hints](help.md)
