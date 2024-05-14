/*
    185. Department Top Three Salaries
    https://leetcode.com/problems/department-top-three-salaries/
*/


/* Write your T-SQL query statement below */
SELECT Department
    , Employee
    , Salary
FROM (
    SELECT dept.name AS "Department"
        , emp.name AS "Employee"
        , emp.salary AS "Salary"
        , DENSE_RANK() OVER (
            PARTITION BY dept.name ORDER BY emp.salary DESC
            ) AS SalaryRank /* DENSE_RANK() window function for sort emp.salry while grouping by dept.name and later use this column for getting top 3 ranks*/
    FROM employee emp
    INNER JOIN department dept
        ON emp.departmentId = dept.id
    ) AS Ranked
WHERE SalaryRank <= 3;