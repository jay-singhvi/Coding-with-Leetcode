"""
    169. Majority Element
    https://leetcode.com/problems/majority-element/
"""


# Two pointers
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        pointer1 = 1
        counter = 1
        element = nums[0]

        for pointer2 in range(1, len(nums)):
            if nums[pointer2] == element:
                counter += 1
            else:
                counter -= 1
                if counter == 0:
                    element = nums[pointer2 + 1]
        return element


print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2


# Alternate solution
class Solution2:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


print(Solution2().majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
