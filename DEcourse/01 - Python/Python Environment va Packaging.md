---
tags: [decourse, python, environment]
module: 01
---

# Python Environment và Packaging

## Khi dùng

Venv cô lập package; pyproject khai báo project và dependency; lock/constraints ghi bộ phiên bản đã kiểm tra để tái lập. Minimum version không bảo đảm mọi bộ phiên bản mới hơn tương thích.

## Lệnh PowerShell — chạy từ repo, cần Python đã cài

```powershell
python --version
python -m venv .venv-study
.\.venv-study\Scripts\python.exe -m pip install -e ".[dev,dbt]"
.\.venv-study\Scripts\python.exe -m pip check
.\.venv-study\Scripts\python.exe -m pytest
```

Repo đề xuất Python 3.12; nếu dùng bản khác phải ghi lại và kiểm tra. Dùng executable của venv trực tiếp tránh cài nhầm vào interpreter khác; `py` launcher không có trên mọi Windows.

## Syntax cấu hình tách sample và real

```powershell
# Ví dụ cho buổi sample: kiểm tra đây không phải thư mục real trước khi tạo.
$env:OLIST_DATA_DIR = "data/sample"
$env:DUCKDB_PATH = "data/warehouse/sample.duckdb"
.\.venv-study\Scripts\python.exe -m olist_platform sample --orders 500
.\.venv-study\Scripts\python.exe -m olist_platform run --offline
```

Biến môi trường còn hiệu lực trong shell; ghi rõ chúng trong log. File `.env` không được commit; `.env.example` chỉ có placeholder hoặc giá trị local.

## Tái lập

Sau một lần chạy thành công ở môi trường sạch, lưu phiên bản Python, pip, dependency, dbt adapter và OS. Cài lại trên môi trường khác từ constraints/lock rồi chạy tests để chứng minh. `pip freeze` từ venv dùng cho nhiều dự án chỉ là snapshot lẫn tạp, không tự thành lock tốt.

> [!bug] Khi gặp lỗi môi trường
> Ghi lệnh, interpreter path, version và traceback đầu tiên. Lỗi dbt đọc file thư viện khác với lỗi SQL mart. Không sửa SQL ngẫu nhiên khi parser chưa đọc xong package.

## Tự luyện và ôn

Tạo venv mới, cài core + dev, kiểm tra thiếu dbt sẽ ảnh hưởng test nào. Sau đó cài dbt và chạy integration. Giải thích khác biệt giữa package đã cài và module tự viết trong `src/`.

Liên quan: [[Delivery va Reproducibility]], [[Testing Logging va CI]]. Nguồn: [venv](https://docs.python.org/3/library/venv.html), [pyproject](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/).
