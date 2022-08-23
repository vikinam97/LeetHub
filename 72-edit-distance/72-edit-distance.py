class Solution:
    
    def recur(self, i, j, word1, word2):
        if i >= len(word1) and j>= len(word2):
            return 0
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        if i >= len(word1): return len(word2) - j
        if j >= len(word2): return len(word1) - i
        
        if word1[i] == word2[j]:
            self.memo[(i, j)] = self.recur(i+1, j+1, word1, word2)
        else:
            self.memo[(i, j)] = min(self.recur(i+1, j, word1, word2),
                      self.recur(i, j+1, word1, word2),
                      self.recur(i+1, j+1, word1, word2)) + 1
        
        return self.memo[(i, j)]
    
    def minDistance(self, word1: str, word2: str) -> int:
        self.memo = {}
        return self.recur(0, 0, word1, word2)
        