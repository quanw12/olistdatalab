# Gợi ý Ngày 2

Chỉ mở đúng phần TODO đang kẹt. Tự gõ lại từng dòng để biết biến nào đang chứa giá trị gì.

## TODO 1 và 2: hai vùng nhớ rỗng

~~~python
temperatures = []
cities = set()
~~~

`[]` tạo list rỗng. `set()` tạo set rỗng; không dùng `{}` vì `{}` là dictionary rỗng.

## TODO 3: đi qua từng hàng

~~~python
for row in rows:
    city = row["city"]
    temperature_c = row["temperature_c"]
~~~

`row` là biến tạm. Sau mỗi lượt lặp, nó trỏ sang dictionary kế tiếp trong `rows`.

## TODO 4: thêm dữ liệu

Đặt các dòng này **bên trong** vòng lặp, cùng mức thụt lề với hai dòng lấy dữ liệu:

~~~python
cities.add(city)
temperatures.append(temperature_c)
~~~

`cities.add` tự bỏ tên thành phố lặp. `temperatures.append` giữ mọi nhiệt độ vì mỗi giá trị đều là một quan sát cần tính.

## TODO 5: tính các số

Đặt phần này **sau** vòng lặp, nghĩa là thụt lề 4 dấu cách trong hàm:

~~~python
lowest_temperature = min(temperatures)
highest_temperature = max(temperatures)
average_temperature = round(sum(temperatures) / len(temperatures), 1)
~~~

Tại đây `temperatures` có 5 số, nên chia cho `len(temperatures)` là tính trung bình.

## TODO 6: trả về báo cáo

~~~python
return {
    "row_count": len(rows),
    "cities": sorted(cities),
    "temperature_min_c": lowest_temperature,
    "temperature_max_c": highest_temperature,
    "temperature_avg_c": average_temperature,
}
~~~

`sorted(cities)` biến set thành list có thứ tự để output lần nào cũng giống nhau.

## Nếu thấy lỗi

| Lỗi | Nguyên nhân hay gặp | Cách sửa |
|---|---|---|
| `NameError: temperatures is not defined` | Chưa tạo list hoặc tạo sai mức thụt lề | Đặt `temperatures = []` ngay trong `summarize_weather`, trước `for` |
| `KeyError: ...` | Gõ sai tên key | Chỉ dùng `"city"` và `"temperature_c"` |
| `TypeError: 'NoneType' object is not subscriptable` | Hàm chưa `return` dictionary | Hoàn thành TODO 6 và xóa `pass` |
| `IndentationError` | Các dòng trong cùng block không thụt lề giống nhau | Dùng 4 spaces; không trộn tab và spaces |
| Trung bình sai | `append` ở ngoài vòng lặp hoặc quên chia cho số dòng | So lại TODO 4 và TODO 5 |

## Tự trace bằng tay

Ở lượt lặp đầu tiên:

~~~python
row = {"city": "Hanoi", "temperature_c": 31.2}
~~~

Sau hai lệnh thêm dữ liệu:

~~~python
cities        # {"Hanoi"}
temperatures  # [31.2]
~~~

Ở lượt thứ hai, `"Da Nang"` và `30.1` được thêm vào. Sau 5 lượt, list có 5 nhiệt độ, còn set chỉ có 3 tên thành phố.
