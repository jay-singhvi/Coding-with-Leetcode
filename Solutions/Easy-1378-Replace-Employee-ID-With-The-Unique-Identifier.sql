/*
    1378. Replace Employee ID With The Unique Identifier
    https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
*/

SELECT empuni.unique_id
 , emp.name
FROM Employees emp
LEFT JOIN Employeeuni empuni
 ON empuni.id = emp.id