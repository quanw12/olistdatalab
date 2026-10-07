# AI07 — Learn

## Define the question and its ground truth

Retrieval evaluation compares returned evidence to labeled relevant documents. It is distinct from evaluating a generated answer. Label your corpus revision: after a document edit/delete, old expected answers may no longer be valid. Do not use an LLM's confident explanation as ground truth.

This course uses unique-document Precision@k=hits/k, Recall@k=hits/number_of_unique_relevant_docs (0 when none), and MRR@k=1/first_relevant_rank (0 when no hit). Precision uses k even if fewer documents are returned; record that convention. Deduplicate repeated chunks from the same document before taking the top k.

## Syntax — inspect context evidence

~~~python
for rank, doc_id in enumerate(["guide-b", "guide-a"], start=1):
    print(rank, doc_id)
~~~
enumerate supplies a one-based rank here. Decide how your implementation will
retain only the first appearance of each document before applying k.
An answer context should retain document/chunk ID, source_uri and revision. Limit context by a measured budget and abstain when evidence is absent. This track can assemble cited context without calling any language model.

[Assignment](exercise.md) · [Hints](help.md)
