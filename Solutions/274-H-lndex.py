"""
    274. H-lndex
    https://leetcode.com/problems/h-index/
"""


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        len_value = len(citations)
        citations.sort(reverse=True)
        if citations[0] == 0:
            return 0
        for i in range(len(citations)):
            if i + 1 > citations[i]:
                return i
        return len_value


Solution().hIndex([3, 0, 6, 1, 5])