class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        countDigits = []
        self.memo = {}
        def get01Count(word):
            counts = [0, 0]
            for i in word:
                if i == '1':
                    counts[1] += 1
                else:
                    counts[0] += 1
            return counts
        
        for i in range(len(strs)):
            countDigits.append(get01Count(strs[i]))
        
        return self.recur(0, m, n, countDigits)-1
    
    def recur(self, idx, m, n, countDigits):
        if (idx, m, n) in self.memo:
            return self.memo[(idx, m, n)]
        
        if idx >= len(countDigits):
            return m >= 0 and n >= 0
        
        if m < 0 or n < 0:
            return 0
        
        take = self.recur(idx+1, m - countDigits[idx][0], n - countDigits[idx][1], countDigits) + 1
        dontTake = self.recur(idx+1, m, n, countDigits) 
        
        self.memo[(idx, m, n)] = max(take, dontTake)
        
        return self.memo[(idx, m, n)]
        