---
tags: [decourse, api, ingestion]
module: 07
---

# API, Retry, Pagination và Replay

## Khi dùng

API có timeout, rate limit, cursor và dữ liệu đổi giữa các trang. Request thành công chưa chứng minh đủ dữ liệu; giữ raw và checkpoint để phục hồi có kiểm soát.

| Tình huống | Hành động |
|---|---|
| Timeout, 429, lỗi server tạm thời | Retry có giới hạn, backoff/jitter, tôn trọng Retry-After nếu có |
| 401/403 | Sửa quyền/credential; không retry vô hạn |
| 404 | Thường không retry; quyết định theo contract API |
| JSON/schema sai | Quarantine/raw; không ghi phần dữ liệu chưa validate |
| POST tạo tài nguyên | Chỉ retry khi semantics/idempotency key cho phép |

## Retry nhỏ chạy độc lập, không gọi mạng

```python
# runnable
def retry(fetch, sleep, attempts=3):
    for attempt in range(attempts):
        try:
            return fetch()
        except TimeoutError:
            if attempt == attempts - 1:
                raise
            sleep(2 ** attempt)

calls, delays = [], []
def fake_fetch():
    calls.append(1)
    if len(calls) < 3:
        raise TimeoutError('temporary')
    return b'{"ok": true}'

assert retry(fake_fetch, delays.append) == b'{"ok": true}'
assert len(calls) == 3 and delays == [1, 2]
```

Ví dụ chỉ minh họa timeout. Production cần requests.Timeout/ConnectionError, status classification, maximum elapsed time và logging không chứa token. Không sleep sau lần thử cuối.

## Pattern requests

```python
# Pattern: url/token do cấu hình cung cấp, không commit secret.
response = session.get(url, params={'cursor': cursor}, timeout=(3.05, 30))
response.raise_for_status()
payload = response.json()
```

Pagination phải theo next cursor của API, chống cursor lặp, lưu page/raw/hash. Checkpoint chỉ tiến khi dữ liệu đã lưu bền vững; cuối batch mới publish dataset nhất quán. Snapshot token hoặc fixed upper bound giúp tránh source đổi giữa trang.

## Tự luyện và ôn

Fake 10 trang, lỗi ở trang 7; restart, chứng minh không thiếu/trùng. Thêm 429 với Retry-After, 404 và cursor lặp. Replay từ raw khi API không còn truy cập được. Retry extractor và retry Airflow lồng nhau làm tăng số request tối đa thế nào?

Liên quan: [[Functions va Error Handling]], [[Incremental CDC Backfill]]. Nguồn: [requests quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/), [AWS backoff/jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/).
