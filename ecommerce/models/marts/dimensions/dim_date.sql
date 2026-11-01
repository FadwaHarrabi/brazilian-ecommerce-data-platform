WITH days AS (
    {{ dbt_utils.date_spine(
        datepart = "day",
        start_date = "cast('2016-01-01' as date)",
        end_date   = "cast('2019-01-01' as date)"
    ) }}
)

SELECT
    TO_CHAR(date_day, 'YYYYMMDD')::int AS Id,
    CAST(date_day AS DATE)                     AS FullDate,
    EXTRACT(year  FROM date_day)               AS Year,
    EXTRACT(quarter FROM date_day)             AS Quarter,
    EXTRACT(month FROM date_day)               AS Month,
    EXTRACT(day   FROM date_day)               AS DayOfMonth,
    TO_CHAR(date_day, 'FMMonth')  AS MonthName,   -- January
    TO_CHAR(date_day, 'FMDay')    AS DayName      -- Monday
FROM days