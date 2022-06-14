class Solution:
    def numTrees(self, n: int) -> int:
        
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
        