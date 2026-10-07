# LAB02 — Learn

## Separate the boundary from the domain

An upstream API renamed fields. Your downstream code should continue receiving one stable shape. An adapter validates the external response, then returns the internal contract. It should not silently invent a missing quantity or accept an unknown API version.

## Syntax — Python

~~~python
version = payload.get("api_version")
if type(version) is not int:
    raise ValueError("api_version must be an integer")
try:
    item = payload["item"]
except (KeyError, TypeError) as exc:
    raise ValueError("missing item") from exc
~~~
type(x) is int excludes bool; isinstance(True, int) is True. str.isdecimal() accepts some non-ASCII digits, so an ASCII-only contract needs a stricter check. A new dictionary avoids mutating the raw payload. Review Python functions/errors and DE04 for contract evolution.

Treat compatibility as explicit support for v1 and v2. Preserve the raw response for diagnosis; the adapter itself performs no network call.

[Assignment](exercise.md) · [Hints](help.md)
