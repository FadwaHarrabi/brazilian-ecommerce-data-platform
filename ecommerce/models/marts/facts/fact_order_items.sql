WITH Item_Order AS(SELECT i.Id AS OrderItemId,
       i.OrderId,
       i.ProductId,
       i.SellerId,
       i.ShippingLimitDate,
       TO_CHAR(i.ShippingLimitDate ,'YYYYMMDD'):: int AS IdShippingLimitDates,
       i.Price,
       i.FreightValue,
       ss.ZipCode
FROM {{ref('stg_items')}} i
LEFT JOIN {{ref('stg_sellers')}} ss
ON i.SellerId=ss.Id
)
SELECT 
     oi.OrderItemId,
     o.Id AS IdOrder,
     p.Id AS IdProduct,
     oi.SellerId,
     oi.ShippingLimitDate,
     oi.Price,
     oi.FreightValue,
     g.Id AS IdGeolocation,
     dd.Id AS IdDate
FROM Item_Order oi
LEFT JOIN {{ref('dim_order')}} o
ON oi.OrderId=o.OrderId
LEFT JOIN {{ref('dim_products')}} p
ON oi.ProductId=p.ProductId
LEFT JOIN {{ref('dim_geolocation')}} g
ON oi.ZipCode=g.ZipCode
LEFT JOIN {{ref('dim_date')}} dd 
ON oi.IdShippingLimitDates=dd.Id