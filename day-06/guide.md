# Day 6 — CLI, environment variable và HTTP API

## Mục tiêu hôm nay

Lấy thời tiết hiện tại từ API công khai Open-Meteo bằng script Python.

~~~text
tham số terminal + WEATHER_TIMEOUT_SECONDS
              -> HTTP GET với timeout
              -> kiểm tra HTTP status + JSON response
              -> output/weather_api_response.json
~~~

Không cần API key cho bài này. `WEATHER_TIMEOUT_SECONDS` là environment variable để bạn học cách đưa cấu hình nằm ngoài code.

## Học theo thứ tự này

1. Đọc [Bài học](lesson.md), mục 1 đến mục 6.
2. Đọc `fetch_weather.py`. Xem trước hàm `parse_args` và `main`.
3. Hoàn thành 4 TODO trong `fetch_current_weather`.
4. Nếu vướng, xem [Gợi ý](help.md).
5. Trong `C:\DE Courses\day-06`, chạy với cấu hình timeout mặc định:

~~~powershell
python fetch_weather.py
~~~

6. Thử một thành phố khác:

~~~powershell
python fetch_weather.py --city "Da Nang" --latitude 16.0544 --longitude 108.2022
~~~

## Environment variable

Đặt timeout 15 giây cho **PowerShell hiện tại**:

~~~powershell
$env:WEATHER_TIMEOUT_SECONDS = "15"
python fetch_weather.py
~~~

Đóng terminal rồi mở lại thì biến này không còn. Đây là chủ ý: cấu hình môi trường hiện tại không được lưu vào Git.

## Kết quả cần có

Terminal sẽ in:

~~~text
city: Ho Chi Minh City
current weather: {...}
wrote: output\weather_api_response.json
~~~

Nhiệt độ và thời điểm trong `current weather` thay đổi theo dữ liệu API lúc bạn chạy. Mở `output/weather_api_response.json` và kiểm tra:

- Có `city` và `requested_at`.
- Có `request` ghi tọa độ, timezone và biến current đã yêu cầu.
- Có `response.current`.

## Khi mạng hoặc API lỗi

Script cần báo lỗi rõ thay vì ghi file JSON rỗng:

| Hiện tượng | Ý nghĩa |
|---|---|
| `Timeout` | API phản hồi quá lâu theo giới hạn cấu hình |
| `HTTPError` | Server trả status lỗi như 4xx hoặc 5xx |
| `ConnectionError` | Máy không kết nối được endpoint |
| `ValueError: response has no current weather` | JSON trả về không đúng data contract bài này |

Không thêm vòng lặp retry hôm nay. Retry cần thiết trong pipeline thật, nhưng phải có giới hạn và quy tắc rõ; ta sẽ quay lại ở Ngày 15.

## Git checkpoint

Khi script chạy đúng:

~~~powershell
git add README.md roadmap.md requirements.txt day-06
git commit -m "feat(day-06): fetch weather with CLI"
git push
~~~

## Gửi mình sau khi xong

1. Toàn bộ terminal output của một lần chạy thành công.
2. Phần `request` và `response.current` từ file output.
3. Phần thân hàm `fetch_current_weather`.
4. Một câu: vì sao dùng `params=...` tốt hơn tự nối query string vào URL?
