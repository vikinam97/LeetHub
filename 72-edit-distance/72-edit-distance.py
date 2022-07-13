class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def recur(i, j, minDist):
            if i >= len(word1) and j >= len(word2):
                return minDist
            
            if i >= len(word1):
                return minDist + (len(word2) - j)
            
            if j >= len(word2):
                return minDist + (len(word1) - i)
            
            if word1[i] == word2[j]:
                return recur(i+1, j+1, minDist)
            else:
                return min(recur(i, j+1, minDist+1),
                          recur(i+1, j, minDist+1),
                          recur(i+1, j+1, minDist+1))
                
        
        return recur(0, 0, 0)