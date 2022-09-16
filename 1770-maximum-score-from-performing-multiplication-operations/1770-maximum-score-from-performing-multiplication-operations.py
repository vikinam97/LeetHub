class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        # Number of Operations
        m = len(multipliers)

        # For Right Pointer
        n = len(nums)

        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for op in range(m - 1, -1, -1):
            for left in range(op, -1, -1):

                dp[op][left] = max(multipliers[op] * nums[left] + dp[op + 1][left + 1],
                                   multipliers[op] * nums[n - 1 - (op - left)] + dp[op + 1][left])

        return dp[0][0]               
        
        
        
        
        
        
        
        
        
        
        

class Solution1:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # Solution - Recusion + Memoization TLE
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
    
