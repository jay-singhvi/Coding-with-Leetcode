"""
    973. K Closest Points to Origin
    https://leetcode.com/problems/k-closest-points-to-origin/
"""

import heapq  # this gives us min heap, but we want max heap


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        # calculate dictance for each point
        def dist_calc(x, y):
            return x**2 + y**2

        heap = []
        for x, y in points:
            val = dist_calc(x, y)
            if len(heap) < k:
                heapq.heappush(
                    heap, (-val, x, y)
                )  # we want max heap so will use -ve of val
            else:
                heapq.heappushpop(
                    heap, (-val, x, y)
                )  # if records more than k required val, so push val and remove max

        return [[x, y] for _, x, y in heap]


print(Solution().kClosest([[1, 3], [-2, 2]], 1))
print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2))
