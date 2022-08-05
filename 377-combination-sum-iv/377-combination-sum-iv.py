class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Solution - DP (coin change)
        # Time - O(N)
        #     - N = target
        # Space - O(N)
        
        dp = [0]*(target+1)
        dp[0] = 1
        
        nums.sort()
        
        for tar in range(target+1):
            for num in nums:
                if num > tar:
                    break
                dp[tar] += dp[tar-num]
        
        return dp[-1]
                    