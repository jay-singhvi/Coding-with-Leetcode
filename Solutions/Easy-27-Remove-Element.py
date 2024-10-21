"""
    27. Remove Element
    https://leetcode.com/problems/remove-element/
"""


# two pointer
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left = 0
        right = len(nums)

        while left < right:  # When left and right pointer reach same index its solution
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1
        return right


print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))  # 5

# Time Complexity: O(N)
# Space Complexity: O(1)
