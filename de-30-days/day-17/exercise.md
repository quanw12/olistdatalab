# Day 17 — Incremental loads, corrections, and backfills


Extend the loader with newer-request conflict handling. Create ops.pipeline_state per the contract and extend load to select candidates with the one-day overlap. Commit data/mart/checkpoint together.

Run base, next, next again, then base again. Record counts and the corrected HCMC value each time. Add backfill for saved raw input and local date bounds. Force a failure before transaction completion to prove checkpoint rollback. Explain the overlap's limitation and equal-version conflicts.
