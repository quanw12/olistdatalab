# LAB01 — Assignment

Implement query.sql as one read-only SQLite SELECT. The checker supplies tables products(product_id TEXT PRIMARY KEY, category TEXT), movements(event_id TEXT PRIMARY KEY, product_id TEXT, units INTEGER), audits(audit_id TEXT PRIMARY KEY, event_id TEXT).

Return columns product_id, total_units, event_count, sorted by product_id. Include every product. Count movements, not audits. Use data/inventory.json as the reproduction. Explain why buggy.sql produces the wrong number; do not edit that demonstration.

Write a regression for an extra M1 audit and another movement with the same units as an existing movement. Do not hard-code product IDs.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
