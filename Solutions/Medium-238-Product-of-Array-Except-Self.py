"""
    238. Product of Array Except Self
    https://leetcode.com/problems/product-of-array-except-self/
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Left and Right End points additional to array endpoints
        left_multiplier = 1
        right_multiplier = 1

        # right pointer
        right = len(nums)

        # empty arrays for direct replacement and indexed traversal
        left_array = [0] * len(nums)
        right_array = [0] * len(nums)

        # left pointer travelling towards right end point
        for left in range(len(nums)):

            # right pointer travelling towards left end point
            right -= 1

            # Initially adding left and right multiplier directly as 1 and later with multiplication
            left_array[left] = left_multiplier  # Left index append
            right_array[right] = right_multiplier

            # Multiplying array value with multiplier value
            left_multiplier *= nums[left]
            right_multiplier *= nums[right]

        # Multiplying each value from left array to corresponding right array value
        return [left * right for left, right in zip(left_array, right_array)]


nums = [-1, 1, 0, -3, 3]
print(Solution().productExceptSelf(nums))

nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))
