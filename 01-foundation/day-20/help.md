# Day 20 — Orchestration with Prefect flows and tasks


Start with number_demo to verify the server connection. If runs do not appear in your local UI, confirm PREFECT_API_URL in the runner terminal, not only the server terminal.

Import your existing functions; do not paste a second transformation implementation into orchestration.py. Let task inputs be plain values/paths and outputs be data/results. Open the DB connection in the load task and call staging/mart/state helpers there.

Use get_run_logger inside a task/flow, not at module import. Log run ID, stage and counts. Keep retries=0 around fetch_envelope because it already retries. Use cache_policy=None on side-effecting tasks.

For a fake retry demo, arrange a first temporary failure and a later success; log the attempt counter. In the real flow, invalid records follow the defined quarantine policy, while unrecoverable errors raise and produce a failed run. Remove deliberate failpoints after capturing evidence.
