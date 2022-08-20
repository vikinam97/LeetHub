class Solution:
    
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
    
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        self.memo = {}
        return self.recur(0, 0, grid, h, w)
        