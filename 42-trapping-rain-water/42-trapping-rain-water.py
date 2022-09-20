class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftMax = [0] * len(height)
        leftMax[0] = height[0]
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i])
            
        rightMax = [0] * len(height)
        rightMax[-1] = height[-1]
        for j in reversed(range(len(height)-1)):
            rightMax[j] = max(rightMax[j+1], height[j])
        
        result = [0] * len(height)
        
        for i in range(len(height)):
            result[i] = min(leftMax[i], rightMax[i]) - height[i]
            
        return sum(result)
        