---
tags: [decourse, python, correctness]
module: 01
---

# Datetime, Decimal và Timezone

## Khi dùng

UTC cho thời điểm/duration; local date cho ngày nghiệp vụ. Tiền dùng Decimal hoặc DECIMAL của database thay cho binary float khi cần đối soát chính xác.

## Ví dụ chạy độc lập

```python
# runnable
from datetime import datetime, timezone
from decimal import Decimal
from zoneinfo import ZoneInfo

local = datetime(2018, 1, 15, 22, 30, tzinfo=ZoneInfo('America/Sao_Paulo'))
utc = local.astimezone(timezone.utc)
assert str(local.date()) == '2018-01-15'
assert str(utc.date()) == '2018-01-16'
assert utc.hour == 0  # Sao Paulo đang có DST: UTC-02

total = Decimal('0.1') + Decimal('0.2')
assert total == Decimal('0.3')
assert Decimal('12.345').quantize(Decimal('0.01')) == Decimal('12.34')
```

Ví dụ rounding cuối dùng mặc định half-even; nghiệp vụ có thể yêu cầu khác, phải quy định rõ. Tạo Decimal từ string, không từ float đã sai số.

## Bẫy DST

`.replace(tzinfo=...)` gắn nhãn timezone, không chuyển thời điểm. Giờ bị lặp khi hết DST cần chính sách `fold`; giờ không tồn tại khi bắt đầu DST cần phát hiện/quarantine. ZoneInfo không tự từ chối mọi local time không hợp lệ.

Olist không cung cấp timezone trong timestamp; America/Sao_Paulo là giả định dự án cần ghi lại và kiểm tra với nguồn. Không xem tên thành phố như bằng chứng chắc chắn timezone của hệ thống nguồn.

## Ứng dụng

Giữ purchase timestamp UTC và purchase local date riêng. Tính số ngày giao theo định nghĩa nghiệp vụ; không trộn duration 24 giờ với chênh lệch calendar date. Frankfurter dùng ngày tỷ giá, ghi rõ ngày carry-forward.

## Tự luyện và ôn

1. Chuyển 2018-07-15 22:30 São Paulo sang UTC, so với tháng 1.
2. Tìm một giờ DST lặp; ghi cách quyết định và tác động nếu không biết fold.
3. Tính 100 lần 0.01 bằng float và Decimal; giải thích cách rounding từng dòng khác rounding tổng.

Liên quan: [[BI Metrics va Data Product]], [[Data Modeling va SCD2]]. Nguồn: [zoneinfo](https://docs.python.org/3/library/zoneinfo.html), [decimal](https://docs.python.org/3/library/decimal.html).
