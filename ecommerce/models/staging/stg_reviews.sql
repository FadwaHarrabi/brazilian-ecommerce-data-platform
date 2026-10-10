SELECT 
    review_id AS Id,
    order_id AS OrderId,
    review_score AS Score,
    INITCAP(review_comment_title) AS CommentTitle,
    lower(review_comment_message) AS CommentMessage,
    review_creation_date AS CreationDate,
    review_answer_timestamp AS AnswerTimestamp

FROM {{source('bronze','reviews')}}