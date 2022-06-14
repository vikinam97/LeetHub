class Solution:
    def numTrees(self, n: int) -> int:
        # Solution - Dynamic programming
        # Time - O(N ^ 2)
        # Space - O(N)
#         dp = [0] * (n + 1)
#         dp[0] = dp[1] = 1
        
#         for i in range(2, n + 1):
#             dp[i] = 0
#             for j in range(i):
#                 dp[i] += dp[j] * dp[i-1-j]
        
#         return dp[n]
            
        
        
        # Solution recurrence with memorization
        # Time O(N ^2)
        # space O(N) memo and call stack
        self.memo = {
            0: 1,
            1: 1
        }
        return self.recHepler(n)
    
    def recHepler(self, n):
        if self.memo.get(n, None):
            return self.memo[n]
        
        sm = 0
        for i in range(n):
            sm += self.recHepler(i) * self.recHepler(n-1-i)
        
        self.memo[n] = sm
        
        return sm
        