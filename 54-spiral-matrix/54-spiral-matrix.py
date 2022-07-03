class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        seen = []
        x, y = 0, 0
        curDi = 0
        result = []
        
        for i in range(m):
            seen.append([0] * n)
        
        for i in range(m * n):
            result.append(matrix[x][y])
            seen[x][y] = 1
            
            nxtX = x + directions[curDi][0]
            nxtY = y + directions[curDi][1]
            
            if 0 <= nxtX < m and 0 <= nxtY < n and seen[nxtX][nxtY] == 0:
                x = nxtX
                y = nxtY
            else:
                curDi = (curDi + 1) % 4
                x = x + directions[curDi][0]
                y = y + directions[curDi][1]
        
        return result