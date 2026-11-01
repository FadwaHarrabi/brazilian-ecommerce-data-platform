CREATE TABLE IF NOT EXISTS public.customer
(

    customer_id TEXT NOT NULL,
    customer_unique_id  TEXT NOT NULL,
    customer_zip_code_prefix  INTEGER NOT NULL,
    customer_city VARCHAR(255),
    customer_state VARCHAR(255),
    PRIMARY KEY(customer_id)
);