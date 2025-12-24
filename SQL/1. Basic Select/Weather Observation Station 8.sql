SELECT DISTINCT CITY
FROm STATION
WHERE  RIGHT(CITY,1) IN ('a','e','i','o','u') AND
        LEFt (CITY,1) IN ('a','e','i','o','u');
