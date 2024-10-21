"""
    88. Merge Sorted Array
    https://leetcode.com/problems/merge-sorted-array/
"""


class Solution:
    """Class representing a Solution"""

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_index = m + n - 1  # last index of nums1 or len(nums1)
        m = m - 1  # convert to index from length
        n = n - 1  # convert to index from length

        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[last_index] = nums1[m]
                m -= 1
            else:
                nums1[last_index] = nums2[n]
                n -= 1
            last_index -= 1


Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
