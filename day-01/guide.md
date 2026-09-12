# Day 1 — Python foundations for a small data pipeline

## Học trước khi làm

Đọc theo thứ tự này trước khi mở `clean.py`:

1. [Bài học: Từ CSV thô đến dữ liệu sạch](lesson.md)
2. [Trợ giúp: lệnh và cách debug](help.md)

Không cần hiểu hết ngay lần đầu. Sau mỗi phần tutorial, chạy ví dụ nhỏ rồi quay lại code khung.

## Today’s outcome

Turn a small, imperfect CSV file into a clean CSV and a short quality report.

You are not expected to know how to build a full system. Today’s job is only to learn the shape of one:

`raw file -> validate -> clean -> output + report`

## Time budget

About 2.5–3.5 hours. Stop after the required part if you get stuck; record the error instead of guessing.

## 1. Set up the project (15 min)

Mở terminal tại `C:\DE Courses` và kích hoạt môi trường Python đã có của project:

```powershell
.\.venv\Scripts\Activate.ps1
python --version
git status
```

Không tạo thêm `.venv` trong `day-01`; cả khóa học dùng một môi trường chung tại thư mục gốc.

Create `.gitignore` containing:

```text
.venv/
__pycache__/
output/
```

## 2. Read the input by hand (15 min)

Open `weather.csv`. Before coding, write your predictions in `notes.txt`:

1. Which rows should be rejected?
2. What makes a row a duplicate?
3. Which values should be converted to numbers?

Use this data contract for the required part:

- A valid row has a non-empty `city` and a date in `YYYY-MM-DD` format.
- `temperature_c` must be a number from -50 to 60.
- `humidity_pct` must be an integer from 0 to 100.
- A duplicate means the same `city` and `observed_at`.
- If duplicates conflict, keep the first valid row and reject later rows.

## 3. Complete `clean.py` (90 min)

Run the scaffold first:

```powershell
python clean.py
```

Then implement the TODOs in this order:

1. Read CSV with the standard-library `csv` module.
2. Validate and clean one row at a time with `clean_row`.
3. Reject invalid rows with a useful reason.
4. Track duplicate keys with a `set`.
5. Write valid rows to `output/clean.csv`.
6. Print a report with counts of accepted/rejected rows and rejection reasons.

Do not use pandas today. The point is to practice ordinary Python: functions, dictionaries, loops, conditionals, exceptions and files.

## 4. Verify it (25 min)

Your program must report:

- `accepted: 5`
- `rejected: 5`
- exactly one duplicate

Open the clean output and check that it contains five data rows, no duplicate `(city, observed_at)` pair, and numeric values formatted consistently.

## 5. Git checkpoint (15 min)

```powershell
git add guide.md lesson.md help.md weather.csv clean.py notes.txt
git commit -m "feat: add weather CSV cleaning exercise"
git log --oneline
```

## Optional stretch (30 min)

Add a `--input` argument with `argparse`, so this works:

```powershell
python clean.py --input weather.csv
```

## What to send me after you finish

Paste these three things:

1. Your program’s final report.
2. Any error that blocked you, verbatim.
3. One sentence: which part felt least clear?

I will review the result and turn the errors into your Day 2 lesson.
