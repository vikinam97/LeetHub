class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxSoFar = 0
        imax, jmax = 0, 0
        for idx in range(len(s)):
            # odd palindrromes
            i, j = idx - 1, idx + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                pMax = j - i + 1
                if maxSoFar < pMax:
                    maxSoFar = pMax
                    imax = i
                    jmax = j
                # maxSoFar = max(maxSoFar, pMax)
                i -= 1
                j += 1
            
            # even palindromes
            i, j = idx, idx + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                pMax = j - i + 1
                if maxSoFar < pMax:
                    maxSoFar = pMax
                    imax = i
                    jmax = j
                i -= 1
                j += 1
        
        return s[imax:jmax+1]
            
            
                