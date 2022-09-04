class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        maxSoFar = 1
        
        for i in range(len(nums)):
            cur, j = nums[i], i + 1
            while j < len(nums) and cur & nums[j] == 0:
                maxSoFar = max(maxSoFar, j - i + 1)
                cur = cur | nums[j]
                j += 1
            
        return maxSoFar
                