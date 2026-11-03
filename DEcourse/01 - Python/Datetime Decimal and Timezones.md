---
tags: [decourse, python, correctness]
module: 01
---

# Datetime, Decimal and Timezones

> [!info] Learning goals
> After this note you can: tell naive from aware datetimes; convert between local time and UTC correctly, including daylight saving time (DST); separate *instants* from *business dates*; compute durations without mixing calendar days and 24-hour periods; and handle money with `Decimal` and explicit rounding rules.

## 1. Two kinds of "time"

- An **instant** is a single point on the global timeline ("the order was placed at 2018-01-16 00:30 UTC"). Store instants in **UTC**: it has no DST and sorts correctly.
- A **business date / wall-clock time** is how people in a place describe it ("the order was placed on 15 January, 22:30 in São Paulo"). Daily reports, "orders per day" and SLAs use the business date in the business's timezone.

The same instant has different dates in different zones. An order at 22:30 in São Paulo on 15 January is already 16 January in UTC. If you group by UTC date, late-evening orders land on the wrong day.

## 2. Naive vs aware datetimes

```python
# runnable
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

naive = datetime(2018, 1, 15, 22, 30)                       # no zone: ambiguous
aware = datetime(2018, 1, 15, 22, 30, tzinfo=ZoneInfo("America/Sao_Paulo"))
assert naive.tzinfo is None
assert aware.utcoffset().total_seconds() == -2 * 3600       # DST was active: UTC-02
try:
    naive < aware                                           # cannot compare the two
except TypeError:
    pass
```

A **naive** datetime has no timezone; Python does not know which instant it means. An **aware** datetime carries a `tzinfo`. Use IANA zone names (`America/Sao_Paulo`, `Asia/Ho_Chi_Minh`), never fixed offsets like `-03:00` for places, because offsets change with DST and with law.

## 3. Converting correctly

```python
# runnable
from datetime import datetime, timezone
from decimal import Decimal
from zoneinfo import ZoneInfo

local = datetime(2018, 1, 15, 22, 30, tzinfo=ZoneInfo('America/Sao_Paulo'))
utc = local.astimezone(timezone.utc)
assert str(local.date()) == '2018-01-15'
assert str(utc.date()) == '2018-01-16'
assert utc.hour == 0  # Sao Paulo was on DST: UTC-02

winter = datetime(2018, 7, 15, 22, 30, tzinfo=ZoneInfo('America/Sao_Paulo'))
assert winter.astimezone(timezone.utc).hour == 1   # no DST in July: UTC-03

total = Decimal('0.1') + Decimal('0.2')
assert total == Decimal('0.3')
assert Decimal('12.345').quantize(Decimal('0.01')) == Decimal('12.34')
```

| Operation | Meaning |
|---|---|
| `dt.replace(tzinfo=zone)` | **Labels** a naive time with a zone. The wall-clock numbers stay the same. Use it to say "this naive value was São Paulo time". |
| `dt.astimezone(zone)` | **Converts** an aware time to another zone. The instant stays the same; the numbers change. |

Mixing them up is a classic bug: `utc_dt.replace(tzinfo=ZoneInfo("America/Sao_Paulo"))` silently shifts the instant by 2–3 hours.

### Parsing source timestamps

Olist timestamps look like `2018-01-15 22:30:00` with **no zone**. The project assumes São Paulo wall-clock time — an assumption you must record and validate with the source, not a fact.

```python
# runnable
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

SAO_PAULO = ZoneInfo("America/Sao_Paulo")

def parse_olist_time(text: str) -> datetime | None:
    if not text or not text.strip():
        return None                      # "not happened yet", e.g. not delivered
    local = datetime.strptime(text.strip(), "%Y-%m-%d %H:%M:%S").replace(tzinfo=SAO_PAULO)
    return local.astimezone(timezone.utc)

assert parse_olist_time("2018-01-15 22:30:00").isoformat() == "2018-01-16T00:30:00+00:00"
assert parse_olist_time("") is None
```

`strptime` format codes: `%Y` year, `%m` month, `%d` day, `%H` hour (24h), `%M` minute, `%S` second. For ISO-8601 strings, `datetime.fromisoformat()` is simpler.

## 4. DST traps: repeated and missing hours

When DST **ends**, clocks go back and one local hour happens twice (ambiguous). When DST **starts**, clocks jump forward and one local hour never exists.

- Ambiguous times: Python's `fold` attribute (`0` = first occurrence, `1` = second) picks which one. Your pipeline needs a documented policy.
- Non-existent times: `zoneinfo` does not reject them; it produces *some* result. Detect them by round-tripping (convert to UTC and back; if the wall time changed, the input did not exist) and quarantine.

```python
# runnable
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

SP = ZoneInfo("America/Sao_Paulo")
# Brazil DST started at 00:00 on 2017-10-15: clocks jumped to 01:00.
ghost = datetime(2017, 10, 15, 0, 30, tzinfo=SP)
round_trip = ghost.astimezone(timezone.utc).astimezone(SP)
assert round_trip.replace(tzinfo=None) != ghost.replace(tzinfo=None)  # 00:30 never existed
```

Brazil abolished DST in 2019, but Olist data (2016–2018) spans DST periods — which is exactly why hard-coding `-03:00` would be wrong.

## 5. Durations vs calendar differences

```python
# runnable
from datetime import date, datetime, timedelta, timezone

placed = datetime(2018, 1, 15, 23, 0, tzinfo=timezone.utc)
delivered = datetime(2018, 1, 16, 1, 0, tzinfo=timezone.utc)
assert delivered - placed == timedelta(hours=2)                  # duration
assert (delivered.date() - placed.date()).days == 1              # calendar days
assert date(2018, 3, 1) - date(2018, 2, 1) == timedelta(days=28)
```

"Delivered in 1 day" can mean 2 hours (crossed midnight) or 47 hours. Define delivery time in the metric contract: hours between instants, or calendar days in the business timezone. Do not mix them in one metric.

## 6. Money: why not float

Floats are binary fractions; most decimal fractions (0.1, 0.2) cannot be represented exactly:

```python
# runnable
from decimal import Decimal, ROUND_HALF_UP

assert 0.1 + 0.2 != 0.3
running = 0.0
for _ in range(100):
    running += 0.01            # naive accumulation, like a loop in a pipeline
assert running != 1.0          # 1.0000000000000007
assert sum([Decimal("0.01")] * 100) == Decimal("1.00")

assert Decimal(0.1) != Decimal("0.1")            # from float: the error is already inside
price = Decimal("12.345")
assert price.quantize(Decimal("0.01")) == Decimal("12.34")                       # half-even (banker's)
assert price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP) == Decimal("12.35")
```

Rules:

1. Create `Decimal` from **strings**, never from floats.
2. Choose the rounding mode deliberately: Python's default is half-even (banker's rounding); invoices often use half-up. Write the rule into the data contract.
3. Decide *when* to round: rounding each line and then summing can differ from summing then rounding. Accounting rules usually specify which.
4. In databases use `DECIMAL(p, s)` / `NUMERIC(p, s)` (for example `DECIMAL(12,2)`), not `FLOAT`/`DOUBLE`. An alternative is storing integer cents.

## 7. Currency conversion and dates

The project converts BRL to USD and VND with daily Frankfurter rates. Rates are published per business day; weekends and holidays have none. A common policy is **carry-forward**: use the last available rate and record which date it came from. Join FX on the **São Paulo order date**, not the UTC date, and keep `rate_date` next to the converted amount so anyone can audit it.

## 8. Applying it to Olist

- Store `purchase_ts_utc` (instant) and `purchase_date_local` (business date) separately.
- Daily revenue groups by the local date; delivery durations use UTC instants.
- Money columns are `DECIMAL(12,2)`; conversion uses Decimal arithmetic and a documented rounding mode.
- Validate the timezone assumption: plot the order count per hour of day; a shopping peak at 4 a.m. local time would suggest the assumption is wrong.

## 9. Common mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Grouping by UTC date for local reports | Late-evening orders on the wrong day | Convert to the business zone, then take `.date()` |
| `.replace(tzinfo=)` on an aware time | Instant silently shifted | `.astimezone()` |
| Fixed offset `-03:00` for São Paulo | Wrong during DST | `ZoneInfo("America/Sao_Paulo")` |
| `Decimal(0.1)` | Float error preserved | `Decimal("0.1")` |
| Floats for money | Cents disappear in totals | Decimal / integer cents / DECIMAL columns |
| "Days" without a definition | Inconsistent delivery KPIs | Define instants vs calendar days in the contract |

## 10. Exercises

1. Convert 2018-07-15 22:30 São Paulo to UTC and compare with 15 January. Explain the difference.
2. Find a repeated hour at the end of Brazil's DST (February 2018). Show both `fold=0` and `fold=1` in UTC and write the policy you would choose.
3. Add 0.01 a hundred times with float and with Decimal. Then round 3 line items individually vs. the total, and show a case where they differ.
4. Write `to_business_date(ts_utc, zone)` and test an order at 01:00 UTC that belongs to the previous local day.

> [!example]- Hint for 2
> In 2018 DST ended at 00:00 on 18 February: clocks went back from 00:00 to 23:00 on the 17th, so 23:30 on 17 February happened twice. Compare `datetime(2018, 2, 17, 23, 30, fold=0, tzinfo=SP)` and `fold=1` after `.astimezone(timezone.utc)`.

## 11. Review questions

> [!question]- Why store instants in UTC and also keep a local date?
> UTC is unambiguous and sortable for durations and ordering; the local date is what the business reports on. Deriving one from the other repeatedly invites mistakes, so keep both explicitly.

> [!question]- What is the difference between `replace(tzinfo=…)` and `astimezone(…)`?
> `replace` attaches a zone label without changing the clock numbers; `astimezone` converts the same instant to another zone, changing the numbers.

> [!question]- Why is `Decimal("0.1")` different from `Decimal(0.1)`?
> The float `0.1` is already an approximation; converting it carries the binary error into the Decimal. A string is converted exactly.

> [!question]- What must a metric contract say about money rounding?
> The rounding mode (half-up, half-even, …), the precision, and whether rounding happens per line or on the total.

Related: [[BI Metrics and Data Products]], [[Data Modeling and SCD2]], [[Module 01 - Python]]. Sources: [zoneinfo](https://docs.python.org/3/library/zoneinfo.html), [datetime](https://docs.python.org/3/library/datetime.html), [decimal](https://docs.python.org/3/library/decimal.html).
