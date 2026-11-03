---
tags: [decourse, roadmap]
---

# Study Map

## Lộ trình chuẩn

| Tuần | Chủ đề | Note chính | Điều kiện chuyển tiếp |
|---|---|---|---|
| 1–3 | Python, Git, shell | [[Python co ban va Collections]], [[Git Branch PR va Review]] | Tự đọc CSV, xử lý lỗi, tạo PR |
| 4–6 | SQL | [[JOIN Grain va Fanout]], [[Aggregation va Window Functions]] | JOIN/window đúng với NULL và 1-n |
| 7–8 | DataFrames, profiling | [[DataFrames pandas Polars]] | G1: CSV→Parquet, SQL từ file trống |
| 9–14 | Modeling, ingest, API, CI | [[Data Modeling va SCD2]], [[Ingestion Contract va Idempotency]], [[Testing Logging va CI]] | G2: lab tự viết trong CI |
| 15–16 | dbt trên Olist thật | [[dbt Models Tests va Incremental]] | Counts và reconciliation thật |
| 17–20 | Postgres, Docker, BI, Airflow | [[Docker PostgreSQL va Serving]], [[Airflow Interval va Backfill]] | G3: batch thật + backfill đúng khoảng |
| 21–23 | Thay đổi dữ liệu và vận hành | [[Incremental CDC Backfill]], [[Observability va Recovery]], [[Security va Governance]] | G4: late update/delete, stale alert, recovery |
| 24–25 | Một cloud | [[GCP BigQuery Terraform va Cost]] | Một mart, quyền và bytes billed |
| 26–28 | Một nhánh | [[Spark Partitions Shuffle va Skew]] / [[Kafka Offsets Replay va Ordering]] hoặc [[ML Features va Point in Time]] / [[LLM Cache Evaluation va Guardrails]] | Một extension có số đo |
| 29–31 | Dự án độc lập, nghiệm thu | [[Du an thu hai]], [[Failure Drills]] | G5: chuyển kiến thức, bàn giao được |
| 32 | Portfolio | [[Interview va Portfolio]] | Demo + mock interview |

Khoảng 384–480 giờ cho core + một nhánh. Gate chưa đạt thì tăng thời gian; không tick theo lịch.

## Chọn nội dung

**Bắt buộc:** Python, SQL, Git/shell, modeling, ingestion/API, tests, dbt, Docker/Postgres, một BI, Airflow, incremental, observability/recovery, security, một cloud, hai dự án.

**Tự chọn:** Polars chuyên sâu, nhiều BI/cloud, Spark và Kafka chuyên sâu, ML model tuning, RAG/text-to-SQL. Không phải cứ học nhiều công cụ là đủ điều kiện Senior.

## Chẩn đoán đầu vào

Thử 60–90 phút không AI: đọc CSV, phát hiện key trùng, pre-aggregate trước JOIN, viết running total và một test cho dữ liệu lỗi. Nếu làm tốt, xem video theo chỗ yếu thay vì xem toàn bộ. Sau mỗi phase vẫn làm gate độc lập.

## Từ bài học tới sản phẩm

[[Olist Product Brief]] định nghĩa người dùng và metric. [[Failure Drills]] kiểm tra lúc hệ thống hỏng. [[Du an thu hai]] kiểm tra bạn có làm lại với yêu cầu khác được không. Dùng [[Tien do va bang chung]] để phân biệt đã đọc, đã chạy và đã làm độc lập.
