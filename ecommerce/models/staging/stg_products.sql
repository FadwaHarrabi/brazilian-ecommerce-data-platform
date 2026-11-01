SELECT  
    P.product_id AS Id,
    INITCAP(REPLACE(P.product_category_name, '_', ' ')) AS CategoryNameBr,
    INITCAP(REPLACE(C.product_category_name_english,'_',' ')) AS CategoryNameEn,
    P.product_weight_g AS Weight,
    P.product_length_cm AS Length,
    P.product_height_cm AS Height,
    P.product_width_cm AS Width
FROM {{source('bronze','products')}} P
LEFT JOIN {{source('bronze','category_name_translation')}} C
ON P.product_category_name=C.product_category_name