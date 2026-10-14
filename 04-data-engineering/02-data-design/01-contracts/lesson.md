# Data contracts, types and evolution

## Understand it

A data contract states what one record means: key, types, units, time semantics and allowed change. A schema alone cannot explain whether amount is cents or whether a timestamp describes an event or extraction. Decide whether a defect belongs in quarantine or makes an entire batch unsafe. Optional added columns can be compatible; changing a key or unit is a semantic migration even when parsing still succeeds.

## Syntax and trace

~~~python
from datetime import datetime, timezone
value = datetime.fromisoformat("2026-09-01T16:00:00+07:00")
print(value.astimezone(timezone.utc).isoformat())
print(type(True) is int, isinstance(True, int))
~~~

The instant becomes 09:00 UTC. bool subclasses int, so exact type checks matter for a JSON integer contract. Naive timestamps require an explicit source policy; do not infer your machine's timezone.

## Engineering connection

Contracts protect downstream tables and tests from plausible but incorrect inputs.

Original practice contract; review [sources.md](../../sources.md) for context.


[Reference](https://json-schema.org/understanding-json-schema). See also [lesson references](../../../docs/lesson-references.md).
