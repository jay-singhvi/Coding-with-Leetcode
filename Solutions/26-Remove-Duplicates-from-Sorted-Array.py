""""
    26. Remove Duplicates from Sorted Array
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) > 1:
            # for i in range(1,len(nums)):
            i = 1
            while nums and i < len(nums):
                if nums[i] == nums[i - 1]:
                    nums.pop(i)
                else:
                    i += 1
            return len(nums)
        elif len(nums) == 1:
            return 1
        else:
            return 0


print(Solution().removeDuplicates([1, 1, 2]))  # 2
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 4, 4]))  # 5

# Time Complexity: O(N)
# Space Complexity: O(1)
