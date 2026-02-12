# Write your MySQL query statement below
with a as
(
    select requester_id id from RequestAccepted
    UNION ALL
    select accepter_id id from RequestAccepted
)

Select id, COUNT(id) as num
FROM a
Group by id
Order By num DESC Limit 1