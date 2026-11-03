# DEcourse · Vault ôn tập Data Engineering

Tài liệu tiếng Việt để học, tra syntax, đối chiếu ứng dụng và ôn lại sau này. Không cần plugin cộng đồng hoặc tài khoản Obsidian Sync.

## Mở trong Obsidian

1. Chọn **Open folder as vault** trong màn hình quản lý vault.
2. Chọn thư mục `C:\DE Courses\DEcourse` sau khi clone repo về máy này. Nếu repo ở chỗ khác, chọn thư mục `DEcourse` tương ứng.
3. Mở **00 - Bat dau → DEcourse** rồi **Study Map**. `Ctrl+O` tìm note; `Ctrl+P` tìm lệnh; `Ctrl+E` chuyển chế độ đọc/sửa trên Windows.
4. Các callout, wiki link, code highlight và graph là tính năng Markdown của Obsidian. CSS có sẵn trong `.obsidian/snippets/decourse.css`, có thể bật/tắt ở Appearance → CSS snippets.

Mở được như Markdown trong editor khác; wiki link hiển thị tốt nhất trong Obsidian. Bộ này độc lập với vault của bạn bè trong ảnh, không sao chép theme hoặc nội dung riêng của họ.

## Cấu trúc

| Thư mục | Dùng để |
|---|---|
| 00 - Bat dau | Trang chủ, Study Map, tiến độ, lịch ôn, cách dùng AI |
| 01 - Python | Syntax ngôn ngữ, file, thời gian/tiền, DataFrames, môi trường |
| 02 - SQL | NULL, joins, aggregation/window, CTE/dedupe, transaction/plan |
| 03 - Git Linux | Git/PR, shell, process và cấu hình |
| 04 - Core DE | Modelling, ingestion, API, incremental/CDC, test |
| 05 - Modern Stack | dbt, Docker/Postgres, Airflow, BI/metric |
| 06 - Production | Giám sát/phục hồi, quyền, phát hành, hiệu năng |
| 07 - Cloud | GCP, BigQuery, Terraform và chi phí |
| 08 - Chuyen sau | Spark, Kafka, ML, LLM, RAG — chọn theo nhánh |
| 09 - Projects | Olist, sự cố, dự án độc lập và phỏng vấn |
| 10 - Templates | Mẫu note, nhật ký, incident, ADR |

## Quy ước code

- **Chạy độc lập:** ví dụ Python/SQL có dữ liệu nhỏ và assertion/kết quả dự kiến. SQL mặc định DuckDB trừ khi ghi PostgreSQL/BigQuery.
- **Pattern cần tích hợp:** phải thay table/path/credential và dựng fixture; không hứa copy là chạy.
- **Lệnh môi trường:** chỉ chạy sau khi cài dependency/dịch vụ và kiểm tra thư mục hiện tại. Cloud có thể phát sinh phí; lệnh Terraform không tự được thực thi bởi tài liệu.
- Snippet dùng `assert` để học và tự kiểm chứng; validation sản phẩm phải dùng điều kiện + exception rõ ràng.

Các bài tự làm ở `labs/` của repo; vault là sổ tay, không thay thế việc code. Lịch chuẩn ở [learning/README.md](../learning/README.md).

## Kiểm tra tài liệu

Từ repo đã cài core dependencies, chạy `python scripts/check_course.py`. Lệnh kiểm tra wiki link, link tương đối, properties/config và chạy các block đánh dấu `runnable`; SQL có expected output để đối chứng. Các pattern cần Spark/Kafka/cloud/Airflow không được tự thực thi và vẫn cần evidence riêng từ lab của bạn.
