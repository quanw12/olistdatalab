# Labs

Your own code for the learning path. Each lab folder has a file with function signatures,
docstrings and hints (no solutions) and a test file that describes the expected behaviour.

```powershell
pytest labs/01-python -v      # red at first; make it green
```

| Lab | Module | Done |
|---|---|---|
| `01-python` | [01 Python](../learning/phase-1-foundations/01-python.md) | [ ] |
| `06-ingest` | [06 Ingestion and quality](../learning/phase-2-core/06-ingestion-quality.md) | [ ] |
| `07-api` | [07 APIs](../learning/phase-2-core/07-apis.md) | [ ] |
| `19-incremental` | [19 Incremental/CDC](../learning/phase-7-production/19-incremental-cdc.md): replay, version conflicts, delete, moving partitions | [ ] |

Other modules tell you to create your own folder here (`09-dbt/`, `11-airflow/`, `12-spark/`,
`13-kafka/`, `15-ml/`, `16-llm/`) and write the code from scratch, using the tasks and hints in
the module.

Labs are not part of the default `pytest` run (they start red on purpose). Add each one to CI
once it passes (module 08).

Modules 20–21 specify operational/permission drills; create your own `20-operations/` and
`21-delivery/` with evidence after running them. Module 22 is an independent domain project,
not another copy of the Olist reference. The current route is [learning/README.md](../learning/README.md);
syntax and review notes live separately in the [DEcourse vault](../DEcourse/README.md).
