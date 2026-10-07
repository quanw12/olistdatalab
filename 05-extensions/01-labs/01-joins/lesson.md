# LAB01 — Learn

## Understand the ticket

The inventory report should count movements, but a newly joined audit table makes the totals too large. This is a cardinality bug: one movement can have several audits. Joining before summing repeats the movement's units once for each matching audit. DISTINCT on units would also be wrong when two legitimate movements have equal units.

The required grain is one result per product, including products with no movements. Establish the grain before choosing an aggregation. Review Foundation Day 09 for JOIN/GROUP BY syntax.

## Syntax to inspect the bug — SQLite

~~~sql
SELECT m.event_id, COUNT(a.audit_id) AS audit_count
FROM movements AS m
LEFT JOIN audits AS a ON a.event_id = m.event_id
GROUP BY m.event_id;
~~~
COUNT(column) ignores NULL. COUNT(*) counts a preserved LEFT JOIN row even when there is no movement. COALESCE(SUM(...), 0) supplies zero for an empty group. Aggregate movement facts at their own grain; attach audit information separately only if the report requires it.

## Debugging routine

Run the buggy query, trace M1 through the join, and write the smallest counterexample. A correct current answer is insufficient: adding one audit must leave inventory totals unchanged.

[Assignment](exercise.md) · [Hints](help.md)
