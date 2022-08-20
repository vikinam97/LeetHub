class Solution:        
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Solution - DP Tabulation
        # Time - O(N*M)
        # Space - O(M)
        
        h, w = len(grid), len(grid[0])
        pdp = [0] * w
        pdp[0] = grid[0][0]
        
        for j in range(1, w):
            pdp[j] = pdp[j-1] + grid[0][j]
        
        for i in range(1, h):
            cdp = [0] * w
            cdp[0] = pdp[0] + grid[i][0]
            for j in range(1, w):
                cdp[j] = min(pdp[j], cdp[j-1]) + grid[i][j]
            
            pdp = cdp
        return pdp[-1]

class Solution1:        
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Solution - DP Tabulation
        # Time - O(N*M)
        # Space - O(N*M)
        
        h, w = len(grid), len(grid[0])
        dp = [[0] * w for _ in range(h)]
        dp[0][0] = grid[0][0]
        
        for i in range(1, h):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, w):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in range(1, h):
            for j in range(1, w):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]

class Solution1:        
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Solution - Recursion + Memoization
        # Time - O(N*M)
        # Space - O(N*M)
        
        self.memo = {}
        return self.recur(0, 0, grid)
    
    def recur(self, i, j, grid):
        if i >= len(grid) or j >= len(grid[0]):
            return float('inf')
        
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        if i == len(grid)-1 and j == len(grid[0])-1:
            return grid[i][j]
        
        self.memo[(i, j)] = min(self.recur(i+1, j, grid),
                  self.recur(i, j+1, grid)) + grid[i][j]
        
        return self.memo[(i, j)]