# LAB05 — Learn

## The failure

A stock batch updates two items, then crashes before recording completion. If each row committed independently, retrying applies one adjustment twice. Make stock changes and the batch ledger one transaction. A batch ID alone cannot detect accidental reuse with different content; bind it to a canonical payload digest.

## Syntax — Python/SQLite

~~~python
import hashlib, json
encoded = json.dumps(changes, sort_keys=True, separators=(",", ":")).encode("utf-8")
digest = hashlib.sha256(encoded).hexdigest()
conn.execute("BEGIN")
try:
    # Perform related operations using parameterized SQL.
    conn.commit()
except Exception:
    conn.rollback()
    raise
~~~
The except block re-raises so the caller sees failure. Parameters belong in execute(sql, tuple), not string interpolation. This function owns a new transaction but borrows the connection; never close it or silently commit someone else's active work. Review DE06/DE11.

[Assignment](exercise.md) · [Hints](help.md)
