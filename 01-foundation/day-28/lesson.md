# Day 28 — Capstone architecture, contracts, and runbook


## Turn an exercise collection into an understandable project

A reviewer should be able to answer: what problem does this solve, how does data move, how is correctness checked, and how can I run it? Good documentation links claims to observable behavior.

Your application already exists from Days14–23. Today consolidate it. Do not add a new framework just to make the architecture look larger. Raw files, Python validation, PostgreSQL staging/mart, Prefect and tests are enough.

## Draw the flow and failure boundaries

Use a small Mermaid diagram in Markdown. Syntax example:

~~~mermaid
flowchart LR
    Input[Saved input] --> Parse[Parse and validate]
    Parse --> Good[Accepted data]
    Parse --> Bad[Rejected data]
~~~

Adapt it to your real pipeline. Show where files persist, where one database transaction begins/ends, and where the success manifest is written. A diagram must reflect implemented behavior, including quarantine and failure paths.

## Document a contract, not just column names

For every field record meaning, type, nullability, timezone/unit, range and identity role. Explain observation time versus request time, source identity and newer-version conflict policy. Include local reporting date derivation and equal-version disagreement.

Lineage means being able to trace an output back to input/run/transform. Your run_id and raw path help, but do not claim full row-level lineage unless you store that mapping. State retention/replay assumptions and what happens if raw files are deleted.

## A runbook answers operational questions

A runbook gives concrete actions for known situations: service unavailable, bad credentials, invalid input, duplicate replay, stale data, partial file publication after DB commit, stopped scheduler and failed CI. Include how to inspect, recover and verify.

A minimal example shape:

~~~text
Symptom: task failed while connecting to PostgreSQL
Inspect: selected host/port/database and server readiness
Recover: start the intended server or correct configuration
Verify: run a read-only connection check, then replay the fixture
~~~

Do not expose passwords in diagnostic commands. Document native and Docker paths separately so someone can choose one complete setup.

## Scope and evidence

The final README should state that weather fixtures are synthetic and live numbers change. Explain single-runner assumptions, current API versus historical replay, and cloud/LLM steps actually performed. Link selected charts and test/CI evidence. Mark unsupported features honestly instead of using a checklist of tool names.

No new dependency is required today.
