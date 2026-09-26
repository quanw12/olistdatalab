# Weather Snapshot Pipeline

Mini-project tuần 1 của lộ trình Data Engineering.

## Bài toán

Chuyển raw response của API thời tiết thành một bản ghi sạch, có contract rõ ràng, rồi chỉ ghi output khi dữ liệu qua đủ 5 quality checks.

## Luồng dữ liệu

~~~text
raw_weather.json -> build_clean_record -> validate_record -> weather_clean.json
~~~

## Chạy project

~~~powershell
python pipeline.py
~~~

Bạn cũng có thể đổi input/output:

~~~powershell
python pipeline.py --input raw_weather.json --output output/weather_clean.json
~~~

## Input

`raw_weather.json` mô phỏng raw layer từ API và giữ:

- thành phố do người dùng chọn;
- thời điểm request;
- request parameters;
- response gốc từ API.

## Output contract

| Trường | Kiểu | Ý nghĩa |
|---|---|---|
| `city` | string | thành phố do người dùng gắn nhãn |
| `requested_at` | ISO datetime string | thời điểm pipeline gọi API |
| `observed_at` | ISO datetime string | thời điểm API quan sát thời tiết |
| `timezone` | string | timezone của quan sát |
| `temperature_c` | float | nhiệt độ Celsius |
| `humidity_pct` | integer | độ ẩm phần trăm |
| `source` | string | nguồn dữ liệu |

## Quality checks

Pipeline từ chối input nếu city/timezone rỗng, observed_at sai ISO format, nhiệt độ ngoài -50 đến 60 hoặc độ ẩm ngoài 0 đến 100.

## What I learned

1. Raw layer giữ dữ liệu gốc gần như nguyên vẹn để debug, audit hoặc chạy lại pipeline.  Clean layer chỉ giữ các trường cần thiết, đồng thời chuẩn hóa và kiểm tra dữ liệu.
2. requested_at là lúc pipeline gọi API, còn observed_at là lúc API ghi nhận thời tiết.
3. Với humidity_pct = 130, hàm sẽ thêm lỗi.
4. Input cố định giúp mỗi lần chạy cho cùng kết quả, dễ debug và kiểm tra hơn API sống.
