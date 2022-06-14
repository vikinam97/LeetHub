class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = []
        for i in range(len(word1)+1):
            dp.append([0] * (len(word2)+1))
            dp[i][0] = i
        
        for i in range(len(word2) + 1):
            dp[0][i] = i
        
        for row in range(1, len(word1)+1):
            for col in range(1, len(word2)+1):
                if word1[row-1] == word2[col-1]:
                    dp[row][col] = dp[row - 1][col - 1]
                else:
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + 1
                
        return dp[len(word1)][len(word2)]