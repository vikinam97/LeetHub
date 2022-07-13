class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = []
        for i in range(len(s1)+1):
            dp.append([0] * (len(s2)+1))
        
        for i in range(1, len(s1)+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        
        for i in range(1, len(s2) + 1):
            dp[0][i] = dp[0][i-1] + ord(s2[i-1])
            
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        
        return dp[-1][-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
class Solution1:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # Solution - TLE bottom up recursion
        # Time - O(M * N)
        # Space - O(M * N)
        memo = {}
        
        def recur(i, j, sm):
            if i >= len(s1) and j >= len(s2):
                return sm
            
            if i >= len(s1):
                return sm + sum(ord(char) for char in s2[j:])
            
            if j >= len(s2):
                return sm + sum(ord(char) for char in s1[i:])
            
            if (i, j, sm) in memo:
                return memo[(i, j, sm)]
            
            if s1[i] == s2[j]:
                memo[(i, j, sm)] = recur(i+1, j+1, sm)
            else:
                memo[(i, j, sm)] = min(recur(i+1, j, sm + ord(s1[i])),
                          recur(i, j+1, sm + ord(s2[j])))
            
            return memo[(i, j, sm)]
        
        return recur(0, 0, 0)