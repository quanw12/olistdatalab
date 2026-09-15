# Bài học Ngày 3: JSON, datetime, cấu hình và log

## 1. JSON là gì?

JSON là định dạng văn bản phổ biến để các hệ thống trao đổi dữ liệu. API thường trả dữ liệu JSON, còn Python thường biến nó thành `dict` và `list` để xử lý.

Trong `weather_response.json`:

~~~json
{
  "timezone": "Asia/Ho_Chi_Minh",
  "current": {
    "time": "2026-09-13T09:00",
    "temperature_2m": 30.4
  }
}
~~~

Phần ngoài cùng là một JSON **object**, tương ứng với Python dictionary:

~~~python
payload = {
    "timezone": "Asia/Ho_Chi_Minh",
    "current": {
        "time": "2026-09-13T09:00",
        "temperature_2m": 30.4,
    },
}
~~~

Lấy object lồng bên trong theo từng tầng:

~~~python
current = payload["current"]
temperature = current["temperature_2m"]

# Hoặc viết trên một dòng:
temperature = payload["current"]["temperature_2m"]
~~~

Dùng biến `current` là cách dễ đọc hơn khi bạn mới học. Nếu gõ sai tên key, Python báo `KeyError`; đó là tín hiệu cấu trúc dữ liệu không đúng như pipeline chờ đợi.

JSON array tương ứng với Python list:

~~~json
{"cities": ["Hanoi", "Da Nang"]}
~~~

~~~python
data["cities"]  # ["Hanoi", "Da Nang"]
~~~

## 2. Đọc và ghi JSON bằng module `json`

Python có sẵn module `json`, không cần cài thư viện.

Đọc JSON từ file:

~~~python
with path.open(encoding="utf-8") as source_file:
    data = json.load(source_file)
~~~

- `path.open(...)` mở file.
- `with ... as ...` tự đóng file khi xong.
- `json.load` đổi **file JSON** thành dictionary/list Python.

Ghi dictionary Python thành JSON:

~~~python
with path.open("w", encoding="utf-8") as output_file:
    json.dump(data, output_file, ensure_ascii=False, indent=2)
~~~

- `"w"` là ghi mới hoặc thay nội dung file cũ.
- `indent=2` chỉ làm file dễ đọc hơn.
- `ensure_ascii=False` giữ tiếng Việt có dấu nếu dữ liệu có tiếng Việt.

Phân biệt hai cặp hàm:

| Hàm | Đọc/ghi với |
|---|---|
| `json.load` / `json.dump` | file đang mở |
| `json.loads` / `json.dumps` | chuỗi văn bản |

Hôm nay `dump` ghi ra file output. `dumps` biến dictionary log thành một dòng text JSON để `print` ra terminal.

## 3. Datetime: chuỗi thời gian và thời điểm thật

Trong JSON, thời gian ban đầu chỉ là chuỗi:

~~~python
time_text = "2026-09-13T09:00"
~~~

Ta đổi nó thành `datetime` để Python biết đây là thời điểm và có thể kiểm tra/so sánh/tính toán sau này:

~~~python
observed_at = datetime.fromisoformat(time_text)
~~~

Nếu `time_text` sai định dạng ISO, Python tạo `ValueError`. Sau khi kiểm tra, ghi lại bằng định dạng chuẩn:

~~~python
observed_at.isoformat()  # "2026-09-13T09:00:00"
~~~

File mẫu có thêm key `timezone` vì `2026-09-13T09:00` không tự nói nó thuộc múi giờ nào. Trong hệ thống thật, thường lưu timestamp theo UTC hoặc lưu timestamp cùng timezone rõ ràng.

`logged_at` trong log khác `observed_at`:

| Trường | Nghĩa |
|---|---|
| `observed_at` | lúc thời tiết được quan sát, lấy từ nguồn |
| `logged_at` | lúc pipeline chạy và ghi log |

Hàm này tạo thời gian UTC hiện tại:

~~~python
datetime.now(timezone.utc).isoformat()
~~~

## 4. Cấu hình: tách luật khỏi code

Trong `settings.json` có thành phố, nguồn dữ liệu và giới hạn nhiệt độ:

~~~json
{
  "city": "Ho Chi Minh City",
  "temperature_min_c": -50,
  "temperature_max_c": 60
}
~~~

Vì sao không viết thẳng `-50` và `60` vào hàm?

~~~python
if not settings["temperature_min_c"] <= temperature_c <= settings["temperature_max_c"]:
    raise ValueError("temperature_c is outside configured range")
~~~

Sau này nếu có nguồn dữ liệu khác hoặc luật mới, chỉ cần sửa file cấu hình. Code kiểm tra không đổi. Đây là cách pipeline dễ dùng lại hơn.

`raise ValueError(...)` chủ động tạo lỗi với lý do rõ ràng khi dữ liệu phá vỡ data contract. Nó khác `return None` của Ngày 1, nhưng mục đích giống nhau: không cho dữ liệu không hợp lệ đi vào output.

## 5. Structured log: log để máy cũng hiểu

Log dạng câu tự do:

~~~text
Đã ghi dữ liệu thời tiết của Thành phố Hồ Chí Minh lúc 09:00
~~~

Con người đọc được, nhưng chương trình khó lọc theo thành phố hay sự kiện. Log có cấu trúc lưu từng thông tin dưới một key:

~~~json
{
  "event": "snapshot_written",
  "logged_at": "2026-09-13T02:05:00+00:00",
  "details": {
    "city": "Ho Chi Minh City",
    "observed_at": "2026-09-13T09:00:00"
  }
}
~~~

Sau này hệ thống log có thể tìm tất cả record với `event = "snapshot_written"`, hoặc đếm số lần từng thành phố được xử lý.

Hàm `log_event` của bài tạo dictionary log rồi dùng:

~~~python
print(json.dumps(record, ensure_ascii=False))
~~~

Một dòng JSON in ra terminal là cách logging phổ biến cho script, container và pipeline. Đừng dùng log để chứa mật khẩu, API key hay dữ liệu riêng tư.

## 6. Đọc `extract.py` như một pipeline

~~~text
main
  -> load settings.json
  -> load weather_response.json
  -> build_snapshot: lấy dữ liệu, đổi kiểu, kiểm tra, chuẩn hóa
  -> write_json: ghi output
  -> log_event: in log JSON
~~~

Ba hàm đã viết sẵn có trách nhiệm rõ:

| Hàm | Nhận vào | Trả ra / tác động |
|---|---|---|
| `load_json(path)` | đường dẫn | dictionary từ file JSON |
| `write_json(path, data)` | đường dẫn, dictionary | tạo file JSON |
| `log_event(event, details)` | tên sự kiện, chi tiết | in một record log |

Bạn chỉ hoàn thành `build_snapshot(payload, settings)`. Hợp đồng của nó:

~~~text
Nhận: payload từ nguồn và settings từ file cấu hình.
Trả: một dictionary đã chuẩn hóa, hoặc ValueError nếu nhiệt độ ngoài giới hạn.
~~~

## 7. Làm theo từng TODO

1. Lấy `current` từ `payload`.
2. Đổi `current["time"]` thành `datetime`.
3. Lấy và chuyển nhiệt độ, độ ẩm sang `float` và `int`.
4. So sánh nhiệt độ với hai giới hạn trong `settings`.
5. `return` dictionary theo đúng key yêu cầu.

Sau TODO 3, có thể thêm tạm:

~~~python
print(current)
print(observed_at, temperature_c, humidity_pct)
~~~

để quan sát giá trị. Xóa các dòng debug trước khi hoàn thành bài.

## 8. Lỗi thường gặp

| Lỗi | Thường do | Cách xem lại |
|---|---|---|
| `FileNotFoundError` | Chạy script ở sai thư mục | Chạy trong `C:\DE Courses\day-03` |
| `JSONDecodeError` | JSON bị thiếu dấu phẩy/dấu ngoặc | Mở file JSON, không sửa nếu chưa cần |
| `KeyError` | Gõ sai key như `temperature` thay vì `temperature_2m` | So lại `weather_response.json` |
| `ValueError: Invalid isoformat string` | Chuỗi thời gian sai | Dùng `datetime.fromisoformat(current["time"])` |
| `TypeError: 'NoneType' ...` | Quên `return` dictionary | Hoàn thành TODO 5 |

## 9. Tài liệu ngoài

- [Python `json`](https://docs.python.org/3/library/json.html)
- [Python `datetime`](https://docs.python.org/3/library/datetime.html)
- [Python exceptions](https://docs.python.org/3/tutorial/errors.html)

Chỉ đọc phần đang dùng trong bài. Mục tiêu là tự chạy được pipeline nhỏ, không phải thuộc hết thư viện.
