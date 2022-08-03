class Solution:
    
    def checkPossible(self, i, j, prev, heights, k, visited):
        if i == len(heights)-1 and j == len(heights[0])-1:
            return abs(heights[i][j] - prev) <= k
        
        if (i, j) in visited:
            return False
        
        if abs(heights[i][j] - prev) > k:
            return False
        
        visited[(i, j)] = 1
        dirMat = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        for di, dj in dirMat:
            x, y = i + di, j + dj
            if 0 <= x < len(heights) and 0 <= y < len(heights[0]):
                if self.checkPossible(x, y, heights[i][j], heights, k, visited):
                    return True
            
        # del visited[(i, j)]
        
        return False
    
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        maxSoFar = float('-inf')
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                maxSoFar = max(maxSoFar, heights[i][j])
        
        l, r = 0, maxSoFar
        result = maxSoFar
        
        while l <= r:
            mid = l + ((r - l) // 2)
            
            isCheck = self.checkPossible(0, 0, heights[0][0], heights, mid, {})
            
            if isCheck:
                result = min(result, mid)
                r = mid - 1
            else: 
                l = mid + 1
        
        return result