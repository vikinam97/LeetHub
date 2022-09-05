MOD = (10**9) + 7

class Solution:
    @cache
    def recur(self, pos, n, k):
        if pos >= n or pos < 0:
            return 0
        
        if k == 0:
            return 1 if pos == 0 else 0
        
        if pos > k:
            return 0
        
        return (self.recur(pos, n, k-1) +
               self.recur(pos+1, n, k-1) + 
               self.recur(pos-1, n, k-1))
            
    
    def numWays(self, steps: int, arrLen: int) -> int:
        return self.recur(0, arrLen, steps) % MOD
        