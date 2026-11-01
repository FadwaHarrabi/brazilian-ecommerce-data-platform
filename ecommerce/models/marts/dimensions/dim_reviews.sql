{{ config(materialized='table') }}

SELECT
    ROW_NUMBER() OVER (ORDER BY Id) AS Id,
    Id AS ReviewsId,
    Score,
    CommentTitle,
    CommentMessage,
    CreationDate,
    AnswerTimestamp
FROM {{ ref('stg_reviews') }}