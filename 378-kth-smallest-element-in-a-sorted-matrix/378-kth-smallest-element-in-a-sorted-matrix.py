class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Solution - Binary search
        # Time - O(log(Min - Max) * M+N)
        #     - Max -> max val in matrix
        #     - Min -> min val in matrix
        #     - M -> Rows
        #     - C -> Cols
        # Space - O(1)
        
        l, r = matrix[0][0], matrix[-1][-1]
        
        result = None
        while l <= r:
            mid = l + ((r - l) // 2)
            
            countOfEle = self.getCountOfNumsLessEqual(mid, matrix)
            
            if countOfEle >= k:
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return result
    
    def getCountOfNumsLessEqual(self, val, matrix):
        count = 0
        
        i, j = len(matrix[0]) - 1, 0
        
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > val:
                i -= 1
            else:
                count += (i+1)
                j += 1
                
        return count
                