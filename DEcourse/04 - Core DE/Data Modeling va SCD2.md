---
tags: [decourse, modeling, warehouse]
module: 05
---

# Data Modeling và SCD2

## Khi dùng

Thiết kế bảng theo câu hỏi nghiệp vụ. Grain quyết định một dòng là gì; dimension cung cấp ngữ cảnh, fact ghi sự kiện/measure. Medallion là tổ chức các lớp xử lý, không thay thế mô hình nghiệp vụ.

| Khái niệm | Ví dụ |
|---|---|
| Natural key | seller_id từ nguồn |
| Surrogate key | seller_sk cho từng version dimension |
| Fact grain | Một dòng cho một order item |
| SCD1 | Ghi đè địa chỉ hiện tại |
| SCD2 | Lưu địa chỉ theo khoảng hiệu lực |
| Additivity | Tiền có thể cộng; tỷ lệ phải tính lại từ tử/mẫu |

## SCD2 join — DuckDB chạy độc lập

```sql
-- runnable
-- expect: [["o1", "SP"], ["o2", "RJ"]]
WITH seller_versions(seller_sk, seller_id, state, valid_from, valid_to) AS (
    VALUES (1,'s1','SP',DATE '2026-01-01',DATE '2026-02-01'),
           (2,'s1','RJ',DATE '2026-02-01',DATE '9999-12-31')
), orders(order_id, seller_id, order_date) AS (
    VALUES ('o1','s1',DATE '2026-01-31'), ('o2','s1',DATE '2026-02-01')
)
SELECT o.order_id, d.state
FROM orders o JOIN seller_versions d
  ON o.seller_id = d.seller_id
 AND o.order_date >= d.valid_from AND o.order_date < d.valid_to
ORDER BY o.order_id;
-- Expected: o1 SP; o2 RJ. Khoảng nửa mở tránh match hai version ở ngày biên.
```

## Ứng dụng Olist

Customer_id là khách theo đơn trong dataset; customer_unique_id đại diện người theo mô tả nguồn. Fact orders khác fact items/payments. Dữ liệu snapshot không có lịch sử thay đổi địa chỉ: muốn học SCD2 thì sinh changes có version, không tự gọi snapshot hiện tại là lịch sử đầy đủ.

## Bẫy

Join dimension hiện tại vào fact cũ sẽ viết lại ngữ cảnh lịch sử. SCD2 có overlap làm fan-out; gap làm mất match. Late-arriving dimension cần unknown member hoặc cập nhật fact có kiểm soát.

## Tự luyện và ôn

Vẽ kho của quán cà phê với 2 fact khác grain. Thêm seller chuyển state và order đúng ngày biên; test không overlap và mỗi fact match đúng một version. Khi nào SCD1 phù hợp hơn SCD2?

Liên quan: [[JOIN Grain va Fanout]], [[Incremental CDC Backfill]], [[BI Metrics va Data Product]]. Nguồn: [Kimball techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/).
