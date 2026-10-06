# Metric definitions and honest analytics

## Understand it

A metric needs grain, population, time basis, units and update policy. Current truth by event date differs from what was known as of a date. Denominators, missing groups and deleted orders affect interpretation. A chart cannot fix an incorrect join. An English explanation should state the decision and the evidence without inventing a business causal story.

## Syntax and trace

~~~sql
-- One current active order per id; integer cents.
SELECT customer_id, COUNT(*) AS order_count,
       SUM(amount_cents) AS total_cents
FROM latest_changes
WHERE op = 'upsert'
GROUP BY customer_id;
~~~

This is current active truth. A historical as-of metric requires reconstructing revisions available at its cutoff.

## Engineering connection

Prepare a trustworthy handoff to DA/BI teams, rather than only moving data.

Original practice contract; review [sources.md](../../sources.md) for context.

