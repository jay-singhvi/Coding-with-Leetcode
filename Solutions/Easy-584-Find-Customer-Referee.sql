/*
    584. Find Customer Referee
    https://leetcode.com/problems/find-customer-referee/
*/

SELECT c.name
FROM customer c
WHERE isnull(c.referee_id,0) <> 2