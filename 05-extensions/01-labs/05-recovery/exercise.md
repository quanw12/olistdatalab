# LAB05 — Assignment

Implement apply_batch(conn, batch_id, changes, fail_after=None).

Schema: items(item_id TEXT PRIMARY KEY, units INTEGER NOT NULL CHECK(units >= 0)); ledger(batch_id TEXT PRIMARY KEY, payload_sha TEXT NOT NULL). Reject an already-active transaction, blank/non-string batch_id, malformed change list, unknown items, negative resulting stock or non-int deltas with ValueError. Each change is exactly {"item_id": nonempty string, "delta": exact int}; duplicates in the list are sequential adjustments. fail_after is None or an exact positive int.

Digest the complete ordered list with the syntax above. Within one transaction: an existing identical batch returns {"status":"replay","rows":0}; changed content for that ID raises ValueError. Otherwise apply every delta and insert the ledger. Return {"status":"applied","rows":len(changes)}. If fail_after=N, raise RuntimeError just after adjustment N, before commit; roll back both tables. Empty changes are a valid applied batch with 0 rows. Convert data/constraint failures to ValueError; re-raise injected RuntimeError. Do not close conn.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
