SELECT 
    Id INT ALWAYS GENERATED AS IDENTITY PRIMARY KEY,
    Id AS ReviewsId,
    Score,
    CommentTitle,
    CommentMessage,
    CreationDate,
    AnswerTimestamp

FROM {{ref('stg_reviews')}}