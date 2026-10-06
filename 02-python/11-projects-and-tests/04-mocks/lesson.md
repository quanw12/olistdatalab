# Dependency injection and mocked HTTP

Original Python-for-DE extension. [Source reference](https://docs.python.org/3.13/library/unittest.mock.html).

## Concept and purpose

Dependency injection passes an external capability into a function instead of constructing it internally. A supplied client can be replaced with a fake in a test.

unittest.mock.Mock records calls, provides return_value, and can raise through side_effect. assert_called_once_with checks a call's arguments. A mock verifies how your code uses the boundary; it does not prove the real service behaves identically.

Validate HTTP status before interpreting the body. A failed response can contain perfectly valid JSON. A successful response may still have the wrong schema.

Mock external dependencies rather than replacing the transformation under test. Keep an optional integration test separate for actual connectivity and service compatibility.

## Syntax example

~~~python
from unittest.mock import Mock
client=Mock()
client.get.return_value.json.return_value={"count":3}
response=client.get("/preview",timeout=5)
print(response.json()["count"])
client.get.assert_called_once_with("/preview",timeout=5)
~~~

## Trace

No network request occurs. The mock returns a configured payload and records the call.

## DE connection

Repeatable tests should not depend on changing data or external uptime.

Use [exercise.py](exercise.py) for the exact input/output contract.
