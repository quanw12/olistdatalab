# Focused resources

[Lesson references](lesson-references.md) index every core lesson. Use this page for optional teachers and deeper reading.

These are references or optional replacements, not an additional set of mandatory courses. Use one teacher per subject, plus documentation for specific questions.

| Topic | Resource | How to use it |
|---|---|---|
| System concepts | [IBM OLAP/OLTP comparison](https://www.ibm.com/think/topics/olap-vs-oltp) | Clarify workload and grain questions in DE01 |
| Reading/debugging code | [Python pdb](https://docs.python.org/3.13/library/pdb.html) and [profiling](https://docs.python.org/3.13/library/profile.html) | Inspect a concrete failure and measure the bounded DE03 workload |
| Python fundamentals | Your [56-lesson companion](../02-python/README.md) and selected video | Follow the existing chapter map; advanced extensions are original |
| Database behavior | [PostgreSQL tutorial](https://www.postgresql.org/docs/18/tutorial.html) and linked DE05–DE07 docs | Verify one constraint/transaction/query-plan question, then do the native lab |
| Local analytics | [DuckDB Python guide](https://duckdb.org/docs/stable/clients/python/overview) | DE12 syntax and local query behavior |
| dbt models/tests | [dbt learning entry](https://docs.getdbt.com/docs/introduction) and [dbt Fundamentals](https://learn.getdbt.com/courses/dbt-fundamentals) | Supplement DE13–DE15; access/enrollment may require an account |
| Orchestration | [Prefect concepts](https://docs.prefect.io/v3/concepts/flows) | Reuse foundation setup and focus on retry/interval semantics |
| Airflow transfer | [TaskFlow tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html) | Optional DE18, not a second mandatory deployment |
| Cloud | [BigQuery sandbox tutorial](https://docs.cloud.google.com/bigquery/docs/sandbox) | Optional SELECT/load lab; check limits and keep billing disabled |
| Spark | [PySpark docs](https://spark.apache.org/docs/latest/api/python/index.html) | Optional schema/plan comparison after core gates |
| Broad DE project examples | [Data Engineering Zoomcamp repository](https://github.com/DataTalksClub/data-engineering-zoomcamp) | Optional later reference; its stack is broader than this course, not an extra workload |
| Linux/Git/Docker | [Linux course](../03-linux/README.md) | Use its setup and corresponding skill lessons |
| Engineering extensions | [Part 5](../05-extensions/README.md) and [source notes](../05-extensions/sources.md) | Prepared repair, GCP, retrieval and Kafka/CDC practice; follow track order after the core |

For independently chosen SQL learning, prefer real datasets, changed-input exercises, joins/cardinality, NULL/time/windows and query reasoning. Validate it against Gate B. Certificates/watch time do not replace independent evidence.

If a reference is unavailable, the lesson/help/expected files still define the local exercise contract. Use the error journal and assessments to guide practice. You do not need an AI subscription, a paid model, a paid cloud account or another purchased course to attempt the core.

## Choosing additional material

Keep your selected Python teacher as the main fundamentals source. Add another explanation only for a demonstrated gap. Inspect a sample lesson before committing to a whole course:

| Criterion | Look for |
|---|---|
| Beginner fit | Explicit syntax, indentation, return values and traced examples |
| Independent practice | Tasks before solutions and a useful way to verify results |
| Real boundaries | Empty/malformed input, duplicates, time/money meaning and failure behavior |
| Debugging | Reproduction, error interpretation and repair of broken code |
| Complete programs | Small functions joined through clear input/output interfaces |
| Engineering habits | Environments, imports, tests, readable code and an honest handoff |
| Source access | Identified chapter/version and accessible notes, examples or transcript |
| Review quality | Feedback on behavior and reasoning, beyond whether the code runs |

For SQL, inspect join cardinality, NULL behavior, window ties/frames, timezone boundaries and reconciliation. Prefer examples you can run on your native PostgreSQL setup. Check progress against Gate B rather than a certificate.

When supplying future teaching material, send the exact chapter/video segment plus accessible notes/transcript or example files. A syllabus or screenshot supports topic alignment; it does not establish what every frame or subtitle says. Course source notes distinguish verified outlines from original supplementary lessons.

