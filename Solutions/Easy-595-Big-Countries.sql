/*
    595. Big Countries
    https://leetcode.com/problems/big-countries/
*/

SELECT w.name,
    w.population,
    w.area
from World w
where w.population >= 25000000
    or w.area >= 3000000