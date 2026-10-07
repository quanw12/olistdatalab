# Cloud Engineering — GCP

[Part 5](../README.md) · [Setup](../setup.md) · [Progress](../progress.md)

Deploy one bounded, checked batch system. Start in local mode. [Live lab](live-lab.md) gives the provisioning/run/recovery sequence for an owned GCP project. Local checks and cloud evidence are recorded separately.

Follow these eight lessons in order. Read each guide, then concepts/syntax, assignment, progressive help and acceptance criteria. A lesson is a unit of work, not necessarily a calendar day. Commit commands are included in every guide.

| Lesson | Focus | Verification |
|---|---|---|
| [CL01](01-boundaries/guide.md) | Plan one cloud pipeline and its ownership | Manual evidence |
| [CL02](02-storage/guide.md) | Create stable object keys and immutable raw input | Offline contract + evidence |
| [CL03](03-jobs/guide.md) | Package a bounded batch job | Offline contract + evidence |
| [CL04](04-warehouse/guide.md) | Load history and materialize current state | Offline contract + evidence |
| [CL05](05-iam/guide.md) | Grant permissions at the right scope | Offline contract + evidence |
| [CL06](06-scheduler/guide.md) | Authenticate a schedule and preserve batch identity | Offline contract + evidence |
| [CL07](07-costs/guide.md) | Bound query work and own cleanup | Offline contract + evidence |
| [CL08](08-capstone/guide.md) | Deliver the cloud inventory batch pipeline | Manual evidence |

## Exit check

Owned object storage, Cloud Run job and BigQuery state/report with replay and recovery evidence. Demonstrate one successful run, one failure and recovery, one unfamiliar input and a clear English explanation. Record guided versus independent work honestly. Update only progress you have actually demonstrated.
