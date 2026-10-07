# AI07 — Assignment

Implement score_ranking(got_doc_ids,relevant_doc_ids,k). Both inputs are lists of nonempty string IDs; duplicates allowed. k exact positive int. Invalid types/elements raise ValueError. Deduplicate returned IDs preserving first occurrence, then take first k; relevant IDs form a set. Return exactly precision_at_k, recall_at_k, mrr_at_k as floats using the formulas above. Empty relevant set produces all zero metrics. No mutation.

Evaluate lexical retrieval using labels_b1 in documents.json, then labels_b2 after the index update. In notes, show one missing-evidence query and the context/citation record you would send to an answerer. Keep document content explicitly untrusted.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
