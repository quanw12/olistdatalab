# 04 · APIs and reliability

**Time:** week 5 · **Stack:** requests, HTTP, retries with backoff, raw replay, FastAPI (serving side)

## Why
Half of real ingestion is APIs: rate limits, pagination, timeouts, partial failures. Reliable
extraction is a core intern task.

## Learn
- HTTP status classes; which errors are worth retrying (timeouts, 429, 5xx) and which are not (4xx)
- Exponential backoff and jitter; timeouts on every request
- Pagination styles: page number, cursor, time windows
- Saving the raw response so you can replay without calling again

## Read in this repo
- `src/olist_platform/fx.py` and `tests/test_fx.py` — the retry tests use fakes, not the network.

## Build
1. Add jitter to the backoff (`delay * random.uniform(0.5, 1.5)`) and keep the tests deterministic
   (inject the random function).
2. Add `olist fx --replay <file>` that loads a saved raw response instead of calling the API.
3. Add a second source: a public holidays API for Brazil (e.g. `date.nager.at`). Store in bronze,
   add `is_holiday` to `dim_date`. **Check:** test with a fake response; holiday count per year.
4. Serve the marts: a small **FastAPI** app with `GET /sellers/{id}/performance` reading DuckDB
   read-only, plus one test with `TestClient`.

## Break it
- Point `URL` at a non-existing host. How many attempts, how long, which exit code?
- Make the fake API return a 200 with an HTML error page. Does `parse()` catch it?

## Interview questions
- How do you avoid hammering an API that is rate limiting you?
- The API returned half the data and then failed. What state is your pipeline in?

## Done when
- [ ] Jitter, replay and the holidays source merged with tests
- [ ] FastAPI endpoint runs locally
