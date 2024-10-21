"""
    274. H-lndex
    https://leetcode.com/problems/h-index/
"""


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        totalNoOfPapers = len(citations)

        # Create array with 0 as placeholders for unique values equal to length of array
        paperCounts = [0] * (totalNoOfPapers + 1)  # +1 for bucket

        # Update paper counts - count-sort algo
        # index is citations and
        # index value is number of papers with that many citations
        for paper in citations:
            # last index will be the bucket for all papers with citations more than total number of papers
            paperCounts[min(totalNoOfPapers, paper)] += 1

        # reverse traversal
        hIndexPapers = paperCounts[totalNoOfPapers]

        for h_index in range(totalNoOfPapers, 0, -1):
            if hIndexPapers >= h_index:
                return h_index
            hIndexPapers += paperCounts[h_index - 1]

        return 0


print(Solution().hIndex([3, 0, 6, 1, 5]))
print(Solution().hIndex([1, 3, 1]))
