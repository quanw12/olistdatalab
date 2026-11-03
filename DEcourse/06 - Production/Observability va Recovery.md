---
tags: [decourse, operations, observability]
module: 20
---

# Observability và Recovery

## Khi dùng

Theo dõi độ tin cậy dữ liệu: đúng, đủ, kịp thời và có thể khôi phục. Scheduler status là một tín hiệu; source freshness, volume, schema và reconciliation là tín hiệu khác.

| Loại | Câu hỏi | Ví dụ |
|---|---|---|
| Freshness | Input/output đã tới kỳ dự kiến? | Thiếu partition hôm qua |
| Volume | Có đủ dòng? | Sụt 90% không có lý do |
| Schema | Contract còn đúng? | Cột bị đổi tên |
| Quality | Nội dung hợp lệ? | Key trùng, FX quá cũ |
| Reconciliation | Các lớp khớp? | Payment source khác fact |

## Phát hiện missing partition — Python chạy độc lập

```python
# runnable
from datetime import date, timedelta

today = date(2026, 11, 3)  # Clock cố định để test tái lập.
expected = {today - timedelta(days=1)}
published = {date(2026, 11, 1)}
missing = expected - published
assert missing == {date(2026, 11, 2)}
job_exit_code = 0
assert job_exit_code == 0 and missing  # Job xanh vẫn phải alert dữ liệu thiếu.
```

Olist lịch sử tĩnh không cần ngày mua mới hôm qua; đo snapshot arrival hoặc dùng feed mô phỏng. Đặt sai freshness definition gây alert vô nghĩa.

## Recovery có kiểm chứng

1. Xác định dataset/interval và người dùng chịu ảnh hưởng.
2. Giữ last good hoặc đánh dấu stale, ngăn downstream dùng số sai.
3. Sửa nguyên nhân, chọn input/code/config version.
4. Replay/backfill đúng phạm vi; không tiến checkpoint sớm.
5. Đối soát keys/counts/tiền và consumer, lưu evidence.
6. Ghi [[Incident Report]], thêm test và cải thiện alert.

**RPO**: mức mất dữ liệu chấp nhận theo thời gian; **RTO**: thời gian khôi phục mục tiêu. Ở lab ghi thời gian thực đo, không tự nhận SLA doanh nghiệp.

## Tự luyện và ôn

[[Failure Drills]] có danh sách. Chọn lỗi sau commit trước Parquet, lỗi API và missing partition; đo thời gian phát hiện/phục hồi. Alert nào thực sự cần người hành động? Nếu alert ồn liên tục thì làm sao cải thiện threshold?

Liên quan: [[Ingestion Contract va Idempotency]], [[Airflow Interval va Backfill]]. Nguồn: [Google SRE SLO](https://sre.google/sre-book/service-level-objectives/).
