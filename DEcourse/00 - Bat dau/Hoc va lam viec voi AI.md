---
tags: [decourse, ai, learning]
---

# Học và làm việc với AI

## Hai chế độ

**Học kỹ năng mới:** tự thử 20–30 phút, hỏi gợi ý và khái niệm, yêu cầu AI giải thích lỗi. Sau đó đóng chat và tự viết lại. **Làm sản phẩm:** có thể dùng AI viết/refactor, nhưng bạn phải đặt yêu cầu, kiểm chứng và chịu trách nhiệm kết quả.

## Prompt dùng khi bị kẹt

```text
Mục tiêu: nạp snapshot mà chạy lại cho cùng kết quả.
Expected: input A -> B -> A thì output cuối là A.
Actual: loader bỏ qua A ở lần cuối.
Đây là ví dụ tối thiểu và query kiểm tra của tôi: ...
Chỉ ra giả định nào sai, gợi ý một test phản ví dụ trước;
chưa đưa toàn bộ lời giải. Hỏi tôi giải thích lại sau khi sửa.
```

## Cách kiểm chứng

| AI đề xuất | Kiểm tra độc lập |
|---|---|
| SQL doanh thu | Expected 3–5 dòng bằng tay; đối soát source; kiểm tra fan-out |
| Retry | Fake timeout/429/404; số lần gọi và sleep; không gọi mạng trong unit test |
| Incremental | Update cũ 30 ngày, delete, đổi partition, so với rebuild |
| API/model mới | Đọc tài liệu chính thức đúng phiên bản; không tin tên model tự sinh |
| Tối ưu | Query plan và số đo trước/sau, cùng dữ liệu |

Không đưa secret hoặc dữ liệu cá nhân chưa được phép vào hosted AI. Code chạy được chưa chứng minh đúng; test do AI viết cùng giả định sai cũng có thể xanh.

## Thử độc lập

Chọn một thay đổi của bạn, nhờ AI phản biện 3 failure mode. Tự tái hiện ít nhất một mode bằng test. Ghi vào [[Nhat ky hoc]]: đề xuất nào đúng, sai, kiểm tra bằng gì.

## Tự hỏi

1. Nếu tắt AI 30 phút, mình còn giải thích được pipeline không?
2. Test nào sẽ bắt lời giải trông hợp lý nhưng sai?
3. Mình đang học hiểu nguyên nhân hay chỉ hỏi patch tiếp theo?

Nguồn: [nghiên cứu Anthropic về hình thành kỹ năng](https://www.anthropic.com/research/AI-assistance-coding-skills), thí nghiệm hẹp trên người học thư viện mới; không suy thành kết luận mọi cách dùng AI đều có hại.
