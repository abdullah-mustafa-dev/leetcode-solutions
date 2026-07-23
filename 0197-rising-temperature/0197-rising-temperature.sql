-- Write your PostgreSQL query statement below
select w1.id from Weather as w1, Weather as w2
where w1.id <> w2.id 
    and w2.recordDate + INTERVAL '1 day' = w1.recordDate
    and w1.temperature > w2.temperature