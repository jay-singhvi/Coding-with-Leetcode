"""
    80. Remove Duplicates from Sorted Array II
    https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""


# Two pointers
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pointer1 = 1
        counter = 1

        for pointer2 in range(1, len(nums)):
            if nums[pointer2] == nums[pointer2 - 1]:
                counter += 1
            else:
                counter = 1

            if counter <= 2:
                nums[pointer1] = nums[pointer2]
                pointer1 += 1

        return pointer1


print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3]))  # 5
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 4, 4]))  # 8

# Time Complexity: O(N)
# Space Complexity: O(1)
