# Data contract and findings

The machine-readable contract is [`contracts/olist.yml`](../src/olist_platform/contracts/olist.yml).
This page explains the decisions behind it. Counts marked _real_ must come from your own run on
the Kaggle files — fill them in yourself; do not copy numbers from anyone else.

## Grain: what one row means

| Table | One row is | Key |
|---|---|---|
| orders | one order | `order_id` |
| order_items | one item line of an order (3 items = 3 rows) | `order_id, order_item_id` |
| order_payments | one payment (voucher + card = 2 rows) | `order_id, payment_sequential` |
| order_reviews | one review of one order | `review_id, order_id` |
| customers | one customer **per order**; `customer_unique_id` is the person | `customer_id` |
| sellers / products | one seller / product | `seller_id` / `product_id` |
| geolocation | one lat/lng point; many per zip prefix | none — dedupe before joining |
| **fct_orders** | one order, items and payments pre-summed | `order_id` |
| **fct_order_items** | one item line | `order_id, order_item_id` |
| **dim_customers** | one person | `customer_unique_id` |
| **mart_daily_revenue** | one São Paulo business day | `order_date` |

## Rules at ingestion (bronze)

| Case | Severity | Why |
|---|---|---|
| Contracted column missing | error — nothing published | Schema drift; every downstream model would break or lie |
| Primary key empty or duplicated | error | The grain is broken |
| Status / payment type / score outside the known set | error | A new value needs a human decision before it reaches reports |
| Timestamp not `YYYY-MM-DD HH:MM:SS`, number not numeric | error | Would silently become NULL after casting |
| `delivered` without a delivery date | warn — kept | The order and its money are real |
| Status with odd casing/spaces | warn — normalised in staging | Same value, different spelling |
| Extra column in the file | warn — ignored | Additive change, safe |

A failed table keeps yesterday's bronze version (candidate table + atomic swap). Every check
result is stored in `audit.quality_results`; every load in `audit.ingest_manifest`.

## Time

Olist timestamps carry no zone. They are São Paulo local time, and Brazil observed summer time
until 2019, so a fixed `-03:00` offset is wrong for part of the data.
- `*_at_utc` columns: converted with the zone database — use for durations.
- `order_date`: the São Paulo calendar date — use for daily reporting. An order at 22:30 local
  time is already the next day in UTC.
- Open question to investigate: timestamps in the repeated hour when summer time ended are
  ambiguous. Count them on the real data and document the effect.

## Money

- Item revenue (`items_price + items_freight`) and payment revenue (`payment_total`) are different
  numbers. Find out by how much on the real data, and explain the gap (orders without items that
  were charged, vouchers, instalment interest).
- Orders without items or payments keep NULL amounts, never 0.
- `tests/assert_money_reconciles.sql` fails the build if fact totals differ from the source by
  more than one cent or if any item/payment row is lost or duplicated.

## Exchange rates

BRL→USD and BRL→VND per São Paulo order date. If a day has no rate (weekend, holiday, gap in the
source) the latest earlier rate is used, at most `fx_max_gap_days` (3) back; `brl_*_rate_date`
shows which day the rate is from. Longer gaps leave the converted amount NULL.

## Fill in from your real run

| Fact | Value |
|---|---|
| Orders / items / payments rows | _real_ |
| Orders without items, by status | _real_ |
| Orders without payment | _real_ |
| Payments total vs items + freight, and the explained gap | _real_ |
| Days where one currency has no rate | _real_ |
| Late delivery rate (delivered orders) | _real_ |
| Ambiguous summer-time timestamps | _real_ |
