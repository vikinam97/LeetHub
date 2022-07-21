class Solution:
    @cache
    def recur(self, i, j, text1, text2):
        if i >= len(text1) or j >= len(text2):
            return 0
        
        if text1[i] == text2[j]:
            return self.recur(i+1, j+1, text1, text2) + 1
        
        return max(self.recur(i, j+1, text1, text2),
                  self.recur(i+1, j, text1, text2))
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.recur(0, 0, text1, text2)