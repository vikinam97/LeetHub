class Solution:
    def maximumScore(self, nums: List[int], muls: List[int]) -> int:
        # Solution - DP - Space Optimized
        # Time - O(M*M)
        # Space - O(M)
        n, m = len(nums), len(muls)
        
        pdp = [0]*(m+1)
        
        for i in range(m - 1, -1, -1):
            cdp = [0]*(m+1)
            for s in range(i, -1, -1):
                cdp[s] = max(
                    (muls[i]*nums[s]) + pdp[s+1],
                    (muls[i]*nums[n - 1 - (i - s)]) + pdp[s])
            pdp = cdp
                
        return pdp[0]

class Solution1:
    def maximumScore(self, nums: List[int], muls: List[int]) -> int:
        # Solution - Iterative DP
        # Time - O(M*M)
        # Space - O(M*M)
        
        n, m = len(nums), len(muls)
        
        dp = [[0]*(m+1) for _ in range(m+1)]
        
        for i in range(m - 1, -1, -1):
            for s in range(i, -1, -1):
                dp[i][s] = max(
                    (muls[i]*nums[s]) + dp[i+1][s+1],
                    (muls[i]*nums[n - 1 - (i - s)]) + dp[i+1][s])
                
        return dp[0][0]
    
class Solution2:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # Solution - TLE - Recusion + Memoization
        # Time - O(M*M)
        #     - M - len(muls)
        # Space - O(M*M)
        
        self.memo = {}
        return self.recur(0, 0, nums, multipliers)
    
    def recur(self, s, i, nums, muls):
        e = len(nums) - 1 - (i - s)
        if i >= len(muls): return 0
        
        if (s, i) in self.memo:
            return self.memo[(s, i)]
        
        self.memo[(s, i)] = max(
            (muls[i]*nums[s]) + self.recur(s+1, i+1, nums, muls),
            (muls[i]*nums[e]) + self.recur(s, i+1, nums, muls))
        
        return self.memo[(s, i)]
    
