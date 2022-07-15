class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        bfs = [[row, col]]
        
        di = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        seen = {}
        
        gridColor = grid[row][col]
        
        while bfs:
            nxtLvl = []
            for i, j in bfs:
                seen[(i, j)] = 1
                border = False
                for xi, yi in di:
                    x, y = i + xi, j + yi
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == gridColor:
                        if (x, y) not in seen:
                            nxtLvl.append([x, y])
                    else:
                        if (x, y) not in seen:
                            border = True
                            
                if border:   
                    grid[i][j] = color
            
            bfs = nxtLvl
        
        return grid