---
tags: [decourse, project, independent]
module: 22
---

# Dự án thứ hai: chuyển kiến thức

## Brief không lời giải

“Đội giao hàng cần báo cáo hàng ngày: đơn trễ theo kho, chi phí giao, hoàn tiền và tình trạng dữ liệu chưa đủ. Một đơn có nhiều lần giao; nguồn có thể sửa sau 30 ngày.”

Tạo domain/dữ liệu mới, không copy đổi tên Olist. CSV order + JSON delivery events, timezone rõ, input versioned để replay offline. Bạn tự làm rõ metric và chọn stack tối thiểu.

## Khung dữ liệu gợi ý, không phải đáp án mô hình

```json
{
  "event_id": "delivery-2-v3",
  "order_id": "order-42",
  "attempt_id": "attempt-2",
  "warehouse_id": "wh-1",
  "event_time": "2026-11-02T08:00:00Z",
  "updated_at": "2026-11-03T04:00:00Z",
  "version": 3,
  "status": "delivered"
}
```

Tự quyết định fact order, attempt hay event; không có một grain duy nhất đúng cho mọi câu hỏi. Business key, delete policy và current-state vs history phải ghi rõ.

## Hai vòng

**V1:** brief một trang, 8 câu hỏi/giả định, ERD, pipeline batch, report, contract, tests và freshness. **V2:** thêm refund muộn, warehouse đổi địa chỉ và source schema mới; lưu quyết định tương thích, backfill và bằng chứng không sai lịch sử.

## Acceptance

- [ ] Expected nhỏ tính bằng tay; incremental khớp rebuild.
- [ ] Replay/out-of-order/delete/đổi partition không sai state.
- [ ] Một alert dữ liệu và một recovery drill.
- [ ] Reader/writer, cấu hình không secret, clone sạch.
- [ ] Một người khác review và dựng lại; tự giải thích 5 phút.

Chấm rubric module 22: tính đúng 30, vận hành 25, sản phẩm 20, bàn giao 15, giải thích 10. Mục tiêu ≥75 và không còn lỗi trọng yếu về mất dữ liệu, nhân tiền, secret hay thiếu recovery.

## Ôn

Điểm nào trong Olist không chuyển nguyên sang domain này? Bạn chọn không dùng công cụ nào và vì sao? Yêu cầu nào còn mơ hồ cần hỏi người sử dụng trước khi code?

Liên quan: [[Data Modeling va SCD2]], [[Architecture Decision Record]], [[Interview va Portfolio]].
