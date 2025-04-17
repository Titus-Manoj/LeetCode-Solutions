# Write your MySQL query statement below
SELECT MAX(num) AS num FROM (SELECT num AS num FROM MyNumbers GROUP BY num Having COUNT(num) = 1) NEW