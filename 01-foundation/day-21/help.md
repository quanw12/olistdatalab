# Day 21 — Mini-project 3: schedule and observe repeated runs

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Import the actual decorated flow from orchestration.py. Call .serve only inside the main guard. Pass fixture mode/input/output through parameters using the actual argument names of your flow.

Use Path(__file__).resolve().parent to locate capstone; its parent/data locates fixtures. Convert Path values to strings if the deployment parameters need JSON-compatible values. Do not put open connections in parameters.

Start the server first, then runner. If a deployment is listed but no work executes, check runner terminal and API URL. If authentication fails in the task, remember PowerShell environment variables belong to each terminal.

Compare distinct observation counts after each run. Raw files and run IDs should differ; the logical database should remain stable. This is expected idempotency, not a failure to schedule.

A Ctrl+C shutdown is a demonstration, not a crash-recovery guarantee. Inspect paused state and resume/restart intentionally. Save only sanitized selected screenshots/logs in evidence/, not the whole server database.

</details>
