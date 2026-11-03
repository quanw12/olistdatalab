# DEcourse · Lộ trình Data Engineer hướng sản phẩm

Khoảng **32 tuần, 12–15 giờ/tuần**; điều chỉnh theo bài kiểm tra đầu ra, không theo số video đã xem. `src/` và `dbt/` là mã tham chiếu để so sánh sau khi tự làm, không phải bằng chứng bạn đã hoàn thành khóa.

**Tài liệu tiếng Việt:** [DEcourse](../DEcourse/README.md). Mở thư mục `DEcourse` thành vault Obsidian, bắt đầu tại `00 - Bat dau/DEcourse.md`. Có syntax, ví dụ nhỏ có kết quả, ứng dụng Olist, lỗi thường gặp, bài tập và lịch ôn.

## Cách học và dùng AI

1. Làm bài chẩn đoán trước. Đã làm và giải thích được thì bỏ qua video tương ứng.
2. Mỗi tuần: khoảng 20% đọc/xem, 55% tự xây/debug, 15% kiểm chứng, 10% ôn và ghi chú. Video dài là thư viện tra cứu, không bắt buộc xem hết trong tuần.
3. Trước khi hỏi AI: ghi kỳ vọng, thực tế, ví dụ tái hiện tối thiểu. Yêu cầu giải thích/phản biện; kiểm tra code sinh ra bằng dữ liệu hoặc test độc lập.
4. Mỗi module làm lại một bài từ file trống không AI. Đây là kiểm tra trí nhớ, không cấm AI khi làm sản phẩm.
5. Ôn sau 1, 7, 30 ngày: trả lời câu hỏi, đổi dữ liệu ví dụ, ghi điểm yếu vào vault.

Chỉ ghi công cụ lên CV khi có kết quả chạy thật và giải thích được quyết định, lỗi, cách phục hồi. Nhãn Basic/Advanced trong module mô tả chủ đề, không chứng nhận cấp bậc nghề nghiệp.

## Đường học chính

Giữ nguyên số module và đường dẫn cũ. **Bảng này thay thế lịch tuyến tính trước đây.**

| Tuần | Học phần | Đầu ra |
|---|---|---|
| 1–3 | [01 Python](phase-1-foundations/01-python.md), [02 Git/Linux](phase-1-foundations/02-git-linux.md) | CLI đọc CSV, xử lý lỗi, PR |
| 4–6 | [03 SQL](phase-1-foundations/03-sql.md) | 8 truy vấn, chứng minh fan-out, window functions |
| 7–8 | [04 DataFrames](phase-1-foundations/04-dataframes.md) | Profile và Parquet; pandas + SQL chính, Polars tự chọn |
| 9 | [05 Modelling](phase-2-core/05-data-modeling.md) | Grain, ERD, metric definitions, SCD2 |
| 10–11 | [06 Ingestion](phase-2-core/06-ingestion-quality.md) | Contract, snapshot A→B→A, phục hồi Parquet |
| 12 | [07 API](phase-2-core/07-apis.md) | Pagination, retry, raw replay, checkpoint |
| 13–14 | [08 Test/CI](phase-2-core/08-testing-ci.md) | Lab tự viết trong CI, test dữ liệu sai |
| 15–16 | [09 dbt](phase-3-modern-stack/09-dbt.md) | **Olist thật**, marts, đối soát tiền |
| 17–18 | [10 Docker/Postgres/BI](phase-3-modern-stack/10-docker-postgres-bi.md) | Một dashboard, query plan, transaction, reader role |
| 19–20 | [11 Airflow](phase-3-modern-stack/11-airflow.md) | Quality gate, backfill đúng khoảng |
| 21 | [19 Incremental/CDC](phase-7-production/19-incremental-cdc.md) | Update muộn 30 ngày, delete, SCD2, replay |
| 22 | [20 Observability/Recovery](phase-7-production/20-observability-recovery.md) | Freshness alert, drills, đo recovery time |
| 23 | [21 Security/Delivery](phase-7-production/21-security-delivery.md) | Dev/prod, quyền, manifest phiên bản, rollback |
| 24–25 | [14 Cloud/Terraform](phase-4-scale/14-cloud-terraform.md) | Một cloud, một mart BigQuery, kiểm chứng quyền/chi phí |
| 26–28 | Chọn một nhánh bên dưới | Extension có số đo chất lượng/hiệu năng |
| 29–31 | [22 Dự án độc lập](phase-7-production/22-independent-project.md), [17 nghiệm thu](phase-6-integration/17-capstone.md) | Dự án thứ hai, review, demo, evidence |
| 32 | [18 Portfolio](phase-6-integration/18-portfolio-interviews.md) | CV trung thực, mock interview, demo recovery |

32 tuần là ngân sách cho **core + một nhánh**. Gate chưa đạt thì kéo dài phần đó và giảm tự chọn; không ép học mọi công nghệ trong cùng ngân sách.

## Nhánh tự chọn

- **Scale/Streaming:** [12 Spark](phase-4-scale/12-spark.md), [13 Kafka](phase-4-scale/13-kafka.md). Chọn một extension chính; Spark cần thí nghiệm shuffle/skew, Kafka cần crash/replay test với broker.
- **Data for AI:** [15 ML](phase-5-ml-ai/15-ml.md) phần point-in-time/leakage, [16 LLM](phase-5-ml-ai/16-llm.md). Chọn scoring hoặc labelling làm extension chính; RAG/text-to-SQL là mở rộng sau core.

Một BI và một cloud đủ cho vòng đầu. Chọn thêm công cụ theo vị trí bạn nhắm tới.

## Gate bắt buộc

| Gate | Điều kiện | Bằng chứng |
|---|---|---|
| G1 | CSV→Parquet, join/window từ file trống; NULL và grain | Script, SQL, kết quả, tự giải thích |
| G2 | Ingestion/API tự viết; duplicate/drift/retry | CI chạy lab của bạn, không chỉ mã mẫu |
| G3 | Batch Olist thật, reconciliation, dashboard, backfill | Counts, proof SQL, run log, screenshot |
| G4 | Update/delete muộn, job xanh nhưng stale, recovery, quyền | Incident report, recovery time, test quyền |
| G5 | Dự án độc lập, đổi yêu cầu, người khác tái lập | Brief, ADR, review, demo, README |

Sau G2 có thể bắt đầu ứng tuyển internship để lấy phản hồi. Gate không bảo đảm tuyển dụng.

## Tích hợp xuyên suốt

- Module 04: có thể profile Olist thật; dữ liệu giả dành cho tests nhanh.
- Module 09: chạy batch thật, điền `docs/data-contract.md`, không đợi tuần 30.
- Module 11: nghiệm thu batch local và backfill đúng khoảng.
- Module 20: drill trên bản sao và phục hồi từ raw.
- Module 17: tổng hợp evidence **core + nhánh đã chọn**, không ép mọi nhánh.

Không chạy `olist sample` vào thư mục Olist thật: lệnh ghi lại sample. Dùng `OLIST_DATA_DIR` và `DUCKDB_PATH` riêng cho sample, real và drill.

## Nguồn và tra cứu

- [Python](https://docs.python.org/3/tutorial/), [PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html): nền tảng.
- [DE Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp): giải thích thứ hai, homework, peer review; tool mỗi cohort có thể khác repo.
- [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html): task tái lập, partition rõ.
- [dbt incremental](https://docs.getdbt.com/docs/build/incremental-models): watermark và adapter strategy.
- [BigQuery cost](https://docs.cloud.google.com/bigquery/docs/best-practices-costs): dry run và bytes billed; budget alert không phải hard cap.

Các video trong module là tùy nhu cầu. Ghi phiên bản Python, dbt/adapter và dịch vụ khi áp dụng snippet.

## Nhịp mỗi tuần

Ba buổi xây/debug, một buổi SQL, một buổi ôn và giải thích. Lưu một lỗi đã hiểu hoặc quyết định có lý do mỗi tuần. Mỗi hai tuần nhờ bạn review một PR hoặc self-review sau 48 giờ.

Lộ trình trước refactor được lưu ở tag `archive/pre-refactor-2026-11-02`; không cần khôi phục để học bản này.
