---
tags: [decourse, career, portfolio]
module: 18
---

# Interview và Portfolio

## Mục tiêu

Chứng minh cách suy nghĩ và kết quả do chính bạn kiểm chứng. Hai dự án giải thích được có ích hơn danh sách công cụ chưa chạy. Không biến nhãn module Advanced thành claim Senior.

## CV có bằng chứng

```text
Built [pipeline] on [dataset/size thực đo], with [key decisions].
Validated [correctness proof], recovered from [failure] in [time đo được].
Served [user/report], with [metric definition/freshness evidence].
```

Thay placeholder bằng số thật. Dữ liệu giả ghi synthetic; Kafka chỉ unit-tested thì không ghi đã vận hành streaming end-to-end. Không ghi cả Spark/Kafka/LLM nếu bạn chỉ hoàn thành một nhánh.

## Bộ câu hỏi và note đối chiếu

| Câu hỏi | Chuẩn bị từ |
|---|---|
| Một dòng trong fact là gì? | [[Data Modeling va SCD2]] |
| Vì sao doanh thu bị nhân? | [[JOIN Grain va Fanout]] |
| Chạy lại A/B/A có đúng không? | [[Ingestion Contract va Idempotency]] |
| Update cũ 30 ngày xử lý sao? | [[Incremental CDC Backfill]] |
| Backfill khác rerun latest thế nào? | [[Airflow Interval va Backfill]] |
| Job xanh nhưng stale phát hiện sao? | [[Observability va Recovery]] |
| Khi nào không cần Spark? | [[Performance va Storage]] |
| AI sinh code sai, bạn bắt thế nào? | [[Hoc va lam viec voi AI]] |

## Mock interview 45 phút

10 phút SQL trên fixture có NULL và 1-n; 10 phút thiết kế từ brief; 10 phút debug incident; 10 phút trade-off/AI; 5 phút tự đánh giá phần chưa hiểu. Làm một lượt tiếng Việt, một lượt tiếng Anh đơn giản.

## Demo 3–5 phút

Nhu cầu → sơ đồ → query kiểm chứng → một sự cố → recovery → giới hạn. Người xem phải biết phần nào chạy thật, phần nào mới là kế hoạch.

Ôn: nếu interviewer bỏ tên công cụ khỏi CV, bạn còn mô tả được vấn đề mình giải quyết không? Việc gì cần Senior review trước khi triển khai production?

Liên quan: [[Tien do va bang chung]], [[Du an thu hai]], [[Failure Drills]].
