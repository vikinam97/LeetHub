class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        seenSum = {0: -1}
        
        longSoFar = 0
        curSum = 0
        for i in range(len(nums)):
            curSum = curSum + (1 if nums[i] == 1 else -1)
            
            if curSum not in seenSum:
                seenSum[curSum] = i
                continue
            
            prevIdx = seenSum[curSum] + 1
            longSoFar = max(longSoFar, (i - prevIdx + 1))
        
        return longSoFar
            
                
        