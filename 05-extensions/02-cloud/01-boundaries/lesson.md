# CL01 — Learn

## One provider, one batch job

This track uses GCP because Part 4 already introduces BigQuery. The design is immutable raw objects → a Python Cloud Run job → BigQuery history/current state → a published report. Cloud Run jobs execute and exit; services serve requests. A batch job does not need an HTTP server. [Job documentation](https://docs.cloud.google.com/run/docs/create-jobs).

Distinguish four identities: you/deployer, job runtime, scheduler caller and provider service agents. A developer who can deploy a job does not automatically give its runtime access to your data. Keep synthetic inputs, one region and owned resource names. A billing-enabled project may incur charges; budget alerts notify rather than imposing a complete hard spending cap.

## Syntax — inspect, not deploy yet

~~~powershell
gcloud version
gcloud config get-value project
gcloud auth list
~~~
The active CLI account and Application Default Credentials used by Python are separate configurations. Do not paste credential output into your Git notes. Installation/sign-in procedures are linked in setup; deploy only in your own learning project after choosing a budget.

## Architecture reasoning

Write where each durable artifact lives, its identity, retention and owner. Container-local files are temporary work, not a recovery ledger. A resource plan can be completed without a paid deployment.

[Assignment](exercise.md) · [Hints](help.md)
