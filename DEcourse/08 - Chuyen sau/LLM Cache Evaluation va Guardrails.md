---
tags: [decourse, llm, elective]
module: 16
---

# LLM: Cache, Evaluation và Guardrails

## Khi dùng

Gán nhãn text hoặc trích thông tin khi rule/baseline chưa đủ. LLM là thành phần không hoàn toàn xác định; JSON hợp lệ chỉ kiểm tra cấu trúc, không chứng minh nhãn đúng nghĩa hoặc chống được prompt injection.

## Cache key — Python chạy độc lập

```python
# runnable
import hashlib

def cache_key(text, prompt_version, provider, model):
    digest = hashlib.sha256(text.encode('utf-8')).hexdigest()
    return digest, prompt_version, provider, model

a = cache_key('Entrega atrasada', 'v1', 'ollama', 'model-A')
assert a == cache_key('Entrega atrasada', 'v1', 'ollama', 'model-A')
assert a != cache_key('Produto excelente', 'v1', 'ollama', 'model-A')
assert a != cache_key('Entrega atrasada', 'v1', 'ollama', 'model-B')
```

Trong sản phẩm còn cần version preprocessing, model revision/generation parameters/schema nếu chúng ảnh hưởng output. Hash full input làm invalidation thận trọng ngay cả khi prompt truncate. Model alias có thể đổi backend; pin revision khi dịch vụ hỗ trợ và ghi thời điểm/cấu hình.

## Evaluation tối thiểu

| Phép đo | Ý nghĩa | Giới hạn |
|---|---|---|
| Parse/schema pass | Output đọc được | Không nói đúng nghĩa |
| Agreement với điểm sao | Tín hiệu weak label | Khách có thể cho điểm lệch nội dung |
| Gold set gán tay | So với rubric người gán | Cần hướng dẫn và giải quyết bất đồng |
| Macro-F1/confusion matrix | Lỗi theo lớp | Cần sample đủ, không chỉ accuracy |
| Latency/cost | Vận hành | Đo retry, token và invalid outputs |

Tách tập phát triển prompt và held-out test; so provider cùng tập input, không lấy cache khác nội dung để so. Bắt đầu 50–100 review có đa dạng lớp; báo rõ độ nhỏ và sai số, không tự gọi benchmark toàn thị trường.

## Reference repo

Cache giữ model + input hash + prompt/provider; migration giữ nhãn cũ nhưng hash không biết không được tái sử dụng. `ai-eval` chỉ so nhãn với nội dung review hiện tại, phân theo model. Dashboard dùng nhãn mới nhất của review hiện tại để không đếm lặp lịch sử.

## Guardrail và bài thực hành

Validate schema với exception rõ, xử lý timeout/rate limit, giới hạn request/token/cost; invalid vào quarantine/DLQ có cách retry. Với text-to-SQL: parse AST, single SELECT, whitelist bảng/cột, role chỉ đọc, cấm external functions/file/network, timeout và scan cap. LIMIT không giới hạn mọi chi phí.

Thử review “ignore instructions” và câu hỏi SQL gây full scan/cross join; đo output semantics và resource controls. Không coi chỉ read-only connection là đủ cho mọi engine.

Ôn: khi nào rule tốt hơn LLM? Tại sao cùng provider nhưng đổi model phải gán nhãn lại? Làm sao nhận ra “positive” đúng schema nhưng sai nội dung?

Liên quan: [[Hoc va lam viec voi AI]], [[Security va Governance]], [[RAG Retrieval va Evaluation]]. Nguồn: [OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/), [Ollama API](https://github.com/ollama/ollama/blob/main/docs/api.md).
