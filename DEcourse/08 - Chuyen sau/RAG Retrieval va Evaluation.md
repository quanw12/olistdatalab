---
tags: [decourse, rag, elective]
module: 16
---

# RAG: Retrieval và Evaluation

## Khi dùng

Trả lời từ tài liệu có nguồn và cập nhật được. RAG gồm ingestion tài liệu, chunking, retrieval/rerank và generation; vector database không tự làm câu trả lời đáng tin.

## Baseline retrieval — Python chạy độc lập, không gọi model

```python
# runnable
docs = {
    'grain': 'fact orders one row per order',
    'timezone': 'timestamps utc local business date',
    'retry': 'api timeout backoff retry',
}
query = set('orders grain order'.split())
scores = {key: len(query & set(text.split())) for key, text in docs.items()}
ranked = sorted(scores, key=lambda key: (-scores[key], key))
assert ranked[0] == 'grain'
gold = {'grain'}
recall_at_1 = len(set(ranked[:1]) & gold) / len(gold)
assert recall_at_1 == 1.0
```

Đây là token overlap baseline, không phải embeddings hoặc RAG hoàn chỉnh. Nó giúp có thước đo retrieval độc lập trước khi thêm model phức tạp.

## Pipeline cần thiết

Doc ID + content hash + version → chunks có source/heading → embeddings version → index → retrieval có access filter → answer dẫn nguồn. Khi tài liệu sửa/xóa, index/chunk cũ phải cập nhật hoặc loại; cache cần invalidation.

## Đánh giá tách lớp

- Retrieval: câu hỏi có gold document/chunk, đo recall@k và lỗi tìm sai nguồn.
- Generation: câu trả lời được nguồn hỗ trợ, citation đúng, biết từ chối khi thiếu bằng chứng.
- Permissions: người dùng không truy xuất chunk ngoài quyền; không chỉ filter sau khi trả lời.
- Freshness/cost/latency: version tài liệu, lần index cuối, thời gian query và chi phí.

## Bài tự chọn

Index tài liệu DEcourse, tạo 20 câu hỏi có nguồn expected, chia dev/test. So lexical baseline với embedding trên cùng tập. Sửa một định nghĩa grain và xóa một note: chứng minh câu trả lời không dùng chunk cũ.

Ôn: model trả lời đúng bằng kiến thức có sẵn có chứng minh retrieval đúng không? Vì sao citation trỏ file tồn tại vẫn có thể không hỗ trợ claim?

Liên quan: [[LLM Cache Evaluation va Guardrails]], [[Ingestion Contract va Idempotency]]. Nguồn: [RAG paper](https://arxiv.org/abs/2005.11401), [OWASP LLM](https://genai.owasp.org/llm-top-10/).
