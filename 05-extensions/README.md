# Part 5 — Engineering extensions

[Master roadmap](../roadmap.md) · [Setup](setup.md) · [Progress](progress.md) · [Sources](sources.md) · [Author verification](verification.md)

**All four extensions are prepared: 32 lessons, eight per track.** Follow the order below after the four core courses and passing core readiness gates. Preparing these materials does not mark practice complete.

| Order | Track | Lessons | Purpose |
|---|---|---|---|
| 1 | [Engineering Labs](01-labs/README.md) | LAB01–LAB08 | Repair unfamiliar code and data work |
| 2 | [Cloud Engineering — GCP](02-cloud/README.md) | CL01–CL08 | Deploy one bounded, checked batch system |
| 3 | [AI Data](03-ai-data/README.md) | AI01–AI08 | Build reliable data for retrieval |
| 4 | [Streaming and CDC](04-streaming/README.md) | ST01–ST08 | Cross a real continuous-change boundary |

Start with [LAB01: repair an inflated SQL report](01-labs/01-joins/guide.md). Engineering Labs comes first because it practises your stated goal: handling an assigned task independently. Cloud reuses your BigQuery introduction and adds service boundaries. AI Data begins locally with Python/SQLite. Streaming comes last because Kafka/CDC adds more running services and ordering/restart behavior.

## Read one lesson at a time

guide.md → lesson.md → exercise.md and named starter → help.md when needed → expected.md → notes.md → progress/commit. Concepts and syntax precede code; starters contain prompts only. Supplied fixtures, checks, benchmark and infrastructure are clearly identified. Every guide has scoped Windows PowerShell commit commands using your feature/... convention.

The 25 offline contracts add changed-input, malformed-data, replay/rollback and ordering cases. Seven concept/integration lessons use manual evidence checklists. A passed local contract does not prove a cloud deployment, Kafka delivery, actual embeddings or a complete integration. Install packages only at their lesson; [setup](setup.md) separates local, cloud, model and streaming environments.

## How much extra time?

Allow roughly **8–12 additional weeks at 10–15 focused hours/week**, as a planning estimate. Split capstones/setup over several sessions. This is additional depth beyond the core schedule, not another requirement before you can apply. After the core readiness gates, begin suitable internship applications while continuing these extensions. Finish a smaller correct artifact before expanding its stack.

## Four portfolio outcomes

1. Inventory maintenance CLI with repair/recovery/performance evidence.
2. GCP batch deployment, or an explicitly local equivalent if you choose no billing.
3. Reproducible document ingestion/search/evaluation with updates/deletes.
4. Kafka plus PostgreSQL CDC demonstration with safe acknowledgements and consumer restart.

Use original synthetic data. Explain source limitations, transaction boundaries and actual environments. Production operations at scale and advanced model training are later responsibilities; the small labs should be described accurately.
