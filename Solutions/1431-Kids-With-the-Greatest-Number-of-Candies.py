"""
1431. Kids With the Greatest Number of Candies
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
"""


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)
        result = []

        # Solution 1 :
        # for i in candies:
        #     if extraCandies+i >= max_val:
        #         result.append(True)
        #     else:
        #         result.append(False)
        # return result

        # Solution 2 :
        result = [True if extraCandies+i >= max_val else False for i in candies]
        return result

        # Solution 3 :
        # for i in candies:
        #     result.append(i + extraCandies >= max_val)
        # return result

        # Solution 4 :
        # result = [i + extraCandies >= max_val for i in candies]
        # return result
