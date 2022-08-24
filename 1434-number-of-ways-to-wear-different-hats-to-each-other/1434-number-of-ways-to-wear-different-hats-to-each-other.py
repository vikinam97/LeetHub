MOD = 10**9+7

class Solution:
    
    def recur(self, i, mask, hatMap, n):
        if mask == (1 << n) -1: return 1
        if i > 40: return 0
        
        if (i, mask) in self.memo: 
            return self.memo[(i, mask)]
        
        count = 0
        count = count + self.recur(i+1, mask, hatMap, n)
        
        for ppl in hatMap[i]:
            if mask & (1 << ppl) == 0: 
                count = count + self.recur(i+1, mask | (1 << ppl), hatMap, n)
        
        self.memo[(i, mask)] = count
        return count
            
    
    def numberWays(self, hats: List[List[int]]) -> int:
        hatMap = defaultdict(list)
        self.memo = {}
        
        for ppl, hatList in enumerate(hats):
            for hat in hatList:
                hatMap[hat].append(ppl)

        return self.recur(0, 0, hatMap, len(hats)) % MOD
        