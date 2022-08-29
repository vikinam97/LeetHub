class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Solution - DFS traversal
        # Time - O(N)
        # Space - O(N)
        
        n, m = len(grid), len(grid[0])
        
        count = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(i, j, grid)
        
        return count
    
    def dfs(self, i, j, grid):
        if i < 0 or i >= len(grid)  or j < 0 or j >= len(grid[0]):
            return
        
        if grid[i][j] != '1':
            return
        
        grid[i][j] = 0
        
        dirList = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        for dx, dy in dirList:
            x, y = i + dx, j + dy
            self.dfs(x, y, grid)
            