"""
    1. Two Sum
    https://leetcode.com/problems/two-sum/
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # O(n^2) solution
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]

        # O(n) solution
        nums_dict = {}

        for i in range(len(nums)):
            nums_dict[nums[i]] = i  # track 1 index of each number

        for i in range(len(nums)):
            diff = target - nums[i]  # difference of number from target
            if (
                diff in nums_dict and nums_dict[diff] != i
            ):  # if difference value exists in dictionary and it is not same as current value
                return [
                    nums_dict[diff],
                    i,
                ]  # return index of diff value and current number index


print(
    f"Input: nums = [2,7,11,15], target = 9 \nOutput: {Solution().twoSum([2, 7, 11, 15], 9)}\n"
)

print(
    f"Input: nums = [3,2,4], target = 6 \nOutput: {Solution().twoSum([3, 2, 4], 6)}\n"
)

print(f"Input: nums = [3,3], target = 6 \nOutput: {Solution().twoSum([3, 3], 6)}\n")
