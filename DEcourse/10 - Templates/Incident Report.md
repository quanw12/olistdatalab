---
tags: [decourse, template, incident]
status: template
---

# Incident report

## Tác động

Dataset/metric/interval nào sai hoặc thiếu, người dùng bị ảnh hưởng thế nào? Chưa xác định thì ghi rõ, không đoán số.

## Timeline

| Thời điểm và timezone | Sự kiện | Bằng chứng |
|---|---|---|
| Điền | Phát hiện | Log/query |
| Điền | Giảm tác động | Thao tác |
| Điền | Phục hồi | Query đối soát |

## Nguyên nhân

Trigger, giả định thiết kế sai, vì sao test/alert chưa bắt được. Phân biệt nguyên nhân với triệu chứng.

## Recovery

Input version, lệnh, phạm vi backfill, checkpoint, thời gian khôi phục. Có mất dữ liệu không và biết bằng cách nào?

## Kiểm chứng và hành động

- [ ] Keys/counts/tiền/partition khớp đối chứng.
- [ ] Test bắt lỗi trước fix và qua sau fix.
- [ ] Action có chủ sở hữu, hạn và điều kiện hoàn thành.
