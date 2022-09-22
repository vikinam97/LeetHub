class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        i = j = 0
        
        runningSum = 0
        
        minSoFar = float('inf')
        
        while i < len(nums):
            runningSum += nums[i]
            
            while j <= i and runningSum >= target:
                minSoFar = min(minSoFar, i - j + 1)
                runningSum -= nums[j]
                j += 1
            
            i += 1
        
        return minSoFar if minSoFar != float('inf') else 0

                
        