"""
    121. Best Time to Buy and Sell Stock
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


# Sliding window
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0  # max_profit - result
        min_price = (
            10**4
        ) + 1  # min_price is greater than max possible price as it will be overwritten

        for price in prices:
            if price < min_price:
                min_price = price

            max_profit = max(max_profit, price - min_price)

        return max_profit


Solution().maxProfit([7, 1, 5, 3, 6, 4])  # 5
Solution().maxProfit([7, 6, 4, 3, 1])  # 0


# Alternate solution
class Solution2:
    def maxProfit(self, prices: list[int]) -> int:
        buy_index = 0
        sell_index = 1
        profit = 0

        while sell_index < len(prices):
            if prices[sell_index] < prices[buy_index]:
                buy_index = sell_index
            elif (prices[sell_index] - prices[buy_index]) > profit:
                profit = prices[sell_index] - prices[buy_index]
            sell_index += 1
        return profit


Solution2().maxProfit([7, 1, 5, 3, 6, 4])  # 5
Solution2().maxProfit([7, 6, 4, 3, 1])  # 0


# Time Complexity: O(n)
# Space Complexity: O(1)
