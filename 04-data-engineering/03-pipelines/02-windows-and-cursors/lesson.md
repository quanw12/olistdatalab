# Event time, extraction cursors and backfills

## Understand it

A watermark summarizes source progress under an ordering assumption. An event-time maximum cannot discover late-arriving events with older occurred_at. A composite extraction cursor can break timestamp ties using a stable ID. This lab's source guarantees unique (updated_at,id) pairs per page set; a real change feed may need an additional revision/event key. Overlap and replay cover bounded lateness only, not arbitrary history.

## Syntax and trace

~~~sql
-- A lexicographic cursor, under the source's stable ordering contract.
WHERE updated_at > :cursor_time
   OR (updated_at = :cursor_time AND id > :cursor_id)
ORDER BY updated_at, id;
~~~

A and C sharing updated_at are distinguished by id. The placeholders illustrate a contract; use your driver's parameter style rather than executing colon placeholders blindly.

## Engineering connection

Backfills are controlled reprocessing with the same state rules, not extra blind INSERTs.

Original practice contract; review [sources.md](../../sources.md) for context.


[Reference](https://docs.python.org/3.13/library/datetime.html). See also [lesson references](../../../docs/lesson-references.md).
