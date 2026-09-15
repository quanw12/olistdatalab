# Day 3 — JSON, datetime, cấu hình và log
## Mục tiêu hôm nay

Đọc một file JSON mô phỏng phản hồi từ API thời tiết, lấy các trường cần thiết, kiểm tra nhiệt độ theo file cấu hình, rồi tạo:

1. `output/weather_snapshot.json` — bản ghi đã chuẩn hóa.
2. Một log JSON trên terminal — cho biết pipeline đã ghi thành công.

Pipeline hôm nay:

~~~text
weather_response.json + settings.json
             -> đọc và chuẩn hóa
             -> weather_snapshot.json + JSON log
~~~

Ngày 15, file `weather_response.json` sẽ được thay bằng API thật. Logic đọc JSON, kiểm tra và ghi output vẫn giống như hôm nay.

## Học theo thứ tự này

1. Đọc [Bài học](lesson.md), mục 1 đến mục 6.
2. Mở `weather_response.json` và `settings.json`. Đọc cấu trúc bằng mắt trước.
3. Mở `extract.py`. Đọc các hàm đã có: `load_json`, `write_json`, `log_event` và `main`.
4. Hoàn thành riêng hàm `build_snapshot` theo 5 TODO. Làm tuần tự, không viết tất cả một lượt.
5. Nếu kẹt, xem [Gợi ý](help.md) đúng phần TODO đó.
6. Trong PowerShell tại `C:\DE Courses\day-03`, chạy:

~~~powershell
python extract.py
~~~

## Kết quả cần có

Terminal có một dòng JSON với các key `event`, `logged_at` và `details`. Giá trị `logged_at` thay đổi theo lúc chạy.

~~~text
{"event": "snapshot_written", "logged_at": "...", "details": {"city": "Ho Chi Minh City", "observed_at": "2026-09-13T09:00:00"}}
~~~

Mở `output/weather_snapshot.json`. Nội dung phải chứa:

~~~json
{
  "city": "Ho Chi Minh City",
  "observed_at": "2026-09-13T09:00:00",
  "timezone": "Asia/Ho_Chi_Minh",
  "temperature_c": 30.4,
  "humidity_pct": 76,
  "source": "open-meteo-demo"
}
~~~

## Checklist hoàn thành

- [ ] Phân biệt được JSON object, JSON array và chuỗi JSON.
- [ ] Lấy được `payload["current"]["temperature_2m"]`.
- [ ] Giải thích được vì sao đổi text thời gian thành `datetime` rồi lại ghi ra text ISO.
- [ ] Biết `settings.json` thay đổi luật mà không cần đổi code.
- [ ] Chạy ra output JSON và log JSON đúng cấu trúc.

## Git checkpoint

Khi hoàn thành Ngày 2 và Ngày 3:

~~~powershell
git add day-02 day-03 README.md roadmap.md
git commit -m "feat(day-03): add JSON weather snapshot exercise"
git push
~~~

## Gửi mình sau khi xong

1. Toàn bộ dòng log từ `python extract.py`.
2. Nội dung `output/weather_snapshot.json`.
3. Phần thân hàm `build_snapshot`.
4. Một câu: tại sao `settings.json` hữu ích hơn việc ghi cứng giới hạn nhiệt độ trong code?
