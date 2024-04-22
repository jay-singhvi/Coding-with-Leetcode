/*
    1757. Recyclable and Low Fat Products
    https://leetcode.com/problems/recyclable-and-low-fat-products/
*/

select p.product_id
from Products p
where p.low_fats='Y'
    and p.recyclable = 'Y'