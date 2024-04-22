/*
    1148. Article Views I
    Link: https://leetcode.com/problems/article-views-i/
*/

SELECT DISTINCT v.author_id as id
FROM Views v
WHERE v.author_id = v.viewer_id