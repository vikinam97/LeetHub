class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        h = float('inf')
        profit = 0
        for ind, value in enumerate(prices):
            h = min(value, h)
            profit = max(profit, value-h)
        return profit 
        # Solution - kadane algo
        # Time O(N)
        # Space O(N)
#         dp = [0] * len(prices)
#         maxSoFar = 0
        
#         dp[len(prices) - 1] = prices[len(prices) - 1]
#         for i in range(len(prices) - 2, 0 - 1, -1):
#             dp[i] = max(dp[i+1], prices[i])
            
#             maxSoFar = max(maxSoFar, dp[i] - prices[i])
            
#         return maxSoFar
            
        