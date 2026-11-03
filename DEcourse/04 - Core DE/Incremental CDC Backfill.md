---
tags: [decourse, cdc, incremental]
module: 19
---

# Incremental, CDC và Backfill

## Chọn chiến lược

| Chiến lược | Phù hợp | Giới hạn |
|---|---|---|
| Full snapshot | Dataset nhỏ, nguồn xuất đầy đủ | I/O lớn, cần biết snapshot hoàn chỉnh |
| updated_at watermark | Nguồn có timestamp tin cậy | Hard delete, cùng timestamp, clock skew |
| Log-based CDC | Theo insert/update/delete | Snapshot bootstrap, ordering, retention, quyền nguồn |
| Backfill theo khoảng | Sửa lịch sử hoặc thay logic | Cần version input và kiểm soát overlap với live |

Purchase date khác updated_at khác thời điểm pipeline xử lý. Bản ghi mua tháng trước có thể sửa hôm nay; lookback 3 ngày theo ngày mua bỏ sót nó.

## Merge theo version — Python chạy độc lập

```python
# runnable
events = [
    {'id': 'o1', 'v': 2, 'amount': 120, 'deleted': False},
    {'id': 'o1', 'v': 1, 'amount': 100, 'deleted': False},
    {'id': 'o2', 'v': 1, 'amount': 50, 'deleted': False},
    {'id': 'o2', 'v': 2, 'amount': 50, 'deleted': True},
]
state = {}
for event in events * 3:
    previous = state.get(event['id'])
    if previous is None or event['v'] > previous['v']:
        state[event['id']] = event
active = {key: row for key, row in state.items() if not row['deleted']}
assert list(active) == ['o1']
assert active['o1']['amount'] == 120
assert len(state) == 2  # Giữ tombstone để event cũ không làm o2 sống lại.
```

Đây là fixture minh họa, không phải consumer bền vững: state phải lưu DB, checkpoint sau commit, conflict cùng version cần xử lý rõ.

## Backfill đúng

Input cố định/versioned + interval `[start,end)` + code/config version → output có thể kiểm tra. Chạy cùng interval hai lần phải khớp. Nếu ngày nghiệp vụ đổi, rebuild ngày cũ lẫn mới; partition trở thành rỗng vẫn phải xóa output cũ.

## Ứng dụng và bài bắt buộc

Module 19 yêu cầu update sau 30 ngày, delete, đổi ngày, event cũ đến muộn và tie timestamp. So với full rebuild theo từng key, không chỉ tổng. Với Olist snapshot, `--full-refresh` là baseline đúng đơn giản; incremental chỉ đáng dùng khi có lợi ích đo được và chính sách sửa lịch sử.

## Ôn

Hard delete biến mất khỏi query updated_at như thế nào? Khi nào checkpoint tiến quá sớm gây mất dữ liệu? Làm sao backfill không đè live bằng version cũ?

Liên quan: [[CTE Dedup va Incremental SQL]], [[Airflow Interval va Backfill]], [[Kafka Offsets Replay va Ordering]]. Nguồn: [Debezium Postgres](https://debezium.io/documentation/reference/stable/connectors/postgresql.html), [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html).
