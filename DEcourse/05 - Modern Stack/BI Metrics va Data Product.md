---
tags: [decourse, metrics, product]
module: 10
---

# BI, Metrics và Data Product

## Khi dùng

Một dataset hữu ích cần người dùng, câu hỏi, định nghĩa metric, độ trễ, owner và cách nhận biết số liệu chưa đầy đủ. Dashboard đẹp không chữa được grain sai.

## Metric contract

| Trường | Ví dụ học tập |
|---|---|
| Người dùng | Operations lead |
| Quyết định | Điều tra vùng giao trễ |
| Metric | Late-delivery rate |
| Tử số | Delivered orders có actual > estimated |
| Mẫu số | Delivered orders có đủ actual và estimated |
| Loại trừ | Hủy/chưa giao; báo riêng số thiếu timestamp |
| Timezone/ngày | Ngày mua theo giả định timezone nguồn |
| Freshness | Theo input snapshot/partition dự kiến |

## Weighted rate — DuckDB chạy độc lập

```sql
-- runnable
-- expect: [[0.16666666666666666, 0.3]]
WITH groups(state, late, eligible) AS (VALUES ('SP',1,2), ('RJ',1,10))
SELECT sum(late)::DOUBLE / sum(eligible) AS correct_rate,
       avg(late::DOUBLE / eligible) AS wrong_unweighted_average
FROM groups;
-- Expected: 2/12 = 0.166666...; trung bình tỷ lệ sai = 0.3.
```

Tỷ lệ thường không cộng/trung bình trực tiếp; lưu tử và mẫu để aggregate lại. “Revenue” phải phân biệt item value, freight, payment, refund và thời điểm ghi nhận. Không tự gọi chênh lệch payment/item là phí lãi nếu chưa có bằng chứng nguồn.

## Ứng dụng Olist

Chọn 3 câu hỏi trong [[Olist Product Brief]]. Mỗi chart có đơn vị, khoảng ngày, định nghĩa và trạng thái cập nhật; một query drill-down tìm ra các order làm nên số tổng.

## Tự luyện và ôn

Người dùng đổi yêu cầu từ ngày mua sang ngày giao: cần đổi date dimension/metric ra sao? Nếu 20% đơn thiếu estimated date, làm sao hiện confidence/coverage thay vì âm thầm bỏ chúng?

Liên quan: [[SELECT NULL va CASE]], [[Data Modeling va SCD2]], [[Observability va Recovery]]. Nguồn: [Kimball facts](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/).
