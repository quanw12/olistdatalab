{#
  Olist timestamps are Sao Paulo wall-clock time with no zone.
  local_ts: parse to a naive TIMESTAMP (still Sao Paulo time). Empty -> NULL.
  to_utc:   label it with the zone, then express it in UTC. Uses the zone database,
            so Brazilian summer time (until 2019) is handled.
#}
{% macro local_ts(column) -%}
    try_strptime(nullif(trim({{ column }}), ''), '%Y-%m-%d %H:%M:%S')
{%- endmacro %}

{% macro to_utc(column) -%}
    timezone('UTC', timezone('America/Sao_Paulo', {{ local_ts(column) }}))
{%- endmacro %}
