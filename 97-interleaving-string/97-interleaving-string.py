class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        m, n = len(s1), len(s2)
        
        dp = [True] + [False] * n
        for j in range(1, n + 1):
            dp[j] = s2[j - 1] == s3[j - 1] and dp[j - 1]

        for i in range(1, m + 1):
            dp[0] = s1[i - 1] == s3[i - 1] and dp[0]
            for j in range(1, n + 1):
                dp[j] = (s1[i - 1] == s3[i + j - 1] and dp[j])
                dp[j] = dp[j] or (s2[j - 1] == s3[i + j - 1] and dp[j - 1])
        return dp[-1]