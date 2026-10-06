# DE26 assignment

Use data/parcels.jsonl, a new domain. In 4 hours build a CLI that validates parcel_id, revision exact positive int, status in created/transit/delivered/cancelled and nonnegative exact-int weight_g; invalid records quarantine with reasons. Latest revision wins, equal-revision identical replay is allowed, conflicting content fails the batch. Tombstones here are cancelled state. Produce one latest row per parcel and counts by final status plus total weight of delivered parcels. Test empty input, duplicate/replay, stale revision and conflicting equal revision. Do not use an LLM for implementation during this diagnostic. Afterwards ask for hints/review if available. Add a separate 45-minute SQL drill from assessment.md.

## Deliverables

solution.py, tests, README and notes.md with actual time, incomplete items and one bug you fixed.

## Reflection

What should you report when the timebox ends before optional work is finished?

Write your answer before opening expected.md. Keep teaching examples in scratch files; your final implementation belongs in the requested starter.

