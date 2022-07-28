class Solution:
    def __init__(self):
        self.memo = dict()
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in self.memo:
            return self.memo[s]
        else:
            if s in wordDict:
                return True
            self.memo[s]=False
            for i in range(1,len(s)):
                if (self.wordBreak(s[:i],wordDict) and self.wordBreak(s[i:],wordDict)):
                    self.memo[s]=True
            return self.memo[s]

class Solution1:
    
    def generateTrie(self, words):
        trie = {}
        for word in words:
            cur = trie
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur[self.end] = True
        return trie
    
    def recur(self, i, word, trie):
        if i >= len(word):
            return self.end in trie
        
        if self.end in trie:
            if self.recur(i, word, self.trie):
                return True
        
        if word[i] in trie:
            return self.recur(i+1, word, trie[word[i]])
        
        return False
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.end = '*'
        self.trie = self.generateTrie(wordDict)

        return self.recur(0, s, self.trie)
