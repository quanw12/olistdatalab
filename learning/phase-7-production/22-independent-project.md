# 22 · Dự án độc lập: vận hành đội giao hàng

**Tuần 29–31 · Bắt buộc · Điều kiện:** G4. Một nhánh tự chọn có thể hoàn thành song song. Tra cứu vault: `09 - Projects/Du an thu hai.md`.

## Brief

“Mỗi sáng tôi cần biết đơn giao trễ theo kho, chi phí giao và đơn hoàn tiền để phân bổ nhân sự. Đơn cũ có thể cập nhật sau một tháng. Tôi muốn biết lúc nào báo cáo chưa đủ dữ liệu.”

Không có mã đáp án. Tự sinh nguồn giao hàng mới hoặc dùng dữ liệu công khai có quyền; không đổi tên bảng Olist để gọi là dự án mới.

## Trước khi code

Viết 8 câu hỏi kèm giả định tạm: trễ so với mốc nào, hoàn tiền tính ngày nào, mẫu số có đơn hủy không, timezone, một đơn nhiều lần giao, độ trễ chấp nhận, quyền, ngân sách. Chốt brief một trang.

## Phạm vi tối thiểu

- CSV đơn hàng và JSON/API sự kiện; fixture version cố định để replay offline.
- Python + SQL + một warehouse, một orchestrator, một report/dashboard. Không bắt buộc Kafka/Spark.
- Contract, grain, metric definitions, incremental update/delete, late update 30 ngày, freshness, CI.
- Hai role reader/writer, một drill phục hồi raw.

## Vòng hai

Sau v1: “Một đơn nhiều lần giao; kho chuyển địa chỉ; hoàn tiền cần sửa số quá khứ.” Lưu commit trước/sau, thay đổi grain/SCD2/metric có lý do và test.

## Rubric

| Nhóm | Điểm | Điều kiện |
|---|---:|---|
| Tính đúng | 30 | Keys, NULL, tiền, update/delete, full rebuild đối chứng |
| Vận hành | 25 | Interval, retry, alert, recovery có đo |
| Sản phẩm | 20 | Đáp ứng brief, metric rõ, báo thiếu dữ liệu |
| Bàn giao | 15 | Clone sạch, quyền, README, ADR |
| Giải thích | 10 | Demo quyết định và giới hạn |

Mục tiêu ≥75/100 và không có lỗi trọng yếu nhân tiền, mất dữ liệu, lộ secret hoặc thiếu bằng chứng recovery. Đây là chuẩn học tập, không dự đoán tuyển dụng.

## Hoàn thành khi

- [ ] Brief, sơ đồ, expected bằng tay, CI, evidence.
- [ ] Một người khác tái lập theo README; ghi câu hỏi của họ và sửa hướng dẫn.
- [ ] Demo 5 phút: nhu cầu → kết quả → lỗi → phục hồi → quyết định.
