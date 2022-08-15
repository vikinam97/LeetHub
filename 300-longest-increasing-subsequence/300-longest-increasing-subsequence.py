class Solution1:
    
    def recur(self, i, prev, nums):
        if i >= len(nums):
            return 0
        
        if self.memo[i][prev+1] != -1:
            return self.memo[i][prev+1]
        
        result = self.recur(i + 1, prev, nums)
        
        if prev == -1 or nums[i] > nums[prev]:
            result = max(result, self.recur(i+1 , i , nums) + 1)
        
        self.memo[i][prev+1] = result
        return result
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.memo = [[-1] * (len(nums) + 1) for _ in range(len(nums) + 1)]
        return self.recur(0, -1, nums)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Solution - LIS
        # Time - O(N^2)
        # Space - O(N)
        
        dp = [1] * len(nums)

        maxSoFar = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]: 
                    dp[i] = max(dp[i],dp[j] + 1)
            maxSoFar = max(dp[i], maxSoFar)

        return maxSoFar
        