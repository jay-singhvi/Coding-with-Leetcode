"""
    134. Gas Station
    https://leetcode.com/problems/gas-station/
"""


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start_index = 0

        for i in range(0, len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                start_index = i + 1

        return start_index


print(Solution().canCompleteCircuit(gas=[5, 1, 2, 3, 4], cost=[4, 4, 1, 5, 1]))
print(Solution().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
