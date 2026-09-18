# Bài học Ngày 6: script CLI gọi HTTP API

## 1. CLI: đưa dữ liệu vào từ terminal

CLI là giao diện dòng lệnh. Thay vì sửa code mỗi lần muốn đổi tọa độ, ta truyền tham số lúc chạy:

~~~powershell
python fetch_weather.py --city "Da Nang" --latitude 16.0544 --longitude 108.2022
~~~

Các phần `--city`, `--latitude` và `--longitude` là arguments. Python dùng `argparse` để đọc chúng:

~~~python
parser.add_argument("--latitude", type=float, default=10.8231)
args = parser.parse_args()
~~~

- `type=float` đổi text người dùng gõ thành số thực.
- `default=...` là giá trị dùng khi không truyền flag.
- `args.latitude` lấy giá trị sau khi parse.

Thử xem tất cả flags:

~~~powershell
python fetch_weather.py --help
~~~

## 2. Environment variable: cấu hình ở ngoài code

Environment variable là key/value gắn với process. Đọc nó trong Python:

~~~python
timeout_seconds = float(os.getenv("WEATHER_TIMEOUT_SECONDS", "10"))
~~~

- `os.getenv("WEATHER_TIMEOUT_SECONDS", "10")`: lấy biến nếu có, nếu không dùng text `"10"`.
- `float(...)`: đổi text thành số để Requests dùng làm timeout.

Timeout là cấu hình triển khai, không phải logic làm sạch. Ta có thể đổi timeout theo môi trường mà không sửa file Python.

API key cũng thường được đọc bằng environment variable, ví dụ `os.getenv("WEATHER_API_KEY")`. Bài này không có API key vì Open-Meteo endpoint công khai không yêu cầu nó. Không đặt secret thật vào source code, file JSON output hoặc Git.

## 3. HTTP GET và query parameters

Một HTTP request có:

~~~text
method + URL + query parameters + headers + body (tùy request)
~~~

Bài này dùng GET: lấy dữ liệu, không thay đổi dữ liệu trên server.

~~~python
params = {
    "latitude": args.latitude,
    "longitude": args.longitude,
    "current": "temperature_2m,relative_humidity_2m",
    "timezone": args.timezone,
}

response = requests.get(API_URL, params=params, timeout=timeout_seconds)
~~~

Requests tự mã hóa `params` thành query string. Đừng ghép URL bằng tay như `f"...?latitude={...}&..."`: dễ quên encode text, khó đọc và khó thêm/xóa tham số.

## 4. Timeout và HTTP status

Không có `timeout`, script có thể chờ rất lâu khi network gặp vấn đề. Luôn truyền timeout:

~~~python
response = requests.get(API_URL, params=params, timeout=timeout_seconds)
~~~

HTTP không tự ném lỗi với status 404 hay 500. Dòng này biến status lỗi thành `HTTPError`:

~~~python
response.raise_for_status()
~~~

Bao hai bước trong `try/except`:

~~~python
try:
    response = requests.get(API_URL, params=params, timeout=timeout_seconds)
    response.raise_for_status()
except requests.exceptions.RequestException as error:
    raise RuntimeError(f"weather request failed: {error}") from error
~~~

`RequestException` bao các lỗi request phổ biến, gồm timeout, connection và HTTP status. `from error` giữ lại nguyên nhân gốc trong traceback.

## 5. JSON response và data contract

Sau khi request thành công:

~~~python
payload = response.json()
~~~

`response.json()` đổi JSON trong HTTP response thành dictionary Python, giống `json.load` ở Ngày 3 nhưng nguồn lần này là network thay vì file.

Bài mong đợi response có:

~~~python
payload["current"]
~~~

Trước khi dùng, kiểm tra contract:

~~~python
if "current" not in payload:
    raise ValueError("response has no current weather")
~~~

Sau này API có thể thay version hoặc trả lỗi dưới dạng JSON. Data contract check giúp phát hiện điều đó sớm.

## 6. Lưu raw response và metadata

Output không chỉ chứa response API. Nó ghi thêm:

~~~python
{
    "city": args.city,
    "requested_at": "...",
    "request": params,
    "response": payload,
}
~~~

Lý do:

- `city` là nhãn con người chọn; API nhận tọa độ chứ không tự xác nhận tên thành phố.
- `requested_at` cho biết pipeline gọi API lúc nào.
- `request` cho phép tái hiện chính xác các tham số đã dùng.
- `response` giữ raw data để transform ở bước sau.

Đây là mô hình nhỏ của data lake `raw layer`: giữ nguyên nguồn và metadata trước khi làm sạch.

## 7. Luồng chạy

~~~text
parse_args
  -> lấy các flag CLI
fetch_current_weather
  -> đọc timeout environment variable
  -> GET API với params và timeout
  -> kiểm tra status
  -> JSON thành dictionary
  -> kiểm tra current
main
  -> tạo record raw gồm metadata + response
  -> ghi JSON
  -> in tóm tắt
~~~

## 8. Tài liệu ngoài

- [Requests quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [Python `argparse`](https://docs.python.org/3/library/argparse.html)
- [Open-Meteo API](https://open-meteo.com/en/docs)

Chỉ cần hiểu GET, `params`, `timeout`, `raise_for_status` và `response.json` hôm nay.
