class Solution:        
    def longestStrChain(self, words: List[str]) -> int:
        
        # to sort list to traverse IN LIS
        words.sort(key=len)
        
        dpDict = {}
        maxSoFar = 1
        for word in words:
            dpDict[word] = 1
            for i in range(len(word)):
                pred = word[:i] + word[i+1:]
                if pred in dpDict:
                    dpDict[word] = max(dpDict[word], dpDict[pred] + 1)
                    maxSoFar = max(maxSoFar, dpDict[word])
        return maxSoFar
            
                    
        
        
#     def longestStrChain(self, words: List[str]) -> int:
#         Solution - LIS and string matching based on given cinstraint
#         # Time O(N ^ 3) LIS N ^ 2 and cmparing string is N = N^2 * N 
#         # Space O(N)
#         def sortLen(wrd):
#             return len(wrd)
#         words.sort(key=sortLen)
        
#         dp = [1] * len(words)
#         maxSoFar = 1
        
#         for i in range(len(words)):
#             for j in range(i):
#                 if len(words[i]) != len(words[j]) + 1:
#                     continue
#                 if self.cmprStr(words[i], words[j]):
#                     dp[i] = max(dp[i], dp[j] + 1)
#                     maxSoFar = max(maxSoFar, dp[i])
        
#         return maxSoFar
    
#     def cmprStr(self, w1, w2): 
#         i, j = 0, 0
#         flag = 0
#         while i < len(w1) and j < len(w2):
#             if w1[i] != w2[j]:
#                 if flag == 1:
#                     return False
#                 flag = 1
#                 i += 1
#                 continue
#             i += 1
#             j += 1            

#         return w1[i-1] == w2[j-1]
        
        
        
        
                
                
            