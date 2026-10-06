# DE01 assignment

Read [the retail fixture description](../../data/README.md), [all changes](../../data/all_changes.json) and [the final project contract](../../project/capstone/contract.md). Do not implement the final project yet.

Create **system.md** and **data-flow.md** in this lesson folder:

1. Write the consumer's question, output grain and freshness assumption.
2. Draw or list the stages from source changes to customer totals. For each stage state input, output, key/grain, owner and one possible failure.
3. Trace order A's correction and order B's deletion through those stages. Explain why discarding the deletion record immediately can make an old record reappear.
4. Explain raw change count, latest-state count and active-order count. Calculate the final active amount by hand.
5. Distinguish occurred_at, updated_at and ingestion/run time. Identify which timestamp advances extraction progress and which timestamp groups business-day results.
6. Choose batch or streaming for a daily report on this tiny fixture. State one requirement that would make you reconsider. Explain why Spark/Kafka are not needed to solve this lab.
7. List three unknowns to clarify before applying this design to a real source, including a source-history/update guarantee.

Use exact words for observations and label assumptions. A diagram without grain or failure behavior is incomplete.

## Reflection

Why can a pipeline run successfully while still failing its consumer's requirement?
