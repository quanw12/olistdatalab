# Logging and observable failures

Original Python-for-DE extension. [Source reference](https://docs.python.org/3.13/howto/logging.html).

## Concept and purpose

print is useful for an exercise result. logging gives operational messages a severity and a destination. DEBUG is diagnostic detail; INFO describes normal progress; WARNING describes something unexpected that can be handled; ERROR describes a failed operation.

Create a module logger with logging.getLogger(__name__). Configure handlers/formatting once at the entry point using basicConfig, not every time a function runs. logger.info("rows=%s", count) postpones message formatting until needed. logger.exception inside an except block includes a traceback.

A useful event includes an event name, run ID, counts and relevant state. Avoid putting credentials or entire customer records into messages. An allowlist of fields is easier to reason about than deleting a few suspicious keys.

The exercise builds a structured event first and then passes it to a supplied logger. Injecting that dependency makes the behavior testable without files or a running server.

## Syntax example

~~~python
import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger("practice")
logger.info("event=%s accepted=%s", "batch_complete", 3)
~~~

## Trace the example

One INFO event is emitted, normally to stderr. Its exact prefix is configured at the application boundary.

## Apply it to DE

When a scheduled job fails unattended, logs should explain which batch failed and whether data was written.

The problem contract is in [exercise.py](exercise.py). The checker supplies fixtures; it does not contain your implementation.
