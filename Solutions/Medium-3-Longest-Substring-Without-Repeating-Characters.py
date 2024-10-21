"""
    3. Longest Substring Without Repeating Characters
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


# sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()  # set for O(1) check value

        result = 0  # max length of substring

        left = 0  # left pointer for sliding window

        for right in range(len(s)):  # right pointer browsing through the string
            while (
                s[right] in charset
            ):  # remove all characters from the set upto the duplicate character
                charset.remove(s[left])
                left += 1  # incrementing left pointer each time we remove the value
            charset.add(s[right])

            result = max(
                result, (right - left) + 1
            )  # after adding new value check difference between the indexes right and left + 1

        return result


print(Solution().lengthOfLongestSubstring("abcabcbb"))
