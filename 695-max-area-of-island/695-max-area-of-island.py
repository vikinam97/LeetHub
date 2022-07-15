class Solution:
    def dfs(self, x, y, grid):
        if not (0 <= x < len(grid)) or not( 0 <= y < len(grid[0])) or grid[x][y] != 1:
            return 0
        
        di = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        grid[x][y] = -1
        
        sm = 1
        for xi, yi in di:
            sm += self.dfs(x + xi, y + yi, grid)
        
        return sm
        
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        longSoFar = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if grid[i][j] == 1:
                count = self.dfs(i, j, grid)
                longSoFar = max(longSoFar, count)

        return longSoFar