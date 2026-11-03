-- One row per day with the BRL->USD and BRL->VND rate valid that day: the rate of that day, or
-- the latest earlier rate at most fx_max_gap_days back. rate_date_* says where it came from,
-- so a carried-over rate is never presented as that day's rate.
with days as (
    select unnest(generate_series(min(rate_date), max(rate_date), interval 1 day))::date as day
    from {{ ref('stg_fx_rates') }}
),
usd as (select rate_date, rate from {{ ref('stg_fx_rates') }} where quote = 'USD'),
vnd as (select rate_date, rate from {{ ref('stg_fx_rates') }} where quote = 'VND'),
joined as (
    select d.day, u.rate as usd_rate, u.rate_date as usd_rate_date
    from days d asof left join usd u on d.day >= u.rate_date
),
joined2 as (
    select j.*, v.rate as vnd_rate, v.rate_date as vnd_rate_date
    from joined j asof left join vnd v on j.day >= v.rate_date
)
select
    day,
    case when day - usd_rate_date <= {{ var('fx_max_gap_days') }} then usd_rate end as brl_usd,
    case when day - usd_rate_date <= {{ var('fx_max_gap_days') }} then usd_rate_date end as brl_usd_rate_date,
    case when day - vnd_rate_date <= {{ var('fx_max_gap_days') }} then vnd_rate end as brl_vnd,
    case when day - vnd_rate_date <= {{ var('fx_max_gap_days') }} then vnd_rate_date end as brl_vnd_rate_date
from joined2
