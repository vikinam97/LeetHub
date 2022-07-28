class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashtable, dp = {i for i in wordDict}, [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j] and s[j:i] in hashtable:
                    dp[i] = True
                    break
        return dp[len(s)]

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
