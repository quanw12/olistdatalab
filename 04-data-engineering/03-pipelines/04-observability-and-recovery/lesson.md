# Batch evidence, publication state and recovery

## Understand it

Observability makes a failure diagnosable: run identity, source identity, stage, counts, timing, outcome and actionable error. A run ledger describes what committed; a log describes execution. Neither a last line saying done nor a stale output file proves that today's work succeeded. Design data commit and file publication as separate states when they cannot share one transaction.

## Syntax and trace

~~~python
import json
print(json.dumps({"run_id": "demo-1", "stage": "publish",
                  "status": "failed", "error_code": "OUTPUT_UNWRITABLE"}))
~~~

A structured event gives a specific failing stage without disclosing a password or an entire sensitive record.

## Engineering connection

An intern who can recover a pipeline and explain evidence is more useful than one who only shows a happy-path screenshot.

Original practice contract; review [sources.md](../../sources.md) for context.


[Reference](https://docs.python.org/3.13/library/logging.html). See also [lesson references](../../../docs/lesson-references.md).
