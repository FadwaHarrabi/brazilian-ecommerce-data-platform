SELECT 

      geolocation_id AS Id,
      geolocation_zip_code_prefix AS ZipCode,
      geolocation_lng AS Longitude,
      geolocation_lat AS Latitude,
      INITCAP(geolocation_city) AS City,
      geolocation_state AS State


FROM {{ source('bronze', 'geolocation') }}