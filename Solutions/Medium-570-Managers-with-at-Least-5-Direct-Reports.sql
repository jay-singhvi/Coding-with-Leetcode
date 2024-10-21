/*
    570. Managers with at Least 5 Direct Reports
    https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
*/

SELECT m.name
FROM Employee e
INNER JOIN Employee m
 ON e.managerId = m.id
GROUP BY e.managerId
 , m.name
HAVING COUNT(e.id) >= 5;