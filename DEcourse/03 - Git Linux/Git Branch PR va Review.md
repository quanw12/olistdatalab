---
tags: [decourse, git, collaboration]
module: 02
---

# Git, Branch, PR và Review

## Khi dùng

Git lưu lịch sử và giúp review thay đổi; commit không phải bản sao lưu dữ liệu thô. Mỗi lab có thay đổi nhỏ, mô tả vì sao và bằng chứng kiểm tra.

## Lệnh — repo thực hành riêng

```bash
git status --short
git switch -c codex/lab-ingest
git diff
git add labs/06-ingest
git diff --cached
git commit -m "feat(lab): validate order keys before publish"
git push -u origin codex/lab-ingest
```

Trước commit kiểm tra file staged, secret, dataset và file tạm. `.gitignore` không xóa file đã track; nếu secret đã lộ phải rotate, không chỉ thêm ignore.

## Fetch và cập nhật

```bash
git fetch origin
git log --oneline --graph -10
git diff origin/main...HEAD
```

fetch cập nhật remote-tracking refs, không tự merge. pull lấy rồi tích hợp theo cấu hình merge/rebase. Không force push nhánh dùng chung để sửa lịch sử nếu chưa phối hợp.

## PR có ích

```text
Vấn đề: snapshot A -> B -> A bị giữ ở B.
Thay đổi: kiểm tra phiên bản đang publish thay vì mọi hash trong lịch sử.
Kiểm chứng: regression A/B/A và retry file output.
Giới hạn: một writer local; DB và filesystem không chung transaction.
```

## Tự luyện

Trong repo bỏ đi: tạo conflict cùng một dòng ở hai nhánh, resolve và giải thích kết quả. Nhờ một bạn review query fan-out, yêu cầu họ hỏi về dữ liệu thiếu, không chỉ style.

Ôn: staged khác modified? revert khác reset? Làm sao xem chính xác những gì sắp push?

Liên quan: [[Testing Logging va CI]], [[Delivery va Reproducibility]]. Nguồn: [Pro Git](https://git-scm.com/book/en/v2), [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow).
