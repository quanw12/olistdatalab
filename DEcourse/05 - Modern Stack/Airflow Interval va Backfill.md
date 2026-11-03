---
tags: [decourse, airflow, orchestration]
module: 11
---

# Airflow, Interval và Backfill

## Khi dùng

Airflow lên lịch và quản lý dependency/retry/history. Data interval là khoảng dữ liệu của run, không phải thời điểm task thực sự chạy. Backfill phải truyền interval tới logic xử lý; chạy lại lệnh đọc “latest” không tái tạo lịch sử.

## Pattern Airflow 3 — cần tích hợp

```python
# Pattern: lab CLI dưới đây do bạn tự viết, không phải lệnh có sẵn của olist.
from datetime import datetime, timezone
from airflow.sdk import dag
from airflow.providers.standard.operators.bash import BashOperator

@dag(schedule='0 6 * * *', start_date=datetime(2026, 1, 1, tzinfo=timezone.utc),
     catchup=False, max_active_runs=1)
def lab_partition_pipeline():
    BashOperator(
        task_id='build_partition',
        bash_command='python labs/11-airflow/partition_job.py '
                     '--start "{{ data_interval_start }}" '
                     '--end "{{ data_interval_end }}"',
    )

lab_partition_pipeline()
```

Tự viết CLI nhận ISO datetime và xử lý `[start,end)`; parse aware timezone, không chèn user text vào Bash. DAG mẫu dùng UTC để rõ ràng; lịch 06:00 UTC khác 06:00 Việt Nam.

## Checklist task

- Input path/version/interval xác định, retry cùng run không đọc nguồn mới ngẫu nhiên.
- Output có trạng thái publish rõ và idempotent.
- XCom cho metadata nhỏ/path, không đẩy DataFrame lớn.
- Không gọi API hoặc đọc dữ liệu nặng lúc DAG parse.
- Retry có giới hạn; failure callback có dataset/run/interval và runbook.

## Reference repo có gì?

DAG `olist_daily` là lịch chạy lại snapshot local, chưa triển khai partition CLI như ví dụ. Dùng nó để học dependency; lab riêng phải bổ sung interval trước khi claim backfill. `max_active_runs=1` giảm cạnh tranh một writer local, không thay mọi cơ chế concurrency.

## Tự luyện và ôn

Tạo input ba ngày có version cố định. Backfill ba interval, kiểm tra mỗi output chỉ chứa ngày tương ứng; chạy lại đúng cùng interval và so hash/counts/tiền. Tạo lỗi sau write trước task success để test retry.

Ôn: logical_date khác now thế nào? Khi nào catchup tạo nhiều run? Làm sao biết job xanh nhưng thiếu partition?

Liên quan: [[Incremental CDC Backfill]], [[Observability va Recovery]]. Nguồn: [Airflow DAG runs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dag-run.html), [best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html).
