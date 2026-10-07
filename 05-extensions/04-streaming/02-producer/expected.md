# ST02 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

Key for either M1 revision is b"M1"; differently ordered dictionaries encode identically. Bool version, naive time and a delete with units=7 fail. Live evidence contains broker acknowledgement positions for every intended message and no ignored delivery error.

## Reflection

1. What does produce() returning prove?

2. Why keep the same key for updates/deletes?

<details>
<summary>After your reflection: compare the reasoning</summary>

produce() queues client work; successful delivery callbacks/flush establish broker acknowledgement. They do not establish the consumer database result. The stable entity key groups updates/deletes under the chosen partitioning policy.

</details>

</details>
