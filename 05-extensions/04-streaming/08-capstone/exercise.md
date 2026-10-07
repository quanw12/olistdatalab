# ST08 — Assignment

Deliver two finite runnable paths: synthetic b1/b2 → keyed producer → manual-commit consumer → ST04 sink; PostgreSQL snapshot/update/delete → Debezium → CDC consumer → ST07 sink. Demonstrate duplicate, stale and conflicting synthetic revisions; PK-only CDC delete; malformed-data quarantine; consumer crash/restart; and environment failure without offset advance.

Write your own tests, README, diagram, contracts, sanitized evidence and recovery/cleanup runbook. Add an unfamiliar M4 source row of 2 units and verify active total changes from 13 to 15 without code edits. Stop only the owned p5-streams stack after collecting evidence. Label any path you could not run incomplete; offline checks do not substitute for live proof.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
