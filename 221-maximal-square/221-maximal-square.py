class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        h, w = len(matrix), len(matrix[0])
        dp = [[0]*w for _ in range(h)]
        
        maxSoFar = 0
        for i in range(0, h):
            for j in range(0, w):
                if i == 0:
                    dp[0][j] = int(matrix[0][j])
                elif j == 0:
                    dp[i][0] = int(matrix[i][0])
                elif matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                maxSoFar = max(maxSoFar, dp[i][j] * dp[i][j])

        return maxSoFar