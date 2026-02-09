# Write your MySQL query statement below
SELECT name FROM Employee WHERE id in
(
    SELECT managerId FROM Employee GROUP BY ManagerId HAVING COUNT(*) >= 5
)