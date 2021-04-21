"""
Best Time to Buy and Sell Stock - Easy

1. Check the minimum price for every price
2. Update the maximum profit using the current price - the minimum price

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = 100000

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profi t