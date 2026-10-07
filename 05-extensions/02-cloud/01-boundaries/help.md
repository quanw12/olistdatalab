# CL01 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — identify durable state

Place raw input in object storage, history in BigQuery and reports in a separate output bucket. A batch identity should survive container replacement.

### Hint 2 — separate deployment from execution

List what the deployer creates versus what the runtime reads/writes. The scheduler needs permission to execute the job, not permission to read your raw data.

### Hint 3 — keep the first slice small

Start with two tiny batches and manual executions. Add scheduling only after correct output/replay behavior. Follow [live-lab.md](../live-lab.md) for the later sequence.

[Return to the assignment](exercise.md)

</details>
