class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSoFar = 0
        charSeen = defaultdict(int)
        charCount = 0
        j = 0 
        for i in range(len(s)):
            if charSeen[s[i]] == 0:
                charCount += 1
            charSeen[s[i]] += 1
            
            while charCount < (i - j + 1):
                charSeen[s[j]] -= 1
                if charSeen[s[j]] == 0:
                    charCount -= 1
                j += 1
            
            if charCount == (i - j + 1):
                maxSoFar = max(maxSoFar, i - j + 1)
        
        return maxSoFar
            