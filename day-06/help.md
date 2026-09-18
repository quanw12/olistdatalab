# Gợi ý Ngày 6

Hoàn thành `fetch_current_weather` theo từng TODO.

## TODO 1: parameters

~~~python
params = {
    "latitude": args.latitude,
    "longitude": args.longitude,
    "current": "temperature_2m,relative_humidity_2m",
    "timezone": args.timezone,
}
~~~

## TODO 2: timeout từ environment

~~~python
timeout_seconds = float(os.getenv("WEATHER_TIMEOUT_SECONDS", "10"))
~~~

PowerShell truyền environment variable dưới dạng text, nên cần `float`.

## TODO 3: GET, timeout và status

~~~python
try:
    response = requests.get(
        API_URL,
        params=params,
        timeout=timeout_seconds,
    )
    response.raise_for_status()
except requests.exceptions.RequestException as error:
    raise RuntimeError(f"weather request failed: {error}") from error
~~~

## TODO 4: JSON và data contract

~~~python
payload = response.json()

if "current" not in payload:
    raise ValueError("response has no current weather")

return payload, params
~~~

`fetch_current_weather` trả về hai giá trị, nên `main` sẽ unpack thành:

~~~python
payload, params = fetch_current_weather(args)
~~~

## Nếu lỗi

| Lỗi | Thường do | Cách xử lý |
|---|---|---|
| `NameError: os is not defined` | Quên `import os` | File khung đã có import; không xóa nó |
| `TypeError: 'str' object is not callable` | Viết sai `os.getenv(...)` | Dùng đúng dấu ngoặc tròn khi gọi hàm |
| `requests.exceptions.Timeout` | Timeout quá thấp hoặc mạng chậm | Tăng `WEATHER_TIMEOUT_SECONDS` |
| `HTTPError` | URL hoặc query params không hợp lệ, API lỗi | Đọc status trong traceback và so lại `params` |
| `JSONDecodeError` | Response không phải JSON | Không ghi output; gửi mình toàn bộ lỗi |
