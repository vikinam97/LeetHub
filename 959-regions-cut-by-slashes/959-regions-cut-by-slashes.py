class Solution:
    
    def dfs(self, i, j, k, grid, height, width):
        if i < 0 or i >= height or j < 0 or j >= width:
            return

        if self.visited[i][j][k] != 0:
            return
        
        self.visited[i][j][k] = 1
        
        if k == 0:
            self.dfs(i-1, j, 2, grid, height, width)
        elif k == 1:
            self.dfs(i, j+1, 3, grid, height, width)
        elif k == 2:
            self.dfs(i+1, j, 0, grid, height, width)
        elif k == 3:
            self.dfs(i, j-1, 1, grid, height, width)
            
        if grid[i][j] != '/':
            self.dfs(i, j, k ^ 1, grid, height, width)
        if grid[i][j] != '\\':
            self.dfs(i, j, k ^ 3, grid, height, width)
    
    def regionsBySlashes(self, grid):
        height, width = len(grid), len(grid[0])
        
        self.visited = [[[0]*4 for j in range(width)] for i in range(height)]
        
        count = 0
        for i in range(height):
            for j in range(width):
                
                for k in range(4):
                    if self.visited[i][j][k] == 1:
                        continue
                        
                    self.dfs(i, j, k, grid, height, width)
                    count += 1
        
        return count
        
        
