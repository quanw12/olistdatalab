# 17 · Capstone: nghiệm thu xuyên suốt

**Lịch:** tích hợp từ module 09; tổng hợp tuần 29–31. **Điều kiện:** core qua G4 và một nhánh đã chọn; không bắt buộc mọi module tự chọn.

> [DEcourse: Olist Product Brief](../../DEcourse/09%20-%20Projects/Olist%20Product%20Brief.md) · [Failure Drills](../../DEcourse/09%20-%20Projects/Failure%20Drills.md) · [Lịch chuẩn](../README.md)

## Mục tiêu

Chứng minh pipeline giải quyết câu hỏi nghiệp vụ, dữ liệu đúng và người khác vận hành được. Không đợi cuối khóa mới chạy dữ liệu thật; module này là checklist nghiệm thu tăng dần.

## Các mốc

| Khi nào | Đầu ra bắt buộc | Evidence |
|---|---|---|
| Module 04 | Profile Olist thật hoặc sample trước khi tải được | Rows/null/key/range và 5 quan sát có query |
| Cuối 09 | Batch Olist thật, live FX, dbt build và reconciliation | Input hash, version, counts thật trong data-contract |
| Cuối 11 | Một dashboard, Postgres, lịch chạy và backfill đúng interval | Logs, proof SQL theo từng ngày, screenshot |
| Cuối 19 | Update cũ 30 ngày, delete, đổi ngày, SCD2 | Incremental so full rebuild theo key |
| Cuối 20 | Stale alert và phục hồi từ raw trên bản sao | Incident report, recovery time, counts/tiền |
| Cuối 21 | Reader/writer, môi trường sạch, rollback | Positive/negative permission tests, release manifest |
| Cuối 14 | Một mart BigQuery, IaC, quyền/chi phí | Plan, dry run, bytes cap, resource cleanup |
| Nhánh tự chọn | Một extension chính dưới đây | Số đo và failure proof |
| Cuối 22 | Dự án mới không lời giải, thay đổi yêu cầu | Brief, ADR, review, demo, rubric |

Giữ log tại `docs/capstone-log.md`: ngày/timezone, code/input/config version, command, expected, actual, vấn đề và fix. Tạo khi bạn chạy; không điền kết quả ước đoán.

## Chọn một extension chính

- **Spark:** RFM khớp SQL, benchmark có skew/partition/shuffle/file count. Olist nhỏ chỉ chứng minh chức năng, không chứng minh scale.
- **Kafka:** broker end-to-end, 10k events, crash/replay, out-of-order và DLQ; đối soát event_id, không chỉ đếm row.
- **ML scoring:** feature known_at, time split, baseline, tracked experiment, batch scoring trên orders đang mở.
- **LLM labelling:** keyword baseline + model trên cùng held-out gold set; schema/unparsed, macro-F1, latency/cost, input/model cache invalidation.

Các nhánh khác, RAG, text-to-SQL và nhiều cloud/BI là mở rộng, không chặn tốt nghiệp core.

## Failure drills core bắt buộc

1. Đổi tên cột/duplicate key: chặn publish, giữ last good, ghi version.
2. Snapshot A→B→A: ra đúng A; output Parquet mất/cũ sau commit được sửa khi retry.
3. API lỗi trang giữa, retry/replay không thiếu/trùng và không publish nửa batch.
4. Update sau 30 ngày, delete, đổi ngày và partition rỗng: kết quả khớp rebuild.
5. Job exit 0 nhưng thiếu partition: freshness phải alert.
6. Mất warehouse bản sao: khôi phục từ raw, đo thời gian và đối soát.
7. Republish mart: reader vẫn đọc được và không ghi/đọc raw.

Kafka/LLM thêm failure drills nếu chọn nhánh đó. Dùng env và thư mục drill riêng; không phá dữ liệu duy nhất. Cập nhật runbook sau mỗi kết quả thực đo.

## Hoàn thành khi

- [ ] G1–G5 có evidence do bạn tạo, không lấy mã mẫu thay kết quả.
- [ ] Core và nhánh đã chọn được ghi đúng trạng thái; phần chưa chạy ghi rõ.
- [ ] Một người khác tái lập batch từ README và review dự án độc lập.
- [ ] Demo giải thích nhu cầu, metric, failure/recovery và một trade-off.
