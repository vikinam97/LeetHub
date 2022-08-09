MOD = (10 ** 9) + 7

class Solution:
    
    def recur(self, parent, arr, hashSet):
        
        if parent in self.memo:
            return self.memo[parent]
        
        sm = 0
        for i in arr:
            if (parent / i) in hashSet:
                sm = ( sm +
                    ((self.recur(i, arr, hashSet) + 1) % MOD) * 
                    ((self.recur(parent / i, arr, hashSet) + 1) % MOD)) % MOD
        self.memo[parent] = sm
        return sm
    
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        self.memo = {}
        hashSet = { i for i in arr}
        arr.sort()
        sm = 0
        for i in arr:
            
            rsm = self.recur(i, arr, hashSet)
            sm = (sm + (rsm + 1)) % MOD 
        return sm
        