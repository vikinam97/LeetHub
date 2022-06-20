class Solution:
    # Solution - using suffix trie and unique strings
    # Time - O(N*M)
    # Space - O(N*M)
    
    def traverse(self, node):
        if node == None:
            return
        
        # if this is the parent string and not sub string
        keys = node.keys()
        if len(keys) == 1 and self.end in node:
            return len(node[self.end]) + 1
        
        sm = 0
        for key in node:
            if key == self.end:
                continue
            sm += self.traverse(node[key])
        
        return sm
    
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # suffix trie formation
        trie = {}
        self.end = '$'
        
        for i, word in enumerate(words):
            word = word[::-1]
            cur = trie
            for char in word:
                if char not in cur:
                    cur[char] ={}
                cur = cur[char]
            cur[self.end] = word
        
        return self.traverse(trie)