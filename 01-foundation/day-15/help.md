# Day 15 — Reliable HTTP extraction and bounded retries


Start with a client returning200, parse the body, then build one envelope. Add the loop only after a single attempt works. Examine status_code before raise_for_status so retryable statuses can be distinguished. Catch Requests Timeout and ConnectionError specifically; keep JSON/shape failures outside that retry category.

A fake response needs status_code, headers, json() and raise_for_status(). A fake client can pop its next response from a list when get() is called. Inject sleeper=recorded_delays.append to record pauses. Use a fixed clock for request metadata.

For Retry-After, try a nonnegative number; otherwise use email.utils.parsedate_to_datetime, compare aware times and clamp past dates to0. An invalid header falls back to normal backoff. A requested wait above30 seconds stops this run.

Log city, attempt, status and delay, without credentials. Save output only after successful parsing. Do not catch every Exception and continue, which would hide programming errors.

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>A tiny fake-response pattern</summary>

~~~python
import requests

class ExampleResponse:
    def __init__(self, status, body):
        self.status_code = status
        self.body = body
        self.headers = {}

    def json(self):
        return self.body

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"status={self.status_code}")
~~~

This is test support, not the extractor. Instantiate it with a parsed copy of api_response.json; a fake client's get method returns the next response. To simulate invalid JSON, make json() raise the same parsing exception your real code catches. To record pauses, pass a list's append method as the sleeper.

</details>
