---
tags: [decourse, api, reliability]
module: 07
---

# API: Retry, Pagination and Replay

> [!info] Learning goals
> After this note you can: explain HTTP requests, status codes and timeouts; classify failures into retryable and non-retryable; implement bounded retries with exponential backoff, jitter and `Retry-After`; paginate with offsets and cursors without gaps or duplicates; store raw responses for replay; checkpoint progress safely; and test all of it without touching the network.

## 1. HTTP in five minutes

A REST API call is an HTTP **request** (method, URL, query parameters, headers, optional body) answered by a **response** (status code, headers, body — usually JSON).

| Method | Meaning | Safe to retry? |
|---|---|---|
| `GET` | read | yes (idempotent) |
| `PUT` / `DELETE` | replace / delete a resource | yes, by definition idempotent |
| `POST` | create / trigger | **only** with an idempotency key or documented semantics |

| Status | Meaning | Typical action |
|---|---|---|
| 200–299 | success | validate the body anyway |
| 400 | bad request | fix your request; do not retry |
| 401 / 403 | not authenticated / not allowed | fix credentials or permissions; do not retry endlessly |
| 404 | not found | usually do not retry; decide per API contract |
| 408 / 429 | timeout / too many requests | retry with backoff; honour `Retry-After` |
| 500 / 502 / 503 / 504 | server or gateway problem | retry with backoff |

A 200 response does not prove you received all the data: the body may be truncated, empty, an error object, or one page of many.

## 2. Timeouts are mandatory

Without a timeout a request can hang forever and block the pipeline. `requests` has **no default timeout**.

```python
# Pattern: url/token come from configuration; never commit secrets.
response = session.get(url, params={'cursor': cursor}, timeout=(3.05, 30))  # (connect, read) seconds
response.raise_for_status()   # raises HTTPError for 4xx/5xx
payload = response.json()
```

Use a `requests.Session` to reuse connections and set common headers. Never log the token or full URL if it contains credentials.

## 3. Retry with backoff and jitter

Retrying immediately in a tight loop hammers a struggling server. **Exponential backoff** waits 1, 2, 4, 8… seconds; **jitter** randomises the wait so thousands of clients do not retry in sync. Always cap the number of attempts and the total elapsed time.

```python
# runnable
import random

class RetryableHTTPError(Exception):
    def __init__(self, status, retry_after=None):
        super().__init__(status)
        self.status, self.retry_after = status, retry_after

RETRYABLE = {408, 429, 500, 502, 503, 504}

def call_with_retry(fetch, *, sleep, attempts=4, base=1.0, cap=30.0, rng=random.Random(0)):
    for attempt in range(attempts):
        try:
            return fetch()
        except (TimeoutError, RetryableHTTPError) as error:
            status = getattr(error, "status", None)
            if status is not None and status not in RETRYABLE:
                raise                                   # e.g. 400/401/404: do not retry
            if attempt == attempts - 1:
                raise                                   # budget exhausted: fail loudly
            retry_after = getattr(error, "retry_after", None)
            delay = retry_after if retry_after is not None else rng.uniform(0, min(cap, base * 2 ** attempt))
            sleep(delay)                                # never sleep after the last attempt

calls, delays = [], []
def flaky():
    calls.append(1)
    if len(calls) == 1:
        raise RetryableHTTPError(429, retry_after=5)
    if len(calls) == 2:
        raise TimeoutError
    return {"page": 1}

assert call_with_retry(flaky, sleep=delays.append) == {"page": 1}
assert len(calls) == 3 and delays[0] == 5 and 0 <= delays[1] <= 2

def not_found():
    raise RetryableHTTPError(404)
calls_404 = []
try:
    call_with_retry(lambda: (calls_404.append(1), not_found()), sleep=delays.append)
except RetryableHTTPError:
    pass
assert len(calls_404) == 1                              # 404 was not retried
```

Production notes: catch `requests.Timeout` and `requests.ConnectionError`, classify by status code, add a maximum total elapsed time, and log each retry with attempt number and reason. Libraries like `tenacity` or `urllib3.Retry` implement this, but you must still decide the policy.

**Nested retries multiply.** If the extractor retries 4 times and Airflow retries the task 3 times, one bad endpoint can receive 12 requests per page. Decide which layer retries what.

## 4. Pagination

APIs return large results in pages.

| Style | Request | Risk |
|---|---|---|
| Offset/limit | `?offset=200&limit=100` | If rows are inserted/deleted between calls, rows shift: duplicates or gaps |
| Page number | `?page=3` | same as offset |
| Cursor / token | `?cursor=eyJpZCI6MTIzfQ` | Stable if the API implements it well; you must follow `next` exactly |
| Keyset | `?updated_after=…&id_after=…` | Stable with a unique, ordered key |

Rules:

- Follow the API's `next` cursor/link; stop when it is absent, not when a page is "short".
- Detect a **repeated cursor** (the API returning the same cursor again) and stop with an error instead of looping forever.
- Freeze the result set when possible: a snapshot token or a fixed upper bound (`updated_before=<run start>`) prevents the data from changing under you between pages.
- Deduplicate by key after collecting pages, because offset-based APIs can repeat rows.

## 5. Raw storage and replay

Store every response **exactly as received** before parsing:

```text
raw/fx/run_id=2026-11-03T06-00/page=0001.json
raw/fx/run_id=2026-11-03T06-00/page=0002.json
raw/fx/run_id=2026-11-03T06-00/_manifest.json   # pages, cursors, hashes, row counts, status
```

Benefits: if your parsing logic has a bug, you **replay** from raw instead of calling the API again (which may be rate-limited, cost money, or no longer return historical data). It also gives evidence of what the API actually sent.

## 6. Checkpoints

A checkpoint records how far you got (last cursor, last page, last `updated_at`) so a restart can resume.

The ordering rule: **write the data durably first, then advance the checkpoint.**

- Checkpoint first, then crash before writing → that page is skipped forever (data loss).
- Data first, then crash before checkpoint → the page is fetched again on restart (duplicate), which idempotent writes absorb.

So: at-least-once fetching + idempotent writes = correct results. Publish the consistent dataset only at the end of the batch, not page by page.

```python
# runnable
def run(pages, store, checkpoint, fail_on=None):
    start = checkpoint.get("next_page", 1)
    for page_no in range(start, len(pages) + 1):
        if page_no == fail_on:
            raise RuntimeError(f"crash on page {page_no}")
        store[page_no] = pages[page_no - 1]          # 1. write data (idempotent: keyed by page)
        checkpoint["next_page"] = page_no + 1        # 2. then advance the checkpoint

pages = [[f"r{p}{i}" for i in range(2)] for p in range(1, 11)]   # 10 pages
store, checkpoint = {}, {}
try:
    run(pages, store, checkpoint, fail_on=7)
except RuntimeError:
    pass
assert checkpoint["next_page"] == 7 and len(store) == 6
run(pages, store, checkpoint)                        # restart resumes at page 7
rows = [row for p in sorted(store) for row in store[p]]
assert len(rows) == 20 and len(set(rows)) == 20      # no gaps, no duplicates
```

## 7. Testing APIs without the network

- Inject `fetch` and `sleep` (see [[Functions and Error Handling]]); use fake responses for 200, 429 with `Retry-After`, 500, 404, timeouts, malformed JSON and a repeated cursor.
- Use `responses` / `requests-mock` / `pytest-httpserver` for HTTP-level tests.
- Keep one recorded real response as a fixture to catch schema surprises; a nightly integration test can call the real API.

## 8. Applying it to Olist

The project loads daily BRL→USD/VND rates from the Frankfurter API. Lab 07 (`labs/07-api/my_fx.py`) asks you to implement the client with timeouts, retries, raw storage and replay. Module 07 adds a fake 10-page API failing on page 7: restart must produce no gaps or duplicates, with a manifest and a checkpoint written after the data.

## 9. Common mistakes

| Mistake | Effect | Fix |
|---|---|---|
| No timeout | Pipeline hangs forever | `timeout=(connect, read)` |
| Retrying 400/401/404 | Wasted calls, possible lockout | Classify status codes |
| Unbounded retries, no jitter | Thundering herd, endless runs | Cap attempts and time; add jitter |
| Sleeping after the final attempt | Slower failure | Raise immediately |
| Checkpoint before data write | Silent data loss on crash | Data first, then checkpoint |
| Parsing without keeping raw | Cannot replay or prove what was received | Store raw pages + manifest |
| Logging tokens | Secret leak | Redact headers and URLs |

## 10. Exercises

1. Build a fake 10-page API that fails on page 7; restart and prove no gaps or duplicates.
2. Add a 429 with `Retry-After: 3`, a 404 and a repeated cursor; test each behaviour.
3. Delete the parsed output and rebuild it purely from raw pages (replay) with the network disabled.
4. Calculate the maximum number of requests for one page if the client retries 4 times and Airflow retries the task 3 times. How would you reduce it?

> [!example]- Answer for 4
> 4 attempts × 3 task tries = 12 requests. Reduce by letting only one layer retry transient errors (often the client), making Airflow retries rare and for infrastructure failures, and by resuming from a checkpoint instead of starting over.

## 11. Review questions

> [!question]- Why must the checkpoint advance only after the data is durable?
> Otherwise a crash between the two leaves the checkpoint past data that was never written, and the restart skips it permanently.

> [!question]- Why is offset pagination risky on changing data?
> Inserts or deletes between page requests shift row positions, causing duplicates or skipped rows.

> [!question]- What is jitter for?
> To spread retries randomly in time so many clients do not hit the server at the same moment after an outage.

> [!question]- When is retrying a POST safe?
> When the API supports an idempotency key or documents that the operation is idempotent; otherwise a retry can create duplicates.

Related: [[Functions and Error Handling]], [[Incremental CDC and Backfill]], [[Ingestion Contracts and Idempotency]], [[Module 07 - APIs]]. Sources: [requests quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/), [AWS: exponential backoff and jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/), [MDN HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).
