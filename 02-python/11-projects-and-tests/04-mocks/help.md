# Help — Dependency injection and mocked HTTP

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Separate transport status from JSON schema validation.

</details>

<details>
<summary>Detailed approach</summary>

Save response, check status, then parse payload. Use isinstance(payload,dict), type(payload.get('count')) is int, and a nonnegative comparison. Status errors should reach a caller that owns retry decisions.

</details>

<details>
<summary>Troubleshooting</summary>

If json is called after a status error, you are swallowing the error. If True passes, exact numeric type validation is missing.

Read the first failing check, compare input/type/output and side effects, then make one focused change. The checker is an executable specification.

</details>

<details>
<summary>Read a mock call</summary>

~~~python
from unittest.mock import Mock

client = Mock()
client.get.return_value.json.return_value = {"status": "ready"}
response = client.get("/health", timeout=2)
response.raise_for_status()
print(response.json()["status"])
client.get.assert_called_once_with("/health", timeout=2)
~~~

A Mock records calls and can return another configured object. return_value describes what a call returns. side_effect can be an exception to raise, or a sequence of successive results. Nothing here sends HTTP.

Your function receives the client as an argument: that is dependency injection. Use it rather than creating a real client inside the function, so tests can control success and failure deterministically. The checker verifies both the returned value and important interactions.

</details>
