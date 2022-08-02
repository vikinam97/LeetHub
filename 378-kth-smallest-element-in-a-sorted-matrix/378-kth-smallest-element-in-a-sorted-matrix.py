class Solution:
    def countMin(self, val, matrix):
        count = 0
        
        i, j = len(matrix[0]) - 1, 0
        
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > val:
                i -= 1
            else:
                count += (i+1)
                j += 1
                
        return count
        
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r = matrix[0][0], matrix[-1][-1]
        
        result = None
        while l <= r:
            mid = l + ((r - l) // 2)
            
            countOfEle = self.countMin(mid, matrix)
            # print(mid, countOfEle)
            
            if countOfEle >= k:
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return result
                