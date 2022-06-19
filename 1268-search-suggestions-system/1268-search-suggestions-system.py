class Solution:
    def traverse(self, trie, result):
        if trie == None or len(result) == 3:
            return
        
        if self.end in trie:
            result.append(trie[self.end])
    
        for ltr in trie:
            if ltr == self.end:
                continue
            self.traverse(trie[ltr], result)
            
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        trie = {}
        products.sort()
        self.end = '#'
        # generate trie
        for i, product in enumerate(products):
            cur = trie
            for char in product:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur[self.end] = product
            
        # print(trie)
        
        result = []
        cur = trie
        for ltr in searchWord:
            tempList = []
            if ltr in cur:
                self.traverse(cur[ltr], tempList)
                cur = cur[ltr]
            else: cur = {}
            result.append(tempList)
        
        return result;
        
        
            
        