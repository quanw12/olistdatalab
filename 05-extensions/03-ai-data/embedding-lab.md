# Optional real embeddings — after AI05

[Track](README.md) · [Sources](../sources.md)

The core uses SQLite FTS5 and vector fixtures. Only this optional lab downloads a real model. No paid LLM API or GPU is required, but package/model downloads use bandwidth, disk and CPU. Do this after the lexical capstone works; record actual performance and retrieval evidence.

## Separate environment — Windows PowerShell

Use a Python interpreter supported by your installed torch/SentenceTransformers wheels. The course pins a direct SentenceTransformers version from PyPI metadata; it is not a complete transitive lock and was not model-executed during authoring. Prefer Python 3.13 as the course reference and record any installation error before changing packages.

~~~powershell
Set-Location "C:\DE Courses"
python -m venv .venv-embeddings
& "./.venv-embeddings/Scripts/python.exe" -m pip install -r "05-extensions/requirements-embeddings.txt"
& "./.venv-embeddings/Scripts/python.exe" -m pip check
$env:HF_HOME = "C:\DE Courses\05-extensions\03-ai-data\output\hf-cache"
~~~

## Minimal syntax example — Python

~~~python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
vectors = model.encode(["Recover a failed batch.", "Persist the source cursor."],
                       normalize_embeddings=True, convert_to_numpy=True)
print(vectors.shape)
~~~

This teaches model/encode syntax, not a completed retrieval implementation. Inspect the [model card](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) and its repository revision before downloading. After the first controlled run, pin revision= to the actual model commit you used. Save model ID/revision, preprocessing/chunk contract, dimension, package lock, CPU runtime and corpus revision. Do not treat a mutable model name as a fully reproduced model.

Before encoding, inspect the model's actual tokenizer lengths and maximum sequence length. The model card describes default truncation beyond 256 word pieces; AI03's character count does not establish a token bound. Choose/chunk passages that fit, or document deliberate truncation and its evaluation impact.

Task: encode your capstone chunks and queries with the same model; feed resulting vectors to your tested ranker; attach provenance; evaluate the same labeled corpus used for lexical search. Compare missed/returned documents, not just a numerical score from different algorithms. Detect dimension/model mismatch. Regenerate embeddings after document edits; remove deleted chunks; test replay. Label a tiny corpus's measured results as a small demonstration rather than general answer-quality evidence.

For answer assembly, return top passages and citation records first. A missing result should produce an explicit no-evidence result. If you later add an LLM, document its separate API/cost/privacy contract and evaluate generated answers separately; document instructions remain untrusted input.
