class WordDictionary:

    def __init__(self):
        self.trie = {}
        self.end = "*"
        
    def addWord(self, word: str) -> None:
        cur = self.trie
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur[self.end] = True
        
    def dfs(self, i, word, trie):
        # print(word[i], list(trie.keys()))
        if i >= len(word):
            return self.end in trie
        
        if word[i] == '.':
            for key in trie:
                if key == self.end:
                    continue
                if self.dfs(i + 1, word, trie[key]):
                    return True
                
        elif word[i] in trie:
            return self.dfs(i + 1, word, trie[word[i]])
        
        return False
            

    def search(self, word: str) -> bool:
        # print("--------------------")
        return self.dfs(0, word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)