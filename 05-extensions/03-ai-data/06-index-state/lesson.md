# AI06 — Learn

## Updating metadata is not enough

If an edited document gets new chunks but old chunks stay searchable, the index still answers from obsolete text. An index update must remove old derived records and add the new revision together with durable document state. A delete retains a tombstone to prevent an older revision from restoring the document.

## Syntax — canonical content identity

~~~python
import hashlib, json
content_sha = hashlib.sha256(
    json.dumps(canonical_doc, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()
~~~
Chunk boundaries alone do not detect changed text at the same version. Bind normalized content/provenance to a digest. Compare a revision before planning derived writes. This lesson is a pure planner; it does not claim a transaction across an external vector database and SQLite.

In AI08, use one local database for state and FTS writes so their commit can be atomic. An external index would require a durable reconciliation/outbox strategy.

[Assignment](exercise.md) · [Hints](help.md)
