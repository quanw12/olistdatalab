# ST05 — Learn

## Failure classification changes recovery

Malformed payload bytes are a data problem; a dead database or missing permission is an environment problem. Quarantining every exception would discard valid events during an outage. Decide which failures can be persisted for review and which must stop/retry processing.

## Syntax — digest a rejection

~~~python
import hashlib
payload_sha = hashlib.sha256(raw_bytes).hexdigest()
~~~
Raw records may contain private information. A rejection manifest can retain position, digest and a sanitized reason without copying the entire payload into normal logs. Keep original bytes only in an explicitly controlled quarantine if required.

A Kafka dead-letter publish and a sink transaction are two boundaries. Use a durable database outbox/quarantine first; publish its records separately and handle duplicate delivery by rejection identity. Do not acknowledge the source record merely because produce() queued a DLQ message.

[Assignment](exercise.md) · [Hints](help.md)
