# AI05 — Learn

## Vector retrieval has two boundaries

An embedding model maps text to a vector; a ranker compares vectors. We can test a ranker with supplied numbers without downloading a model. Those numbers do not prove semantic search works. A real embedding demonstration must name the model/revision, preprocessing and actual corpus/query outputs.

Cosine similarity is dot(a,b)/(norm(a)×norm(b)). It is undefined for a zero-length norm. Negative similarity is valid and must not be clamped away. All candidate vectors must use the query dimension and the same model contract.

## Syntax — Python

~~~python
import math
dot = sum(x * y for x, y in zip(a, b))
length = math.sqrt(sum(x * x for x in a))
~~~
zip truncates unequal sequences, so validate dimensions before it. Check math.isfinite for NaN/infinity. For arbitrary huge finite numbers use stable normalization (for example math.hypot and normalized components) to avoid intermediate overflow.

Optional real embeddings use SentenceTransformers on CPU; see [embedding-lab.md](../embedding-lab.md). No paid language model is required.

[Assignment](exercise.md) · [Hints](help.md)
