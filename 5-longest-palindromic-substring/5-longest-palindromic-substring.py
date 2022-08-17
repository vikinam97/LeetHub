class Solution:
    def expandPalindrome(self, i, j, s):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            pMax = j - i + 1
            if self.maxSoFar < pMax:
                self.maxSoFar = pMax
                self.imax = i
                self.jmax = j
            i -= 1
            j += 1
            
    def longestPalindrome(self, s: str) -> str:
        self.maxSoFar = 0
        self.imax, self.jmax = 0, 0
                
        for idx in range(len(s)):
            # odd palindrromes
            i, j = idx - 1, idx + 1
            self.expandPalindrome(i, j, s)
            
            # even palindromes
            i, j = idx, idx + 1
            self.expandPalindrome(i, j, s)
        
        return s[self.imax:self.jmax+1]