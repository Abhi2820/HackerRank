SELECT 
CASE
WHEN((A+b)<=C) OR ((A+C)<=B) OR ((B+C)<=A) THEN 'Not A Triangle'

WHEN A=B AND B=C THEN 'Equilateral'
WHEN (A=B AND b!= c) OR (b=c AND a!=c) OR (A=c AND A!=b)THEN 'Isosceles'

Else 'Scalene'
END AS Triangle
FROM TRIANGLES;