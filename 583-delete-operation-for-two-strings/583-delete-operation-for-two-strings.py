class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # Solution - LCS
        # Time = O(N * M) N = len(word1), M = len(word2)
        # Space = O(N * M) N = len(word1), M = len(word2)
        
        dp = [[0] * (len(word2)+1) for _ in range(len(word1) + 1)]
        
        for row in range(1, len(word1)+1):
            for col in range(1, len(word2)+1):
                if word1[row-1] == word2[col-1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
                
        return len(word1) + len(word2) - (2 * dp[-1][-1])