WITH one_review_per_order AS (SELECT 
    review_id AS Id,
    order_id AS OrderId,
    review_score AS Score,
    INITCAP(review_comment_title) AS CommentTitle,
    lower(review_comment_message) AS CommentMessage,
    review_creation_date AS CreationDate,
    review_answer_timestamp AS AnswerTimestamp,
    ROW_NUMBER() OVER(PARTITION BY order_id  ORDER BY review_creation_date DESC NULLS LAST,
                                                      review_answer_timestamp DESC NULLS LAST,review_id DESC) AS rn
FROM {{source('bronze','reviews')}})
SELECT * FROM one_review_per_order 
WHERE rn=1