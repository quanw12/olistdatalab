-- fct_orders must have exactly one row per staged order: no fan-out, no lost orders.
select
    (select count(*) from {{ ref('stg_orders') }})  as staged_orders,
    (select count(*) from {{ ref('fct_orders') }})  as fact_orders
where staged_orders <> fact_orders
