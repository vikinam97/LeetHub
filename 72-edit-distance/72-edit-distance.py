class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Solution - DP - Space Optimized
        # Time - O(N*M)
        # Space - O(M)
        
        n, m = len(word1), len(word2)
        pdp = [0] * (m+1)
        
        for j in range(1, m+1): pdp[j] = pdp[j-1] + 1
        
        for i in range(1, n+1):
            cdp = [0] * (m+1)
            cdp[0] = pdp[0] + 1
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    cdp[j] = pdp[j-1]
                else:
                    cdp[j] = min(pdp[j-1], cdp[j-1], pdp[j]) + 1
            pdp = cdp
            
        return pdp[-1]

class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        # Solution - DP Tabulation
        # Time - O(N*M)
        # Space - O(N*M)
        
        n, m = len(word1), len(word2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        
        for i in range(1, n+1): dp[i][0] = dp[i-1][0] + 1
        for j in range(1, m+1): dp[0][j] = dp[0][j-1] + 1
            
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1],
                                  dp[i][j-1],
                                  dp[i-1][j]) + 1
        
        return dp[-1][-1]
        

class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        # Solution - Recursion + Memoization
        # Time - O(N*M)
        # Space - O(N*M)
        
        self.memo = {}
        return self.recur(0, 0, word1, word2)
        
    def recur(self, i, j, word1, word2):
        if i >= len(word1) and j>= len(word2):
            return 0
        
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        if i >= len(word1): return len(word2) - j
        if j >= len(word2): return len(word1) - i
        
        if word1[i] == word2[j]:
            self.memo[(i, j)] = self.recur(i+1, j+1, word1, word2)
        else:
            self.memo[(i, j)] = min(self.recur(i+1, j, word1, word2),
                                  self.recur(i, j+1, word1, word2),
                                  self.recur(i+1, j+1, word1, word2)) + 1
        
        return self.memo[(i, j)]
    
        