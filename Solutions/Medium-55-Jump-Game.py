"""
    55. Jump Game
    https://leetcode.com/problems/jump-game/
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return not goal


nums = [2, 3, 1, 1, 4]
print(Solution().canJump(nums))

nums2 = [3, 2, 1, 0, 4]
print(Solution().canJump(nums2))
