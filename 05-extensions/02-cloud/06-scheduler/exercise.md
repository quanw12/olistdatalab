# CL06 — Assignment

Implement build_scheduler_target(project, region, job, service_account). project must match [a-z][a-z0-9-]{4,28}[a-z0-9]; region [a-z]+-[a-z]+[0-9]; job [a-z][a-z0-9-]{0,61}[a-z0-9] or a single lowercase letter. service_account local name follows the project regex length rule and email domain must be {project}.iam.gserviceaccount.com. These are restricted lab names, not an exhaustive provider name validator. Reject invalid inputs with ValueError.

Return the shown fields plus uri="https://run.googleapis.com/v2/projects/{project}/locations/{region}/jobs/{job}:run". Headers/body/method are fixed. No network call. Follow live-lab.md to create the trigger with the scheduler identity granted run.invoker on the owned job. Record your no-overlap policy.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
