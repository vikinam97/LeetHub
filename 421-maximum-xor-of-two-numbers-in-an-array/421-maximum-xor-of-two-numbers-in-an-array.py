class Solution:
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Solution - trie  + bit logic
        # Time - O(N * 32)
        # Space - O(N * 32)
        
        self.end = '*'
        self.trie = {}
        maxSoFar = 0
        for num in nums:
            self.addToTrie(num, self.trie)
            maxVal = self.maximize(num, self.trie)
            maxSoFar = max(maxSoFar, maxVal)
        return maxSoFar
    
    def addToTrie(self, num, trie):
        cur = trie
        i = 31
        while i >= 0:
            key = 1 if num & (1 << i) else 0
            if key not in cur:                
                cur[key] = {}
            cur = cur[key]
            i -= 1
        cur[self.end] = num
    
    def maximize(self, num, trie):
        val = 0
        i = 31
        while i >= 0:
            key = 1 if num & (1 << i) else 0
            # print(key, (int(not key)) in trie, list(trie.keys()))
            if (int(not key)) in trie:
                trie = trie[int(not key)]
                val = val | (1 << i)
            else:
                trie = trie[key]
            i -= 1
        return val
            
        
        
        
        
        