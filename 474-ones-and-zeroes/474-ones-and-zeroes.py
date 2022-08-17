class Solution:
    
    def recur(self, idx, ms, ns, m, n, countDigits):
        if (idx, ms, ns) in self.memo:
            return self.memo[(idx, ms, ns)]
        
        if idx >= len(countDigits):
            return ms <= m and ns <= n
        
        if ms > m or ns > n:
            return 0
        
        take = self.recur(idx+1, ms + countDigits[idx][0], ns + countDigits[idx][1], m, n, countDigits) + 1
        dontTake = self.recur(idx+1, ms, ns, m, n, countDigits) 
        
        self.memo[(idx, ms, ns)] = max(take, dontTake)
        
        return self.memo[(idx, ms, ns)]
    
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
        
        print(countDigits)
            
        return self.recur(0, 0, 0, m, n, countDigits)-1
        