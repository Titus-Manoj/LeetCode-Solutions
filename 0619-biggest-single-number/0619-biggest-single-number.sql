# Write your MySQL query statement below
SELECT MAX(num) as num
FROM MYNumbers
where num in 
(
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
)
