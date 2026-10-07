# AI03 — Assignment

Implement chunk_document(doc_id, version, text, size, overlap). doc_id follows AI01's ID rule; version is an exact positive int; text is a string assumed already normalized. size is an exact int 1–1000; overlap is an exact int 0 <= overlap < size. Invalid arguments raise ValueError.

Return a list of dictionaries with exactly chunk_id, doc_id, version, start, end, text. Start at 0; end=min(start+size,len(text)); emit text[start:end]. If end==len(text), stop; otherwise next start=end-overlap. Empty text returns []. Do not generate an extra final overlap-only chunk. Same inputs must give identical IDs/content.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
