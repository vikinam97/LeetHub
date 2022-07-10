class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Solution - dynamic programmin
        # Time - O(N)
        # Space - O(1)
        secondLast, last = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            val = cost[i]
            cur = min(secondLast + val, last + val)
            secondLast, last = last, cur
        
        return min(secondLast, last)
    
class Solution1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Solution - dynamic programmin
        # Time - O(N)
        # Space - O(N)
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            val = cost[i]
            dp[i] = min(dp[i-1] +val, dp[i-2] + val)
        
        return min(dp[-1], dp[-2])
        
        return min(a, b)
        
        