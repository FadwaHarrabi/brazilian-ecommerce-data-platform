from duckdb import cursor
import psycopg2
import pandas as pd
import logging
from dagster import asset

logging.basicConfig(level=logging.INFO)
logging.info("Database connection established successfully.")
@asset
def customer():
    conn=psycopg2.connect(
        host="localhost",
        port=5566,
        user="postgres",
        password="admin",
        database="OlistBronze"
    )

    cursor=conn.cursor()
    customer_data = pd.read_csv("data/olist_customers_dataset.csv")
    customer_data = customer_data.where(pd.notnull(customer_data), None)

    for _,row in customer_data.iterrows():
        query="""
        INSERT INTO public.customer (customer_id,customer_unique_id,customer_zip_code_prefix,customer_city,customer_state)
        VALUES(%s,%s,%s,%s,%s)"""
        cursor.execute(query, (row['customer_id'], row['customer_unique_id'], row['customer_zip_code_prefix'], row['customer_city'], row['customer_state']))
    conn.commit()
    cursor.close()
    conn.close()
@asset
def geolocation():
    geolocation_data = pd.read_csv("data/olist_geolocation_dataset.csv")
    geolocation_data = geolocation_data.where(pd.notnull(geolocation_data), None)
    conn=psycopg2.connect(
            host="localhost",
            port=5566,
            user="postgres",
            password="admin",
            database="OlistBronze"
        )
    cursor=conn.cursor()
    for _,row in geolocation_data.iterrows():
        query="""
        INSERT INTO public.geolocation (geolocation_zip_code_prefix,geolocation_lat,geolocation_lng,geolocation_city, geolocation_state)
        VALUES(%s,%s,%s,%s,%s)"""
        cursor.execute(query, (row['geolocation_zip_code_prefix'], row['geolocation_lat'], row['geolocation_lng'], row['geolocation_city'], row['geolocation_state']))

    conn.commit()
    cursor.close()
    conn.close()
@asset
def order_items():
    order_items_data = pd.read_csv("data/olist_order_items_dataset.csv")
    order_items_data = order_items_data.where(pd.notnull(order_items_data), None)

    conn=psycopg2.connect(
            host="localhost",
            port=5566,
            user="postgres",
            password="admin",
            database="OlistBronze"
        )
    cursor=conn.cursor()
    for i,row in order_items_data.iterrows():
        query="""
        INSERT INTO public.items (order_id,order_item_id,product_id,seller_id,shipping_limit_date,price,freight_value)
        VALUES(%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(query, (row['order_id'], row['order_item_id'], row['product_id'], row['seller_id'], row['shipping_limit_date'], row['price'], row['freight_value']))
    conn.commit()
    cursor.close()
    conn.close()
@asset
def order_payments():
    order_payments_data = pd.read_csv("data/olist_order_payments_dataset.csv")
    order_payments_data = order_payments_data.where(pd.notnull(order_payments_data), None)

    conn=psycopg2.connect(
            host="localhost",
            port=5566,
            user="postgres",
            password="admin",
            database="OlistBronze"
        )
    cursor=conn.cursor()
    for i,row in order_payments_data.iterrows():
        query="""
        INSERT INTO public.payments (order_id,payment_sequential,payment_type,payment_installments,payment_value)
        VALUES(%s,%s,%s,%s,%s)"""
        cursor.execute(query, (row['order_id'], row['payment_sequential'], row['payment_type'], row['payment_installments'], row['payment_value']))
    conn.commit()
    cursor.close()
    conn.close()
@asset
def order_reviews():
    order_reviews_data = pd.read_csv("data/olist_order_reviews_dataset.csv")
    order_reviews_data = order_reviews_data.where(pd.notnull(order_reviews_data), None)

    conn=psycopg2.connect(
            host="localhost",
            port=5566,
            user="postgres",
            password="admin",
            database="OlistBronze"
        )
    cursor=conn.cursor()
    for i,row in order_reviews_data.iterrows():
        query="""
        INSERT INTO public.reviews (review_id,order_id,review_score,review_comment_title,review_comment_message,review_creation_date,review_answer_timestamp)
        VALUES(%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(query, (row['review_id'], row['order_id'], row['review_score'], row['review_comment_title'], row['review_comment_message'], row['review_creation_date'], row['review_answer_timestamp']))
    conn.commit()
    cursor.close()
    conn.close()
@asset
def order():
    order_data = pd.read_csv("data/olist_orders_dataset.csv")
    order_data = order_data.where(pd.notnull(order_data), None)

    conn=psycopg2.connect(
            host="localhost",
            port=5566,
            user="postgres",
            password="admin",
            database="OlistBronze"
        )
    cursor=conn.cursor()
    for i,row in order_data.iterrows():
        query="""
        INSERT INTO public.orders (order_id,customer_id,order_status,order_purchase_timestamp,order_approved_at,order_delivered_carrier_date,order_delivered_customer_date,order_estimated_delivery_date)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(query, (row['order_id'], row['customer_id'], row['order_status'], row['order_purchase_timestamp'], row['order_approved_at'], row['order_delivered_carrier_date'], row['order_delivered_customer_date'], row['order_estimated_delivery_date']))
    conn.commit()
    cursor.close()
    conn.close()
@asset
def product():
    product_data = pd.read_csv("data/olist_products_dataset.csv")
    product_data = product_data.where(pd.notnull(product_data), None)

    conn=psycopg2.connect(
            host="localhost",
            port=5566,
            user="postgres",
            password="admin",
            database="OlistBronze"
        )
    cursor=conn.cursor()
    for _,row in product_data.iterrows():
        query="""
        INSERT INTO public.products (product_id,product_category_name,product_name_lenght,product_description_lenght,product_photos_qty,product_weight_g,product_length_cm,product_height_cm,product_width_cm)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(query, (row['product_id'], row['product_category_name'], row['product_name_lenght'], row['product_description_lenght'], row['product_photos_qty'], row['product_weight_g'], row['product_length_cm'], row['product_height_cm'], row['product_width_cm']))
    conn.commit()
    cursor.close()
    conn.close()
@asset
def sellers():
    sellers_data = pd.read_csv("data/olist_sellers_dataset.csv")
    sellers_data = sellers_data.where(pd.notnull(sellers_data), None)

    conn=psycopg2.connect(
            host="localhost",
            port=5566,
            user="postgres",
            password="admin",
            database="OlistBronze"
        )
    cursor=conn.cursor()
    for _,row in sellers_data.iterrows():
        query="""
        INSERT INTO public.sellers (seller_id,seller_zip_code_prefix,seller_city,seller_state)
        VALUES(%s,%s,%s,%s)"""
        cursor.execute(query, (row['seller_id'], row['seller_zip_code_prefix'], row['seller_city'], row['seller_state']))
    conn.commit()
    cursor.close()
    conn.close()
@asset
def product_category_name_translation():
    product_category_name_translation_data = pd.read_csv("data/product_category_name_translation.csv")
    product_category_name_translation_data = product_category_name_translation_data.where(pd.notnull(product_category_name_translation_data), None)

    conn=psycopg2.connect(
            host="localhost",
            port=5566,
            user="postgres",
            password="admin",
            database="OlistBronze"
        )
    cursor=conn.cursor()
    for _,row in product_category_name_translation_data.iterrows():
        query="""
        INSERT INTO public.category_name_translation (product_category_name,product_category_name_english)
        VALUES(%s,%s)"""
        cursor.execute(query, (row['product_category_name'], row['product_category_name_english']))
    conn.commit()
    cursor.close()
    conn.close()
