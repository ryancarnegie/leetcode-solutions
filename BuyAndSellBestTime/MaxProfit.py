class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > 0:
                    max_profit = max(max_profit, profit)
        return max_profit

# Time : O(N^2) - It's a nested for loop
# Space : O(1)
