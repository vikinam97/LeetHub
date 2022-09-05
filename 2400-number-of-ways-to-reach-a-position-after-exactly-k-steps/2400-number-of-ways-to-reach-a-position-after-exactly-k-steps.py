MOD = (10**9) + 7

class Solution:
    @cache
    def recur(self, pos, end, k):
        if k == 0:
            return 1 if pos == end else 0
        
        if pos - end > k:
            return 0
        
        return self.recur(pos + 1, end, k-1) + self.recur(pos - 1, end, k - 1)
    
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        return self.recur(startPos, endPos, k) % MOD