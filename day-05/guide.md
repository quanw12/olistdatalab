# Day 5 — Ghép dữ liệu và tạo báo cáo thành phố

## Mục tiêu hôm nay

Ngày 4 tạo bảng thời tiết sạch. Ngày 5 thêm thông tin vùng miền từ một bảng tra cứu, rồi tổng hợp số liệu theo thành phố.

~~~text
weather_clean.csv + city_lookup.csv
             -> merge theo city
             -> kiểm tra thành phố chưa có vùng
             -> groupby region + city
             -> output/city_weather_summary.csv
~~~

Trong hệ thống thật, `weather_clean.csv` sẽ là output từ Ngày 4. Bài hôm nay để sẵn bản sao dữ liệu sạch, nên bạn có thể chạy độc lập.

## Học theo thứ tự này

1. Đọc [Bài học: merge, groupby và kiểm tra](lesson.md), mục 1 đến mục 6.
2. Mở `weather_clean.csv` và `city_lookup.csv`. Nhìn xem key dùng để ghép là gì.
3. Đọc `summary.py`, đặc biệt `main` để hiểu đầu vào và output.
4. Hoàn thành 4 TODO trong `build_summary`.
5. Khi kẹt, đọc [Gợi ý](help.md) theo đúng TODO.
6. Chạy trong `C:\DE Courses\day-05`:

~~~powershell
python summary.py
~~~

## Kết quả cần có

Terminal phải có:

~~~text
weather rows: 4
city lookup rows: 3
summary rows: 2
~~~

File `output/city_weather_summary.csv`:

~~~csv
region,city,observation_count,avg_temperature_c,min_temperature_c,max_temperature_c,avg_humidity_pct
Central,Da Nang,2,29.8,29.5,30.1,79.5
North,Hanoi,2,32.6,31.2,34.1,75.0
~~~

## Data contract của báo cáo

Mỗi dòng output đại diện cho **một thành phố trong một vùng**. Đây gọi là grain của bảng tổng hợp.

| Cột | Ý nghĩa |
|---|---|
| `region`, `city` | nhóm được tổng hợp |
| `observation_count` | số quan sát thời tiết trong nhóm |
| `avg_temperature_c` | nhiệt độ trung bình |
| `min_temperature_c`, `max_temperature_c` | nhiệt độ thấp/cao nhất |
| `avg_humidity_pct` | độ ẩm trung bình |

Hai kiểm tra chất lượng bắt buộc:

1. Sau merge, không được có `region` bị thiếu.
2. Tổng `observation_count` phải bằng số hàng dữ liệu thời tiết sau merge.

## Git checkpoint

Khi output đúng:

~~~powershell
git add README.md roadmap.md day-05
git commit -m "feat(day-05): summarize weather by city"
git push
~~~

## Gửi mình sau khi xong

1. Toàn bộ output của `python summary.py`.
2. Nội dung `output/city_weather_summary.csv`.
3. Phần thân hàm `build_summary`.
4. Một câu: vì sao `how="left"` phù hợp hơn `how="inner"` khi ta muốn phát hiện thành phố thiếu trong bảng tra cứu?
