"""
    692. Top K Frequent Words
    https://leetcode.com/problems/top-k-frequent-words/
"""

import heapq


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:

        word_dict = {}

        # dictionary of word frequency
        for i in words:
            if i in word_dict:
                word_dict[i] += 1
            else:
                word_dict[i] = 1

        # create heap for access
        heap = [
            (-freq, word) for word, freq in word_dict.items()
        ]  # heap default sorts by -freq and then by word as required by the problem
        heapq.heapify(heap)  # in-place convert to heap data-structure

        # return 1st K-elements
        return [
            heapq.heappop(heap)[1] for _ in range(k)
        ]  # heappop for popping values from heap


print(
    Solution().topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=2)
)
print(
    Solution().topKFrequent(
        words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
        k=4,
    )
)
