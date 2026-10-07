# Retry only transient failures

Original Python-for-DE extension. [Source reference](https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts).

## Concept and purpose

A retry repeats an operation after a failure that may be temporary. Invalid input, an invalid password, or a programming error normally needs correction rather than repetition. Define the retryable exception/status list explicitly.

Bound attempts, use backoff, and decide when to stop. For network code consider provider Retry-After instructions and a total job deadline. A write can succeed remotely while its response is lost; retrying it safely may require an idempotency key or an operation that tolerates repeats.

Inject the operation and sleep functions so tests run without delays. The exercise catches built-in TimeoutError only. A real Requests adapter can translate requests.exceptions.Timeout into this boundary error; do not assume the types are identical.

The final failed attempt must not sleep afterward, because no retry remains. Preserve the last exception so upstream logging can describe the failure.

## Syntax example

~~~python
def attempt():
    raise TimeoutError("simulated timeout")

try:
    attempt()
except TimeoutError as error:
    print(type(error).__name__)
~~~

## Trace

The example reports TimeoutError. A retry wrapper decides whether another attempt is allowed; the operation itself does not loop.

## DE connection

Unbounded retries can leave a scheduled pipeline stuck indefinitely.

Use [exercise.py](exercise.py) for the exact input/output contract.

## API quick reference

| Syntax | Purpose |
|---|---|
| `range(max_attempts)` | Bound total calls; the first request counts as an attempt. |
| `except TimeoutError:` | Catch only the transient exception named in this exercise's contract. |
| `raise` | Re-raise the current exception; do not convert exhausted attempts into success. |
| `sleep(seconds) / 2 ** exponent` | Use the injected sleeper for the declared backoff; no actual sleeping is needed in tests. |
