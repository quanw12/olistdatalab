---
tags: [decourse, review]
---

# Lịch ôn tập

| Khi nào | Làm gì | Dấu hiệu đã nhớ |
|---|---|---|
| Ngay sau buổi học | Viết 5 dòng giải thích, một ví dụ nhỏ | Tự nói được input/output và điều kiện |
| Sau 1 ngày | Đóng note, viết lại 10–20 dòng | Không chép syntax nguyên xi |
| Sau 7 ngày | Đổi dữ liệu, thêm NULL/duplicate/lỗi | Dự đoán đúng kết quả trước khi chạy |
| Sau 30 ngày | Dùng trong bài toán khác, giải thích trade-off | Biết khi nào không nên dùng |

Đây là lịch gợi ý thủ công, chưa tạo reminder tự động. Đặt ngày ôn trong [[Nhat ky hoc]]; tăng tần suất cho chủ đề đang sai.

## Mỗi tuần 30 phút

1. Chọn 2 note từng thấy khó, trả lời câu hỏi cuối note không mở đáp án.
2. Chạy lại một ví dụ, thay key/cardinality/timezone hoặc thêm event cũ.
3. Viết một câu “Mình từng nghĩ…; ví dụ này cho thấy…”.
4. Chuyển bài yếu sang tuần sau, không chỉ đọc lại phần quen.

## Thẻ tự hỏi

- Khi nào COUNT(*) khác COUNT(column)?
- Tại sao chạy lại không duplicate vẫn có thể giữ dữ liệu cũ?
- Retry trước/sau commit offset khác gì?
- SLO kiểm tra dữ liệu hay kiểm tra scheduler?
- Nhãn AI đúng JSON có chắc đúng nghĩa không?

Xem [[Aggregation va Window Functions]], [[Ingestion Contract va Idempotency]], [[Kafka Offsets Replay va Ordering]], [[Observability va Recovery]], [[LLM Cache Evaluation va Guardrails]].
