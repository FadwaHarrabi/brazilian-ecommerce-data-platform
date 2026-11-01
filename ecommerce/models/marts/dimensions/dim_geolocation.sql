{{ config(materialized='table') }}

SELECT
    ROW_NUMBER() OVER (
        ORDER BY ZipCode, Longitude, Latitude
    ) AS Id,
    Id AS GeolocationId,
    ZipCode,
    Longitude,
    Latitude,
    City,
    State
FROM {{ ref('stg_geolocation') }}
