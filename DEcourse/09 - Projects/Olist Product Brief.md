---
tags: [decourse, project, olist]
module: 17
---

# Olist Product Brief

## Người dùng và quyết định

Operations lead muốn điều tra vùng giao trễ và seller có vấn đề; finance analyst cần xem payments theo ngày mà không bị nhân do join. Đây là giả lập yêu cầu sản phẩm để học, không đại diện yêu cầu thật của Olist.

## Ba câu hỏi cần trả lời

1. Payments theo ngày/tháng là bao nhiêu; dữ liệu thiếu payment bao nhiêu đơn?
2. Late-delivery rate theo state, với mẫu số hợp lệ, thay đổi ra sao?
3. Seller nào có volume và tỷ lệ trễ đáng điều tra; drill-down tới order nào?

## Definition of done

- Grain/key mỗi nguồn và mỗi fact rõ; không mất parent vì LEFT JOIN sai điều kiện.
- Tiền source/fact đối soát; payment khác item+freight được báo riêng, nguyên nhân chỉ nêu khi có bằng chứng.
- Raw version/hash, timezone assumption, NULL policy và snapshot freshness được ghi lại.
- Một dashboard có metric definitions và trạng thái dữ liệu.
- Batch thật đã chạy, counts thật trong docs/data-contract; sample dùng cho tests.
- Replay/recovery được kiểm chứng; quyền reader sau publish được thử.

## Môi trường sample/real riêng — PowerShell từ repo

```powershell
# Sample: tạo trong đường dẫn riêng, không trỏ Olist thật.
$env:OLIST_DATA_DIR = "data/sample"
$env:DUCKDB_PATH = "data/warehouse/sample.duckdb"
python -m olist_platform sample --orders 500
python -m olist_platform run --offline

# Real: tự tải dataset đúng quyền về data/real/landing/olist trước.
$env:OLIST_DATA_DIR = "data/real"
$env:DUCKDB_PATH = "data/warehouse/real.duckdb"
python -m olist_platform run
```

Chọn Python trong venv đã cài project. `--offline` dùng FX giả để test, không dùng số đó làm kết quả finance thật. Dữ liệu không được commit vào repo.

## Mốc tích hợp

Module 04 profile thật → module 09 batch thật → module 11 schedule/backfill → module 20 recovery → module 14 cloud → một nhánh extension → nghiệm thu. Không dồn tất cả vào hai tuần cuối.

## Evidence cần lưu

Command/version/input hash, counts/key checks, query reconciliation, một screenshot/dashboard và một incident report có recovery time. Screenshot là minh họa, query/log là bằng chứng kiểm chứng được.

Liên quan: [[BI Metrics va Data Product]], [[Failure Drills]], [[Tien do va bang chung]]. Nguồn dữ liệu: [Olist Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce); kiểm tra điều kiện sử dụng trước khi chia sẻ.
