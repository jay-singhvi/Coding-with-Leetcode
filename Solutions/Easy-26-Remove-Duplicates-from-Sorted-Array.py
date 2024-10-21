""""
    26. Remove Duplicates from Sorted Array
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


# Two pointers
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pointer1 = 1
        pointer2 = 1

        while pointer1 < len(nums):
            if nums[pointer1] != nums[pointer1 - 1]:
                nums[pointer2] = nums[pointer1]
                pointer2 += 1
            pointer1 += 1

        return pointer2


print(Solution().removeDuplicates([1, 1, 2]))  # 2
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 4, 4]))  # 5

# Time Complexity: O(N)
# Space Complexity: O(1)
