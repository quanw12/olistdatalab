-- No money lost or counted twice between the source rows and the order fact.
-- Returns a row (= test failure) for any measure that differs by more than one cent.
with source as (
    select 'payments' as measure, sum(payment_value) as amount, count(*) as row_count
    from {{ ref('stg_order_payments') }}
    union all
    select 'items', sum(price + freight_value), count(*)
    from {{ ref('stg_order_items') }}
),

fact as (
    select 'payments' as measure, sum(payment_total) as amount, sum(payment_count) as row_count
    from {{ ref('fct_orders') }}
    union all
    select 'items', sum(items_price + items_freight), sum(item_count)
    from {{ ref('fct_orders') }}
)

select s.measure, s.amount as source_amount, f.amount as fact_amount,
       s.row_count as source_rows, f.row_count as fact_rows
from source s
join fact f using (measure)
where abs(s.amount - f.amount) > 0.01 or s.row_count <> f.row_count
