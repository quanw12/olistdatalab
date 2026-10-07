# AI06 — Assignment

Implement index_actions(current,event). current is None or the last stored state for this same id. Both state/event use exactly id, version, op, chunk_ids, content_sha. id follows AI01; version exact positive int; op upsert/delete. chunk_ids is a list of unique nonempty strings. upsert requires >=1 chunk and a lowercase 64-hex content_sha; delete requires [] and content_sha=None. Invalid state/event or mismatched IDs raises ValueError.

Return {"state":new copied state,"remove":old chunk IDs to remove,"add":new chunk IDs to add}. New/higher revision: remove all current chunks (if any), add all event chunks, store event. Identical same revision: no actions. Differing same revision: ValueError. Older revision: preserve current with no actions. Preserve list order and do not mutate either input.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
