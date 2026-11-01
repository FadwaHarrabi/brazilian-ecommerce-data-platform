SELECT 

      geolocation_zip_code_prefix AS Id,
      geolocation_zip_code_prefix AS ZipCode,
      AVG(geolocation_lng) AS Longitude,
      AVG(geolocation_lat) AS Latitude,
      MAX(INITCAP(geolocation_city)) AS City,
      MAX(geolocation_state) AS State

FROM {{ source('bronze', 'geolocation') }}
GROUP BY geolocation_zip_code_prefix
ORDER BY geolocation_zip_code_prefix ASC