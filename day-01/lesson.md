# Tutorial Ngày 1: từ file CSV thô đến dữ liệu sạch

## 1. Hôm nay bạn đang học gì?

Data Engineer không chỉ “đọc file rồi lưu lại”. Công việc là biến dữ liệu không chắc chắn thành dữ liệu mà người khác có thể tin và dùng được.

Ví dụ: một hệ thống thời tiết muốn biết nhiệt độ trung bình ở Hà Nội. Nếu file có ngày sai định dạng, nhiệt độ ghi chữ, độ ẩm 105% và dữ liệu trùng, phép tính trung bình có thể sai hoặc chương trình dừng giữa chừng.

Pipeline nhỏ hôm nay có 4 bước:

```text
CSV thô -> đọc từng dòng -> kiểm tra/làm sạch -> CSV sạch + báo cáo lỗi
```

Đây là phiên bản mini của pipeline thực tế. Sau này CSV sẽ thành API, kho dữ liệu và database, nhưng cách suy nghĩ không đổi.

## 2. Data contract: luật của dữ liệu

Trước khi code, hãy viết luật. Luật này gọi là **data contract**: bên gửi dữ liệu phải gửi gì, và pipeline chấp nhận gì.

Data contract của bài:

| Cột | Kiểu sau khi làm sạch | Luật |
|---|---|---|
| `city` | chuỗi | Không được rỗng |
| `observed_at` | chuỗi ngày `YYYY-MM-DD` | Phải là một ngày hợp lệ |
| `temperature_c` | số thực | Từ -50 đến 60 |
| `humidity_pct` | số nguyên | Từ 0 đến 100 |

Khóa duy nhất của bài là `(city, observed_at)`. Nghĩa là chỉ có một quan sát cho cùng thành phố trong cùng một ngày.

Trong dữ liệu thật, luật này thường nằm trong tài liệu, database constraint, hoặc code test. Hôm nay nó nằm trong `clean_row`.

## 3. CSV không “biết” kiểu dữ liệu

CSV là văn bản. Khi `csv.DictReader` đọc dòng này:

```csv
Hanoi,2026-08-01,31.2,78
```

Python nhận được:

```python
{
    "city": "Hanoi",
    "observed_at": "2026-08-01",
    "temperature_c": "31.2",
    "humidity_pct": "78",
}
```

Hai số vẫn là chuỗi. Vì vậy `"31.2" + "1"` sẽ cho `"31.21"`, không phải `32.2`.

Ta phải đổi kiểu dữ liệu có chủ đích:

```python
temperature_c = float(raw_row["temperature_c"])
humidity_pct = int(raw_row["humidity_pct"])
```

Nếu giá trị là `not_available`, hai dòng trên sẽ tạo `ValueError`. Đó không phải lỗi đáng sợ; đó là tín hiệu để pipeline loại dòng này và ghi lại lý do.

## 4. Hàm `clean_row`: một việc rõ ràng

Hàm trong bài nhận một dòng thô rồi trả về một trong hai kết quả:

```python
clean_row(raw_row)
# hợp lệ: (cleaned_dictionary, None)
# không hợp lệ: (None, "lý do")
```

Ví dụ một dòng hợp lệ:

```python
cleaned = {
    "city": "Hanoi",
    "observed_at": "2026-08-01",
    "temperature_c": 31.2,
    "humidity_pct": 78,
}
return cleaned, None
```

Ví dụ một dòng bị loại:

```python
return None, "temperature_c is not a number"
```

Lý do tách việc theo hàm: bạn có thể đọc, test và sửa luật của **một dòng** mà không phải nghĩ cùng lúc về file, output hay thống kê.

## 5. Kiểm tra từng trường theo thứ tự

Trong `clean_row`, làm theo thứ tự sau. Sau mỗi bước không đạt, trả về ngay.

### 5.1 Thành phố

```python
city = raw_row["city"].strip()
if not city:
    return None, "city is empty"
```

`strip()` xóa khoảng trắng đầu/cuối. Dòng chỉ có dấu cách cũng được xem là rỗng.

### 5.2 Ngày

```python
observed_at = raw_row["observed_at"].strip()
try:
    date.fromisoformat(observed_at)
except ValueError:
    return None, "observed_at is not YYYY-MM-DD"
```

`date.fromisoformat` vừa kiểm tra định dạng, vừa kiểm tra ngày có tồn tại. `2026-02-30` cũng sẽ bị loại.

### 5.3 Số

```python
try:
    temperature_c = float(raw_row["temperature_c"])
    humidity_pct = int(raw_row["humidity_pct"])
except ValueError:
    return None, "temperature_c or humidity_pct is not numeric"
```

Sau đó kiểm tra phạm vi:

```python
if not -50 <= temperature_c <= 60:
    return None, "temperature_c is outside allowed range"

if not 0 <= humidity_pct <= 100:
    return None, "humidity_pct is outside allowed range"
```

Đừng dùng `except Exception`. Nó che cả lỗi lập trình của bạn. Hôm nay ta chỉ biết có thể xảy ra `ValueError` khi chuyển chuỗi thành số hoặc ngày.

## 6. Bốn cấu trúc dữ liệu bạn đang dùng

| Cấu trúc | Dùng trong bài | Vì sao |
|---|---|---|
| `dict` | Một dòng dữ liệu | Truy cập theo tên cột, ví dụ `row["city"]` |
| `list` | `accepted_rows` | Giữ các dòng sạch theo thứ tự để ghi ra file |
| `set` | `seen_keys` | Kiểm tra “đã thấy khóa này chưa” rất nhanh |
| `Counter` | `rejection_reasons` | Đếm số lần từng lý do bị loại |

Ví dụ kiểm tra trùng:

```python
key = (clean["city"], clean["observed_at"])
if key in seen_keys:
    rejection_reasons["duplicate city and observed_at"] += 1
    continue

seen_keys.add(key)
accepted_rows.append(clean)
```

`continue` nghĩa là bỏ phần còn lại của vòng lặp hiện tại, rồi chuyển sang dòng CSV kế tiếp.

## 7. Đọc và ghi file an toàn

Mẫu `with` bảo đảm file được đóng, kể cả khi chương trình xảy ra lỗi.

```python
with INPUT_PATH.open(newline="", encoding="utf-8") as source_file:
    reader = csv.DictReader(source_file)
    for raw_row in reader:
        print(raw_row)
```

`DictReader` dùng dòng đầu tiên của CSV làm tên cột. `newline=""` là khuyến nghị của thư viện `csv` để đọc/ghi CSV đúng trên các hệ điều hành.

Khi ghi file, `DictWriter` cần biết thứ tự các cột:

```python
writer = csv.DictWriter(output_file, fieldnames=[
    "city", "observed_at", "temperature_c", "humidity_pct",
])
writer.writeheader()
writer.writerows(accepted_rows)
```

## 8. Pseudocode cho phần còn thiếu

Đọc pseudocode, tự chuyển thành Python, rồi mới xem lại các phần trên nếu kẹt:

## 8.1 TODO 5–7: khối code cần đặt trong vòng lặp

Trong `main`, bạn đang có ba biến đã chuẩn bị sẵn:

```python
accepted_rows = []          # nơi giữ dòng hợp lệ
rejection_reasons = Counter()  # nơi đếm lý do bị loại
seen_keys = set()           # nơi nhớ các khóa đã gặp
```

Ngay sau dòng này:

```python
clean, rejection_reason = clean_row(raw_row)
```

hãy **thay cả ba TODO và dòng `pass`** bằng khối sau:

```python
if clean is None:
    rejection_reasons[rejection_reason] += 1
    continue

key = (clean["city"], clean["observed_at"])

if key in seen_keys:
    rejection_reasons["duplicate city and observed_at"] += 1
    continue

seen_keys.add(key)
accepted_rows.append(clean)
```

### Đọc khối này theo từng nhánh

**Nhánh 1: dòng không hợp lệ.** `clean_row` trả về `(None, "lý do")`. `clean is None` sẽ đúng. Ta tăng số đếm cho lý do đó, rồi `continue` để bỏ qua mọi bước dưới và sang dòng CSV kế tiếp.

```python
if clean is None:
    rejection_reasons[rejection_reason] += 1
    continue
```

Ví dụ với dòng có `temperature_c = not_available`, kết quả trở thành:

```python
rejection_reasons["temperature_c or humidity_pct is not numeric"]
# 1
```

**Nhánh 2: dòng hợp lệ nhưng trùng.** Khi đã qua nhánh 1, `clean` chắc chắn là một dictionary. Ta tạo tuple gồm thành phố và ngày. Tuple dùng được làm phần tử của `set`.

```python
key = (clean["city"], clean["observed_at"])
```

Với bản ghi Hà Nội ngày 2026-08-01, `key` là:

```python
("Hanoi", "2026-08-01")
```

Nếu key đã có trong `seen_keys`, ta chỉ đếm lỗi trùng và chuyển sang dòng tiếp theo. Không thêm bản ghi đó vào `accepted_rows`.

```python
if key in seen_keys:
    rejection_reasons["duplicate city and observed_at"] += 1
    continue
```

**Nhánh 3: dòng hợp lệ và chưa trùng.** Đây là vị trí duy nhất được phép lưu dữ liệu. Thứ tự quan trọng: nhớ key trước, rồi thêm dòng.

```python
seen_keys.add(key)
accepted_rows.append(clean)
```

## 8.2 Ba cú pháp cần biết đúng cho TODO 5–7

| Cú pháp | Nghĩa trong bài |
|---|---|
| `if condition:` | Chỉ chạy phần thụt vào khi condition đúng |
| `continue` | Dừng xử lý dòng hiện tại, quay sang dòng tiếp theo trong `for` |
| `key in seen_keys` | Hỏi set xem key này đã được gặp chưa |
| `counter[name] += 1` | Tăng bộ đếm cho một tên lý do |

Đọc đúng các phần sau, mỗi phần 5–10 phút:

- [Python: `if`](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Python: `continue` trong vòng lặp](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
- [Python: `set`](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Python: `Counter`](https://docs.python.org/3/library/collections.html#collections.Counter)

## 8.3 Kiểm tra một lỗi trước khi chạy

Trong `weather.csv`, tên cột là `temperature_c`. Vì vậy trong phần TODO 2, dòng chuyển nhiệt độ phải dùng chính key đó:

```python
temperature_c = float(raw_row["temperature_c"])
```

Nếu dùng `raw_row["temperature"]`, chương trình sẽ báo `KeyError` vì CSV không có cột tên `temperature`.

```text
tạo thư mục output
tạo list các dòng hợp lệ
tạo Counter cho lý do bị loại
tạo set các khóa đã thấy

với mỗi dòng trong CSV:
    gọi clean_row
    nếu dòng không hợp lệ:
        tăng Counter theo lý do
        chuyển sang dòng tiếp theo

    tạo khóa từ city và observed_at
    nếu khóa đã có:
        tăng Counter duplicate
        chuyển sang dòng tiếp theo

    lưu khóa vào set
    thêm dòng sạch vào list

ghi list hợp lệ ra CSV
in số lượng và Counter
```

## 9. Tự kiểm tra trước khi chạy

Trả lời được các câu này nghĩa là bạn hiểu bài ở mức đủ tốt:

1. Vì sao phải đổi `"78"` thành `78`?
2. Vì sao không nên để một dòng lỗi làm cả pipeline dừng?
3. Vì sao dùng `(city, observed_at)` thay vì chỉ `city` để tìm dòng trùng?
4. Nếu chạy script hai lần, file output có bị nhân đôi không? Vì sao?

Câu 4 là mầm mống của khái niệm **idempotency**: chạy lại cùng đầu vào vẫn cho kết quả đúng. Ta sẽ quay lại nó ở Ngày 17.

## 10. Tài liệu ngoài cho đúng bài hôm nay

Không cần đọc hết. Chỉ mở khi cần làm rõ:

- [Python Tutorial: flow control, functions và data structures](https://docs.python.org/3/tutorial/)
- [Python `csv`: DictReader và DictWriter](https://docs.python.org/3/library/csv.html)
- [Python `datetime`: xử lý ngày](https://docs.python.org/3/library/datetime.html)
- [Pro Git: phần cơ bản](https://git-scm.com/book/en/v2)

## Khi nào mới xem đáp án?

Tự làm tối đa 45 phút cho một TODO. Nếu kẹt, gửi mình phần code hiện tại và lỗi. Mình sẽ đưa gợi ý theo đúng bước đang vướng, không ném cả đáp án để bạn mất cơ hội luyện tư duy.
