# AI08 — Learn

## Build the data system behind retrieval

Your capstone ingests documents, normalizes/chunks them, stores provenance and revision state, indexes text, searches and evaluates. A generated chat interface is optional; the required result is a correct, reproducible search system with edited/deleted data handled.

## Syntax — transactional FTS maintenance

~~~python
conn.execute("BEGIN")
try:
    conn.execute("DELETE FROM chunks WHERE doc_id = ?", (doc_id,))
    # Insert checked new chunks and persist revision state in this transaction.
    conn.commit()
except Exception:
    conn.rollback()
    raise
~~~
This snippet illustrates the boundary, not the final indexer. Keep state and FTS in the same SQLite connection/transaction. For optional vectors, persist model/revision and vectors consistently or rebuild the derived index from committed source state. Never silently mix models/dimensions.

Separate a useful local retrieval portfolio from claims about production scale, answer correctness or model training.

[Assignment](exercise.md) · [Hints](help.md)
