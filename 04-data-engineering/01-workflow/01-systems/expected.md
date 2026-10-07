# DE01 evidence checklist

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

- Two documents describe a connected flow with inputs/outputs, grain, ownership and failure behavior.
- The five source changes yield three latest-state IDs, including B's tombstone. Two active orders remain: A=1200 and C=800 cents, totaling 2000 cents.
- A correction changes A's state; B's newer delete blocks its older upsert. Raw versions are not counted as separate active orders.
- Event time describes the business event; update time supports the declared change-feed extraction; ingestion time describes the pipeline's work. A source must actually provide the guarantee you rely on.
- Batch is a defensible choice for the assumed daily small-data requirement; lower-latency or substantially different scale could change that choice. A product name alone is not the justification.
- Unknowns and assumptions are explicit; no claim of production execution is made.

<details><summary>Reflection explanation — reveal after answering</summary>

Successful execution only means the program completed its current operations. The output could use the wrong grain, miss a correction, arrive too late or compute the wrong metric. Acceptance criteria, reconciliation and freshness checks connect technical completion to the consumer's need.

</details>

</details>
