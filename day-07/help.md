# Gợi ý Ngày 7

Hoàn thành `build_clean_record` trước, rồi mới làm `validate_record`.

## build_clean_record

~~~python
response = raw["response"]
current = response["current"]

return {
    "city": raw["city"].strip(),
    "requested_at": raw["requested_at"],
    "observed_at": current["time"],
    "timezone": response["timezone"],
    "temperature_c": float(current["temperature_2m"]),
    "humidity_pct": int(current["relative_humidity_2m"]),
    "source": "open-meteo",
}
~~~

## validate_record

~~~python
errors = []

if not record["city"]:
    errors.append("city is empty")

try:
    datetime.fromisoformat(record["observed_at"])
except ValueError:
    errors.append("observed_at is not ISO datetime")

if not record["timezone"]:
    errors.append("timezone is empty")

if not -50 <= record["temperature_c"] <= 60:
    errors.append("temperature_c is outside allowed range")

if not 0 <= record["humidity_pct"] <= 100:
    errors.append("humidity_pct is outside allowed range")

return errors
~~~

## Debug có kiểm soát

Trước `return` trong `build_clean_record`, có thể tạm thêm:

~~~python
print(response)
print(current)
~~~

Trước `if errors` trong `main`, có thể in:

~~~python
print(clean_record)
print(errors)
~~~

Khi hiểu xong, xóa các `print` debug để terminal chỉ hiện report cuối.
