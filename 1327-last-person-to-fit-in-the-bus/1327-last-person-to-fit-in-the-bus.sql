# Write your MySQL query statement below
SELECT person_name from (Select person_name, turn , sum(weight) over (order by turn) As cum from queue) p1
WHERE cum<=1000 order by turn DESC limit 1