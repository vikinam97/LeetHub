class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxSoFar = 0
        for idx, height in enumerate(heights):
            lastPopped = idx
            while stack and stack[-1][1] > height:
                popped = stack.pop()
                print(idx, popped)
                area = (idx - popped[0]) * popped[1]
                lastPopped = popped[0]
                maxSoFar = max(maxSoFar, area)
            stack.append([lastPopped, height])
        
        while stack:
            popped = stack.pop()
            area = (len(heights) - popped[0]) * popped[1]
            maxSoFar = max(maxSoFar, area)
            
        return maxSoFar
            
                