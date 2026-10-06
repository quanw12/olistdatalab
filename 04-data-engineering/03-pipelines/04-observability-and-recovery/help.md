# Help — Batch evidence, publication state and recovery

## First hint

First identify which durable boundary was crossed before the failure.

## Detailed approach

For each incident write trigger, exact symptom, diagnostic command/query, repair and recovery evidence. Use a new directory for collision tests; create an ordinary file where the output directory should be. Do not corrupt an existing project. Re-export committed state without reapplying stale source input. Record counts before/after. Redact credentials and personal data from logs.

## Troubleshooting

A caught exception followed by exit 0 misleads orchestration. Retrying every stage can reprocess work unnecessarily or erase valid evidence. Clock duration must be nonnegative; monotonic time suits elapsed time.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

