# Interview practice bank

Answer aloud before revealing the short answer. Use your own project example and one limitation; memorized definitions are insufficient.

| Prompt | What a useful answer should include |
|---|---|
| What did you build? | Business question, source, grain, state/mart, one failure proof and limits |
| Why Data Engineering? | Your interest in reliable data plus a concrete learning/project experience |
| What does one fact row mean? | Explicit grain, business key and measures |
| Why did a JOIN increase revenue? | Cardinality and one-to-many duplication, with a tiny example |
| COUNT(*) versus COUNT(key)? | Null-extended LEFT JOIN rows and zero-match groups |
| How are corrections handled? | Source version policy, equal-version conflict and stable key |
| Why retain a delete? | Tombstone blocks resurrection from old input |
| Where is the checkpoint written? | Same transaction as durable state changes |
| What if export fails after commit? | Publication status and re-export from committed state |
| Why not use max occurred_at? | Late availability and source cursor guarantee |
| What does exactly once mean here? | No distributed claim; replay-safe state under explicit assumptions |
| Which errors should retry? | Transient versus permanent, bounded budget and one owner |
| What does a data test prove? | Its specific invariant/cases, not universal correctness |
| How do you define freshness? | Clock, timestamp meaning, threshold, future/missing-data policy |
| What is ref in dbt? | Resource resolution/dependency, not API ingestion |
| Why can incremental SUM be wrong? | Old contribution/correction/delete and affected-group rebuild |
| Why might an index be unused? | Selectivity, cost estimates, table size and measurements |
| When would you use Spark? | Workload/distribution need, shuffles/skew, operations and alternatives |
| What must an analyst be allowed to do? | Scoped mart read access, no broad source/write credentials |
| How did you use AI? | A suggestion, validation, rejected case and independent reproduction |
| How can features leak future data? | Availability cutoff, future corrections and chronological splits |
| Tell me about a bug you fixed. | Symptom, smallest reproduction, cause, test and repaired evidence |
| How can another person run your work? | Fresh setup, versions, configuration, commands and expected evidence |
| What don't you know yet? | Specific gap and practice plan without pretending production experience |

## Short answer examples

<details>
<summary>Checkpoint and publication</summary>

The loader writes source state and progress in one PostgreSQL transaction. An injected pre-commit error rolls both back. File export occurs after commit, so an export failure leaves committed data and explicit pending publication. Recovery regenerates the export from committed state. I do not claim that PostgreSQL, files and the warehouse share one atomic transaction.

</details>

<details>
<summary>Replay and deletes</summary>

I keep the highest source version per order ID. Equal consistent versions are replay, conflicting equal versions fail, and stale versions cannot overwrite current state. Deleted B remains a tombstone so replaying an older upsert cannot resurrect it. This relies on a single-source version guarantee and one writer.

</details>

<details>
<summary>Tool choice</summary>

The small fixture needs no distributed cluster. I use PostgreSQL for authoritative transaction state and DuckDB/dbt for local analytical transformations. Prefect coordinates stages. Spark/Airflow/cloud are optional transfer labs; I would choose deeper exposure from a target role or workload requirement rather than add them to every project.

</details>

## Five-minute demo

- 0:00–0:45: problem, input and grain.
- 0:45–1:45: normal source load and reconciled mart.
- 1:45–2:30: replay plus correction/delete behavior.
- 2:30–3:45: controlled failure and repaired recovery.
- 3:45–4:30: tests, fresh setup and delivery.
- 4:30–5:00: assumptions, limitations and next improvement.

Practise an interviewer changing one condition: late revision, duplicate key, zero-order customer, unavailable database or wrong amount unit. Explain before editing. Record unclear answers in notes, then revisit the relevant lesson.

