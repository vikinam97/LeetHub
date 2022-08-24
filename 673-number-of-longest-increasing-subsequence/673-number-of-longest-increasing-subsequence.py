class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # Solution - LIS Iterative
        # Time - O(N^2)
        # Space - O(N)
        
        dp = [1] * len(nums)
        cnt = [1] * len(nums)
        
        maxSoFar = 1
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]
                        
            maxSoFar = max(maxSoFar, dp[i])
            
        nos = 0
        for i in range(len(nums)):
            if dp[i] == maxSoFar:
                nos += cnt[i]
                
        return nos