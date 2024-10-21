"""
    763. Partition Labels
    https://leetcode.com/problems/partition-labels/
"""


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        dict_lastIndex = {}

        for ind, char in enumerate(s):  # hashmap of last index for each char
            dict_lastIndex[char] = ind

        result = []
        size, end = 0, 0

        for ind, char in enumerate(s):
            size += 1
            end = max(
                end, dict_lastIndex[char]
            )  # compare last index of current char or existing char in partition

            if end == ind:
                result.append(
                    size
                )  # append size of each block when last index of current char and current index is same
                size, end = 0, 0

        return result


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
print(Solution().partitionLabels("eccbbbbdec"))
