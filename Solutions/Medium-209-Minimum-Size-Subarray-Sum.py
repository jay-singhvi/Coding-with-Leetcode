"""
    209. Minimum Size Subarray Sum
    https://leetcode.com/problems/minimum-size-subarray-sum/
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # 1. find every subarray whose sum >= target
        # 2. take the minimal one of those subarray
        # 3. if there is none, return 0

        # approach
        # sliding window

        # two pointers, one left, one right of a sliding window
        # in the beginning fill up the window until sum is reached
        # then move pointer by one on the left
        # check whether sum is still fulfilled, compare whether this is smaller than previous minLength
        # if not greater than the sum
        # we start adding elements by moving the right pointer, checking again when the sum is >= target

        result = float("inf")
        total = 0
        left = right = 0

        while right < len(nums) or (
            left < len(nums) and total >= target
        ):  # improve condition
            if total >= target:
                total -= nums[left]
                left += 1
                result = min(result, right - left + 1)
            else:
                total += nums[right]
                right += 1

        return 0 if result == float("inf") else result


print(Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
