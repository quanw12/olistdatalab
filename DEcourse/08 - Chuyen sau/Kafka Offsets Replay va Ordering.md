---
tags: [decourse, kafka, elective]
module: 13
---

# Kafka: Offsets, Replay và Ordering

## Khi dùng

Feed sự kiện cần nhiều consumer, replay và xử lý gần thời gian thực. Kafka không tự quyết định business key, thời điểm sự kiện hay exactly-once tới database ngoài.

| Khái niệm | Ý nghĩa |
|---|---|
| Key | Ảnh hưởng partition; cùng order nên cùng key khi partitioner/config phù hợp |
| Partition | Log có thứ tự trong partition, không có global order mặc định |
| Consumer group | Các consumer chia partition; group khác đọc độc lập |
| Offset | Vị trí trong một partition, không phải thời điểm nghiệp vụ |
| Lag | Khoảng consumer chưa xử lý, không trực tiếp bằng latency theo giây |

## Commit pattern — cần broker và client

```python
# Pattern; write_idempotently và dead_letter phải do lab triển khai bền vững.
messages = consumer.consume(num_messages=100, timeout=1.0)
for message in messages:
    if message.error():
        handle_broker_error(message.error())
        continue
    write_idempotently(message)  # transaction DB: event_id + state update/DLQ
    consumer.commit(message=message, asynchronous=False)
```

Tắt `enable.auto.commit`; nếu tự quản batch offsets phải hiểu auto offset store và phạm vi đã xử lý. Commit sau write cho at-least-once: crash giữa hai bước tạo redelivery, sink dedup giải quyết. Commit trước write có thể mất dữ liệu. Không commit vượt qua record lỗi chưa lưu DLQ/được xử lý theo policy.

## Event envelope

```json
{
  "event_id": "order-o1-version-2",
  "order_id": "o1",
  "version": 2,
  "event_time": "2026-11-02T10:00:00Z",
  "schema_version": 1,
  "status": "delivered"
}
```

Version/sequence giúp xử lý cùng timestamp; state update chỉ nhận bản mới. Event time khác processing time. Window theo event time cần lateness policy/watermark và xử lý sự kiện quá muộn.

## Bài bắt buộc nếu chọn Kafka

Produce 10k events, kill consumer sau DB write trước offset commit, restart và đối soát event_id; gửi schema lỗi vào DLQ, replay sau sửa. Đo lag, duplicate redelivery và recovery. Mã unit test không chứng minh broker end-to-end đã chạy.

Ôn: thêm consumer khi số consumer vượt partition có tăng song song không? Replay toàn topic cần retention còn đủ không? Dedup event id có giữ state đúng khi out-of-order không?

Liên quan: [[Incremental CDC Backfill]], [[Failure Drills]]. Nguồn: [Confluent Python client](https://docs.confluent.io/kafka-clients/python/current/overview.html), [delivery semantics](https://docs.confluent.io/kafka/design/delivery-semantics.html).
