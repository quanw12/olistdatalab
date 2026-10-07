# ST07 — Assignment

Implement sink.py with apply_cdc and a finite CLI consumer. Use decode_cdc but keep this state contract separate from ST04's versioned synthetic events. For each accepted position, atomically persist its digest ledger and current CDC state; apply upsert/delete in stream order. Transport nulls do not create a new business revision; they may be ledgered as processed no-ops. Retain a delete marker for M2. Store topic/partition/last applied offset per entity and define source epoch in your runbook.

Run the initial snapshot (M1=7,M2=3), then the SQL changes above. Inject a process exit after a sink commit and before offset commit; restart with the same group/database. Verify no duplicate application. Follow live-lab.md for connector setup and source updates.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
