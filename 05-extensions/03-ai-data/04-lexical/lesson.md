# AI04 — Learn

## Measure a simple baseline first

SQLite FTS5 provides a local full-text index. Lexical retrieval matches indexed tokens; it does not understand semantic similarity. Its BM25 score is ordered with smaller values representing better matches in SQLite's implementation. Score magnitudes are not calibrated probabilities. [FTS5 documentation](https://www.sqlite.org/fts5.html).

## Syntax — SQLite

~~~sql
CREATE VIRTUAL TABLE chunks USING fts5(chunk_id UNINDEXED, doc_id UNINDEXED, text);
SELECT chunk_id, bm25(chunks) AS score
FROM chunks WHERE chunks MATCH :query;
~~~
Named SQL parameters avoid SQL interpolation. FTS MATCH still has its own query grammar: a bound malformed FTS expression can fail. A search CLI should deliberately choose literal-token escaping or expose documented search syntax; do not claim parameterization validates that grammar.

Use the supplied tiny corpus as a baseline. Retain chunk text, doc_id and source metadata so later results can be checked rather than trusted blindly.

[Assignment](exercise.md) · [Hints](help.md)
