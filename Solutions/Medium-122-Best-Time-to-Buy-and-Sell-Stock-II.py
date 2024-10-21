"""
    122. Best Time to Buy and Sell Stock II
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if (
                prices[i] > prices[i - 1]
            ):  # We get profit only if previous price is lower than current price
                profit += prices[i] - prices[i - 1]

        return profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 7
print(Solution().maxProfit([1, 2, 3, 4, 5]))  # 4
print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0


class Solution2:
    def maxProfit(self, prices: list[int]) -> int:
        i = 0
        buy = prices[0]
        sell = prices[0]
        profit = 0
        n = len(prices)

        while i < n - 1:
            # buy at lows
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            buy = prices[i]
            # sell at highs
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            sell = prices[i]

            profit += sell - buy

        return profit


print(Solution2().maxProfit([7, 1, 5, 3, 6, 4]))  # 7
print(Solution2().maxProfit([1, 2, 3, 4, 5]))  # 4
print(Solution2().maxProfit([7, 6, 4, 3, 1]))  # 0

# Time Complexity: O(n)
# Space Complexity: O(1)
