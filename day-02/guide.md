# Day 2 — Python căn bản qua báo cáo thời tiết

## Review Ngày 1

Kết quả bạn gửi là đúng:

~~~text
accepted: 5
rejected: 5
~~~

Năm dòng bị loại cũng khớp với data contract. Không có lỗi nào chặn bài. Phần bạn chưa rõ là cú pháp, hàm và logic Python, nên Ngày 2 sẽ chậm lại để học đúng những thứ đó trước khi đi tiếp tới JSON, API hay database.

## Mục tiêu hôm nay

Từ 5 bản ghi thời tiết đã sạch, viết một hàm tạo báo cáo:

~~~text
rows: 5
cities: Da Nang, Hanoi, Ho Chi Minh City
temperature min: 29.8 C
temperature max: 33.4 C
temperature avg: 31.3 C
~~~

Đây là một bước **transform** nhỏ trong pipeline: dữ liệu sạch đi vào, bảng tổng hợp đi ra.

## Học theo thứ tự này

1. Đọc [Bài học: đọc hiểu `clean.py` và Python căn bản](lesson.md), mục 1 đến mục 7.
2. Mở `exercise.py`. Đọc dữ liệu `WEATHER_ROWS` và phần `print_summary` trước.
3. Tự gõ phần thân của `summarize_weather` theo từng TODO, không cần dùng pandas hay tìm thư viện mới.
4. Nếu vướng một TODO quá 15 phút, xem đúng mục tương ứng trong [Gợi ý và cú pháp](help.md).
5. Chạy bài trong PowerShell khi đang ở thư mục `C:\DE Courses\day-02`:

~~~powershell
python exercise.py
~~~

6. Đối chiếu với output ở đầu trang này.

## Checklist hoàn thành

- [ ] Giải thích được hàm nhận gì, trả về gì.
- [ ] Biết vì sao dùng `list` cho nhiệt độ và `set` cho tên thành phố.
- [ ] Biết `for row in rows` chạy lần lượt thế nào.
- [ ] Chạy ra đúng 5 dòng báo cáo.
- [ ] Tự xóa dòng `pass` trong `summarize_weather` sau khi đã viết code thật.

## Git checkpoint

Khi đã chạy đúng:

~~~powershell
git status
git add day-02
git commit -m "feat(day-02): add weather summary exercise"
git push
~~~

Chỉ commit sau khi bạn đã tự viết và hiểu bài. Không cần tạo branch mới cho bài học cá nhân này.

## Việc thêm nếu còn thời gian

Quay lại `C:\DE Courses\day-01\clean.py` và tự chỉ ra:

1. `pass` ở cuối vòng lặp làm gì?
2. Vì sao sau `if clean is None: ... continue`, biến `clean` có thể được dùng như dictionary?
3. Vì sao `str(clean["city"])` là không cần thiết trong bài này?

Chưa cần sửa file Ngày 1. Gửi câu trả lời cho mình trước; mình sẽ review cách bạn suy luận.

## Gửi mình sau khi xong

1. Toàn bộ output của `python exercise.py`.
2. Phần thân hàm `summarize_weather` bạn đã viết.
3. Một câu trả lời: `return` khác `print` ở điểm nào?
