# AI05 — Assignment

Implement cosine(a,b): lists/tuples of equal nonzero dimension; each value a finite int/float excluding bool; both norms >0. Return cosine in [-1,1], allowing small floating-point tolerance. Invalid input raises ValueError. Handle large finite magnitudes without non-finite intermediate results.

Implement rank_vectors(query,candidates,k). candidates is a list of exactly {"chunk_id":nonempty string,"vector":valid vector}; unique chunk_ids. k is an exact positive int. Return at most k {"chunk_id":...,"score":...} dictionaries, sorted score descending then chunk_id ascending. Validate query even with no candidates; validate every candidate, including those outside top k; no mutation.

First pass fixtures; optionally produce real text embeddings and record actual search/evaluation results. Do not label fixture rankings as model quality.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
