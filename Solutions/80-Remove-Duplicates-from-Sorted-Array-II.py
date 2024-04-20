"""
    80. Remove Duplicates from Sorted Array II
    https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) > 2:
            # for i in range(1,len(nums)):
            i = 2
            while nums and i < len(nums):
                if nums[i - 2] == nums[i - 1] == nums[i]:
                    nums.pop(i)
                else:
                    i += 1
            return len(nums)
        else:
            return len(nums)


print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3]))  # 5
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 4, 4]))  # 8

# Time Complexity: O(N)
# Space Complexity: O(1)
