# Write your MySQL query statement below
SELECT p.product_name, s.year, s.price FROM Sales as s Left join Product As p on s.product_id = p.product_id 