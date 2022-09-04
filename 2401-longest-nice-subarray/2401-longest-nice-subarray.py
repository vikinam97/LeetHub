class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # Solution - bit manipulation 
        # Time - O(N*N)
        # Space - O(1)
        
        maxSoFar = 1
        
        for i in range(len(nums)):
            cur, j = nums[i], i + 1
            while j < len(nums) and cur & nums[j] == 0:
                maxSoFar = max(maxSoFar, j - i + 1)
                cur = cur | nums[j]
                j += 1
            
        return maxSoFar
                