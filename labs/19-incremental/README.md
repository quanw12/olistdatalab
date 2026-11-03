# Lab 19 · Thay đổi dữ liệu, replay và lịch sử

Tự triển khai `my_state.py`, không mở reference trước khi có một lần thử. Tests cố ý đỏ và không nằm trong `pytest` mặc định.

```powershell
python -m pytest labs/19-incremental -v
```

## Hợp đồng

Event có order_id, version (số nguyên dương), business_date (ISO date), amount_cents (số nguyên không âm), deleted (bool). Version tăng theo từng order, không theo toàn feed. Cùng order/version nhưng nội dung khác là conflict phải báo ValueError, không âm thầm chọn bản tới trước.

`apply_events` nhận các event có thể lặp/out-of-order, trả current state theo order_id, giữ tombstone. `daily_totals` chỉ tổng current orders chưa deleted theo ngày; ngày rỗng phải không còn trong kết quả. Không sửa input của caller.

Sau pure functions, tự mở rộng persistence DuckDB/Postgres, input batch/checkpoint và backfill `[start,end)`. Test hai chiều với full rebuild sau mỗi batch, nhất là đổi ngày và delete hết một partition. Đây là lab mini về semantics CDC, chưa phải connector log-based CDC.

Evidence: pytest, expected nhỏ tính bằng tay, ADR chọn version/checkpoint, logs trước/sau recovery. Xem module 19 và note `Incremental CDC Backfill` trong vault.
