class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if min_price > 0:
                profit = price - min_price
                min_price = min(price, min_price)
                max_profit = max(profit, max_profit)
        return max_profit


Time: O(N)
Space : O(1)

