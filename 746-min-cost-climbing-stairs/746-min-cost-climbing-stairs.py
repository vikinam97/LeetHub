class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            val = cost[i]
            dp[i] = min(dp[i-1] +val, dp[i-2] + val)
        
        return min(dp[-1], dp[-2])