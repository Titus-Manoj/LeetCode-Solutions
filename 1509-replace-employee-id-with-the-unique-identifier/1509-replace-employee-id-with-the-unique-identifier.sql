# Write your MySQL query statement below
SELECT u.unique_id, e.name FROM Employees as e Left Join EmployeeUNI as u ON e.id = u.id