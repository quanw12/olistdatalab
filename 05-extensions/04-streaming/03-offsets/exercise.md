# ST03 — Assignment

Implement safe_offsets(records). Each dict has exactly topic, partition, offset, status. topic nonempty string; partition/offset exact nonnegative ints; status processed/failed. Reject malformed records and conflicting statuses for the same position with ValueError; identical duplicates allowed.

Group by (topic,partition), sort delivered offsets, take processed records up to but excluding the first failed record. Return sorted {"topic":...,"partition":...,"offset":last_safe+1} entries only for partitions with a nonempty safe prefix. Success after a failed record is not safe. Empty input returns []. No mutation.

Write consumer.py with auto commit/store disabled and a finite stop policy. Apply events to the sink first; use safe offsets only for durable outcomes.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
