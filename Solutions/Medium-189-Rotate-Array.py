"""
    189. Rotate Array
    https://leetcode.com/problems/rotate-array/
"""


# Two pointers for reversing the array
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def helper_reverse_array(left, right):
            while left < right:
                # Swap left and right together else it will not work as it will be overwritten
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        helper_reverse_array(left=0, right=len(nums) - 1)  # Reverse whole array
        helper_reverse_array(left=0, right=k - 1)  # Reverse 0 to K - 1 elements
        helper_reverse_array(
            left=k, right=len(nums) - 1
        )  # Reverse K to End of Array elements


Solution().rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)  # [5,6,7,1,2,3,4]
# reverse 1 = [7,6,5,4,3,2,1]
# reverse 2 = [5,6,7,4,3,2,1]
# reverse 3 = [5,6,7,1,2,3,4] # Solution

Solution().rotate(nums=[-1, -100, 3, 99], k=2)  # [3,99,-1,-100]
