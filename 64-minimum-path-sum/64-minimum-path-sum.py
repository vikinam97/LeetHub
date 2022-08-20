class Solution:
    
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
        
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.memo = {}
        return self.recur(0, 0, grid)