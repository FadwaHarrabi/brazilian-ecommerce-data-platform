from dagster import Definitions, ScheduleDefinition, define_asset_job, AssetSelection
from dagster_dbt import DbtCliResource
from pathlib import Path
import sys
from .assets.ingestion import (
    customer, geolocation, order_items, order_payments, order_reviews,
    order, product, sellers, product_category_name_translation,
)
from .assets.source_assets import (
    olist_customers_dataset_csv, olist_geolocation_dataset_csv,
    olist_order_items_dataset_csv, olist_order_payments_dataset_csv,
    olist_order_reviews_dataset_csv, olist_orders_dataset_csv,
    olist_products_dataset_csv, olist_sellers_dataset_csv,
    product_category_name_translation_csv,
)
from .assets.dbt_assets import my_dbt_assets
from .assets.dbt_project import dbt_project

source_assets = [
    olist_customers_dataset_csv, olist_geolocation_dataset_csv,
    olist_order_items_dataset_csv, olist_order_payments_dataset_csv,
    olist_order_reviews_dataset_csv, olist_orders_dataset_csv,
    olist_products_dataset_csv, olist_sellers_dataset_csv,
    product_category_name_translation_csv,
]
ingestion_assets = [
    customer, geolocation, order_items, order_payments, order_reviews,
    order, product, sellers, product_category_name_translation,
]
all_assets = [*source_assets, *ingestion_assets, my_dbt_assets]

# Ingestion + dbt (without the raw source assets)
daily_pipeline = define_asset_job(
    name="daily_pipeline",
    selection=AssetSelection.assets(*ingestion_assets, my_dbt_assets),
)

# Or only dbt:
# dbt_job = define_asset_job("daily_dbt", selection=AssetSelection.assets(my_dbt_assets))

daily_schedule = ScheduleDefinition(
    job=daily_pipeline,
    cron_schedule="0 6 * * *",
)

defs = Definitions(
    assets=all_assets,
    jobs=[daily_pipeline],
    schedules=[daily_schedule],
    resources={
    "dbt": DbtCliResource(
        project_dir=dbt_project,
        dbt_executable=str(Path(sys.executable).parent / "dbt.exe"),
    )
},
)