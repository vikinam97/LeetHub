class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bfs = []
        minutes = 0
        r, c = len(grid), len(grid[0])
        # insert all rotten ones
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    bfs.append([i, j])
        
        # simulate bfs
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        while bfs:
            nxtLevel = []
            for i, j in bfs:
                for dirs in directions:
                    ti, tj = i + dirs[0], j + dirs[1]
                    if 0 <= ti < r and 0 <= tj < c and grid[ti][tj] == 1:
                        grid[ti][tj] = 2
                        nxtLevel.append([ti, tj])
            # print(grid)
            # print(nxtLevel)
            if nxtLevel:
                minutes += 1

            bfs = nxtLevel
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    return -1
        
        return minutes
        
        
                        
                
                
                
        