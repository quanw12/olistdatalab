# Help — Processes, jobs and graceful stopping

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Use a requested termination before a forced termination.

</details>

<details>
<summary>Detailed approach</summary>

Capture practice_pid=$! immediately after starting sleep. Never target a guessed PID or all Python processes. A cleanup function can check that its known temporary directory exists and call rmdir -- "$temporary_dir"; only an empty directory is removed. Register trap cleanup EXIT. Test one process and one directory at a time. A normal shell exit runs the EXIT handler; an uncatchable signal cannot run it.

</details>

<details>
<summary>Troubleshooting</summary>

jobs from another terminal does not show the first shell's job list. A variable captured after another background launch identifies a different PID. A trap using a broad path can remove unrelated work; keep ownership exact.

</details>
