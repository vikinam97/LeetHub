class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seenMap = {}
        
        i, j = 0, 0
        
        longSoFar = 0
        
        while i < len(s):
            
            if s[i] in seenMap and seenMap[s[i]] >= j:
                j = seenMap[s[i]] + 1
            
            seenMap[s[i]] = i
            longSoFar = max(longSoFar, i - j + 1)
            i += 1 
        
        return longSoFar
            
            
            
        