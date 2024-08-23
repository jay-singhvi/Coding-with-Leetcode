"""
    1071. Greatest Common Divisor of Strings
    https://leetcode.com/problems/greatest-common-divisor-of-strings/
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(s1: str, s2: str) -> str:
            if not s2:
                return s1
            if len(s1) < len(s2):
                return gcd(s2, s1)
            if s1[:len(s2)] != s2:
                return ""
            return gcd(s1[len(s2):], s2)

        return gcd(str1, str2)