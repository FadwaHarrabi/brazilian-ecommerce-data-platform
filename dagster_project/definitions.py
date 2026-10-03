from .assets.ingestion import customer, geolocation, order_items, order_payments, order_reviews, order, product, sellers, product_category_name_translation
from dagster import Definitions


definitions = Definitions(
    assets=[customer, geolocation, order_items, order_payments, order_reviews, order, product, sellers, product_category_name_translation])