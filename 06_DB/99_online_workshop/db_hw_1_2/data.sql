SELECT 
  * 
FROM
  tracks;

SELECT 
  Name, Milliseconds, UnitPrice 
FROM
  tracks;

SELECT 
  * 
FROM
  tracks
WHERE
  GenreId = '1';

SELECT 
  * 
FROM
  tracks
ORDER BY
  Name ASC;

SELECT 
  * 
FROM
  tracks
LIMIT 10;