# Cheat sheet Ngày 1

## Chạy bài

Mở PowerShell trong `C:\DE Courses\day-01`:

```powershell
python clean.py
```

Nếu terminal đang ở `C:\DE Courses`, dùng:

```powershell
python .\day-01\clean.py
```

## Lỗi thường gặp

| Hiện tượng | Nguyên nhân thường gặp | Cách kiểm tra |
|---|---|---|
| `FileNotFoundError` | Chạy ở sai thư mục | Dùng `Get-Location`, rồi chạy lại trong `day-01` |
| `TypeError: cannot unpack...` | `clean_row` không trả về đúng hai giá trị | Mọi nhánh của hàm phải trả `(clean, reason)` |
| `AttributeError: 'NoneType'...` | Dùng `clean[...]` trước khi kiểm tra `clean is None` | Xử lý dòng bị loại trước |
| Output rỗng | `clean_row` luôn trả `None` hoặc chưa thêm dòng vào list | In thử `raw_row`, rồi in `clean` |
| Số dòng hợp lệ sai | Kiểm tra trùng trước khi xác nhận dòng hợp lệ, hoặc quên `continue` | So lại pseudocode trong tutorial |



Phần cú pháp đầy đủ cho TODO 5–7 nằm ở mục **8.1** trong `lesson.md`.

## In để debug

Tạm thời thêm một trong các dòng sau trong vòng lặp:

```python
print(raw_row)
print(clean, rejection_reason)
print(seen_keys)
```

Sau khi hiểu lỗi, xóa hoặc comment các dòng `print` đó để output sạch.

## Git tối thiểu hôm nay

```powershell
git status
git add .
git commit -m "feat: clean weather CSV"
git log --oneline
```

Commit là một mốc lưu thay đổi có mô tả. Chưa cần học branch, rebase hay pull request hôm nay.
