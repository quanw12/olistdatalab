# Bài học Ngày 5: merge, groupby và kiểm tra dữ liệu

## 1. Hai bảng, hai mục đích

`weather_clean.csv` có các sự kiện thời tiết:

| city | observed_at | temperature_c | humidity_pct |
|---|---|---:|---:|
| Hanoi | 2026-09-14 | 31.2 | 78 |
| Da Nang | 2026-09-14 | 30.1 | 81 |

`city_lookup.csv` có thông tin dùng chung theo thành phố:

| city | region |
|---|---|
| Hanoi | North |
| Da Nang | Central |

Không nên lặp `region` trong nguồn dữ liệu thời tiết nếu nó có thể được tra bằng `city`. Ta ghép hai bảng bằng key chung `city`.

## 2. `merge` là gì?

~~~python
enriched_df = weather_df.merge(
    city_df,
    on="city",
    how="left",
    validate="many_to_one",
)
~~~

Đọc từng phần:

| Phần | Nghĩa |
|---|---|
| `weather_df.merge(city_df, ...)` | ghép bảng tra cứu vào bảng thời tiết |
| `on="city"` | dùng city làm key |
| `how="left"` | giữ tất cả hàng của weather_df |
| `validate="many_to_one"` | nhiều hàng thời tiết được ghép với tối đa một hàng lookup |

Sau merge, mỗi dòng thời tiết có thêm cột `region`.

### Vì sao là `left` join?

Nếu `weather_df` có city mới mà `city_df` chưa có, `left` join vẫn giữ dòng thời tiết và đặt `region` là missing. Pipeline nhờ đó phát hiện được vấn đề.

`inner` join sẽ im lặng bỏ hẳn dòng không có match. Báo cáo có vẻ chạy bình thường, nhưng dữ liệu bị mất.

### Vì sao có `validate`?

Nếu lookup vô tình có hai dòng cho `Hanoi`, một hàng weather có thể bị nhân thành hai hàng sau merge. `validate="many_to_one"` khiến pandas báo lỗi thay vì âm thầm tạo báo cáo sai.

## 3. Kiểm tra ngay sau merge

~~~python
missing_region = enriched_df["region"].isna()

if missing_region.any():
    unknown_cities = enriched_df.loc[missing_region, "city"].unique()
    raise ValueError(f"city lookup is missing: {unknown_cities.tolist()}")
~~~

- `isna()` tạo mask True/False.
- `any()` là True khi có ít nhất một giá trị True.
- `.loc[mask, "city"]` lấy city của những dòng bị thiếu region.
- `unique()` bỏ city lặp để thông báo lỗi ngắn hơn.

Đây là một data-quality check: đừng tạo báo cáo khi dữ liệu chưa có ngữ cảnh cần thiết.

## 4. `groupby`: tạo các nhóm

~~~python
enriched_df.groupby(["region", "city"], as_index=False)
~~~

Lệnh này chia dữ liệu thành nhóm. Mỗi nhóm có cùng `region` và `city`. Nó chưa tính kết quả; ta thêm `agg`:

~~~python
summary_df = (
    enriched_df.groupby(["region", "city"], as_index=False)
    .agg(
        observation_count=("observed_at", "count"),
        avg_temperature_c=("temperature_c", "mean"),
        min_temperature_c=("temperature_c", "min"),
        max_temperature_c=("temperature_c", "max"),
        avg_humidity_pct=("humidity_pct", "mean"),
    )
)
~~~

Đây là **named aggregation**. Dạng chung:

~~~python
ten_cot_output=("cot_input", "phep_tinh")
~~~

Ví dụ `("temperature_c", "mean")` nghĩa là lấy trung bình cột `temperature_c` trong từng nhóm.

## 5. Làm tròn, sắp xếp và kiểm tra tổng

Mean thường có nhiều chữ số thập phân. Báo cáo dễ đọc hơn khi làm tròn:

~~~python
summary_df["avg_temperature_c"] = summary_df["avg_temperature_c"].round(1)
summary_df["avg_humidity_pct"] = summary_df["avg_humidity_pct"].round(1)
~~~

Sắp xếp để file luôn có cùng thứ tự:

~~~python
summary_df = summary_df.sort_values(["region", "city"]).reset_index(drop=True)
~~~

`reset_index(drop=True)` tạo index 0, 1, ... mới. `drop=True` không giữ index cũ thành cột.

Cuối cùng, tổng số quan sát trong báo cáo phải bằng số dòng đã ghép:

~~~python
if summary_df["observation_count"].sum() != len(enriched_df):
    raise ValueError("summary observation count does not match input rows")
~~~

Đây không chứng minh báo cáo hoàn hảo, nhưng nó bắt được một loại lỗi phổ biến: vô tình làm mất hoặc nhân bản hàng trong quá trình tổng hợp.

## 6. Luồng của bài

~~~text
main
  -> đọc weather_clean.csv và city_lookup.csv
  -> build_summary
       -> merge
       -> kiểm tra missing region
       -> groupby + agg
       -> làm tròn + sắp xếp
       -> kiểm tra tổng quan sát
  -> ghi CSV summary
  -> in report
~~~

## 7. Tài liệu ngoài

- [pandas `merge` API](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)
- [pandas `merge` user guide](https://pandas.pydata.org/docs/user_guide/merging.html)
- [pandas `groupby` user guide](https://pandas.pydata.org/docs/user_guide/groupby.html)

Chỉ cần hiểu `left merge`, `validate`, `groupby` và `agg` cho bài này. Chưa cần học nhiều kiểu join hoặc pivot table.
