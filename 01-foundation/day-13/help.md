# Day 13 — Load PostgreSQL from Python


## 1. Establish the connection

Run the lesson's SELECT example first. Connection refused means inspect the PostgreSQL service and port; authentication failed means credentials; unknown database means create weather_course. Do not print PGPASSWORD.

## 2. Define the table

Create the staging schema first, then the table. Commas separate column definitions. Put the composite key after the columns. Use NOT NULL as well as range checks: CHECK alone accepts SQL NULL. Exact types are in the shared contract.

## 3. Validate one row

Print one input dictionary. Validate text, then parse both times. Reject missing offsets. Use math.isfinite for temperature. Check that humidity has no fractional part before int conversion: int(72.9) silently truncates. Validate the whole list before loading.

## 4. Prepare SQL

List all seven destination columns and seven %s placeholders. Build tuples in exactly that order. ON CONFLICT updates requested_at, timezone_name, temperature_c and humidity_pct. The three key fields stay fixed. Test one row, then use cursor.executemany(sql, parameter_rows). Its rowcount does not necessarily mean new rows.

## 5. Connect the driver

Parse --input, read JSON, validate, enter the connection context, call load_records, and query the total. Print success after leaving the context successfully. Keep execution behind the main guard so imports do not connect.

## 6. Prove atomicity

In a scratch transaction run BEGIN, a valid insert, a CHECK-violating insert, then ROLLBACK. Compare before/after contents. In Python let the exception leave the connection context; catch outside only to report failure and exit nonzero. Rollback cannot undo an earlier committed transaction.
