# LAB08 — Assignment

Build a small inventory maintenance CLI in app.py using the earlier lab functions through explicit modules or copied, attributed interfaces. Input: a JSON change list {item_id,delta}; a batch ID; a database path under output/. Initialize a new lab database deliberately; do not reset it on every run.

Ticket: valid batches update inventory atomically; replays do nothing; changed content for an old batch ID fails; an injected interruption rolls back; a product report includes zero-stock products. Add at least six regression tests. Then add a new product p04 with initial stock 9 and a batch that subtracts 4: demonstrate that your implementation works without hard-coded fixtures.

Deliver README.md with install/run/check instructions, a reproduction, a short repair rationale, test evidence and a recovery runbook. Implement one ticket slice first, then expand. Do not import a finished external project as your submission.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
