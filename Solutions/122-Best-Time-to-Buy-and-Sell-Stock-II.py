"""
    122. Best Time to Buy and Sell Stock II
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_index = 0
        sell_index = 1
        profit = 0

        while sell_index < len(prices):
            # print("--------------- Loop ----------------")
            # print("buy_index", buy_index, "prices[buy_index]", prices[buy_index])
            # print("sell_index", sell_index, "prices[sell_index]", prices[sell_index])
            if prices[sell_index] < prices[buy_index]:
                # print("Cond 1: Buy val",prices[buy_index],"more than sell val", prices[sell_index])
                buy_index = sell_index
            elif prices[sell_index] - prices[buy_index]:
                # print("Cond 2: Buy val",prices[buy_index]," - sell val", prices[sell_index], "is greater than profit", profit)
                profit += prices[sell_index] - prices[buy_index]
                buy_index = sell_index
            # else:
            #     print("Cond 3: Buy val",prices[buy_index]," - sell val", prices[sell_index], "is not greater than profit", profit)
            sell_index += 1
            # print("profit", profit)
        return profit


Solution().maxProfit([7, 1, 5, 3, 6, 4])  # 7
Solution().maxProfit([1, 2, 3, 4, 5])  # 4
Solution().maxProfit([7, 6, 4, 3, 1])  # 0

# Time Complexity: O(n)
# Space Complexity: O(1)
