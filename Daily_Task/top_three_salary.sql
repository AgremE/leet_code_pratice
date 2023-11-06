# Write your MySQL query statement below
WITH top_three_each_dp AS 
(
SELECT salary, departmentId
    from 
    (
        SELECT 
        salary,
        departmentId,
        ROW_NUMBER() over (PARTITION BY  departmentId ORDER BY salary DESC) as rn
        FROM 
        (SELECT DISTINCT salary,departmentId from Employee) tb1
    )tb2
    WHERE rn between 1 and 3
)


SELECT
dp.name as Department,
ep.name as Employee,
ep.salary as Salary 
from 
Employee ep
inner join
top_three_each_dp top
on
top.salary = ep.salary
and 
top.departmentId = ep.departmentId
inner join
Department dp
on 
dp.id = ep.departmentId
