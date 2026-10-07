# ST02 — Assignment

Implement encode_event(event) and event_key(event), both validating the complete input. Exactly six keys: event_id, sku, observed_at, version, units, op. event_id/sku are nonempty strings already stripped; observed_at is an aware ISO timestamp string; version exact positive int; units exact int 0–10000; op upsert/delete and delete units must be 0. Reject extra/missing fields or invalid input with ValueError.

encode_event returns UTF-8 bytes of json.dumps(event,sort_keys=True,separators=(",",":")); event_key returns event_id.encode("utf-8"). No mutation. Write producer.py CLI to publish b1/b2 from data/batches.json with delivery checks, finite timeout and nonzero failure. Use the supplied topic and SDK setup.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
