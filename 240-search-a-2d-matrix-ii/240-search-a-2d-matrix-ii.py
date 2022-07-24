class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        r, c = 0, len(matrix[0])-1
        
        while r < len(matrix) and c >= 0:
            if target == matrix[r][c]:
                return True
            
            if target < matrix[r][c]:
                c -= 1
            else:
                r += 1
        
        return False