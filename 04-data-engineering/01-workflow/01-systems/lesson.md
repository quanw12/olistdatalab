# A data system has a purpose

A Data Engineer makes data available in a form consumers can trust and use. A Data Analyst defines/explores metrics and explains results; an ML practitioner may use data to train or evaluate a model. These responsibilities can overlap, but the consumer's requirement determines what the pipeline must deliver.

## Trace the lifecycle

Start with the question: **Who needs which data, at what grain, how fresh, and for what decision?** Then trace:

1. **Source:** a transactional database, API or file. Identify its owner, keys, timestamps and change guarantees.
2. **Ingestion:** fetch/receive a bounded input. Record provenance and avoid committing progress before durable loading.
3. **Raw evidence:** preserve the received representation when permitted. This helps reproduce a parser or transformation failure.
4. **Validated state:** normalize types and maintain the agreed representation, including versions/deletes if the source supplies them.
5. **Transformation and quality:** produce the intended grain; reconcile counts/amounts and reject defects explicitly.
6. **Serving:** expose a mart, report, export or feature dataset that a consumer can understand.
7. **Operation:** observe runs, explain missing/stale data and recover after a failure. This surrounds the other stages.

Raw data, latest state and a daily summary have different grains. Counting their rows as if they represented the same thing creates misleading reconciliation checks. A contract states what a row means, its fields, valid values and update policy; DE04 develops this in code.

## Common system choices

| Choice | Meaning | Question to ask |
|---|---|---|
| OLTP | Frequent transactional work on operational records | What consistency and constraints does the source need? |
| OLAP | Analytical queries across many records | What grain, history and query pattern does the consumer need? |
| Batch | Process a bounded set at an interval | What maximum freshness delay is acceptable? |
| Stream | Process an ongoing flow of events | Is lower latency necessary, and can we operate the extra state? |
| ETL | Transform before loading the serving destination | Where do validation and compute run? |
| ELT | Load first, then transform within an analytical system | How do we isolate raw/staging/mart access and test transformations? |

An engine's name alone does not determine the correctness of a design. A relational database can support small analytical exercises; a tiny file does not justify distributed computation by itself. Choose a tool for a measured requirement, not for its position on a roadmap.

## Read the shape before writing code

Python example, in a scratch file:

~~~python
sample = {"id": "x7", "amount_cents": 350, "updated_at": "2026-09-02T10:00:00+00:00"}
print(sample["id"])
print(type(sample["amount_cents"]).__name__)
~~~

This prints x7 and int. It tells you a field's current representation, not whether its business meaning is correct. Missing-key handling, validation and source change semantics need an explicit contract.

Before connecting systems, record source/destination, owner, grain, keys, event/update/ingestion time, units/currency, freshness target, rerun policy and failure behavior. State what is unknown. If an API only returns the current snapshot, do not promise a complete historical backfill from it.

## References

[IBM: OLAP and OLTP](https://www.ibm.com/think/topics/olap-vs-oltp) explains the workload distinction. Our exercise is an original small design lab; its source guarantees are declared in the supplied fixtures, not inferred from a production API.
