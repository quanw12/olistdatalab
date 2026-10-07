# CL08 — Learn

## Integrate the boundaries

The final result is evidence that data crossed real services correctly. Reuse your local contracts, but add identity, durable input, job completion and publication verification. Uploading a file alone does not prove that the warehouse or report is correct.

## Syntax — JSON lines

~~~python
import json
with open(path, "w", encoding="utf-8") as file:
    for row in rows:
        file.write(json.dumps(row, sort_keys=True) + "\n")
~~~
The provided batches.json contains two arrays; write each as a separate JSONL object file for BigQuery loads. Preserve the six named fields and exact integer versions. Keep a manifest with batch identity and content hash. Do not put the entire wrapper {b1,b2} into a row loader.

Use one explicit manual writer for the lab. A production schedule needs a durable overlap policy (lease/queue/transactional control) beyond configuring one task. Document this limitation.

[Assignment](exercise.md) · [Hints](help.md)
