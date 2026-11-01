import dagster as dg


olist_customers_dataset_csv=dg.AssetSpec(
    key=["csv","olist_customers_dataset"]
)
olist_geolocation_dataset_csv=dg.AssetSpec(
    key=["csv","olist_geolocation_dataset"]
)
olist_order_items_dataset_csv=dg.AssetSpec(
    key=["csv","olist_order_items_dataset"]
)
olist_order_payments_dataset_csv=dg.AssetSpec(
    key=["csv","olist_order_payments_dataset"]
)
olist_order_reviews_dataset_csv=dg.AssetSpec(
    key=["csv","olist_order_reviews_dataset"]
)
olist_orders_dataset_csv=dg.AssetSpec(
    key=["csv","olist_orders_dataset"]
)
olist_products_dataset_csv=dg.AssetSpec(
    key=["csv","olist_products_dataset"]
)
olist_sellers_dataset_csv=dg.AssetSpec(
    key=["csv","olist_sellers_dataset"]
)
product_category_name_translation_csv=dg.AssetSpec(
    key=["csv","product_category_name_translation"]
)