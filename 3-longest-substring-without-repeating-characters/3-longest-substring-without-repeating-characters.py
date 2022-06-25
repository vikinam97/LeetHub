class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seenMap = {}
        maxSoFar = 0
        j = 0
        for i in range(len(s)):
            if s[i] in seenMap and seenMap[s[i]] >= j:
                j = seenMap[s[i]] + 1
            seenMap[s[i]] = i
            print( s[i], j, i)
            maxSoFar = max(maxSoFar, i - j + 1)
        return maxSoFar
                
        
        
        
        # Solution - sliding window
        # Time - O(N)
        # Space - O(N)
#         maxSoFar = 0
#         charSeen = defaultdict(int)
#         charCount = 0
#         j = 0 
#         for i in range(len(s)):
#             if charSeen[s[i]] == 0:
#                 charCount += 1
#             charSeen[s[i]] += 1
            
#             while charCount < (i - j + 1):
#                 charSeen[s[j]] -= 1
#                 if charSeen[s[j]] == 0:
#                     charCount -= 1
#                 j += 1
            
#             if charCount == (i - j + 1):
#                 maxSoFar = max(maxSoFar, i - j + 1)
        
#         return maxSoFar
            