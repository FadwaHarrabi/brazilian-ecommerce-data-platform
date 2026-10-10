SELECT 
      Id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY 
      Id AS GeolocationId,
      ZipCode,
      Longitude,
      Latitude,
      City,
      State

FROM {{ref('stg_geolocation')}}