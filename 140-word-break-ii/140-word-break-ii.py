class Solution:
    def generateTrie(self, wordList):
        trie = {}
        
        for word in wordList:
            cur = trie
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur[self.end] = True
        
        return trie
    
    def backtrack(self, i, lastBreak, string, curTrie, path):
        if not curTrie:
            return
        
        if i >= len(string):
            if self.end in curTrie:
                self.resultWords.append(" ".join(path + [string[lastBreak:i]]))
            return
        
        if self.end in curTrie:
            path.append(string[lastBreak:i])
            self.backtrack(i, i, string, self.trie, path)
            path.pop()
            
        if string[i] not in curTrie:
            return
        
        self.backtrack(i+1, lastBreak, string, curTrie[string[i]], path)            
            
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.end = "*"
        self.trie = self.generateTrie(wordDict)
        
        self.resultWords = []
        self.backtrack(0, 0, s, self.trie, [])
        
        return self.resultWords
        
        
        
        
        