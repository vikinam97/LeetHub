class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        
        maxSoFar = float('-inf')
        
        for i in range(len(heights)):
            lastPopped = i
            while stack and stack[-1][0] > heights[i]:
                ele = stack.pop()
                lastPopped = ele[1]
                area = ele[0] * ( i - ele[1])
                maxSoFar = max(maxSoFar, area)
                
            stack.append([heights[i], lastPopped])
        
        while stack:
            ele = stack.pop()
            area = ele[0] * (len(heights) - ele[1])
            maxSoFar = max(maxSoFar, area)
        
        return maxSoFar
            
            
        