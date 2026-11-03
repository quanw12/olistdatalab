---
tags: [decourse, python, reliability]
module: 01
---

# Functions và Error Handling

## Khi dùng

Chia logic thành hàm có input/output rõ để kiểm thử. Exception thể hiện lỗi mà caller cần xử lý; không nuốt lỗi rồi tiếp tục xuất dữ liệu sai.

## Ví dụ chạy độc lập

```python
# runnable
def parse_count(text: str | None, *, allow_missing: bool = True) -> int | None:
    if text is None or not text.strip():
        if allow_missing:
            return None
        raise ValueError('count is required')
    try:
        value = int(text)
    except ValueError as error:
        raise ValueError(f'invalid count: {text!r}') from error
    if value < 0:
        raise ValueError('count must be non-negative')
    return value

assert parse_count(' 12 ') == 12
assert parse_count('') is None
try:
    parse_count('bad')
except ValueError as error:
    assert 'invalid count' in str(error)
else:
    raise AssertionError('expected rejection')
```

`*` bắt caller ghi tên tham số `allow_missing`; type hint mô tả hợp đồng, không tự validate runtime. `raise ... from error` giữ nguyên chuỗi nguyên nhân.

## Syntax kiểm soát tài nguyên

```python
# runnable
from io import StringIO

with StringIO('order_id\no1\n') as stream:
    lines = stream.readlines()
assert stream.closed
assert len(lines) == 2
```

## Ứng dụng

Extractor nhận `fetch` và `sleep` từ bên ngoài để test retry không gọi mạng và không chờ thật. Loader raise ContractError; CLI log exception và exit khác 0 để scheduler biết lỗi.

> [!bug] Bẫy
> `except Exception: pass` làm scheduler xanh giả. Default argument `rows=[]` bị chia sẻ giữa nhiều lần gọi; dùng None rồi tạo list mới trong hàm.

## Tự luyện và ôn

- Thêm `parse_count('-1')` và `allow_missing=False` vào test.
- Giải thích lỗi nào retry được, lỗi nào phải sửa input.
- Viết hàm normalize độc lập rồi test trường hợp None/blank.

Liên quan: [[API Retry Pagination va Replay]], [[Testing Logging va CI]]. Nguồn: [Python exceptions](https://docs.python.org/3/tutorial/errors.html).
