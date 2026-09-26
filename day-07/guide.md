# Day 7 — Mini-project 1: Weather snapshot pipeline

## Mục tiêu tuần 1

Bạn đã học Python cơ bản, CSV/JSON, pandas, Git và HTTP API. Hôm nay ghép chúng thành một pipeline nhỏ, có thể chạy lại từ đầu:

~~~text
raw_weather.json
  -> đọc raw response + request metadata
  -> chuẩn hóa thành weather record
  -> chạy 5 quality checks
  -> output/weather_clean.json
~~~

Input được lưu sẵn, mô phỏng output của Ngày 6. Không cần mạng để chạy; đây là tính chất quan trọng của một bài test/review có thể tái lập.

## Học theo thứ tự này

1. Đọc [Project README](README.md) để hiểu mục tiêu như một reviewer portfolio.
2. Đọc [Bài ôn tập](lesson.md), nhất là data contract và 5 quality checks.
3. Mở `raw_weather.json`. Xác định đường đi để lấy nhiệt độ:

~~~python
raw["response"]["current"]["temperature_2m"]
~~~

4. Hoàn thành hai hàm trong `pipeline.py`: `build_clean_record` và `validate_record`.
5. Chỉ mở [Gợi ý](help.md) khi cần.
6. Trong `C:\DE Courses\day-07`, chạy:

~~~powershell
python pipeline.py
~~~

## Kết quả cần có

~~~text
checks passed: 5
wrote: output\weather_clean.json
~~~

`output/weather_clean.json` phải có:

~~~json
{
  "city": "Ho Chi Minh City",
  "requested_at": "2026-09-18T04:31:14+00:00",
  "observed_at": "2026-09-18T11:30",
  "timezone": "Asia/Ho_Chi_Minh",
  "temperature_c": 30.7,
  "humidity_pct": 72,
  "source": "open-meteo"
}
~~~

## Năm quality checks

1. `city` không rỗng.
2. `observed_at` là ISO datetime hợp lệ.
3. `timezone` không rỗng.
4. `temperature_c` nằm từ -50 đến 60.
5. `humidity_pct` nằm từ 0 đến 100.

Nếu một check thất bại, pipeline không được ghi output. Đây là nền tảng của data quality.

## Đánh giá bản thân trước khi commit

Trả lời bằng lời của bạn:

1. Raw layer khác clean layer ở đâu?
2. Vì sao giữ `requested_at` và `observed_at` là hai trường riêng?
3. Điều gì xảy ra nếu API trả `humidity_pct = 130`?
4. Vì sao input cố định giúp kiểm tra pipeline dễ hơn API sống?

Viết câu trả lời ngắn vào cuối [README.md](README.md), mục `What I learned`.

## Git checkpoint

Khi pipeline chạy đúng và README có reflection:

~~~powershell
git add README.md roadmap.md day-07
git commit -m "feat(day-07): add weather snapshot pipeline"
git push
~~~

## Gửi mình sau khi xong

1. Output terminal.
2. Nội dung `output/weather_clean.json`.
3. Hai hàm bạn đã hoàn thành.
4. Bốn câu reflection trong README.
