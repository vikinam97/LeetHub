class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        
        di = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for xi, yi in di:
                        x, y = i + xi, j + yi
                        # if xi >= len(grid) or xi < 0 or yi >= len(grid[0]) or yi < 0
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                            if grid[x][y] == 0:
                                perimeter += 1
                        else:
                            perimeter += 1
        
        return perimeter
                    