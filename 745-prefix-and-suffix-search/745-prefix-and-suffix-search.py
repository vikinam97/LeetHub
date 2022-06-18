class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.idxMark = '$' 
        self.delimiter = '#'
        # jst for simplicity
        idMark =  self.idxMark
        
        for idx in range(len(words)):
            word = words[idx]
            wrdLen = len(word)
            word = word + self.delimiter + word
            
            for i in range(wrdLen):
                cur = self.trie
                # cur[idMark] = idx
                for char in word[i:]:
                    if char not in cur:
                        cur[char] = {}
                    cur = cur[char]
                    cur[idMark] = idx
            # print(self.trie)
    def f(self, prefix: str, suffix: str) -> int:
        
        searchWrd = suffix + self.delimiter + prefix
        cur = self.trie
        for i in range(len(searchWrd)):
            char = searchWrd[i]
            if char not in cur:
                return -1
            cur = cur[char]

        return cur[self.idxMark]
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)