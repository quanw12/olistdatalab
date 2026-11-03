---
tags: [decourse, shell, linux]
module: 02
---

# Shell Linux và PowerShell

## Khi dùng

Tìm file, đọc log, kiểm tra process/port, cấu hình env và chạy pipeline. Bash và PowerShell có quoting, biến và pipeline khác nhau; không chép lẫn syntax.

| Nhu cầu | Bash/WSL | PowerShell |
|---|---|---|
| Thư mục | `pwd`, `ls -la` | `Get-Location`, `Get-ChildItem -Force` |
| Đầu file | `head -5 file.csv` | `Get-Content file.csv -TotalCount 5` |
| Log cuối | `tail -50 logs/ingest.log` | `Get-Content logs/ingest.log -Tail 50` |
| Tìm lỗi | `rg -n ERROR logs/` | `rg -n ERROR logs/` |
| Biến môi trường | `export MODE=dev` | `$env:MODE = 'dev'` |
| Exit code | `echo $?` | `$LASTEXITCODE` cho native command |
| Port | `ss -ltnp` | `Get-NetTCPConnection -LocalPort 5432` |

## Hash file — chọn shell của bạn

```bash
sha256sum data/landing/olist/olist_orders_dataset.csv
```

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath data\landing\olist\olist_orders_dataset.csv
```

Expected: cùng file bytes cho cùng hash; khác newline/BOM thì hash đổi dù dữ liệu logic tương tự. Không dùng hash bytes thay cho mọi kiểm tra tương đương nghiệp vụ.

## Bẫy

`wc -l` đếm newline, không đếm CSV record có quote chứa newline. `cut -d,` không phải CSV parser. Chuỗi có khoảng trắng phải quote; PowerShell ưu tiên `-LiteralPath` cho path có ký tự đặc biệt.

## Tự luyện

Tìm log lần chạy mới nhất, lấy các dòng ERROR và run_id, xác định process giữ port. Viết script trả exit khác 0 nếu file input thiếu. Tạo CSV chứa newline trong quote rồi so đếm dòng với csv.DictReader.

Ôn: env trong shell còn hiệu lực bao lâu? Làm sao biết lỗi ở source, code hay process khác giữ DB lock?

Liên quan: [[Files CSV JSON Parquet]], [[Observability va Recovery]]. Nguồn: [Missing Semester shell](https://missing.csail.mit.edu/2020/course-shell/), [PowerShell documentation](https://learn.microsoft.com/en-us/powershell/).
