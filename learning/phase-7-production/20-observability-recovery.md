# 20 · Observability và phục hồi

**Tuần 22 · Bắt buộc · Điều kiện:** 08, 11, 19. Tra cứu vault: `06 - Production/Observability va Recovery.md`.

## Mục tiêu

Phát hiện job xanh nhưng dữ liệu sai/trễ, xác định ảnh hưởng, phục hồi và đối soát. Thực hành trên bản sao, không phá dữ liệu thật duy nhất.

## Bài thực hành `labs/20-operations`

SLO học tập: partition hôm qua sẵn sàng trước 07:00 Asia/Ho_Chi_Minh. Dùng feed mô phỏng có dữ liệu mới; không áp freshness hiện tại lên ngày mua hàng Olist 2016–2018.

1. Audit: run_id, interval, input version, rows read/written/rejected, duration, status.
2. Freshness dựa partition dự kiến/source arrival; không chỉ giờ task kết thúc.
3. Chặn batch mới nhưng cho code exit 0: phát hiện thiếu partition.
4. Giả lập số dòng giảm mạnh; cảnh báo có baseline, minimum sample và cách ghi nhận ngoại lệ hợp lệ.
5. Lỗi sau DB commit nhưng trước export: retry sửa file thiếu và file cũ còn tồn tại.
6. Xóa warehouse trong môi trường drill; phục hồi từ raw, đối soát keys/counts/tiền; đo thời gian và dữ liệu có thể mất.
7. Incident report: tác động, phát hiện, timeline, nguyên nhân, phục hồi, kiểm chứng, ngăn lặp lại.

## SQL kiểm chứng

```sql
-- Pattern: tạo hai bảng audit với các cột này trong lab trước.
SELECT expected_date FROM expected_partitions
EXCEPT
SELECT partition_date FROM published_partitions WHERE status = 'published';
-- Kỳ vọng 0 dòng; khác 0 phải cảnh báo dù scheduler xanh.
```

## Hoàn thành khi

- [ ] Alert nêu dataset, interval, ảnh hưởng và runbook.
- [ ] Ít nhất 4 failure drill có kết quả và recovery time đo được.
- [ ] Không gọi hệ thống production-ready chỉ vì chạy thành công một lần.
