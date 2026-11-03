select
    day::date                          as date_day,
    year(day)                          as year,
    month(day)                         as month,
    strftime(day, '%Y-%m')             as year_month,
    isodow(day)                        as iso_day_of_week,
    isodow(day) in (6, 7)              as is_weekend
from (
    select unnest(generate_series(min(order_date), max(order_date), interval 1 day)) as day
    from {{ ref('fct_orders') }}
)
