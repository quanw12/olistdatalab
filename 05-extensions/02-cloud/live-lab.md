# GCP live lab — deploy your completed batch implementation

[Track](README.md) · [Setup](../setup.md) · [Sources](../sources.md)

Use this alongside CL01–CL08. These instructions provision infrastructure for your own worker; the worker/load/MERGE/publication logic remains your assignment. No cloud resources were created during material preparation. Choose local-only mode if you do not have an owned billing-enabled project and an agreed learning budget. Label local results accurately.

## 1. Choose owned resources (CL01)

Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) for Windows, open a new PowerShell window and verify gcloud/bq. In Cloud Console create/select your own learning project, enable billing only when you intend to do the live lab, set budget alerts and inspect current regional pricing. Do not use a school/company project without authority over these resources.

Replace YOUR_PROJECT_ID with an actual owned ID. These P5 variables are lab configuration; no credentials belong in them. Check the active account/project before creating anything.

~~~powershell
gcloud version
bq version
gcloud auth login
$env:P5_PROJECT = "YOUR_PROJECT_ID"
$env:P5_REGION = "asia-southeast1"
$env:P5_RAW = "$($env:P5_PROJECT)-p5-raw"
$env:P5_OUTPUT = "$($env:P5_PROJECT)-p5-output"
$env:P5_RUNTIME = "p5-runtime@$($env:P5_PROJECT).iam.gserviceaccount.com"
$env:P5_SCHEDULER = "p5-scheduler@$($env:P5_PROJECT).iam.gserviceaccount.com"
gcloud config set project $env:P5_PROJECT
gcloud config get-value project
gcloud auth list
gcloud auth application-default login
~~~

ADC is for local Python SDK work; the deployed job uses its attached runtime service account. Do not export JSON private keys or commit token files. Bucket names are globally unique; if your chosen owned names are unavailable, choose new names and keep your plan/configuration consistent. Keep dataset/storage/job locations compatible.

## 2. Provision only the lab infrastructure (CL02–CL05)

Run creation commands once. If a resource exists, inspect ownership/configuration; do not delete it to hide an error. Every resource below is scoped to the selected project and named p5- or p5_inventory.

~~~powershell
gcloud services enable run.googleapis.com artifactregistry.googleapis.com storage.googleapis.com bigquery.googleapis.com cloudscheduler.googleapis.com iam.googleapis.com
gcloud iam service-accounts create p5-runtime --display-name "P5 batch runtime"
gcloud iam service-accounts create p5-scheduler --display-name "P5 schedule caller"
gcloud storage buckets create "gs://$env:P5_RAW" --location $env:P5_REGION --uniform-bucket-level-access
gcloud storage buckets create "gs://$env:P5_OUTPUT" --location $env:P5_REGION --uniform-bucket-level-access
bq --location=$env:P5_REGION mk --dataset "$($env:P5_PROJECT):p5_inventory"
gcloud artifacts repositories create p5-images --repository-format docker --location $env:P5_REGION
gcloud storage buckets add-iam-policy-binding "gs://$env:P5_RAW" --member "serviceAccount:$env:P5_RUNTIME" --role roles/storage.objectViewer
gcloud storage buckets add-iam-policy-binding "gs://$env:P5_OUTPUT" --member "serviceAccount:$env:P5_RUNTIME" --role roles/storage.objectCreator
gcloud storage buckets add-iam-policy-binding "gs://$env:P5_OUTPUT" --member "serviceAccount:$env:P5_RUNTIME" --role roles/storage.objectViewer
gcloud projects add-iam-policy-binding $env:P5_PROJECT --member "serviceAccount:$env:P5_RUNTIME" --role roles/bigquery.jobUser
~~~

In BigQuery Console select p5_inventory → Sharing/Permissions → add the runtime service account with BigQuery Data Editor on **this dataset**. UI wording may vary; inspect the resulting resource scope. Do not grant it project Owner. The deployer needs permissions to create resources/push images/deploy and act as the runtime identity; the runtime grants above do not grant you those deployment permissions. For a constrained account, use the [documented deployment roles](https://docs.cloud.google.com/run/docs/create-jobs) and request only the missing scoped action.

Create history/current using schema.sql in the BigQuery editor after replacing YOUR_PROJECT_ID in your own copy. history retains all accepted revisions; current retains one latest state including deletes. No SQL solution for your MERGE is provided. First load manually as the deployer to isolate format/schema problems; repeat under the runtime during the job.

## 3. Prepare/upload two immutable inputs (CL02)

From data/batches.json write b1 and b2 as separate UTF-8 JSONL files under this track's output/ directory. Implement CL02/upload.py with --batch-id, --file and --bucket arguments and a generation=0 upload. Its filename must be changes.jsonl for these commands. Record object generation and digest.

~~~powershell
Set-Location "C:\DE Courses\05-extensions\02-cloud"
& "C:/DE Courses/.venv-extensions/Scripts/python.exe" "02-storage/upload.py" --batch-id b1 --file output/b1/changes.jsonl --bucket $env:P5_RAW
& "C:/DE Courses/.venv-extensions/Scripts/python.exe" "02-storage/upload.py" --batch-id b2 --file output/b2/changes.jsonl --bucket $env:P5_RAW
gcloud storage ls "gs://$env:P5_RAW/raw/"
~~~

The scripts are unfinished until you implement them. The first object key is raw/b1/changes.jsonl. Reusing its identity with altered bytes must fail; matching content may be reported as explicitly verified replay. Do not silently overwrite raw input.

## 4. Complete and test your worker locally (CL03–CL04)

Target environment variables: PROJECT_ID, BQ_DATASET=p5_inventory, RAW_BUCKET, OUTPUT_BUCKET, BATCH_ID, FAIL_AFTER_WAREHOUSE=0/1 and QUERY_BYTE_LIMIT. The worker must:

1. Fetch immutable input, validate every six-field event and compare durable batch/content identity.
2. Load checked JSONL into history using a stable job_id based on batch identity/content. Set location; inspect result(), and retrieve the same existing job after an uncertain submission rather than blindly append again.
3. Detect conflicting equal event_id/version payloads, deduplicate identical revisions, materialize latest-state staging and run your CL04 MERGE. Do not remove tombstones first.
4. Reconcile counts/active units, then create an immutable report/manifest in the output bucket using preconditions. A failed publication remains pending delivery even if warehouse work committed.
5. Log stage/batch/execution identity and exit truthfully. Use a deliberate single writer; do not treat tasks=1 as an overlap lock.

Use deterministic request identities for derived SQL work too, or make rerunning it explicitly safe. Persist enough metadata outside the container to recover. Cross-service operations are not one transaction. Reject changed batch content before modifying current state. For this lab process one batch at a time and leave unattended scheduling disabled; a durable lease/queue design is required before concurrent automation.

Package your worker and all imported student modules in 03-jobs. Copy requirements-cloud.txt to that build context as requirements.txt and complete its Dockerfile. Do not COPY local ADC credentials into the image. First run its contract/unit checks locally, then build.

~~~powershell
Set-Location "C:\DE Courses\05-extensions\02-cloud\03-jobs"
$env:P5_IMAGE = "$($env:P5_REGION)-docker.pkg.dev/$($env:P5_PROJECT)/p5-images/worker:v1"
docker build -t $env:P5_IMAGE .
gcloud auth configure-docker "$($env:P5_REGION)-docker.pkg.dev"
docker push $env:P5_IMAGE
~~~

Record the image digest from the push. Before deployment, set P5_IMAGE to the same repository/image path followed by @sha256: and your actual pushed digest, replacing its :v1 suffix. Deploy that immutable reference; the v1 tag can move if you overwrite it. A container shell requiring an interactive login is not a suitable Cloud Run runtime.

## 5. Deploy, execute and inspect actual completion (CL03/CL08)

~~~powershell
gcloud run jobs create p5-inventory --image $env:P5_IMAGE --region $env:P5_REGION --service-account $env:P5_RUNTIME --tasks 1 --parallelism 1 --max-retries 1 --task-timeout 300s --memory 512Mi --set-env-vars "PROJECT_ID=$env:P5_PROJECT,BQ_DATASET=p5_inventory,RAW_BUCKET=$env:P5_RAW,OUTPUT_BUCKET=$env:P5_OUTPUT,BATCH_ID=b1,FAIL_AFTER_WAREHOUSE=0,QUERY_BYTE_LIMIT=10000000"
gcloud run jobs execute p5-inventory --region $env:P5_REGION --wait
gcloud run jobs executions list --job p5-inventory --region $env:P5_REGION
gcloud run jobs execute p5-inventory --region $env:P5_REGION --update-env-vars "BATCH_ID=b2,FAIL_AFTER_WAREHOUSE=0" --wait
~~~

--wait checks execution completion; a normal execute request without it can return after startup. In Console inspect each execution's status and structured logs. Use your actual execution ID for detailed inspection; do not reuse example IDs.

BigQuery validation query (replace YOUR_PROJECT_ID):

~~~sql
SELECT COUNT(*) AS current_rows,
       COUNTIF(op = 'upsert') AS active_rows,
       SUM(IF(op = 'upsert', units, 0)) AS active_units
FROM `YOUR_PROJECT_ID.p5_inventory.current`;
~~~

Expected after b2: 3/2/13. Verify input manifests, current rows and output report together. Use the Cloud Run runtime to perform raw read allowed/raw overwrite denied tests; your deployer's permissions do not prove runtime scope. Implement a bounded permission-probe mode on worker.py if needed and log only sanitized results.

## 6. Replay/failure/cost evidence (CL07–CL08)

Replay b2: final result stays 13 and raw objects/current/report remain consistent. Try an altered-content b2 upload: immutable identity/conflict handling refuses it. Inject failure after warehouse work, then rerun the same batch with injection disabled. If already published b2 cannot reproduce pending-publication behavior, create a new owned test batch b3 with a no-op logical replay, crash before its first publication and recover it. Do not delete prior evidence to manufacture a failure.

Run a dry-run estimate with use_query_cache=False, compare to your chosen byte bound, and run with maximum_bytes_billed for on-demand SQL. Use a deliberately too-small bound to demonstrate provider refusal. Retain actual bytes/status. An alert/byte limit is not a total-cloud spending hard cap.

## 7. Trigger once, then pause (CL06)

The default job still targets stable b1; its repeat must be safe. Grant the scheduler caller only job invocation, then create a low-frequency trigger. This uses the Google Run API endpoint with an OAuth service-account token. Cloud Scheduler's service agent must retain its provider-managed role; do not replace it with the runtime identity.

~~~powershell
gcloud run jobs add-iam-policy-binding p5-inventory --region $env:P5_REGION --member "serviceAccount:$env:P5_SCHEDULER" --role roles/run.invoker
gcloud scheduler jobs create http p5-inventory-trigger --location $env:P5_REGION --schedule "0 9 * * *" --time-zone "Asia/Ho_Chi_Minh" --uri "https://run.googleapis.com/v2/projects/$($env:P5_PROJECT)/locations/$($env:P5_REGION)/jobs/p5-inventory:run" --http-method POST --oauth-service-account-email $env:P5_SCHEDULER --headers "Content-Type=application/json" --message-body "{}"
gcloud scheduler jobs pause p5-inventory-trigger --location $env:P5_REGION
gcloud scheduler jobs run p5-inventory-trigger --location $env:P5_REGION
gcloud scheduler jobs pause p5-inventory-trigger --location $env:P5_REGION
~~~

The paused job can be manually triggered. Check Scheduler result and the corresponding Run execution; a successful trigger only starts the job. Stop if you cannot enforce sequential runs; finish manually instead. Document the same-batch replay and no-overlap policy.

## 8. Retire owned resources

Inventory your exact lab resource identities and costs, keep sanitized evidence, pause the scheduler first, then remove only the resources listed in your plan. Use the Cloud Console's resource-specific delete actions for the owned trigger, job, p5_inventory dataset/tables, lab bucket contents/buckets, image repository and the two lab service accounts. Confirm the displayed project/resource before each irreversible deletion. Keep any resource you still need and account for its continuing storage cost. Do not delete an entire/shared project as a course cleanup shortcut.

Troubleshooting: permission denied → identity/action/scope; load error → JSONL/schema/location; job succeeds with no report → incorrect exit/status boundary; duplicate totals → lost request identity or wrong grain; overwritten raw → missing create precondition; schedule startup success but failed job → inspect execution logs. Record the actual limitation rather than suppressing it.
