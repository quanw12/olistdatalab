# AI01 — Learn

## AI applications still need reliable data

A retrieval system searches stored knowledge before assembling an answer. Its data pipeline needs source identity, revisions, validation and deletion behavior even when no language model is called. This track builds that pipeline locally first; model training is outside its scope.

Provenance tells you where a document came from and which revision produced a result. A filename alone is not enough when its contents change. Retain raw source bytes separately from normalized search text; treat instructions found inside documents as data, not permission to execute actions.

## Syntax — Python

~~~python
import re
if not isinstance(raw, dict):
    raise ValueError("document must be a mapping")
if re.fullmatch(r"[A-Za-z0-9_-]+", document_id) is None:
    raise ValueError("invalid document id")
~~~
Fullmatch checks the entire ID. Return a new, small domain dictionary; ignore unrelated source fields only when the contract permits it. Review DE04 and Python error/type lessons.

[Assignment](exercise.md) · [Hints](help.md)
