---
tags: [decourse, python, foundations]
module: 01
---

# Python cơ bản và Collections

> [!info] Khi dùng
> Python xử lý điều khiển, file, API và logic pipeline. SQL phù hợp biến đổi tập dữ liệu; không cần thay mọi GROUP BY bằng vòng lặp Python.

## Syntax cần nhớ

| Kiểu | Dùng cho | Bẫy |
|---|---|---|
| list | Chuỗi phần tử có thứ tự | Tìm kiếm tuyến tính O(n) |
| tuple | Nhóm giá trị không đổi | Một phần tử cần dấu phẩy `(x,)` |
| set | Membership/dedup | Không dùng thứ tự set làm thứ tự nghiệp vụ |
| dict | Key→value | Gán lại cùng key ghi đè giá trị |
| None | Thiếu giá trị | Không đồng nghĩa 0 hay chuỗi rỗng |

## Ví dụ chạy độc lập

```python
# runnable
from collections import Counter

statuses = ['Delivered', ' delivered ', None, 'canceled']
normalized = [s.strip().lower() if s is not None else None for s in statuses]
counts = Counter(normalized)
assert counts['delivered'] == 2
assert counts[None] == 1

ids = ['o1', 'o2', 'o1', 'o3', 'o2']
seen, duplicates = set(), set()
for order_id in ids:
    if order_id in seen:
        duplicates.add(order_id)
    seen.add(order_id)
assert duplicates == {'o1', 'o2'}
```

Kết quả: hai delivered, một thiếu status; hai ID có lặp. Membership của set trung bình O(1), cả lượt duyệt trung bình O(n).

## Ứng dụng Olist

Module 01, `labs/01-python/olist_basics.py`: normalize status và tìm duplicate. Giữ nguyên raw và dòng nguồn; normalize trong staging để truy vết được.

> [!warning] Không chữa dữ liệu bằng cách che mất lỗi
> `set(ids)` làm mất số lần lặp. Dict ghi đè có thể làm biến mất bản ghi mà không cảnh báo. Phải kiểm tra grain trước khi quyết định dedup.

## Tự luyện

1. Viết đếm trạng thái không dùng Counter, sau đó đối chứng với Counter.
2. Thêm chuỗi rỗng: nó có nên thành None? Ghi chính sách.
3. Đo cách `ids.count(x)` trong vòng lặp với 10k và 20k phần tử.

## Ôn không mở note

- Khi nào chọn set thay vì list?
- Dedup theo ID có thể làm mất thông tin gì?

Liên quan: [[Functions va Error Handling]], [[JOIN Grain va Fanout]]. Nguồn: [Python data structures](https://docs.python.org/3/tutorial/datastructures.html).
