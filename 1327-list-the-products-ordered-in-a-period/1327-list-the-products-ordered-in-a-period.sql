-- Write your PostgreSQL query statement below
select p.product_name, sum(o.unit) as unit
from Products p
join Orders o on o.product_id = p.product_id
WHERE o.order_date >= '2020-02-01'::date
  AND o.order_date < '2020-02-01'::date + '1 month'::interval
group by product_name
having sum(o.unit) >= 100;