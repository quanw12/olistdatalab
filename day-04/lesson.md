# Bài học Ngày 4: pandas cho làm sạch dữ liệu theo cột

## 1. Vì sao dùng pandas?

Ở Ngày 1, bạn đọc từng row của CSV rồi dùng `for`, `if` và `set` để xử lý. Cách đó rất tốt để hiểu logic pipeline.

Pandas phù hợp khi dữ liệu là một bảng. Thay vì nói “lấy một dòng rồi kiểm tra”, ta nói “chuyển cả cột này thành số” hoặc “giữ các dòng thỏa tất cả điều kiện”.

~~~text
CSV                 DataFrame
city,temperature    một bảng có cột và hàng
Hanoi,31.2          có thể lọc/xử lý theo cả cột
~~~

Pandas không thay thế tư duy data contract. Nó chỉ làm thao tác bảng ngắn hơn và ít vòng lặp hơn.

## 2. DataFrame và Series

~~~python
import pandas as pd

df = pd.read_csv("messy_weather.csv")
~~~

`df` là một **DataFrame**: toàn bộ bảng. Lấy một cột:

~~~python
temperature = df["temperature_c"]
~~~

`temperature` là một **Series**: một danh sách có nhãn, tương ứng với cột `temperature_c`.

Ba lệnh nên dùng khi mở một file chưa quen:

~~~python
print(df.head())
print(df.dtypes)
print(df.info())
~~~

- `head()` xem vài dòng đầu.
- `dtypes` xem pandas đang hiểu kiểu dữ liệu mỗi cột.
- `info()` cho biết số dòng non-null và kiểu dữ liệu.

## 3. Missing value và `NaN`

CSV không có kiểu dữ liệu thật. Một ô trống hoặc giá trị không đổi được sang số có thể trở thành `NaN` trong pandas. `NaN` nghĩa là “giá trị số bị thiếu hoặc không hợp lệ”.

~~~python
pd.isna(df["temperature_c"])
df["temperature_c"].isna()
df["temperature_c"].notna()
~~~

Kết quả là một Series True/False theo từng dòng.

| Giá trị trong CSV | Sau khi chuyển số với `errors="coerce"` |
|---|---|
| `31.2` | `31.2` |
| `not_available` | `NaN` |
| ô trống | `NaN` |

Điều này cho pipeline cơ hội xử lý lỗi theo quy tắc của mình, thay vì dừng ngay ở dòng lỗi đầu tiên.

## 4. Chuẩn hóa cột

### Dọn text

~~~python
df["city"] = df["city"].str.strip()
~~~

`df["city"]` lấy Series thành phố. `.str` mở các method text cho cả cột; `.strip()` xóa khoảng trắng đầu/cuối của từng giá trị.

### Đổi số

~~~python
df["temperature_c"] = pd.to_numeric(
    df["temperature_c"],
    errors="coerce",
)
~~~

Không dùng `float(...)` ở đây vì `float` chỉ đổi được một giá trị. `pd.to_numeric` đổi toàn bộ Series.

### Đổi ngày

~~~python
df["observed_at"] = pd.to_datetime(
    df["observed_at"],
    format="%Y-%m-%d",
    errors="coerce",
)
~~~

Sau dòng này, ngày hợp lệ trở thành kiểu pandas datetime; ngày thiếu hoặc sai trở thành `NaT`, nghĩa là missing datetime.

## 5. Boolean mask: điều kiện cho cả cột

Trong Python thường:

~~~python
if 0 <= humidity <= 100:
    ...
~~~

Trong pandas, điều kiện đó áp dụng cho cả Series:

~~~python
df["humidity_pct"].between(0, 100)
~~~

Kết quả có dạng:

~~~text
0     True
1     True
2    False
...
~~~

Nối nhiều điều kiện bằng `&`. Mỗi điều kiện phải nằm trong ngoặc:

~~~python
valid_rows = (
    df["city"].notna()
    & df["observed_at"].notna()
    & df["temperature_c"].between(-50, 60)
    & df["humidity_pct"].between(0, 100)
)
~~~

Đây là một **mask**: `True` cho dòng được giữ, `False` cho dòng bị loại.

Đếm dòng invalid:

~~~python
invalid_rows = int((~valid_rows).sum())
~~~

`~` đảo mask: True thành False và ngược lại. Với Boolean trong Python, `True` được tính như 1, `False` như 0, nên `sum()` đếm số dòng True.

## 6. Lọc, copy và bỏ trùng

Lọc DataFrame bằng `.loc`:

~~~python
candidate_df = df.loc[valid_rows].copy()
~~~

`.loc[valid_rows]` giữ các dòng có mask True. `copy()` tạo bảng mới độc lập, giúp bạn có thể sửa bảng lọc mà không vô tình sửa `df` gốc.

Bỏ trùng theo city và ngày:

~~~python
before_deduplicate = len(candidate_df)
clean_df = candidate_df.drop_duplicates(
    subset=["city", "observed_at"],
    keep="first",
).copy()
duplicate_rows = before_deduplicate - len(clean_df)
~~~

`subset` chỉ định cột tạo khóa trùng. `keep="first"` giữ dòng hợp lệ xuất hiện đầu tiên, giống quy tắc Ngày 1.

## 7. Chuẩn bị output

Ở thời điểm này `observed_at` là datetime. CSV nên có text ngày rõ ràng:

~~~python
clean_df["observed_at"] = clean_df["observed_at"].dt.strftime("%Y-%m-%d")
~~~

Ghi CSV:

~~~python
clean_df.to_csv(output_path, index=False)
~~~

`index=False` quan trọng: nó không ghi thêm cột đánh số 0, 1, 2... của pandas vào file.

## 8. Luồng code của bài

~~~text
main
  -> pd.read_csv: CSV thành DataFrame
  -> clean_weather
       -> copy bảng
       -> chuẩn hóa text, số, ngày
       -> tạo valid_rows
       -> lọc invalid
       -> bỏ trùng
       -> trả clean_df và hai số đếm
  -> to_csv: ghi output
  -> print: in report
~~~

Hàm `clean_weather` trả về ba giá trị:

~~~python
clean_df, invalid_rows, duplicate_rows = clean_weather(raw_df)
~~~

Đây là tuple unpacking, giống `clean, rejection_reason = clean_row(raw_row)` ở Ngày 1.

## 9. Tài liệu ngoài

- [pandas: Getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
- [pandas: Missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [pandas: `read_csv` API](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

Đọc khi cần, sau đó quay lại bài. Không cần học `groupby`, merge hay biểu đồ hôm nay; chúng thuộc Ngày 5.
