class Solution:
    @cache
    def recur(self, i, j, m, n):
        if i > m or j > n:
            return 0
        
        if i == (m-1) and j == (n-1):
            return 1
        
        return self.recur(i, j+1, m, n) + self.recur(i+1, j, m, n)
    
    def uniquePaths(self, m: int, n: int) -> int:
        
        return self.recur(0, 0, m, n)
        