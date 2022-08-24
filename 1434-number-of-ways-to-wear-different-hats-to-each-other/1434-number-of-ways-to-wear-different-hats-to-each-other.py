# class Solution:
#     def numberWays(self, hats: List[List[int]]) -> int:
#         n = len(hats)
#         MOD = 10**9 + 7
#         hat2ppl = defaultdict(list)
#         for i, hat in enumerate(hats):
#             for x in hat:
#                 hat2ppl[x] += i,
#         memo = defaultdict(int)

#         def dp(h, mask):
#             if mask == (1 << n) - 1: 
#                 return 1
#             if h == 40:
#                 return 0
#             if (h, mask) not in memo:
#                 memo[h, mask] = dp(h+1, mask)
#                 for p in hat2ppl[h+1]:
#                     if mask & (1<<p) == 0:
#                         memo[h, mask] += dp(h+1, mask | (1 << p))
#             return memo[h, mask] % MOD
        
#         return dp(0, 0)








MOD = 10**9+7

class Solution:
    
    def recur(self, i, mask, hatMap, n):
        
        if (i, mask) in self.memo:
            return self.memo[(i, mask)]
        
        if mask == (1 << n) -1:
            return 1
        
        if i >= 40:
            return 0
        
        count = 0
        count = (count + (self.recur(i+1, mask, hatMap, n) % MOD)) % MOD
        
        for ppl in hatMap[i+1]:
            if mask & (1 << ppl) == 0: 
            
                mask = mask | (1 << ppl)
                count = (count + (self.recur(i+1, mask, hatMap, n) % MOD)) % MOD
                mask = mask ^ (1 << ppl)
        
        self.memo[(i, mask)] = count
        return count
            
    
    def numberWays(self, hats: List[List[int]]) -> int:
        hatMap = defaultdict(list)
        self.memo = {}
        
        for ppl, hatList in enumerate(hats):
            for hat in hatList:
                hatMap[hat].append(ppl)

        return self.recur(0, 0, hatMap, len(hats)) % MOD
        