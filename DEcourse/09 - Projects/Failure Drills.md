---
tags: [decourse, project, recovery]
module: 20
---

# Failure Drills

> [!warning] Môi trường thực hành
> Dùng bản sao raw/warehouse ở thư mục drill với env riêng, không phá bản dữ liệu thật duy nhất. Snapshot trước thao tác; không tự động xóa database dùng chung.

## Ma trận nghiệm thu

| Drill | Kỳ vọng | Proof |
|---|---|---|
| Rename/drop cột bắt buộc | Contract fail, last good giữ nguyên | Exception + query version cũ |
| Duplicate key | Không publish | Key/count query |
| Snapshot A→B→A | Cuối là A | Hash đang publish |
| File Parquet thiếu hoặc cũ sau commit | Retry sửa output | Đọc Parquet so DB |
| API lỗi ở trang 7/10 | Không dataset nửa batch | Page manifest + counts |
| API trả 404 | Không retry vô hạn | Request count |
| Update đơn 30 ngày trước | Tiền ngày cũ sửa | So full rebuild theo key |
| Đổi ngày / delete hết một ngày | Partition cũ không giữ số stale | EXCEPT ALL hai chiều |
| Job exit 0 nhưng thiếu batch | Freshness alert | Expected vs published |
| Warehouse drill mất | Rebuild từ raw | Recovery time + reconciliation |
| Reader sau republish | Đọc được mart, không ghi/raw | Test bằng login reader |
| Consumer crash sau write | Redelivery không duplicate/mất | Produced vs event_id sink |
| Review đổi / model đổi | Không tái dùng nhãn cũ | Cache versions + eval |

Kafka/LLM là bắt buộc chỉ nếu chọn nhánh tương ứng; các drill core còn lại phải có evidence. Không ghi “passed” dựa vào đọc code.

## Mẫu ghi kết quả

```text
Drill: ...
Input snapshot/code/config: ...
Trigger: ...
Expected: ...
Actual và query proof: ...
Thời gian phát hiện / phục hồi: ...
Nguyên nhân và giới hạn: ...
Test/commit ngăn tái diễn: ...
```

## Tự hỏi

Lỗi được phát hiện trước hay sau người dùng? Giữ dữ liệu cũ có đánh dấu stale không? Retry có làm tình hình tệ hơn không? Sau sửa, consumer có đọc được schema và quyền cũ không?

Liên quan: [[Incident Report]], [[Observability va Recovery]], [[Ingestion Contract va Idempotency]].
