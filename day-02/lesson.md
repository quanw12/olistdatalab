# Bài học Ngày 2: hiểu Python bằng chính pipeline Ngày 1

## 1. Bức tranh lớn: script Ngày 1 chạy như thế nào?

Khi bạn chạy:

~~~powershell
python clean.py
~~~

Python đọc file từ trên xuống. Nó **định nghĩa** các hàm trước, nhưng chưa chạy nội dung trong hàm ngay. Cuối file có:

~~~python
if __name__ == "__main__":
    main()
~~~

Khi một file được chạy trực tiếp, Python đặt biến đặc biệt `__name__` thành `"__main__"`. Điều kiện đúng, nên `main()` được gọi.

Luồng chạy sau đó là:

~~~text
main()
  -> tạo thư mục output và các vùng nhớ
  -> mở weather.csv
  -> lặp qua từng raw_row
       -> gọi clean_row(raw_row)
       -> nếu không hợp lệ: đếm lý do, sang dòng tiếp
       -> nếu trùng: đếm lý do, sang dòng tiếp
       -> nếu hợp lệ: giữ lại dòng
  -> ghi các dòng hợp lệ ra CSV
  -> in báo cáo
~~~

Đây là cách chia nhỏ một chương trình: `main` điều phối công việc, còn `clean_row` chỉ chịu trách nhiệm làm sạch **một** dòng.

## 2. Biến và giá trị

Một biến là tên trỏ tới một giá trị:

~~~python
city = "Hanoi"
temperature_c = 31.2
~~~

Dấu `=` nghĩa là “gán giá trị ở bên phải cho tên ở bên trái”, không phải phép so sánh. Muốn so sánh bằng nhau thì dùng `==`:

~~~python
city == "Hanoi"  # kết quả là True hoặc False
~~~

Bốn kiểu dữ liệu gặp nhiều nhất trong bài:

| Kiểu | Ví dụ | Dùng để làm gì |
|---|---|---|
| `str` | `"Hanoi"` | văn bản |
| `int` | `78` | số nguyên |
| `float` | `31.2` | số có phần thập phân |
| `bool` | `True`, `False` | kết quả đúng/sai |

Các hàm chuyển kiểu bạn đã dùng:

~~~python
int("78")        # 78
float("31.2")    # 31.2
str(78)          # "78"
~~~

Nếu Python không thể chuyển `"not_available"` thành số, nó ném ra `ValueError`.

## 3. Hàm: đóng gói một việc có tên

Hàm được tạo bằng `def`:

~~~python
def say_hello(name):
    message = f"Hello, {name}"
    return message
~~~

- `def` bắt đầu định nghĩa hàm.
- `say_hello` là tên hàm.
- `name` là **tham số**: chỗ trống nhận dữ liệu đi vào.
- Phần thụt vào là thân hàm.
- `return` gửi một giá trị ra ngoài hàm và kết thúc lần gọi hàm đó.

Gọi hàm:

~~~python
greeting = say_hello("Quan")
print(greeting)  # Hello, Quan
~~~

Trong `clean.py`:

~~~python
clean, rejection_reason = clean_row(raw_row)
~~~

Nghĩa là gửi một dòng thô vào `clean_row`. Hàm trả về **hai giá trị**. Python ghép hai giá trị đó thành một tuple rồi tách chúng ra:

~~~python
result = clean_row(raw_row)
clean = result[0]
rejection_reason = result[1]
~~~

Hai cách trên có cùng ý nghĩa; cách đầu ngắn và thường gặp hơn.

### `return` và `print` khác nhau

~~~python
def double(number):
    return number * 2

answer = double(4)  # answer nhận 8
print(answer)       # chỉ hiển thị 8 ra terminal
~~~

`return` chuyển dữ liệu cho phần khác của chương trình dùng tiếp. `print` chỉ hiển thị để người chạy nhìn thấy.

## 4. Type hint trong `clean.py`

Dòng này trông dài vì có type hint:

~~~python
def clean_row(raw_row: dict[str, str]) -> tuple[dict[str, object] | None, str | None]:
~~~

Đọc phần quan trọng trước:

~~~python
def clean_row(raw_row):
~~~

Đó là một hàm tên `clean_row`, nhận một tham số tên `raw_row`. Các phần còn lại chỉ là **nhãn mô tả**:

| Phần | Ý nghĩa |
|---|---|
| `raw_row: dict[str, str]` | `raw_row` là dictionary có key và value dạng chuỗi |
| `-> ...` | mô tả giá trị hàm trả về |
| `tuple[A, B]` | trả về cặp gồm A và B |
| `X | None` | giá trị có thể là X, hoặc `None` |
| `object` | chấp nhận một giá trị Python bất kỳ |

Python vẫn chạy được nếu bỏ type hint:

~~~python
def clean_row(raw_row):
~~~

Trong Ngày 2, ta cố tình chưa dùng type hint trong `exercise.py` để nhìn rõ logic. Bạn sẽ dùng lại chúng khi đã quen.

## 5. Cấu trúc dữ liệu: `dict`, `list`, `set`

### Dictionary: một hàng dữ liệu có tên cột

~~~python
row = {
    "city": "Hanoi",
    "temperature_c": 31.2,
}

city = row["city"]                 # "Hanoi"
row["temperature_c"] = 30.5        # cập nhật giá trị
~~~

`row["city"]` không phải hàm. Dấu ngoặc vuông lấy giá trị bằng key `"city"`. Nếu key không tồn tại, Python báo `KeyError`.

### List: giữ nhiều giá trị theo thứ tự

~~~python
temperatures = []
temperatures.append(31.2)
temperatures.append(30.1)
~~~

`append` là một **method**: hàm gắn với list. List bây giờ là `[31.2, 30.1]`. List giữ được giá trị trùng và giữ thứ tự thêm vào.

### Set: chỉ giữ mỗi giá trị một lần

~~~python
cities = set()
cities.add("Hanoi")
cities.add("Hanoi")
cities.add("Da Nang")
~~~

`cities` chỉ có `"Hanoi"` và `"Da Nang"`. Vì vậy `set` phù hợp để phát hiện key trùng ở Ngày 1 và tìm các thành phố khác nhau ở Ngày 2.

~~~python
"Hanoi" in cities  # True
~~~

## 6. Vòng lặp và điều kiện

### `for`

~~~python
for row in rows:
    print(row["city"])
~~~

Nếu `rows` có 5 dictionary, phần thụt vào chạy 5 lần. Mỗi lần, `row` lần lượt là một dictionary.

### `if`, `not` và `continue`

~~~python
if clean is None:
    rejection_reasons[rejection_reason] += 1
    continue
~~~

- `is None` hỏi liệu biến có đúng là giá trị đặc biệt `None` không.
- `+= 1` tăng giá trị hiện có thêm 1.
- `continue` bỏ phần còn lại của vòng lặp hiện tại và bắt đầu dòng kế tiếp.

Sau `continue`, code bên dưới không chạy cho dòng lỗi. Vì thế ở các dòng sau đó, `clean` không còn là `None`; nó là dictionary hợp lệ.

So sánh phạm vi:

~~~python
if not 0 <= humidity_pct <= 100:
    return None, "humidity_pct is outside allowed range"
~~~

Python hiểu `0 <= humidity_pct <= 100` là “nằm trong khoảng từ 0 đến 100”. `not` đảo kết quả: nằm ngoài khoảng thì điều kiện đúng.

## 7. Xử lý lỗi mong đợi với `try` và `except`

~~~python
try:
    temperature_c = float(raw_row["temperature_c"])
except ValueError:
    return None, "temperature_c is not numeric"
~~~

Python thử phần `try`. Nếu đổi chuỗi thành số thất bại và tạo đúng lỗi `ValueError`, nó chuyển vào `except` thay vì làm toàn bộ chương trình dừng.

Chỉ bắt lỗi mà bạn dự đoán và biết cách xử lý. Trong bài này, bắt `ValueError` là hợp lý; `except Exception` quá rộng, có thể che mất lỗi code thật.

## 8. Các module và method còn lại của `clean.py`

`import` đưa công cụ từ thư viện có sẵn của Python vào file:

| Cú pháp trong file | Công dụng |
|---|---|
| `import csv` | đọc/ghi file CSV |
| `from collections import Counter` | dictionary đặc biệt để đếm |
| `from datetime import date` | kiểm tra ngày ISO |
| `from pathlib import Path` | làm việc với đường dẫn file/thư mục |

Các lời gọi bạn gặp:

| Cú pháp | Nó làm gì |
|---|---|
| `raw_row["city"].strip()` | lấy city rồi xóa khoảng trắng đầu/cuối |
| `OUTPUT_DIR.mkdir(exist_ok=True)` | tạo `output`; không lỗi nếu thư mục đã tồn tại |
| `INPUT_PATH.open(...)` | mở file |
| `with ... as source_file:` | tự đóng file sau khi xong, kể cả khi lỗi |
| `csv.DictReader(source_file)` | đọc CSV thành từng dictionary |
| `Counter()` | tạo bộ đếm rỗng |
| `rejection_reasons[reason] += 1` | tăng đếm cho reason |
| `seen_keys.add(key)` | thêm một giá trị vào set |
| `accepted_rows.append(clean)` | thêm một dictionary vào cuối list |
| `date.fromisoformat(text)` | kiểm tra/đổi chuỗi ngày ISO thành đối tượng ngày |
| `len(values)` | đếm số phần tử |
| `sum(values)` | cộng các số |
| `min(values)`, `max(values)` | số nhỏ nhất/lớn nhất |
| `round(number, 1)` | làm tròn đến một chữ số thập phân |
| `sorted(values)` | tạo một list đã sắp xếp |

Một f-string đặt chữ `f` trước chuỗi để chèn biến vào `{}`:

~~~python
count = 5
print(f"accepted: {count}")
~~~

`pass` nghĩa là “không làm gì”. Nó thường là chỗ giữ chỗ cho code chưa viết. Dòng `pass` còn lại ở cuối vòng lặp của bạn không làm chương trình sai, nhưng khi đã có `seen_keys.add` và `accepted_rows.append`, nó không còn cần thiết.

## 9. Làm bài `exercise.py`

Hàm `summarize_weather` có hợp đồng đơn giản:

~~~text
Đầu vào: một list các dictionary đã sạch.
Đầu ra: một dictionary chứa số dòng, danh sách thành phố,
         nhiệt độ thấp nhất, cao nhất và trung bình.
~~~

Hãy làm theo đúng thứ tự:

1. Tạo `temperatures` là list rỗng và `cities` là set rỗng.
2. Dùng `for` để đi qua từng `row`.
3. Lấy city và temperature bằng key của dictionary.
4. Thêm city vào set, thêm temperature vào list.
5. Tính `min`, `max`, trung bình.
6. `return` một dictionary.

Đừng cố viết hết trong một lần. Sau khi làm xong phần vòng lặp, bạn có thể tạm thêm:

~~~python
print(temperatures)
print(cities)
~~~

để nhìn thấy vùng nhớ thay đổi. Xóa các `print` debug đó trước khi nộp bài.

## 10. Tài liệu ngoài, chỉ đọc phần cần thiết

- [Python Tutorial: defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Tutorial: lists, dictionaries và sets](https://docs.python.org/3/tutorial/datastructures.html)
- [Python Tutorial: errors and exceptions](https://docs.python.org/3/tutorial/errors.html)

Đọc 10–15 phút mỗi phần, gõ lại một ví dụ nhỏ, rồi quay về bài. Nếu chỉ đọc mà không chạy code, cú pháp sẽ rất khó nhớ.
