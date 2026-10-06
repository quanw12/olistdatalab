# Fixed practice data

Synthetic orders in fictional currency units; no personal data. Amounts have two decimal places. order_id identifies a mutable order snapshot; updated_at identifies its source version, not request time. All source times must include an offset.

orders.csv: eight rows, four valid rows including one exact A2 replay, four rejected rows. Latest distinct state: three orders, 3050 cents. Rejections: city=1, amount=2, time=1.

orders_next.csv: A2 correction, valid A4, and an older A1 snapshot. Applying it to the base state gives four orders, 3850 cents. Replaying either file must not reverse the correction.

These counts use the Chapter 14 capstone rules. Earlier lessons may read all eight strings without performing validation.
