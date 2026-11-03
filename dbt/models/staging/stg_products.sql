select
    trim(p.product_id)                                         as product_id,
    nullif(trim(p.product_category_name), '')                  as category_pt,
    coalesce(nullif(trim(t.product_category_name_english), ''),
             nullif(trim(p.product_category_name), ''),
             'unknown')                                        as category,
    try_cast(p.product_weight_g as double)                     as weight_g,
    try_cast(p.product_length_cm as double)
        * try_cast(p.product_height_cm as double)
        * try_cast(p.product_width_cm as double)               as volume_cm3,
    try_cast(p.product_photos_qty as integer)                  as photos_qty
from {{ source('bronze', 'products') }} p
left join {{ source('bronze', 'category_translation') }} t
    on trim(p.product_category_name) = trim(t.product_category_name)
