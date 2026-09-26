# Bài ôn tập Ngày 7: từ raw JSON đến clean record

## 1. Raw layer và clean layer

Ngày 6 ghi raw API response:

~~~json
{
  "city": "Ho Chi Minh City",
  "requested_at": "...",
  "request": {"latitude": 10.8231},
  "response": {
    "timezone": "Asia/Ho_Chi_Minh",
    "current": {"temperature_2m": 30.7}
  }
}
~~~

Raw layer giữ dữ liệu gần nguồn nhất có thể. Nó hữu ích khi cần debug API, thay đổi logic transform hoặc chạy lại pipeline.

Clean layer chỉ giữ trường đã chuẩn hóa để downstream dùng:

~~~json
{
  "city": "Ho Chi Minh City",
  "observed_at": "2026-09-18T11:30",
  "temperature_c": 30.7,
  "humidity_pct": 72
}
~~~

Clean layer nhỏ hơn và dễ query hơn, nhưng không thay thế raw layer.

## 2. Hai thời điểm khác nhau

| Trường | Lấy từ đâu | Ý nghĩa |
|---|---|---|
| `requested_at` | máy chạy pipeline | lúc request được gửi |
| `observed_at` | `response.current.time` | lúc nguồn quan sát thời tiết |

Không thay `observed_at` bằng `requested_at`. API có thể trả một quan sát cũ hơn thời điểm request, hoặc timestamp theo timezone khác.

## 3. Xây một clean record

Đường đi qua nested dictionary:

~~~python
response = raw["response"]
current = response["current"]

temperature_c = float(current["temperature_2m"])
humidity_pct = int(current["relative_humidity_2m"])
~~~

Sau đó return dictionary mới. Không sửa trực tiếp `raw`; raw data phải giữ nguyên để debug hoặc replay.

## 4. Data contract và validate

Một contract viết ra các điều kiện clean layer phải thỏa. Hôm nay `validate_record` không tự ghi file, nó chỉ trả về list lỗi:

~~~python
errors = validate_record(clean_record)

if errors:
    raise ValueError("; ".join(errors))
~~~

Điểm tốt của list lỗi: nếu nhiều trường sai, bạn thấy tất cả lỗi trong một lần chạy thay vì sửa từng lỗi một.

### Kiểm tra datetime

~~~python
try:
    datetime.fromisoformat(record["observed_at"])
except ValueError:
    errors.append("observed_at is not ISO datetime")
~~~

### Kiểm tra range

~~~python
if not -50 <= record["temperature_c"] <= 60:
    errors.append("temperature_c is outside allowed range")
~~~

`not` đảo kết quả condition. Đọc câu này như: “nếu nhiệt độ không nằm trong khoảng -50 đến 60”.

## 5. Fail before write

Trong `main`:

~~~python
errors = validate_record(clean_record)
if errors:
    raise ValueError("; ".join(errors))

write_json(args.output, clean_record)
~~~

Thứ tự quan trọng: validate trước, ghi sau. Nếu ghi trước rồi mới phát hiện lỗi, output layer đã có dữ liệu không đáng tin.

## 6. CLI và reproducibility

`--input` và `--output` làm pipeline linh hoạt mà không phải sửa code:

~~~powershell
python pipeline.py --input raw_weather.json --output output/weather_clean.json
~~~

Lưu raw input cố định trong repo giúp cùng một lệnh luôn cho cùng output. Khi test API sống, kết quả có thể đổi do thời tiết và thời gian.

## 7. Tài liệu ngoài

- [Python `json`](https://docs.python.org/3/library/json.html)
- [Python `datetime`](https://docs.python.org/3/library/datetime.html)
- [Pro Git: recording changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
