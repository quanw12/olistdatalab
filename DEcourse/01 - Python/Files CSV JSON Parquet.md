---
tags: [decourse, python, storage]
module: 01
---

# Files, CSV, JSON và Parquet

## Khi dùng

CSV để trao đổi đơn giản, JSON cho cấu trúc lồng, Parquet để phân tích theo cột và lưu kiểu dữ liệu. Dùng pathlib để tránh ghép đường dẫn bằng chuỗi.

## CSV và JSON chạy độc lập

```python
# runnable
import csv
import json
from io import StringIO

source = StringIO('order_id,note\no1,"giao nhanh, dong goi tot"\n')
rows = list(csv.DictReader(source))
assert len(rows) == 1
assert rows[0]['note'] == 'giao nhanh, dong goi tot'
payload = json.dumps(rows, ensure_ascii=False)
assert json.loads(payload) == rows
```

`split(',')` sẽ tách sai comment có dấu phẩy nằm trong quote. Khi đọc file: `path.open(newline='', encoding='utf-8-sig')` xử lý newline và BOM của Excel.

## Ghi file nguyên tử trên cùng filesystem

```python
# runnable
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as directory:
    target = Path(directory) / 'raw.json'
    temporary = target.with_suffix('.json.tmp')
    temporary.write_text('{"batch": 1}', encoding='utf-8')
    temporary.replace(target)
    assert target.read_text(encoding='utf-8') == '{"batch": 1}'
    assert not temporary.exists()
```

Rename cùng filesystem tránh người đọc thấy file viết dở; không tạo transaction chung giữa DB và filesystem, cũng chưa bảo đảm dữ liệu sống sót mọi lỗi nguồn điện.

## Parquet — cần pandas và pyarrow

```python
# runnable
import pandas as pd
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as directory:
    path = Path(directory) / 'orders.parquet'
    expected = pd.DataFrame({'order_id': ['o1', 'o2'], 'amount': [10, 20]})
    expected.to_parquet(path, index=False)
    actual = pd.read_parquet(path)
    pd.testing.assert_frame_equal(expected, actual)
```

## Ứng dụng và bẫy

Raw API lưu trước transform để replay; Parquet export có thể lỗi sau DB commit, nên retry phải sửa output dù DB đã nạp. Không khẳng định file tồn tại nghĩa là file đúng phiên bản.

## Tự luyện

CSV có dấu phẩy, newline trong quote, BOM và blank: đọc bằng csv rồi chứng minh cách split tay sai. Sau đó xóa Parquet của bản sao và chạy lại loader.

Ôn: lúc nào chọn JSON thay Parquet? Vì sao write-to-temp chưa làm cả pipeline atomic?

Liên quan: [[Ingestion Contract va Idempotency]], [[Performance va Storage]]. Nguồn: [csv](https://docs.python.org/3/library/csv.html), [pandas IO](https://pandas.pydata.org/docs/user_guide/io.html).
