SELECT  
    Id INT ALWAYS GENERATED AS IDENTITY PRIMARY KEY
    PaymentSequential,
    PaymentType,
    PaymentInstallments,
    PaymentValue

FROM {{ref('stg_payments')}}