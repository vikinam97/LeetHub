class Solution:
    
    def dfs(self, i, j, grid, visited):
        if visited[i][j] == 1:
            return
        
        visited[i][j] = 1
        
        dirList = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for dx, dy in dirList:
            x, y = i + dx, j + dy
            
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[i][j] <= grid[x][y]:
                self.dfs(x, y, grid, visited)
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Solution - DFS outer boundary
        # Time - O(N*M)
        #     - N = len(heights)
        #     - M = len(heights[0])
        # Space - O(N*M)
        
        
        n, m = len(heights), len(heights[0])
        
        # to check flow from pacific ocean top and left
        pacificFlow = [[0]*m for _ in range(n)]
        
        for i in range(n):
            self.dfs(i, 0, heights, pacificFlow)
        
        for j in range(m):
            self.dfs(0, j, heights, pacificFlow)
        
        # to check flow from atlantic ocean bottom and right
        atlanticFlow = [[0]*m for _ in range(n)]
        
        for i in range(n):
            self.dfs(i, m-1, heights, atlanticFlow)
        
        for j in range(m):
            self.dfs(n-1, j, heights, atlanticFlow)
        
        # all regions colliding         
        result = []
        for i in range(n):
            for j in range(m):
                if pacificFlow[i][j] == 1 and atlanticFlow[i][j] == 1:
                    result.append([i, j])
        
        return result