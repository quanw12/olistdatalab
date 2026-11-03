---
tags: [decourse, career, portfolio]
module: 18
---

# Interviews and Portfolio

> [!info] Goal
> Show how you think and results you verified yourself. Two projects you can explain beat a long list of tools you never ran. Do not turn an "Advanced" module label into a senior-level claim.

## 1. What employers look for in junior data engineers

- Solid SQL (joins, grain, windows, NULLs) and Python.
- Understanding of data modelling and correctness: can you tell why revenue doubled?
- Reliability thinking: idempotency, retries, backfills, monitoring, recovery.
- Communication: explaining trade-offs, asking about requirements, writing clear PRs and docs.
- Honesty about what you have and have not done.

## 2. Evidence-based CV bullets

```text
Built [pipeline] on [dataset / measured size], with [key decisions].
Validated [correctness proof], recovered from [failure] in [measured time].
Served [user/report], with [metric definition / freshness evidence].
```

Replace placeholders with real numbers. Mark synthetic data as synthetic. If Kafka was only unit-tested, do not claim you operated end-to-end streaming. Do not list Spark, Kafka and LLM if you completed only one branch.

Example (only if true for you): "Built a batch pipeline over 100k Olist orders (DuckDB, dbt, Airflow); reconciled payments to the cent with dbt tests; detected a fan-out bug that doubled revenue; restored the warehouse from raw in 6 minutes during a recovery drill."

## 3. Question bank and where to prepare

| Question | Prepare from |
|---|---|
| What does one row of this fact table mean? | [[Data Modeling and SCD2]] |
| Why is revenue multiplied? | [[JOIN Grain and Fan-out]] |
| Is re-running A/B/A correct? | [[Ingestion Contracts and Idempotency]] |
| How do you handle a 30-day-old update? | [[Incremental CDC and Backfill]] |
| How is a backfill different from rerunning "latest"? | [[Airflow Intervals and Backfill]] |
| How do you detect a green-but-stale job? | [[Observability and Recovery]] |
| When do you not need Spark? | [[Performance and Storage]] |
| How do you catch wrong AI-generated code? | [[Learning with AI]] |
| ROW_NUMBER vs RANK vs DENSE_RANK? | [[Aggregation and Window Functions]] |
| What happens with NOT IN and NULL? | [[SELECT NULL and CASE]] |
| At-least-once vs exactly-once? | [[Kafka Offsets Replay and Ordering]] |
| How do you keep secrets and PII safe? | [[Security and Governance]] |

Answer structure for design/behaviour questions: **situation → what you did → how you verified → what you learned / would change.**

## 4. 45-minute mock interview

- 10 min SQL on a fixture with NULLs and 1:n relationships.
- 10 min design from a brief (ask clarifying questions first!).
- 10 min debugging an incident (missing partition, doubled revenue).
- 10 min trade-offs and AI usage.
- 5 min self-assessment of what you did not understand.

Do one round in your native language and one in simple English.

## 5. 3–5 minute demo

Need → architecture diagram → a verification query → one incident → recovery → limits. The audience must be able to tell what really ran and what is only a plan.

## 6. Portfolio repository checklist

- [ ] README: problem, architecture diagram, how to run (sample data), results with real numbers, limits.
- [ ] Tests and CI badge that run your code.
- [ ] Docs: data contract, ADRs, runbook, an incident report.
- [ ] No secrets, no large data, clean history.

## 7. Review questions

> [!question]- If an interviewer removed tool names from your CV, could you still describe the problem you solved?
> You should: the problem, constraints, decisions, verification and outcome matter more than the tool list.

> [!question]- What should a senior engineer review before you deploy to production?
> Data model and grain, idempotency/backfill behaviour, permissions and secrets, monitoring and alerting, cost, and the rollback plan.

Related: [[Progress and Evidence]], [[Second Project]], [[Failure Drills]], [[Module 18 - Portfolio and Interviews]].
