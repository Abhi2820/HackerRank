SELECT DISTINCT CITY
FROM STATION
WHERE CITY NOT LIKE '%a' and
        CITY NOT LIKE '%e' and
        CITY NOT LIKE '%i' and
        CITY NOT LIKE '%o' and
        CITY NOT LIKE '%u' ;


/*
SELECT DISTINCT CITY
FROM STATION
WHERE RIGHT(CITY,1) NOT IN ('a','i','e','o','u');

*/