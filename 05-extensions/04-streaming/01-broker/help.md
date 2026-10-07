# ST01 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — diagnose one boundary

Check Docker Engine availability, Compose configuration and broker logs separately. A missing daemon is not a Python syntax problem.

### Hint 2 — use the correct addresses

localhost inside Connect means Connect itself. Use broker:9092 and source:5432 inside the Compose network; host programs use mapped localhost ports.

### Hint 3 — describe the topic

Use the provided Kafka CLI command to confirm one partition/one replica. Later experiments can use two partitions, but the CDC ordering lesson explicitly keeps one.

[Return to the assignment](exercise.md)

</details>
