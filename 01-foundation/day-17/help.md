# Day 17 — Incremental loads, corrections, and backfills


1. Read the state row; on first use there is no lower bound. Parse request times to aware datetimes before filtering. File order is not a sorting guarantee.
2. Select candidates >= watermark minus one day. Process with a version-aware upsert; do not use file position as the version.
3. Add the incoming-newer WHERE condition. Detect equal-version disagreements before overwriting. Refresh the mart from final staging state, not directly from stale input rows.
4. Upsert the maximum checkpoint inside the same transaction. Raise a temporary test exception after writes but before context exit; compare both checkpoint and data afterward.
5. Parse --start/--end with date.fromisoformat and reject end<=start. Convert each observation to its named timezone before taking date(); use start <= local_date < end.
6. Backfill skips the normal incremental filter. Reuse validation/loading, retain the previous checkpoint, and do not delete records outside the selected interval.
7. Label counters accurately: input 4/candidate4/stored 10 is meaningful. Do not call all four candidates 'inserted'.
