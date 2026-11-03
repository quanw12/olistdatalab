---
tags: [decourse, review]
---

# Review Schedule

Spaced review beats re-reading. Retrieval — pulling the answer out of your head before you check — is what makes knowledge stick.

| When | What to do | Sign that you remember |
|---|---|---|
| Right after the session | Write a 5-line explanation and one small example | You can state input, output and conditions |
| After 1 day | Close the note and rewrite 10–20 lines | You do not copy syntax verbatim |
| After 7 days | Change the data; add NULLs, duplicates or errors | You predict the result correctly before running it |
| After 30 days | Use it in a different problem and explain the trade-off | You know when *not* to use it |

This is a manual schedule; nothing creates reminders automatically. Put review dates in your [[Study Log]] and review more often for topics you keep getting wrong.

## 30 minutes every week

1. Pick 2 notes you found hard and answer the review questions at the end without unfolding the answers.
2. Re-run one example after changing the key, cardinality or timezone, or after adding an old event.
3. Write one sentence: "I used to think …; this example shows …".
4. Move weak topics to next week; do not just re-read the parts you already know.

## Flash-card questions

- When does `COUNT(*)` differ from `COUNT(column)`?
- Why can a re-run produce no duplicates and still keep stale data?
- What is the difference between retrying before and after committing an offset?
- Does an SLO check the data or the scheduler?
- Is an AI label that is valid JSON necessarily correct?
- Why does a moving average over 7 rows not equal a 7-day average?
- Why must you rank versions before filtering out deletes?
- What makes a backfill idempotent?

See [[Aggregation and Window Functions]], [[Ingestion Contracts and Idempotency]], [[Kafka Offsets Replay and Ordering]], [[Observability and Recovery]], [[LLM Caching Evaluation and Guardrails]], [[CTE Dedup and Incremental SQL]].
