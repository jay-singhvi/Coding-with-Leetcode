"""
    45. Jump Game II
    https://leetcode.com/problems/jump-game-ii/
"""


# sliding window
class Solution:
    def jump(self, nums: list[int]) -> int:
        left = 0
        right = 0
        numberOfJumps = 0

        while right < len(nums) - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])

            left = right + 1
            right = farthest
            numberOfJumps += 1

        return numberOfJumps


print(Solution().jump([2, 3, 1, 1, 4]))
