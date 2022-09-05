MOD = (10**9) + 7

class Solution:
    def recur(self, pos, end, k):
        if k == 0:
            return 1 if pos == end else 0
        
        if pos - end > k:
            return 0
        
        if (pos, k) in self.memo:
            return self.memo[(pos, k)]
        
        self.memo[(pos, k)] = (self.recur(pos + 1, end, k-1) + 
                               self.recur(pos - 1, end, k - 1))
        
        return self.memo[(pos, k)]
    
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        self.memo = {}
        return self.recur(startPos, endPos, k) % MOD