# Day 15 — Reliable HTTP extraction and bounded retries


## Classify failures

A request can fail while connecting, waiting, checking a status, parsing JSON or validating its shape. A 200 body can still be invalid. Use saved data or a fake client to learn this behavior without repeatedly calling a service.

A Session reuses connections. Request syntax:

~~~python
import requests

with requests.Session() as session:
    response = session.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": 21.0285, "longitude": 105.8542,
                "current": "temperature_2m,relative_humidity_2m",
                "timezone": "Asia/Ho_Chi_Minh"},
        timeout=(3, 10),
    )
    response.raise_for_status()
    payload = response.json()
~~~

The tuple sets connection/read timeouts. It is not a strict total wall-clock deadline. This exercise bounds attempts and pauses; a production deadline is a separate policy.

## Retry rules

For this read-only GET, allow three total attempts. Retry connection failures, timeouts, and429/500/502/503/504. Fail other statuses immediately. Malformed JSON or a missing current object is a validation failure, not a transient retry.

Pause1 then2 seconds before attempts 2 and3. No pause after the final failure. Respect Retry-After seconds or HTTP-date; if it requires more than the lab's30-second allowed pause, stop and report deferral/failure instead of retrying early.

~~~python
for attempt in range(1, 4):
    print("attempt", attempt)
    # Perform one request; return on success.
    # Raise on permanent error or exhausted attempts.
~~~

return exits the function. raise propagates failure; a bare raise inside except preserves the current exception. Never return an empty dictionary as fake success.

## Inject replaceable dependencies

Dependency injection means passing a dependency to a function. fetch_envelope accepts a client, sleeper and clock. Real code passes a Session, time.sleep and a UTC clock. Tests pass fakes that record calls and return chosen responses, with no network or waiting.

Capture requested_at immediately before each attempt; the successful attempt's time belongs in the envelope. observed_at comes from provider current.time. Preserve the full successful payload plus city/source/request time. Use open-meteo for live calls, open-meteo-demo for fixtures.

Read: [Requests advanced usage](https://requests.readthedocs.io/en/stable/user/advanced/), [Open-Meteo](https://open-meteo.com/en/docs), [Retry-After](https://www.rfc-editor.org/rfc/rfc9110.html#name-retry-after).

## Minimal class syntax for your fake client

A class defines a kind of object. Each object stores its own attributes. __init__ initializes it; self means the current object. A method is a function attached to that object.

~~~python
class Counter:
    def __init__(self, start=0):
        self.value = start

    def increase(self):
        self.value += 1
        return self.value

counter = Counter(4)
print(counter.increase())  # 5
~~~

Your fake client follows this same shape: store a response list on self, then return its next item from get(). list.pop(0) removes and returns the first item. Raising an exception from get() simulates a connection failure. A fake response exposes status_code, headers, json() and raise_for_status() because those are the members your extractor uses. It does not need the entire Requests implementation.
