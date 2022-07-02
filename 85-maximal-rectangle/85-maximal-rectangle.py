class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        histogram = [0]*len(matrix[0])
        
        maxSoFar = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    histogram[j] = histogram[j] + int(matrix[i][j])
                else:
                    histogram[j] = 0
            tMax = self.largestRectangleArea(histogram)
            maxSoFar = max(maxSoFar, tMax)
        
        return maxSoFar
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Solution - using stack and continuation index
        # Time - O(N)
        # Space - O(N)
        stack = []
        maxSoFar = 0
        for idx, height in enumerate(heights):
            lastPopped = idx
            while stack and stack[-1][1] > height:
                popped = stack.pop()
                area = (idx - popped[0]) * popped[1]
                lastPopped = popped[0]
                maxSoFar = max(maxSoFar, area)
            stack.append([lastPopped, height])
        
        while stack:
            popped = stack.pop()
            area = (len(heights) - popped[0]) * popped[1]
            maxSoFar = max(maxSoFar, area)
            
        return maxSoFar
                
                
