class Solution:
    @cache
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
    
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestCommonSubsequence(s, s[::-1])
        