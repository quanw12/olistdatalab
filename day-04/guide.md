# Day 4 — Làm sạch CSV với pandas

## Mục tiêu hôm nay

Ngày 1 làm sạch CSV bằng vòng lặp từng dòng. Hôm nay bạn làm cùng kiểu công việc bằng `pandas`: thao tác trên cả cột dữ liệu.

Pipeline:

~~~text
messy_weather.csv -> DataFrame -> chuẩn hóa kiểu dữ liệu + lọc lỗi
                 -> bỏ trùng -> output/clean_weather.csv + báo cáo
~~~

Pandas đã có trong môi trường Python hiện tại. Nếu cần tự kiểm tra:

~~~powershell
python -c "import pandas as pd; print(pd.__version__)"
~~~

## Học theo thứ tự này

1. Đọc [Bài học pandas](lesson.md), mục 1 đến mục 7.
2. Mở `messy_weather.csv`. Dự đoán 6 dòng nào sẽ không đi vào output.
3. Mở `clean_pandas.py`. Đọc `main` để biết đầu vào, đầu ra và báo cáo.
4. Hoàn thành 4 TODO trong `clean_weather` theo thứ tự.
5. Khi kẹt, xem [Gợi ý theo TODO](help.md), rồi tự gõ code lại.
6. Trong PowerShell tại `C:\DE Courses\day-04`, chạy:

~~~powershell
python clean_pandas.py
~~~

## Kết quả cần có

~~~text
input rows: 10
invalid rows: 5
duplicate rows: 1
accepted rows: 4
~~~

File `output/clean_weather.csv` phải có đúng 4 dòng dữ liệu:

~~~csv
city,observed_at,temperature_c,humidity_pct
Hanoi,2026-09-14,31.2,78
Da Nang,2026-09-14,30.1,81
Hanoi,2026-09-15,34.1,72
Da Nang,2026-09-15,29.5,78
~~~

Ở dataset này, độ ẩm không có missing value nên được ghi dạng số nguyên. Nếu một cột số nguyên có missing value, pandas có thể hiển thị giá trị dạng `78.0`; điều đó không làm dữ liệu sai. Ta sẽ học kiểm soát schema kỹ hơn khi vào database.

## Điều cần hiểu sau bài

- `DataFrame` là bảng dữ liệu trong Python.
- `Series` là một cột trong DataFrame.
- `pd.to_numeric(..., errors="coerce")` biến dữ liệu không đổi được thành `NaN` để pipeline có thể phát hiện và loại bỏ.
- Boolean mask là một cột `True/False` dùng để lọc dòng.
- `drop_duplicates` xử lý trùng lặp mà không cần tự tạo `set`.

## Git checkpoint

Khi output đúng:

~~~powershell
git add requirements.txt roadmap.md day-04
git commit -m "feat(day-04): clean weather data with pandas"
git push
~~~

## Gửi mình sau khi xong

1. Toàn bộ report của `python clean_pandas.py`.
2. Nội dung `output/clean_weather.csv`.
3. Phần thân hàm `clean_weather`.
4. Một câu: vì sao `errors="coerce"` hữu ích hơn để script dừng ngay khi gặp `not_available`?
