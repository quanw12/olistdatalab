# DE05 assignment

Create schema.sql for current source changes and an analytical fact at one current order per id. Keep tombstones in current state. Design a customer-history dimension in a separate exercise table and write queries.sql testing event-time joins. Use c1 segment student from Sep 1 00:00 UTC until Sep 2 00:00 UTC, professional thereafter. Events immediately before and exactly at the boundary must each match one dimension row. Deliberately show how overlapping intervals multiply facts. Document whether the mart is current truth by occurred date or a historical as-of report.

## Deliverables

schema.sql, queries.sql, model.md with grain/key/metric/time definitions and actual pgAdmin evidence.

## Reflection

Does replacing a customer's current segment reproduce historical segment revenue?

Write your answer before opening expected.md. Keep teaching examples in scratch files; your final implementation belongs in the requested starter.

