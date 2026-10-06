# Connecting the pagination idea to real HTTP

The checker uses a callable fixture. A real Requests adapter has this shape:
~~~python
import requests

def get_json(session, url):
    try:
        response = session.get(url, timeout=(3, 10))
    except requests.exceptions.Timeout as exc:
        raise TimeoutError("HTTP request timed out") from exc
    response.raise_for_status()
    return response.json()

# Construct requests.Session() at your application boundary.
# Only call get_json with a trusted, deliberately chosen endpoint.
~~~
Do not pass the local tokens page1/page2 as URLs. A real service defines its own URL, cursor parameters and response keys; translate them explicitly into the exercise's items/next interface.

For token-based services, build requests against the same approved base URL and pass the cursor as a parameter. If following returned URLs, verify scheme/host before reusing authorization headers. Load tokens using os.environ; do not print them.

A successful HTTP status does not prove a valid schema. Keep a separate integration test for the actual provider. This file provides syntax, not a claim that every API has the same pagination format.

The adapter translates Requests' timeout exception into built-in TimeoutError, matching the next lesson's retry contract. Those exception types are not interchangeable automatically. timeout=(3, 10) specifies connect and read timeouts; it is not a total deadline for the entire paginated job. The retry exercise deliberately handles only timeouts. A production client also needs provider-specific handling of rate limits/Retry-After, bounded elapsed time and retry-safe operations; do not blindly retry every error or every write request.
