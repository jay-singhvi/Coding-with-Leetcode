"""
    169. Majority Element
    https://leetcode.com/problems/majority-element/
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}
        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) + 1
        return max(nums_dict, key=nums_dict.get)


Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])  # 2


# Alternate solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
