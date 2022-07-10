class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Solution - dynamic programmin
        # Time - O(N)
        # Space - O(N)
        # dp = [0] * len(cost)
        a, b = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            val = cost[i]
            c = min(a + val, b + val)
            a, b = b, c
        
        return min(a, b)