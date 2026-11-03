---
tags: [decourse, ml, elective]
module: 15
---

# ML Features và Point-in-time

## Khi dùng

DE tạo dataset huấn luyện/scoring đúng grain, thời điểm và version. Ưu tiên feature availability, leakage, reproducibility; không cần học mọi model để làm DE.

## Point-in-time join — DuckDB chạy độc lập

```sql
-- runnable
-- expect: [["o1", 0.2]]
WITH predictions(order_id, at_time) AS (
    VALUES ('o1',TIMESTAMP '2026-01-02 10:00:00')
), feature_versions(order_id, known_at, risk) AS (
    VALUES ('o1',TIMESTAMP '2026-01-01 10:00:00',0.2),
           ('o1',TIMESTAMP '2026-01-03 10:00:00',0.9)
)
SELECT p.order_id, f.risk
FROM predictions p LEFT JOIN feature_versions f
  ON p.order_id=f.order_id AND f.known_at <= p.at_time
QUALIFY row_number() OVER (PARTITION BY p.order_id, p.at_time ORDER BY f.known_at DESC)=1;
-- Expected: o1,0.2; không lấy giá trị biết sau thời điểm dự đoán.
```

`known_at` là lúc thông tin thực sự có thể dùng, không chỉ event_time nguồn. Một thuộc tính sản phẩm hiện tại có thể không phải thuộc tính lúc order được duyệt. Chia train/test theo thời gian chưa tự loại mọi leakage.

## Đánh giá

- Baseline majority/rule trước model; log prevalence.
- Time split có khoảng thời gian rõ; tránh cùng ngày bị chia ngẫu nhiên khi điều đó vi phạm giả định.
- ROC-AUC kèm PR-AUC/average precision, precision/recall ở threshold phù hợp chi phí nghiệp vụ.
- Cohort delivered-only phù hợp target có điều kiện; không tự suy sang tất cả đơn hủy/chưa giao.
- Dataset/code/feature/model version và metric lưu cùng experiment.

## Ứng dụng Olist

Không dùng delivery_days, review_score hoặc trạng thái cuối cùng làm feature dự đoán tại approval. Kiểm tra từng feature “biết lúc nào?”, không chỉ deny-list tên cột. Scoring orders đang mở cần query riêng; feature training và scoring cùng semantics.

## Tự luyện và ôn

Thêm feature biết sau delivery và quan sát metric tăng; giải thích vì sao vô dụng ở thời điểm dự đoán. So baseline và model trên cùng test set. Drift dữ liệu khác model quality giảm thế nào?

Liên quan: [[Data Modeling va SCD2]], [[LLM Cache Evaluation va Guardrails]]. Nguồn: [scikit-learn leakage](https://scikit-learn.org/stable/common_pitfalls.html), [model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html).
