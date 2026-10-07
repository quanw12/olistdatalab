# ST06 — Assignment

Implement decode_cdc(value). Accept None (decoded Kafka null) or a dict containing either a plain envelope or a payload wrapper; payload=None is also a transport tombstone. Return exactly kind,event_id,row,source_lsn.

Tombstone → kind=tombstone and all other fields None. For r/c/u require after dict with event_id/sku stripped nonempty strings and units exact nonnegative int; return kind=upsert, copied row containing only those three fields, event_id from row. For d require before dict with a stripped nonempty event_id only; return kind=delete,row=None. Extra envelope/row fields may be ignored. source must be a dict; source.lsn may be absent/None or an exact nonnegative int. Unknown op (including truncate), malformed envelope/row/LSN → ValueError. Never mutate input.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
