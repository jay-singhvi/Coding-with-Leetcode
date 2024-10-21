/*
    1683. Invalid Tweets
    https://leetcode.com/problems/invalid-tweets/
*/

SELECT t.tweet_id
FROM Tweets t
WHERE len(t.content) > 15