class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n <= 1:
            return 0
        
        striverList = [True] * n
        
        striverList[0] = striverList[1] = False
        
        for i in range(2, math.isqrt(n) + 1):
            if striverList[i] == False:
                continue
            j = i * i
            while j < n:
                striverList[j] = False
                j += i
            
        count = 0
        for i in range(2, n):
            if striverList[i] == True:
                count += 1
        
        return count
            
                
        