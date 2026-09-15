# Gợi ý Ngày 3

Xem từng phần theo TODO. Tự gõ code vào `build_snapshot` thay vì dán cả hàm.

## TODO 1: lấy object `current`

~~~python
current = payload["current"]
~~~

Sau dòng này, `current` là:

~~~python
{
    "time": "2026-09-13T09:00",
    "temperature_2m": 30.4,
    "relative_humidity_2m": 76,
}
~~~

## TODO 2: đổi text thời gian thành datetime

~~~python
observed_at = datetime.fromisoformat(current["time"])
~~~

Không cần tạo thời gian mới. Đây là thời gian có sẵn từ nguồn.

## TODO 3: lấy số

~~~python
temperature_c = float(current["temperature_2m"])
humidity_pct = int(current["relative_humidity_2m"])
~~~

Trong file mẫu, hai giá trị đã là số. Viết `float` và `int` để hàm vẫn có ý nghĩa khi API trả số dưới dạng text.

## TODO 4: kiểm tra luật từ config

~~~python
if not settings["temperature_min_c"] <= temperature_c <= settings["temperature_max_c"]:
    raise ValueError("temperature_c is outside configured range")
~~~

Đặt khối này sau phần chuyển nhiệt độ sang số và trước `return`.

## TODO 5: trả về snapshot

~~~python
return {
    "city": settings["city"],
    "observed_at": observed_at.isoformat(),
    "timezone": payload["timezone"],
    "temperature_c": temperature_c,
    "humidity_pct": humidity_pct,
    "source": settings["source"],
}
~~~

`observed_at.isoformat()` biến object `datetime` quay lại chuỗi ISO để ghi JSON. `json.dump` không tự ghi được object `datetime`.

## Tự trace một lần

| Biến | Giá trị sau khi chạy |
|---|---|
| `current` | dictionary bên trong key `"current"` |
| `observed_at` | datetime cho 2026-09-13 09:00 |
| `temperature_c` | `30.4` |
| `humidity_pct` | `76` |
| snapshot trả về | dictionary 6 key cần ghi ra file |

Nếu bị `KeyError`, in tạm `payload` hoặc `current`, rồi so key thật trong file JSON. Không tự đổi tên key theo cảm giác.
