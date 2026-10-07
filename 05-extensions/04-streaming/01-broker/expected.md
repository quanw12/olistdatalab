# ST01 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

Manual checklist: Compose validates; broker runs; synthetic topic describes 1 partition and replication factor 1; host producer can reach advertised broker; diagram distinguishes ordering, durability and group progress. Do not claim production resilience from one broker.

## Reflection

1. What does a committed offset identify?

2. Why can a valid bootstrap address still lead to connection failures?

<details>
<summary>After your reflection: compare the reasoning</summary>

The committed offset is the next position to consume within that partition. A bootstrap address discovers broker metadata; advertised addresses must then be reachable from the client network. Partition order is not topic-wide global order.

</details>

</details>
