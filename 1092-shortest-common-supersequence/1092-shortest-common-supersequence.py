class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        dp = [[0] * (len(str2)+1)  for _ in range(len(str1)+1)]
        
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        result = []
        i, j = len(str1), len(str2)
        
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                result.append(str1[i-1])
                i, j = i-1, j-1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    result.append(str1[i-1])
                    i, j = i-1, j
                else:
                    result.append(str2[j-1])
                    i, j = i, j-1
                    
        # print(result[::-1], i, j)
        
        if  i == 0 and j > 0:
            result.append(str2[:j])
        if j == 0 and i > 0:
            result.append(str1[:i])
            
        return "".join(result[::-1])
