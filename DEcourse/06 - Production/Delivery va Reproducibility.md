---
tags: [decourse, deployment, reproducibility]
module: 21
---

# Delivery và Reproducibility

## Khi dùng

Một người khác phải dựng lại hệ thống từ repo với input/version xác định. “Máy mình chạy được” cần chuyển thành lệnh, cấu hình và bằng chứng rõ.

## Release manifest

```yaml
# Pattern ghi bằng giá trị đo được của bạn, không chép placeholder thành kết quả.
release:
  git_commit: "dien-sha"
  python: "dien-version"
  os: "dien-os"
  dependencies_lock: "dien-file-va-hash"
  input_snapshot_sha256: "dien-hash"
  dbt_adapter: "dien-version"
  image_digest: "dien-digest-neu-co"
  data_interval: "dien-start-end"
```

## Quy trình thực hành

1. Tạo venv sạch, cài dependency có phiên bản, chạy pip check.
2. Chạy unit + integration và sample batch; ghi skip/error nếu có.
3. Clone ở thư mục/WSL khác, chạy lại từ README.
4. Kiểm tra counts, keys, tiền, output và quyền, không chỉ exit code.
5. Lưu manifest + commit; review trước publish.

## Rollback

Rollback code không tự rollback schema/data. Với thêm cột tương thích có thể chuyển consumer theo từng bước. Với phá vỡ schema cần migration, versioned tables/views, đường phục hồi hoặc forward fix. Giữ raw/version input cho rebuild.

> [!warning] Reference local
> Publish từng bảng bằng DROP/RENAME có giới hạn về grant/index/dependency và multi-table consistency. Bài production yêu cầu kiểm tra reader sau publish và quyết định chiến lược phục vụ phù hợp.

## Tự luyện và ôn

Thêm một cột không bắt buộc, deploy v2 rồi rollback v1; chứng minh consumer vẫn đọc. Sau đó đổi kiểu cột phá vỡ và mô tả bước chuyển an toàn. Khác biệt môi trường nào gây “same code, different result”?

Liên quan: [[Python Environment va Packaging]], [[Git Branch PR va Review]], [[Architecture Decision Record]]. Nguồn: [pip repeatable installs](https://pip.pypa.io/en/stable/topics/repeatable-installs/).
