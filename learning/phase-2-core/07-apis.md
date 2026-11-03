# 07 · APIs and reliability

> **DEcourse:** [Syntax và ví dụ tiếng Việt](../../DEcourse/04%20-%20Core%20DE/API%20Retry%20Pagination%20va%20Replay.md) · [Lịch chuẩn và core/tự chọn](../README.md). Video dùng theo bài chẩn đoán, không bắt buộc xem hết.

**Lịch mới:** 12 · **Điều kiện:** 01, 06

## Goal
Extract data from HTTP APIs safely: timeouts, retries only for errors worth retrying, backoff,
validation before saving, raw responses kept for replay. Serve data with a tiny API too.

## 1. Watch
| Video | What to watch | Length |
|---|---|---|
| [Python Requests Tutorial — Corey Schafer](https://www.youtube.com/watch?v=tb8gHvYlCFs) | All | 25 min |
| [REST API Crash Course — Caleb Curry](https://www.youtube.com/watch?v=qbLc5a9jdXo) | First half (concepts, status codes) | 26 min |
| [FastAPI Course for Beginners — freeCodeCamp](https://www.youtube.com/watch?v=tLKKmouUams) | Week 12 end, for the serving task | 1 h |

## 2. Read
- [requests: quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/) — especially *Timeouts* and *Errors and Exceptions*
- [MDN: HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)
- [Frankfurter API docs](https://frankfurter.dev/) — the FX source used here
- [AWS: exponential backoff and jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/)
- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)

## 3. Syntax sheet
```python
import requests, time, json

r = requests.get("https://api.example.com/items",
                 params={"page": 1, "limit": 100},
                 timeout=(3.05, 30))          # (connect, read) — ALWAYS set one
r.status_code                                 # 200, 404, 429, 503 ...
r.raise_for_status()                          # raises requests.HTTPError for 4xx/5xx
data = r.json()                               # parsed; r.content = raw bytes to save

try:
    requests.get(url, timeout=5)
except requests.Timeout: ...
except requests.ConnectionError: ...

# a custom error that carries a decision
class ApiError(RuntimeError):
    def __init__(self, msg, *, retryable: bool):
        super().__init__(msg)
        self.retryable = retryable

# exponential backoff: 1, 2, 4, 8 ... seconds
for attempt in range(1, 4):
    delay = 1.0 * 2 ** (attempt - 1)

# tests never call the network: pass the dependency in, or monkeypatch it
def fetch(url, session=requests): return session.get(url, timeout=5)
```

## 4. Practice
1. Call a public API without a key (e.g. `https://date.nager.at/api/v3/PublicHolidays/2017/BR`), print the holiday names.
2. Paginate: fetch all pages of `https://jsonplaceholder.typicode.com/posts?_page=N&_limit=10` until an empty list.
3. Make a request time out on purpose (`timeout=0.001`) and catch it.

## 5. Apply to the project — lab 07
Folder: [`labs/07-api`](../../labs/07-api). Write `my_fx.py` until `pytest labs/07-api -v` is green.
The tests use fake responses, no network.
1. `classify(status_code)` → retryable or not. Hint: which codes mean "try again later"?
2. `fetch_with_retry(fetch, attempts, base_delay, sleep)` — retry only retryable errors, wait
   1 s, 2 s, 4 s…; re-raise after the last attempt. `sleep` is injected so tests run instantly.
3. `validate(rows, quotes)` — reject the whole response if it is not a non-empty list, a row has
   no date/quote, or a currency was not requested; drop rows whose rate is not a number.
4. `save_raw(content, path)` — write to `path.tmp` then rename, so a crash never leaves half a file.

Extensions (no tests given — write your own):
- Add jitter to the delay and keep the test deterministic by injecting the random function.
- New source: Brazilian public holidays → `bronze.holidays`, then an `is_holiday` column in `dim_date`.
- Serve: a FastAPI app with `GET /sellers/{seller_id}` that reads `marts.mart_seller_performance`
  read-only. Test it with `fastapi.testclient.TestClient`.

Compare with `src/olist_platform/fx.py` when done.

## 6. Self-check
- Which HTTP errors do you retry, and why not a 404?
- Why validate the whole response before writing anything?
- The API timed out on page 7 of 10. What does your pipeline contain now?

## Done when
- [ ] Lab 07 green, pagination/replay failure scenario demonstrated
- [ ] **Gate 2 almost done** — finish module 08

## Yêu cầu cập nhật · hướng sản phẩm

Bắt buộc fake pagination 10 trang, lỗi trang 7; giữ raw/page manifest và checkpoint sau write. Restart không thiếu/trùng; xử lý cursor lặp và 429/Retry-After có giới hạn. FastAPI serving là tự chọn, không dùng nó thay bài pagination/replay.
