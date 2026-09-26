# Lộ trình Data Engineering 30 ngày

## Cách dùng thư mục này

Mỗi ngày học có một thư mục riêng theo mẫu `NN-day-ten-ngan`.

- Đọc `README.md` của ngày đó trước.
- Tự viết code, không chép nguyên đáp án.
- Lưu ghi chú, ảnh lỗi và kết quả chạy vào chính thư mục ngày học.
- Chỉ chuyển sang ngày tiếp theo khi hoàn thành "đầu ra" của ngày hiện tại.

Mỗi buổi được thiết kế cho 2.5–4 giờ. Nếu cần lâu hơn, không sao; điều quan trọng là hiểu và tự chạy lại được.

## Đích đến sau 30 ngày

Xây được một pipeline dữ liệu thời tiết: lấy dữ liệu API, lưu raw data, làm sạch, nạp PostgreSQL, tạo bảng phân tích, kiểm tra chất lượng, chạy lại an toàn bằng Docker và orchestration cơ bản. Có README, test, log mẫu và báo cáo ngắn để đưa vào portfolio.

## Stack của tháng đầu

Python, SQL/PostgreSQL, Git/GitHub, terminal, CSV/JSON/Parquet, `pytest`, Docker Compose, Prefect, BigQuery Sandbox và một LLM API ở mức hỗ trợ pipeline.

Không học trong tháng đầu: Kafka, Kubernetes, Terraform, nhiều cloud cùng lúc, Spark chuyên sâu, vector database hay RAG. Spark chỉ xem khái niệm sau capstone.

## Lịch từng ngày

| Ngày | Chủ đề | Đầu ra |
|---|---|---|
| 01 | Python, file CSV, Git cơ bản | Chương trình làm sạch CSV thời tiết |
| 02 | Python: hàm, dict, list, set, exception | Báo cáo thời tiết nhỏ và hiểu/refactor chương trình ngày 1 |
| 03 | Datetime, JSON, logging, cấu hình | Đọc JSON và ghi log có cấu trúc |
| 04 | pandas: đọc, lọc, kiểu dữ liệu, missing values | Script làm sạch dữ liệu theo cột |
| 05 | pandas: merge, groupby, kiểm tra kết quả | Báo cáo tổng hợp thời tiết theo thành phố |
| 06 | CLI, environment variables, HTTP cơ bản | Script CLI lấy thời tiết hiện tại từ API |
| 07 | Ôn và mini-project 1 | Repository sạch, README và 5 quality checks |
| 08 | PostgreSQL: bảng, kiểu dữ liệu, khóa và constraint | Schema dữ liệu thời tiết |
| 09 | SQL: SELECT, WHERE, JOIN, GROUP BY | 10 truy vấn có lời giải thích |
| 10 | SQL: CTE, CASE, date/time, subquery | 10 truy vấn nâng cao |
| 11 | SQL: window functions | Phân tích rank, lag và rolling average |
| 12 | Data modeling: grain, OLTP/OLAP, fact/dimension | ERD và star schema |
| 13 | PostgreSQL từ Python: transaction, upsert | Script nạp staging an toàn |
| 14 | Ôn và mini-project 2 | Weather analytics mart |
| 15 | REST API: timeout, status, JSON, retry | Module extract từ Open-Meteo |
| 16 | Raw/staging/mart, ETL và ELT | Pipeline ba lớp dữ liệu |
| 17 | Incremental load, idempotency, backfill | Chạy lại không sinh dữ liệu trùng |
| 18 | Docker: image, container, volume, network | PostgreSQL bằng Docker Compose |
| 19 | Docker Compose cho toàn ứng dụng | Một lệnh khởi động môi trường |
| 20 | Prefect: flow, task, retry, logs | Pipeline được điều phối |
| 21 | Ôn và mini-project 3 | Pipeline chạy theo lịch local |
| 22 | Testing: pytest, fixtures, mock API | Test cho transform và ingestion |
| 23 | Data quality: schema, null, unique, range, freshness | Bộ kiểm tra chất lượng |
| 24 | Data warehouse: columnar storage, partitioning, chi phí | Bài lab BigQuery Sandbox |
| 25 | Analytics: KPI, SQL mart, trực quan hóa | Ba biểu đồ và nhận xét có số liệu |
| 26 | CI cơ bản với GitHub Actions | Test chạy tự động khi push |
| 27 | AI/LLM hỗ trợ DE: docs, test, tóm tắt có kiểm chứng | Một thử nghiệm được đánh giá |
| 28 | Thiết kế capstone và README | Architecture, data dictionary, runbook |
| 29 | Chạy capstone và xử lý lỗi | Demo pipeline từ đầu đến cuối |
| 30 | Hoàn thiện portfolio | README, video demo, retrospective |

## Quy tắc hoàn thành

Một phần được xem là xong khi bạn có thể:

1. Chạy lại từ đầu mà không phụ thuộc vào notebook hoặc trạng thái máy cũ.
2. Giải thích đầu vào, đầu ra, lỗi có thể xảy ra và cách chương trình xử lý chúng.
3. Có một commit Git mô tả đúng thay đổi.

## Vai trò của roadmap.sh

[Data Engineer Roadmap](https://roadmap.sh/data-engineer) là bản đồ tham khảo dài hạn. Nó đúng ở các mảng Python, SQL, data storage, pipelines, orchestration, warehouse, big data và cloud. Ta dùng nó để biết phần nào sẽ đến sau, không dùng nó làm checklist phải học hết trong một tháng.
