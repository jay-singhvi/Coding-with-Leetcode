"""
    189. Rotate Array
    https://leetcode.com/problems/rotate-array/description/
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        move_by = len(nums) - (k % len(nums))
        nums.extend(nums[:move_by])
        del nums[:move_by]


Solution().rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)  # [5,6,7,1,2,3,4]
Solution().rotate(nums=[-1, -100, 3, 99], k=2)  # [3,99,-1,-100]
