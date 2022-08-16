class Solution:    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Solution - recursion with memorization
        # Time - O(N * M)
        #     - N = len of text1
        #     - M = len of text2
        # Space - O(N * M)
        
        dp = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]
        
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
        
class Solution1:    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Solution - recursion with memorization
        # Time - O(N * M)
        #     - N = len of text1
        #     - M = len of text2
        # Space - O(N * M)
        
        self.memo = {}
        return self.recur(0, 0, text1, text2)
    
    def recur(self, i, j, text1, text2):
        if i >= len(text1) or j >= len(text2):
            return 0
        
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        if text1[i] == text2[j]:
            self.memo[(i, j)] = self.recur(i+1, j+1, text1, text2) + 1
        else:
            self.memo[(i, j)] = max(self.recur(i, j+1, text1, text2),
                  self.recur(i+1, j, text1, text2))
        
        return self.memo[(i, j)]