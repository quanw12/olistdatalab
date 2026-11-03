---
tags: [decourse, docker, postgres]
module: 10
---

# Docker, PostgreSQL và Serving

## Khi dùng

Docker đóng gói runtime, Compose nối các dịch vụ local; Postgres phục vụ nhiều người đọc BI. Container chạy được trên laptop chưa chứng minh production HA, backup hoặc quyền truy cập.

| Thuật ngữ | Ý nghĩa |
|---|---|
| Image | Mẫu filesystem/runtime |
| Container | Một instance đang chạy từ image |
| Volume | Dữ liệu ngoài vòng đời container |
| Healthcheck | Tín hiệu kiểm tra cụ thể, không phải mọi metric nghiệp vụ |
| Network | Tên service dùng được giữa các container |

## Lệnh — từ repo, cần Docker

```bash
docker compose config
docker compose up -d postgres metabase
docker compose ps
docker compose logs --tail 50 postgres
docker compose exec postgres psql -U olist -d olist
```

Không chia sẻ output config nếu chứa secret thật. `localhost` trong container là chính container đó; service cần nối `postgres:5432`, khác `localhost:5432` từ host.

## Pattern quyền đọc PostgreSQL

```sql
-- Pattern local, chạy bằng admin sau khi có schema marts.
CREATE ROLE analyst_reader NOLOGIN;
GRANT USAGE ON SCHEMA marts TO analyst_reader;
GRANT SELECT ON ALL TABLES IN SCHEMA marts TO analyst_reader;
-- Login thực hành được cấp role này qua cấu hình riêng, không ghi password thật ở đây.
```

Grant hiện tại không tự áp cho mọi table tương lai. Default privileges gắn với role tạo bảng; publish DROP/CREATE phải kiểm tra lại grant/index/view phụ thuộc. Không coi atomic swap từng bảng là atomic snapshot cho cả dashboard.

## Ứng dụng và tự luyện

Một dashboard Metabase là đủ. Publish Olist thật tới Postgres, kiểm tra counts/tiền và reader. Stop/remove container rồi dùng volume cũ: dữ liệu còn? Làm trên volume lab; `docker compose down -v` xóa volume nên không dùng tùy tiện.

Chạy EXPLAIN trước/sau index trên query dashboard; giữ benchmark và nhận xét nếu index không có lợi.

Ôn: vì sao notebook và pipeline cùng ghi DuckDB có thể lock? Vì sao BI đọc Postgres phù hợp hơn đọc chung file DuckDB?

Liên quan: [[Transactions Index va EXPLAIN]], [[Security va Governance]]. Nguồn: [Docker get started](https://docs.docker.com/get-started/), [Postgres privileges](https://www.postgresql.org/docs/current/ddl-priv.html).
