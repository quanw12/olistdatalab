# DE09 assignment

Implement select_window(records,start,end): times are aware ISO strings; return records with start <= updated_at < end, sorted by instant and id, preserving original records. Raise ValueError for a naive timestamp or start >= end. Implement page_after(records,cursor,limit): cursor is None or a two-item (aware ISO time,id) tuple; return records strictly after that pair, ordered and limited. limit must be exact positive int. Input fixtures have unique pairs. Test a tie split across pages, offset equivalence, an empty window and the exact end boundary. Write backfill.md comparing an occurred-time filter against updated-time extraction.

## Deliverables

exercise.py, backfill.md and one boundary test.

## Reflection

Does an overlap window guarantee recovery of arbitrarily late updates?

Write your answer before opening expected.md. Keep teaching examples in scratch files; your final implementation belongs in the requested starter.

