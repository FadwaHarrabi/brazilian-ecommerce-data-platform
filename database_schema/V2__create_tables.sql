CREATE TABLE IF NOT EXISTS public.customer
(

    customer_id TEXT NOT NULL,
    customer_unique_id  TEXT NOT NULL,
    customer_zip_code_prefix  INTEGER NOT NULL,
    customer_city VARCHAR(255),
    customer_state VARCHAR(255),
    PRIMARY KEY(customer_id)
);
CREATE TABLE IF NOT EXISTS public.geolocation(

    geolocation_id BIGSERIAL NOT NULL,
    geolocation_zip_code_prefix INTEGER NOT NULL,
    geolocation_lat DOUBLE PRECISION,
    geolocation_lng DOUBLE PRECISION,
    geolocation_city VARCHAR(255),
    geolocation_state VARCHAR(255),
    PRIMARY KEY(geolocation_id)
    
);

CREATE TABLE IF NOT EXISTS public.items
(
    order_item_id TEXT NOT NULL,
    order_id TEXT NOT NULL,
    product_id TEXT NOT NULL,
    seller_id TEXT NOT NULL,
    shipping_limit_date TIMESTAMPTZ,
    price DECIMAL(10, 2),
    freight_value DECIMAL(10, 2),
    PRIMARY KEY (order_id, order_item_id)

);

CREATE TABLE IF NOT EXISTS public.payments(
    
    payment_id BIGSERIAL NOT NULL,
    order_id TEXT NOT NULL,
    payment_sequential INTEGER NOT NULL,
    payment_type VARCHAR(255),
    payment_installments INTEGER,
    payment_value DECIMAL(10, 2),
    PRIMARY KEY (payment_id)
);

CREATE TABLE IF NOT EXISTS  public.reviews(
    review_id TEXT NOT NULL,
    order_id TEXT NOT NULL,
    review_score INTEGER,
    review_comment_title VARCHAR(255),
    review_comment_message TEXT,
    review_creation_date TIMESTAMPTZ,
    review_answer_timestamp TIMESTAMPTZ,
    PRIMARY KEY (review_id)

);
CREATE TABLE IF NOT EXISTS public.orders(
    order_id TEXT NOT NULL,
    customer_id TEXT NOT NULL,
    order_status VARCHAR(255),
    order_purchase_timestamp TIMESTAMPTZ,
    order_approved_at TIMESTAMPTZ,
    order_delivered_carrier_date TIMESTAMPTZ,
    order_delivered_customer_date TIMESTAMPTZ,
    order_estimated_delivery_date TIMESTAMPTZ,
    PRIMARY KEY (order_id)
);
CREATE TABLE IF NOT EXISTS public.products(
    
    product_id TEXT NOT NULL,
    product_category_name VARCHAR(255),
    product_name_lenght INTEGER,
    product_description_lenght INTEGER,
    product_photos_qty INTEGER,
    product_weight_g INTEGER,
    product_length_cm INTEGER,
    product_height_cm INTEGER,
    product_width_cm INTEGER,
    PRIMARY KEY (product_id)
);
CREATE TABLE IF NOT EXISTS public.sellers(
    
    seller_id TEXT NOT NULL,
    seller_zip_code_prefix INTEGER NOT NULL,
    seller_city VARCHAR(255),
    seller_state VARCHAR(255),
    PRIMARY KEY (seller_id)
);
CREATE TABLE IF NOT EXISTS public.category_name_translation(
    category_name_id BIGSERIAL NOT NULL,
    product_category_name VARCHAR(255) NOT NULL,
    product_category_name_english VARCHAR(255),
    PRIMARY KEY (category_name_id)
);