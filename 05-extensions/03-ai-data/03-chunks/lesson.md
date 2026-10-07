# AI03 — Learn

## Chunks are derived records

A search system usually indexes smaller passages, not one entire document. Every chunk needs a document ID, revision and boundaries so you can trace or remove it. Overlap retains context across a boundary but creates redundant passages; evaluation should count unique documents where the metric asks for documents.

## Syntax — Python

~~~python
piece = text[start:end]
chunk_id = f"{doc_id}:{version}:{start}:{end}"
~~~
Slicing excludes end. These are character/code-point offsets in normalized text. They are not tokenizer positions and do not predict a model's maximum input length. A final short chunk should end the loop; creating another overlap-only chunk would duplicate an already-covered ending.

Start with character chunks because the algorithm can be inspected precisely. A production semantic/token-aware chunker is a later substitution with its own tests, not a reason to obscure this contract.

[Assignment](exercise.md) · [Hints](help.md)
