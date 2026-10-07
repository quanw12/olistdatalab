# Sources, teaching choices and version boundaries

[Course](README.md) · [Setup](setup.md) · [Verification](verification.md)

Researched October 7, 2026. These are original exercises/contracts using synthetic data. They are not a transcript of a video, a copied course, or a claim that every tutorial frame/subtitle was watched. Documentation verifies specific APIs/behaviors; the learning order, constraints and tiny fixtures are course design choices.

## Focused primary references

| Boundary | Reference | What it verifies / how to use it |
|---|---|---|
| Python/SQLite transactions | [Python 3.13 sqlite3](https://docs.python.org/3.13/library/sqlite3.html), [SQLite ALTER TABLE](https://www.sqlite.org/lang_altertable.html) | Connection/transaction behavior and the additive migration syntax; reproduce locally |
| Backfill/calendar types | [datetime](https://docs.python.org/3.13/library/datetime.html) | Aware timestamps, UTC conversion and timedelta; course UTC-midnight policy is narrower |
| Profiling | [Python profiling](https://docs.python.org/3.13/library/profile.html) | Instrument your own function; no universal timing threshold |
| Raw objects | [Cloud Storage upload](https://docs.cloud.google.com/storage/docs/uploading-objects), [preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions) | Upload/generation boundaries and create-only intent |
| Cloud execution | [Cloud Run jobs](https://docs.cloud.google.com/run/docs/create-jobs), [execute CLI](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/execute) | A job runs/exits; execution --wait versus startup request; task/retry limits configured explicitly |
| Scheduler | [Run jobs on a schedule](https://docs.cloud.google.com/run/docs/execute/jobs-on-schedule) | Google API OAuth target and invocation identity |
| Warehouse | [JSON loads](https://docs.cloud.google.com/bigquery/docs/loading-data-cloud-storage-json), [queries](https://docs.cloud.google.com/bigquery/docs/running-queries), [MERGE syntax](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax) | Actual load/result/query and merge boundaries; the local SQL checker does not execute GoogleSQL |
| Scoped access | [Storage roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles), [BigQuery roles](https://docs.cloud.google.com/bigquery/docs/access-control), [dataset access](https://docs.cloud.google.com/bigquery/docs/control-access-to-resources-iam) | Course action/role plan must be checked with actual runtime identity |
| Text search | [SQLite FTS5](https://www.sqlite.org/fts5.html) | Virtual-table syntax, MATCH grammar and BM25 ordering |
| Embeddings | [SentenceTransformers usage](https://sbert.net/docs/sentence_transformer/usage/usage.html), [all-MiniLM-L6-v2 model card](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) | Optional real encode step, model assumptions and token truncation; fixtures are not semantic-model evidence |
| Kafka | [Kafka 3.9 quickstart](https://kafka.apache.org/39/getting-started/quickstart/), [official Compose example](https://github.com/apache/kafka/blob/3.9.1/docker/examples/docker-compose-files/single-node/plaintext/docker-compose.yml) | Official image/KRaft/listener configuration; this lab is one broker/replica |
| Python Kafka client | [Confluent API](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html) | Delivery callbacks, poll/flush, manual offset commit and TopicPartition |
| PostgreSQL CDC | [Debezium 3.3 compatibility](https://debezium.io/releases/3.3/), [connector reference](https://debezium.io/documentation/reference/3.3/connectors/postgresql.html), [Connect entrypoint](https://github.com/debezium/container-images/blob/main/connect-base/3.3/docker-entrypoint.sh) | Tested PostgreSQL12–17, envelope/delete semantics and CONNECT_ configuration mapping |

The selected Debezium 3.3 series lists PostgreSQL versions through 17; the lab therefore isolates PostgreSQL 17 rather than changing your native18 installation. This is a documented tested matrix, not proof that all other combinations fail. Kafka offsets, WAL/LSN and a domain revision have different semantics.

## Teaching references and community inspection

[DataTalksClub's LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) provides a practical outline for retrieval/evaluation/monitoring; use a relevant lesson when you need another explanation. Our local index/state contracts are original and avoid requiring its entire stack. [DE Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) provides broader project examples; it is a reference, not another mandatory course.

Research also inspected community discussions such as [CDC setup experiences](https://www.reddit.com/r/dataengineering/comments/1kft7bp/) and [Kafka Compose/listener discussion](https://www.reddit.com/r/apachekafka/comments/16p0v5i/). These help identify common addressing/configuration problems; their older commands/versions are not used as compatibility proof. Primary version/API sources above determine the supplied configuration.

## Direct package pins

| File | Pin | Metadata checked |
|---|---|---|
| requirements-cloud.txt | `google-cloud-storage==3.16.0`, `google-cloud-bigquery==3.46.1` | [Storage](https://pypi.org/project/google-cloud-storage/3.16.0/), [BigQuery](https://pypi.org/project/google-cloud-bigquery/3.46.1/); declared Python >=3.10 |
| requirements-streaming.txt | `confluent-kafka==2.15.1` | [PyPI](https://pypi.org/project/confluent-kafka/2.15.1/); declared Python >=3.8, binary wheels published |
| requirements-embeddings.txt | `sentence-transformers==6.1.0` | [PyPI](https://pypi.org/project/sentence-transformers/6.1.0/); declared Python >=3.10; actual torch/model setup is separate |

These are direct pins, not a complete transitive dependency lock or a guarantee for every Python/OS combination. All four direct wheels were downloaded for Windows/Python 3.13 without installing their transitive dependencies. Standard-library references were executed on that interpreter. Record your actual package resolution with pip check and a lock/freeze after a successful environment; an SDK import alone does not prove remote behavior. Real embeddings were not downloaded or model-executed during preparation.

## Container pins

compose.yml uses apache/kafka:3.9.1, quay.io/debezium/connect:3.3.2.Final and postgres:17.6-alpine, each with a registry digest checked during preparation. [Kafka release](https://kafka.apache.org/39/getting-started/quickstart/), [Debezium release](https://debezium.io/releases/3.3/) and [Postgres image](https://hub.docker.com/_/postgres) identify the source images. Exact digests are in compose.yml; record pulled platform/image IDs during your live lab. They are compatibility-oriented teaching snapshots, not a production maintenance recommendation. Review supported/security releases before reusing the configuration outside this synthetic lab.

Compose syntax validation does not establish service startup/integration compatibility. The author did not run the live stack because the Docker Linux engine was unavailable. A learner's live connector/producer/consumer evidence remains required. If a referenced service/API changes, preserve the contract and investigate the actual error rather than substituting an unverified configuration.
