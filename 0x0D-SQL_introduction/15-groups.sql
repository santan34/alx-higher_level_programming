-- counts the number of records with the same 
SELECT `score`, COUNT(`score`) AS number  FROM second_table GROUP BY `score` ORDER BY `SCORE` DESC;
