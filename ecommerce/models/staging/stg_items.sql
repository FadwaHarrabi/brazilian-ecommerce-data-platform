SELECT 
      order_item_id AS Id,
      order_id AS OrderId,
      product_id AS ProductId,
      seller_id AS SellerId,
      shipping_limit_date AS ShippingLimitDate,
      price AS Price,
      freight_value AS FreightValue
FROM {{source('bronze','items')}}