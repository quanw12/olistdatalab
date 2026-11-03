select product_id, category, category_pt, weight_g, volume_cm3, photos_qty
from {{ ref('stg_products') }}
