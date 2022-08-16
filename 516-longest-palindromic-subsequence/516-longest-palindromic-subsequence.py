class Solution:    
    def longestPalindromeSubseq(self, s: str) -> int:
        # Solution - recursion with memorization
        # Time - O(N^2)
        #     - N = len of s
        # Space - O(N^2)
        return self.longestCommonSubsequence(s, s[::-1])
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:        
        dp = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]
        
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
        