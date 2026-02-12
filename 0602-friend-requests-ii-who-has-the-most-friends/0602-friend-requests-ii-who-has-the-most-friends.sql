# Write your MySQL query statement below
Select id, COUNT(id) as num
FROM 
(
    select requester_id id from RequestAccepted
    UNION ALL
    select accepter_id id from RequestAccepted
) a
Group by id
Order By num DESC Limit 1