# Sources, job evidence and verification limits

Research dates: October 6–7, 2026. These Engineering explanations, synthetic fixtures and exercises are original; they are not a video transcript. Your selected Python course remains its own companion track.

## Why these priorities

Employer descriptions inspected:
- [Data Impact DE intern](https://dataimpact.vn/recruiter/detail/intern-data-engineer): SQL/programming, database basics, English and teamwork; big data/cloud/ML appear as advantages.
- [TC Data intern/trainee](https://tcdata.vn/career/intern-trainee-data-engineer/): SQL, modeling, scripting, ETL and communication; platform/big-data exposure is additional.
- [Pizza Hut Vietnam intern](https://pizzahut.talent.vn/job/hcm-data-engineer-intern-53453): SQL/Python, ETL/modeling/cloud fundamentals and familiarity with at least one listed tool. Its displayed June 30, 2026 deadline has passed.
- [Norrin's integration internship](https://careers.norrin.com/o/azure-data-integration-engineer-intern-1?lang=en) was inspected October 7: SQL/programming, English/problem solving; Git/APIs/cloud are additional. Its August start is past; current availability is unconfirmed.

These are examples, not a representative hiring survey or verified active-vacancy list. Some descriptions require final-year/recent graduates or a minimum attendance schedule. Your upcoming third year needs a separate eligibility check. The study priority is an inference from your gaps and these examples, not a universal employer syllabus.

Community/tutorial research included [an internship interview thread](https://www.reddit.com/r/dataengineering/comments/1ads8ru/interview_help_for_data_engineering_internship/) and [DuckDB's local dbt tutorial](https://duckdb.org/2025/04/04/dbt-duckdb). Community comments are anecdotal and do not establish hiring guarantees. An older tutorial's adapter limitation can differ from current releases; current adapter docs and local reference execution determine this course's configuration.

## Technical references

- [PostgreSQL constraints](https://www.postgresql.org/docs/18/ddl-constraints.html), [INSERT/ON CONFLICT](https://www.postgresql.org/docs/18/sql-insert.html), [EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html).
- [IBM OLAP/OLTP](https://www.ibm.com/think/topics/olap-vs-oltp), [Python pdb](https://docs.python.org/3.13/library/pdb.html) and [Python profiling](https://docs.python.org/3.13/library/profile.html): consulted for the DE01–DE03 workflow bridge added during course consolidation. Task planning and the synthetic debugging lab are original exercises.
- [DuckDB Python](https://duckdb.org/docs/stable/clients/python/overview) and [dbt-duckdb adapter](https://github.com/duckdb/dbt-duckdb).
- [dbt models](https://docs.getdbt.com/docs/build/models), [data tests](https://docs.getdbt.com/docs/build/data-tests), [incremental models](https://docs.getdbt.com/docs/build/incremental-models).
- [Prefect flows](https://docs.prefect.io/v3/concepts/flows), [retries](https://docs.prefect.io/v3/how-to-guides/workflows/retries), [deployments](https://docs.prefect.io/v3/concepts/deployments).
- [Airflow 3 TaskFlow](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html).
- [BigQuery sandbox](https://docs.cloud.google.com/bigquery/docs/sandbox), [cost controls](https://docs.cloud.google.com/bigquery/docs/best-practices-costs).
- [PySpark installation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html).

Primary pages were inspected to verify tool behavior. Sandbox docs currently describe a lifetime 10 GiB storage allowance, monthly 1 TiB query processing, 60-day expiry and exclusions for DML/streaming/Data Transfer Service. Older sources describe storage differently; recheck the current sandbox page before use rather than relying on older blog limits. Budget alerts do not cap spending. No live cloud resources are created for this course.

PyPI metadata was checked before selecting duckdb 1.5.6, dbt-duckdb 1.11.0 and dbt-core 1.12.5. These are pinned v1/Core local-lab choices; current documentation also discusses newer engines. Do not migrate the course automatically because another major version exists.

## Author validation boundary

See [verification.md](verification.md) for actual checks and environments. Offline contract checks use synthetic data. Reference implementations remain outside the learner course; starter files are intentionally unfinished.

Native PostgreSQL rollback, Prefect service/task states, optional Airflow/Spark/cloud and deployment CI need your live evidence. A parsed Python file or mock check does not prove a scheduler/database/container worked. No guarantee of production readiness or employment follows from prepared material.



## Teaching audit additions

DE27 supplies synthetic source profiling with a behavioral checker. DE28 supplies isolated native-database setup and logical restore practice; verification SQL is learner work. See [course review](../docs/course-review.md) for the audit and validation limits.
