class Solution:
    def trap(self, height: List[int]) -> int:
        
        rightMax = [0] * len(height)
        leftMax = [0] * len(height)
        
        leftMax[0] = height[0]
        # find the leftMax max for height
        for i in range(1, len(height)):
            leftMax[i] = max(height[i], leftMax[i-1])
        
        rightMax[len(height)-1] = height[len(height)-1]
        # find the right max of the heights
        for i in range(len(height) - 2, 0 - 1, -1):
            rightMax[i] = max(height[i], rightMax[i+1])
        
        # to find the water above
        waterList = [0] * len(height)
        for i in range(len(height)):
            waterLevel = min(rightMax[i], leftMax[i])
            if waterLevel > height[i]:
                waterList[i] = waterLevel - height[i]
        
        return sum(waterList)
            
            
        
        