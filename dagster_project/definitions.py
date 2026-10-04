from .assets.ingestion import customer, geolocation, order_items, order_payments, order_reviews, order, product, sellers, product_category_name_translation
from .assets.source_assets import olist_customers_dataset_csv, olist_geolocation_dataset_csv, olist_order_items_dataset_csv, olist_order_payments_dataset_csv, olist_order_reviews_dataset_csv, olist_orders_dataset_csv, olist_products_dataset_csv, olist_sellers_dataset_csv, product_category_name_translation_csv
from dagster import Definitions


definitions = Definitions(
    assets=[olist_customers_dataset_csv, 
            olist_geolocation_dataset_csv, 
            olist_order_items_dataset_csv,
            olist_order_payments_dataset_csv, 
            olist_order_reviews_dataset_csv,
            olist_orders_dataset_csv, 
            olist_products_dataset_csv, 
            olist_sellers_dataset_csv, 
            product_category_name_translation_csv,
            customer,
            geolocation,
            order_items,
            order_payments,
            order_reviews,
            order,
            product,
            sellers,
            product_category_name_translation])