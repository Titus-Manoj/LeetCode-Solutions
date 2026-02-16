# Write your MySQL query statement below
WITH t as (select d.name as Department, 
                  e.name as Employee, 
                  (e.salary)  as Salary,
                  DENSE_RANK() OVER (PARTITION by departmentId ORDER BY Salary DESC) as rnk
            from Employee e join Department d
            on e.departmentId = d.id)

select Department, Employee, Salary
from t
where t.rnk <=3