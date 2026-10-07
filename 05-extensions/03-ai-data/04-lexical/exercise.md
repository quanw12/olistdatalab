# AI04 — Assignment

Implement lexical.sql as one SQLite SELECT over the supplied FTS5 chunks table (chunk_id, doc_id, text). Bind :query and :limit. Return chunk_id, doc_id, text, score using bm25(chunks), ascending score then chunk_id. Filter with chunks MATCH :query; LIMIT :limit. The checker uses valid query strings and positive integer limits.

Write a tiny search CLI using sqlite3 parameters to run your query, plus tests for a known token, an absent token and deterministic ties. Use document metadata to attach provenance in the later capstone; do not overwrite source fixtures.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
