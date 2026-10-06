# Day 16 — ETL, file layers, and a complete batch pipeline


1. Normalize one row on paper:09:00 local becomes02:00 UTC; request time remains02:01 UTC. Compare payload timezone with configured timezone.
2. Check fields before conversions. Wrap expected field/conversion errors with context. Do not hide all exceptions across the whole program.
3. Append each accepted or rejected result. Never let an invalid row claim a duplicate key before validation.
4. Generate run_id with uuid.uuid4().hex. Save the original list before transformation.
5. Open one connection transaction for load_records and refresh_mart. Only after context exit write the success/warning manifest.
6. On failure keep raw evidence and a failure manifest when possible. Do not overwrite a previous successful run's files.
7. CLI errors must exit nonzero. Document whether warnings use zero or a separate code; a warning is not silent success.
