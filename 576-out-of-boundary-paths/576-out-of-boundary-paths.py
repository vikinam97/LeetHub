class Solution:
    
    @cache
    def noOfWays(self, x, y, moves, m, n):
        if x < 0 or x >= m or y < 0 or y >= n:
            return 1
        
        if moves <= 0:
            if x < 0 or x >= m or y < 0 or y >= n:
                return 1
            return 0
        
        di = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        count = 0
        for xi, yi in di:
            count += self.noOfWays(x + xi, y + yi, moves - 1, m, n)
        
        return count
    
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        count = self.noOfWays(startRow, startColumn, maxMove, m, n)
            
        return count % ((10 ** 9) + 7)