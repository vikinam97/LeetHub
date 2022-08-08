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
        