class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # Solution - Space Optimized DP
        # Time - O(N*M)
        # Space - O(M)
        
        h, w = len(grid), len(grid[0])
        
        pdp = [0]*w
        pdp[0] = 0 if grid[0][0] == 1 else 1
                    
        for j in range(w):
            if grid[0][j] == 1:
                break
            pdp[j] = 1
        
        for i in range(1, h):
            cdp = [0] * w
            cdp[0] = 1 if pdp[0] == 1 and grid[i][0] == 0 else 0 
            for j in range(1, w):
                if grid[i][j] != 1:
                    cdp[j] = pdp[j] + cdp[j-1]
            pdp = cdp
            
        return pdp[-1]

class Solution1:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # Solution - DP Tabulation
        # Time - O(N*M)
        # Space - O(N*M)
        
        h, w = len(grid), len(grid[0])
        
        dp = [[0]*w for _ in range(h)]
        dp[0][0] = 0 if grid[0][0] == 1 else 1
        for i in range(h):
            if grid[i][0] == 1:
                break
            dp[i][0] = 1
            
        for j in range(w):
            if grid[0][j] == 1:
                break
            dp[0][j] = 1
        
        for i in range(1, h):
            for j in range(1, w):
                if grid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]


class Solution1:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # Solution - Recursion + Memoization
        # Time - O(N*M)
        # Space - O(N*M)
        
        h, w = len(grid), len(grid[0])
        self.memo = {}
        return self.recur(0, 0, grid, h, w)
    
    def recur(self, i, j, grid, h, w):
        if i >= h or j >= w:
            return 0
        
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        if grid[i][j] == 1:
            return 0
        
        if i == h-1 and j == w-1:
            return 1
        
        self.memo[(i, j)] = (self.recur(i+1, j, grid, h, w) +
               self.recur(i, j+1, grid, h, w))
            
        return self.memo[(i, j)]
        