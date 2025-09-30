select e.name 
from Employee e, Employee s
where e.id = s.managerId 
group by s.managerId
having count(s.managerId) >= 5;