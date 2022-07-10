class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        memo = {}
        def dfs(cur, prevPaint, t):
            if t < 0 or t > m-cur:
                return float('inf')
            
            if cur == m:
                if t == 0:
                    return 0
                else:
                    return float('inf')
            
            if (cur, prevPaint, t) in memo:
                return memo[(cur, prevPaint, t)]
            
            if houses[cur]:
                memo[(cur, prevPaint, t)] = dfs(cur + 1, houses[cur], t - (1 if houses[cur] != prevPaint else 0))
                return memo[(cur, prevPaint, t)]
            
            minCost = float('inf')
            for j in range(1, n+1):
                minCost = min(minCost,  cost[cur][j-1] + dfs(cur+1, j, t - (1 if j != prevPaint else 0)))
            
            memo[(cur, prevPaint, t)] = minCost
            return memo[(cur, prevPaint, t)]
        
        cost = dfs(0, 0, target)
    
        return cost if cost != float('inf') else -1