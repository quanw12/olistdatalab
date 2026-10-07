# ST06 — Learn

## CDC is not the synthetic event schema

Debezium records snapshots (r), creates (c), updates (u) and deletes (d). Upserts use after; deletes use before. Under PostgreSQL's default replica identity, a delete may provide only its primary key, not all old columns. A following Kafka null value is a transport tombstone, distinct from the business delete event. [PostgreSQL connector reference](https://debezium.io/documentation/reference/3.3/connectors/postgresql.html).

## Syntax — Python envelope access

~~~python
envelope = value.get("payload", value)
operation = envelope["op"]
row = envelope["after"]
~~~
Validate each boundary before indexing. A JSON converter can wrap an event in schema/payload or emit the plain envelope depending on configuration. The live lab disables schemas for simpler inspection.

The source LSN is useful source-position evidence, not a globally unique business revision. Do not fabricate delete version=current+1 to fit ST04: this source table has no business version. ST07 uses ordered Kafka positions and a separate CDC sink contract.

[Assignment](exercise.md) · [Hints](help.md)
