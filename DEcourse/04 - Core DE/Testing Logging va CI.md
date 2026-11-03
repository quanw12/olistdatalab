---
tags: [decourse, testing, ci]
module: 08
---

# Testing, Logging và CI

## Khi dùng

Test bắt giả định sai trước khi metric tới người dùng. Unit test logic nhỏ; integration kiểm tra kết nối/engine; end-to-end đi qua các lớp. Chỉ test input “đẹp” không chứng minh recovery.

## Ví dụ chạy độc lập

```python
# runnable
def latest(events):
    state = {}
    for key, version, value in events:
        if key not in state or version > state[key][0]:
            state[key] = (version, value)
    return state

events = [('o1', 2, 120), ('o1', 1, 100)]
expected = {'o1': (2, 120)}  # Oracle viết tay, không gọi lại code để tính expected.
assert latest(events) == expected
assert latest(events * 3) == expected
assert latest(list(reversed(events))) == expected
```

## Pattern pytest — cần cài dev

```python
# Pattern trong file test, không chạy riêng trong note.
@pytest.mark.parametrize('text', ['', None])
def test_required_value_rejected(text):
    with pytest.raises(ValueError, match='required'):
        parse_required(text)
```

Fixture `tmp_path` cô lập filesystem; monkeypatch/fake tách network, clock, sleep. Không mock hết engine rồi gọi đó là integration.

## Ma trận test cho pipeline

| Lỗi | Bằng chứng |
|---|---|
| Fan-out | Count/key + payment reconcile |
| Snapshot A/B/A | Output cuối đúng A |
| Output thiếu/stale | Retry khôi phục từ DB/raw |
| API lỗi trang 7 | Không thiếu/trùng, checkpoint đúng |
| Late update/delete | Incremental khớp rebuild |
| Reader ghi dữ liệu | Quyền bị từ chối bằng role thật |

## Logging và CI

Log run_id, source version, interval, rows, duration và error code. Không log token/PII. CI cần cài dependency đúng, lint, unit và integration phù hợp; nếu skip, ghi rõ phạm vi chưa được kiểm tra. Job xanh chỉ chứng minh những gì job đã chạy.

Repo mặc định `testpaths=[tests]`, lab chưa giải không chạy mặc định. Khi hoàn thành thêm job `pytest labs/01-python labs/06-ingest labs/07-api` theo tiến độ; không chuyển lab sang skip vĩnh viễn để làm xanh giả.

## Tự luyện và ôn

Viết một test khiến lời giải ban đầu thất bại, lưu trước/sau fix. Coverage cao có thể vẫn thiếu failure mode nào? Có test nào chỉ chép lại implementation mà không kiểm tra yêu cầu không?

Liên quan: [[Observability va Recovery]], [[Git Branch PR va Review]]. Nguồn: [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html), [Python logging](https://docs.python.org/3/howto/logging.html).
