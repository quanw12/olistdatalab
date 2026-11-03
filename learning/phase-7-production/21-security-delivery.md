# 21 · Quyền truy cập, tái lập và phát hành

**Tuần 23 · Bắt buộc · Điều kiện:** 10, 20. Tra cứu vault: `06 - Production/Security va Governance.md` và `Delivery va Reproducibility.md`.

## Mục tiêu

Người khác triển khai được từ repo; analyst chỉ đọc dữ liệu được phép; thay đổi có đường rollback.

## Bài thực hành `labs/21-delivery`

1. Tách sample/dev/real bằng env; sample không ghi đè real.
2. Postgres role reader/writer. Dùng chính reader để chứng minh SELECT mart được, INSERT và SELECT raw bị từ chối. Kiểm tra lại sau publish: drop/recreate có thể mất grant/index.
3. Đưa một cột PII giả vào raw, loại/mask trước mart và log. Chỉ dùng dữ liệu có quyền với hosted AI.
4. Ghi Python, dependency, dbt/adapter, image tag/digest, Java nếu dùng Spark. Lưu lock/constraints từ môi trường sạch đã chạy thành công.
5. Clone sạch: tạo venv, cài theo lock, tests, dbt sample, export. Ghi OS thực sự đã kiểm tra, không suy Windows thành Linux.
6. Release v1; thêm cột tương thích; thử thay đổi phá vỡ và kế hoạch chuyển consumer.
7. Rollback code/cấu hình; dữ liệu đã migrate cần phục hồi/forward fix riêng. Chứng minh reader vẫn dùng dataset hợp lệ.

## Hoàn thành khi

- [ ] Test quyền có cả cho phép và từ chối.
- [ ] Fresh clone tái lập với version manifest.
- [ ] PR có vấn đề, thay đổi, kiểm chứng, rollback; được review hoặc self-review sau 48 giờ.
