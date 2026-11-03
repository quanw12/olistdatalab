# 19 · Incremental, CDC và dữ liệu thay đổi

**Tuần 21 · Bắt buộc · Điều kiện:** 06, 09, 11. Tra cứu trong vault: `04 - Core DE/Incremental CDC Backfill.md`.

## Mục tiêu

Giữ kết quả đúng khi bản ghi đến trễ, bị sửa hoặc bị xóa. Phân biệt snapshot, timestamp watermark và log-based CDC. Lookback 3 ngày không giải quyết mọi thay đổi lịch sử.

## Đọc có mục đích

- [dbt incremental](https://docs.getdbt.com/docs/build/incremental-models): unique key và filter.
- [Debezium PostgreSQL](https://debezium.io/documentation/reference/stable/connectors/postgresql.html): snapshot, change event, delete. Cài Debezium là mở rộng, không bắt buộc để hiểu CDC.

## Bài thực hành `labs/19-incremental`

Tự tạo fixture `orders(order_id, order_date, amount, updated_at, is_deleted)`. Mỗi thay đổi có version tăng dần; lưu event time và processing time riêng.

1. Nạp 5 đơn; lưu baseline count và tiền theo ngày.
2. Sửa đơn có order_date cũ 30 ngày nhưng updated_at mới. Chứng minh lọc purchase date bỏ sót.
3. Merge theo key và version; tính lại cả ngày cũ lẫn ngày mới nếu order_date đổi.
4. Thêm tombstone/delete; quy định xóa khỏi mart hay giữ cờ và điều chỉnh aggregate.
5. Replay cùng event; kết quả không đổi. Event cũ đến sau không làm state lùi.
6. Backfill `[start, end)` hai lần; đối chứng full rebuild bằng `EXCEPT ALL` ở hai chiều.
7. SCD2 seller có hai địa chỉ: không overlap; join fact bằng `valid_from <= event_time AND event_time < valid_to`.

Gợi ý: watermark cần xử lý cùng timestamp; hard delete không xuất hiện trong truy vấn updated_at nếu nguồn không có tombstone. Commit checkpoint sau output bền vững.

## Kiểm tra bắt buộc

| Thay đổi | Kỳ vọng |
|---|---|
| Update đơn 30 ngày trước | Một order hiện hành, tiền lịch sử được sửa |
| Delete | Không tiếp tục tính tiền theo chính sách đã chọn |
| Đổi ngày mua | Ngày cũ và mới khớp full rebuild |
| Replay/out-of-order | Không trùng, không quay về version cũ |
| Hai changes cùng timestamp | Có tie-breaker xác định |

## Hoàn thành khi

- [ ] Có tests cho năm tình huống và expected bằng tay.
- [ ] Có ADR chọn watermark/CDC, giới hạn và chính sách delete.
- [ ] Có lệnh backfill theo khoảng, version đầu vào và counts trước/sau.
