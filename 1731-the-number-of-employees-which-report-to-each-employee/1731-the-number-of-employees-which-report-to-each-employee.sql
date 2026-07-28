-- Write your PostgreSQL query statement below
select 
    e.employee_id,
    e.name,
    (
        select count(*) 
        from Employees e2 
        where e.employee_id = e2.reports_to
    ) as reports_count,
    round((
        select avg(age) 
        from Employees e2 
        where e.employee_id = e2.reports_to
    )) as average_age
from Employees e
where exists (
    select 1
    from Employees e2
    where e.employee_id = e2.reports_to
)
group by e.employee_id, e.name
order by employee_id;