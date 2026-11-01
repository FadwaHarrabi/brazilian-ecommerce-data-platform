WITH source_orders AS (SELECT 
     O.CustomerId AS IdCustomer,
     O.Id AS  OrderId,
     C.ZipCode,
     R.Id AS ReviewId,
     P.PaymentSequential,
     P.PaymentValue,
     P.PaymentInstallments,
     TO_CHAR(O.PurchaseTimestamp,'YYYYMMDD')::int AS IdPurchaseTimestamp


FROM {{ref('stg_orders')}} O
LEFT JOIN {{ref('stg_customer')}} C
ON O.CustomerId=C.Id
LEFT JOIN {{ref('stg_reviews')}} R
ON R.OrderId=O.Id
LEFT JOIN {{ref('stg_payments')}} P
ON P.OrderId=O.Id)


SELECT 
      SO.IdCustomer,
      O.Id AS IdOrder,
      G.Id AS IdGeolocation,
      R.Id AS IdReview,
      P.Id AS IdPayment,
      dd.Id AS IdDate,
      SO.PaymentValue,
      SO.PaymentInstallments
      


FROM source_orders SO
LEFT JOIN {{ref('dim_order')}} O
ON SO.OrderId=O.OrderId
LEFT JOIN {{ref('dim_geolocation')}} G
ON G.ZipCode=SO.ZipCode
LEFT JOIN {{ref('dim_reviews')}} R
ON SO.ReviewId=R.ReviewsId
LEFT JOIN {{ref('dim_payments')}} P
ON SO.PaymentSequential=P.PaymentSequential
AND SO.OrderId=P.OrderId
LEFT JOIN {{ref('dim_date')}} dd
ON SO.IdPurchaseTimestamp=dd.Id
