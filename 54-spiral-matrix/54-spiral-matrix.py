class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        seen = defaultdict(int)
        
        x, y = 0, 0
        curDi = 0
        m, n = len(matrix), len(matrix[0])
        result = []
        for i in range(m * n):
            result.append(matrix[x][y])
            seen[chr(x) + "-"+ chr(y)] = 1
            
            nxtX = x + directions[curDi][0]
            nxtY = y + directions[curDi][1]
            
            if 0 <= nxtX < m and 0 <= nxtY < n and chr(nxtX) + '-' + chr(nxtY) not in seen:
                x = nxtX
                y = nxtY
            else:
                curDi = (curDi + 1) % 4
                x = x + directions[curDi][0]
                y = y + directions[curDi][1]
        
        return result